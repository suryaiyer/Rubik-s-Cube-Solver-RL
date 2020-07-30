
import numpy as np

from random import randint


class cube:
    
    def __init__(self):
        """        
        self.front = np.array([['111','112','113'],['121','122','123'],['131','132','133']])
        self.top = np.array([['211','212','213'],['221','222','223'],['231','232','233']])
        self.left = np.array([['311','312','313'],['321','322','323'],['331','332','333']])
        self.right = np.array([['411','412','413'],['421','422','423'],['431','432','433']])
        self.bottom = np.array([['511','512','513'],['521','522','523'],['531','532','533']])
        self.back = np.array([['611','612','613'],['621','622','623'],['631','632','633']])
        """
        self.front = np.array([[111,112,113],[121,122,123],[131,132,133]])
        self.top = np.array([[211,212,213],[221,222,223],[231,232,233]])
        self.left = np.array([[311,312,313],[321,322,323],[331,332,333]])
        self.right = np.array([[411,412,413],[421,422,423],[431,432,433]])
        self.bottom = np.array([[511,512,513],[521,522,523],[531,532,533]])
        self.back = np.array([[611,612,613],[621,622,623],[631,632,633]])

        self.cube = np.column_stack([self.front,self.top,self.left,self.right,self.bottom,self.back])

    def print_cube(self):
        print('front - ',self.front[0],self.front[1],self.front[2])
        print('top - ', self.top[0],self.top[1],self.top[2])
        print('left - ', self.left[0],self.left[1],self.left[2])
        print('Right - ',self.right[0],self.right[1],self.right[2])
        print('bottom - ' ,self.bottom[0],self.bottom[1],self.bottom[2])
        print('back',self.back[0],self.back[1],self.back[2])
    
    def move(self,move):
        
        if move == 1:
            
            temp = [i for i in self.front[0]]
            self.front[0] = self.right[0]
            self.right[0] = self.back[0]
            self.back[0] = self.left[0]
            self.left[0] = temp
            self.top = np.rot90(self.top,-1)
            
        elif move ==2:
        
            temp = [i for i in self.front[0]]
            self.front[0] = self.left[0]
            self.left[0] = self.back[0]
            self.back[0] = self.right[0]
            self.right[0] = temp
            self.top = np.rot90(self.top)
        
        
        elif move == 3:
            
            temp = [i for i in self.front[1]]
            self.front[1] = self.right[1]
            self.right[1] = self.back[1]
            self.back[1] = self.left[1]
            self.left[1] = temp
            
        elif move ==4:
        
            temp = [i for i in self.front[1]]
            self.front[1] = self.left[1]
            self.left[1] = self.back[1]
            self.back[1] = self.right[1]
            self.right[1] = temp
       
            
        elif move == 5:
            
            temp = [i for i in self.front[2]]
            self.front[2] = self.right[2]
            self.right[2] = self.back[2]
            self.back[2] = self.left[2]
            self.left[2] = temp
            self.bottom = np.rot90(self.bottom,-1)
            
        elif move ==6:
        
            temp = [i for i in self.front[2]]
            self.front[2] = self.left[2]
            self.left[2] = self.back[2]
            self.back[2] = self.right[2]
            self.right[2] = temp
            self.bottom = np.rot90(self.bottom)
            
        elif move == 7:
            temp = [i for i in self.front[:,0]]
            self.front[:,0] = self.top[:,0]
            self.top[:,0] = np.flipud(self.back[:,2])
            self.back[:,2] = np.flipud(self.bottom[:,0])
            self.bottom[:,0] = temp
            self.left = np.rot90(self.left,-1)
            
        elif move == 8:
            temp = [i for i in self.front[:,0]]
            self.front[:,0] = self.bottom[:,0]
            self.bottom[:,0] = np.flipud(self.back[:,2])
            self.back[:,2] = np.flipud(self.top[:,0])
            self.top[:,0] = temp
            self.left = np.rot90(self.left)
        
        elif move == 9:
            temp = [i for i in self.front[:,1]]
            self.front[:,1] = self.top[:,1]
            self.top[:,1] = np.flipud(self.back[:,1])
            self.back[:,1] = np.flipud(self.bottom[:,1])
            self.bottom[:,1] = temp
            
        elif move == 10:
            temp = [i for i in self.front[:,1]]
            self.front[:,1] = self.bottom[:,1]
            self.bottom[:,1] = np.flipud(self.back[:,1])
            self.back[:,1] = np.flipud(self.top[:,1])
            self.top[:,1] = temp
        
        elif move == 11:
            temp = [i for i in self.front[:,2]]
            self.front[:,2] = self.top[:,2]
            self.top[:,2] = np.flipud(self.back[:,0])
            self.back[:,0] = np.flipud(self.bottom[:,2])
            self.bottom[:,2] = temp
            self.right = np.rot90(self.right,-1)
            
        elif move == 12:
            temp = [i for i in self.front[:,2]]
            self.front[:,2] = self.bottom[:,2]
            self.bottom[:,2] = np.flipud(self.back[:,0])
            self.back[:,0] = np.flipud(self.top[:,2])
            self.top[:,2] = temp
            self.right = np.rot90(self.right)
      

        elif move == 13:
            
            temp = [i for i in self.top[0]]
            self.top[0] = self.right[:,0]
            self.right[:,0] = self.bottom[0]
            self.bottom[0] = self.left[:,0]
            self.left[:,0] = temp
            self.back = np.rot90(self.back,-1)
            
        elif move == 14 :
        
            temp = [i for i in self.top[0]]
            self.top[0] = self.left[:,0]
            self.left[:,0] = self.bottom[0]
            self.bottom[0] = self.right[:,0]
            self.right[:,0] = temp
            self.back = np.rot90(self.back,1)
        
        
        elif move == 15:
            
            temp = [i for i in self.top[1]]
            self.top[1] = self.right[:,1]
            self.right[:,1] = self.bottom[1]
            self.bottom[1] = self.left[:,1]
            self.left[:,1] = temp
            
        elif move == 16 :
        
            temp = [i for i in self.top[1]]
            self.top[1] = self.left[:,1]
            self.left[:,1] = self.bottom[1]
            self.bottom[1] = self.right[:,1]
            self.right[:,1] = temp
            
            
        elif move == 17:
            

            temp = [i for i in self.top[2]]
            self.top[2] = self.right[:,2]
            self.right[:,2] = self.bottom[2]
            self.bottom[2] = self.left[:,2]
            self.left[:,2] = temp
            self.front = np.rot90(self.front,-1)
            
        elif move == 18 :
        
            temp = [i for i in self.top[2]]
            self.top[2] = self.left[:,2]
            self.left[:,2] = self.bottom[2]
            self.bottom[2] = self.right[:,2]
            self.right[:,2] = temp
            self.front = np.rot90(self.front,1)
        
        self.cube = np.column_stack([self.front,self.top,self.left,self.right,self.bottom,self.back])

        return self
            


rcube = cube()
# rcube = rcube.move(1)


"""
rcube.print_cube()

rcube.move(17)

rcube.print_cube()
rcube.move(18)


l = cube()


t = rcube.cube - l.cube 


flag = False
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j] != 0:
            flag = True
            break

print(t)

print(flag)        


"""

moves = []


for i in range(10):
    n = randint(1,18)
    moves.append(n)
    rcube.move(n)

rcube.print_cube()


print(moves)
moves.reverse()
for i in range(len(moves)):
    if moves[i]%2 == 0:
        moves[i] = moves[i] - 1
    else:
        moves[i] = moves[i] + 1

print(moves)
for i in range(10):
    rcube.move(moves[i] )
   
rcube.print_cube()

