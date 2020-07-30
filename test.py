		

from cube2 import cube
import torch
import torchvision
import torch.optim as optim
import torch.nn as nn
from model import net
import numpy as np
from copy import copy, deepcopy
from random import randint


move = 11

model = net()

model.load_state_dict(torch.load('models/model.ckpt'))
model.cuda()

rcube = cube()

rcube = rcube.move(move)

m = nn.Softmax(dim=0)

rcube_flatten = rcube.flatten()
state = torch.FloatTensor(rcube_flatten).cuda()
policy,val = model.forward(state,False)

print(policy)
rcube =rcube.move(torch.argmax(policy)+ 1)
rcube.print_cube()


