from cube2 import cube
import torch
import torchvision
import torch.optim as optim
import torch.nn as nn
from model import net
import numpy as np
from copy import copy, deepcopy
from random import randint


def one_hot_ce_loss(outputs, targets):
    criterion = nn.CrossEntropyLoss()
    _, labels = torch.max(targets, dim=1)
    return criterion(outputs, labels)
    
def train_epoch(data,k,model):
    model.cuda()
    model.train()
    criterion_policy = nn.BCEWithLogitsLoss()
    criterion_value = nn.MSELoss()
    optimizer = optim.RMSprop(model.parameters(), lr=0.0001, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0.9, centered=False)
    epoch_loss = 0
    m = nn.Softmax(dim=0)
    for i in range(k):
        optimizer.zero_grad()
        target_policy = []
        target_value = []
        cube_list = []
        for j in range(k):
            cube_list.append(data[i*k + j][0].flatten())
            target_policy.append(data[i*k + j][1])
            target_value.append(data[i*k + j][2])	
        #target_policy = data[i*k:i*k +k][1]
        #target_value = data[i*k:i*k +k][2]
        #state = state.flatten()
        cube_list = torch.FloatTensor(cube_list).cuda()
        target_policy = torch.FloatTensor(target_policy).cuda()
        target_value = torch.FloatTensor(target_value).cuda()
        target_value = target_value[:,None]
        policy,val = model.forward(cube_list,False)
        policy = policy.unsqueeze(0)
        target_policy = target_policy.unsqueeze(0)
        #target_policy = target_policy.long()
        
        loss1 = criterion_value(val,target_value)
        loss2 = criterion_policy(policy,target_policy)
    
        loss = loss1 + loss2
        epoch_loss += loss
        loss.backward()
        optimizer.step()
    return model,epoch_loss

def cube_copy(cube1,cube2):
    cube1.left = deepcopy(cube2.left)
    cube1.right = deepcopy(cube2.right)
    cube1.top = deepcopy(cube2.top)
    cube1.bottom = deepcopy(cube2.bottom)
    cube1.front = deepcopy(cube2.front)
    cube1.back = deepcopy(cube2.back)
    
    return cube1
    
def get_targets(cubes,model):
    
    actions = cubes.get_actions()
    target_list = []
    target_policy = [0 for i in range(12)]
    val_list  = []
    main = deepcopy(cubes)

    for a in actions:
            
        c = cubes.move(a)
        
        cubes = deepcopy(main)
        cube_flatten =c.flatten()
        cube_flatten = torch.FloatTensor(cube_flatten).cuda()
        val = model.forward(cube_flatten,True)
        
        if c.is_goal():	
            #cubes.print_cube()
            val = 1 + val
        #else:
        #   val = val - 1
        
        val_list.append(val)

    t = np.argmax(val_list)
    target_policy[t] = 1
            
    return [cubes,target_policy,val]

def get_data(N,K,model):
    data = []
    for i in range(N):
        c =cube()
        for j in range(K):
            n = randint(1,12)
            c = c.move(n)
            data.append(get_targets(c,model))
    
    return data
    
def main():
	
    model = net()
    model.cuda()
    #print(data[0])
    for i in range(2000):
        
        data = get_data(200,10,model)
        model,epoch_loss = train_epoch(data,10,model)
        print("Epoch - ", i ," Completed with Loss - " ,epoch_loss)
        
        if i % 10 ==0:
            torch.save(model.state_dict(), 'models/model.ckpt')
    
if __name__ == "__main__":
	main()

