import torch
import torch.optim as optim
import torch.nn as nn
import numpy as np


class net(nn.Module):
   
    def __init__(self):
        super(net,self).__init__()
        
        self.fc1 = nn.Linear(144,1024)
        nn.init.xavier_uniform(self.fc1.weight)
        
        self.fc2 = nn.Linear(1024,512)
        nn.init.xavier_uniform(self.fc2.weight)
        
        self.fc3_1 = nn.Linear(512,128)
        nn.init.xavier_uniform(self.fc3_1.weight)
        
        self.fc3_2 = nn.Linear(512,128)
        nn.init.xavier_uniform(self.fc3_2.weight)
        
        self.fc4_1 = nn.Linear(128,12)
        nn.init.xavier_uniform(self.fc4_1.weight)
        
        self.fc4_2 = nn.Linear(128,1)
        nn.init.xavier_uniform(self.fc4_2.weight)
        
        self.RL = nn.LeakyReLU(0.1)
        
    def forward(self,x,flag):
    
        x = self.RL(self.fc1(x))
        x = self.RL(self.fc2(x))
        x1 = self.RL(self.fc3_1(x))
        x2 = self.RL(self.fc3_2(x))
        x1 = self.RL(self.fc4_1(x1))
        x2 = self.RL(self.fc4_2(x2))
        if flag:
            return x2
            
        return x1,x2
    
