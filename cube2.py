
import numpy as np

from random import randint

def is_equal(a1,a2):
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

class cube:
    
    def __init__(self):
        
        self.front = np.array([[1,1],[1,1]])
        self.top = np.array([[2,2],[2,2]])
        self.left =np.array([[3,3],[3,3]])
        self.right = np.array([[4,4],[4,4]])
        self.bottom = np.array([[5,5],[5,5]])
        self.back = np.array([[6,6],[6,6]])
        
        self.cube = np.column_stack([self.front,self.top,self.left,self.right,self.bottom,self.back])
    
    def get_actions(self):
        
        return [1,2,3,4,5,6,7,8,9,10,11,12]
    
    def print_cube(self):
        print('front - \n',self.front)
        print('top - \n', self.top)
        print('left - \n', self.left)
        print('Right - \n',self.right)
        print('bottom - \n' ,self.bottom)
        print('back',self.back)
        
    def is_goal(self):
        flag = True
        
        left = [item for sublist in self.left for item in sublist]
        if all(ele == left[0] for ele in left) == False: 
            return False
            
        top = [item for sublist in self.top for item in sublist]
        if all(ele == top[0] for ele in top) == False: 
            return False
            
        bottom = [item for sublist in self.bottom for item in sublist]
        if all(ele == bottom[0] for ele in bottom) == False: 
            return False

        right = [item for sublist in self.right for item in sublist]
        if all(ele == right[0] for ele in right) == False: 
            return False

        front = [item for sublist in self.front for item in sublist]
        if all(ele == front[0] for ele in front) == False: 
            return False

        back = [item for sublist in self.back for item in sublist]
        if all(ele == back[0] for ele in back) == False:
            return False
        
        return True
        
    def flatten(self):
        out = []
        
        dict = {}
        for i in range(1,7):
            dict[i] = [0,0,0,0,0,0]
            dict[i][i-1] = 1
        
        for i in range(len(self.cube)):
            for j in range(len(self.cube[i])):
                out.extend(dict[self.cube[i][j]])
        
        return out
    
    def scramble(self,N):
        
        for i in range(N):
            n = randint(1,12)
            rcube.move(n)
        
        return self
        
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
            self.bottom = np.rot90(self.bottom,-1)
            
        elif move ==4:
            temp = [i for i in self.front[1]]
            self.front[1] = self.left[1]
            self.left[1] = self.back[1]
            self.back[1] = self.right[1]
            self.right[1] = temp
            self.bottom = np.rot90(self.bottom)
            
        elif move == 5:
            temp = [i for i in self.front[:,0]]
            self.front[:,0] = self.top[:,0]
            self.top[:,0] = np.flipud(self.back[:,1])
            self.back[:,1] = np.flipud(self.bottom[:,0])
            self.bottom[:,0] = temp
            self.left = np.rot90(self.left,-1)
            
        elif move == 6:
            temp = [i for i in self.front[:,0]]
            self.front[:,0] = self.bottom[:,0]
            self.bottom[:,0] = np.flipud(self.back[:,1])
            self.back[:,1] = np.flipud(self.top[:,0])
            self.top[:,0] = temp
            self.left = np.rot90(self.left)
        
    
        elif move == 7:
            temp = [i for i in self.front[:,1]]
            self.front[:,1] = self.top[:,1]
            self.top[:,1] = np.flipud(self.back[:,0])
            self.back[:,0] = np.flipud(self.bottom[:,1])
            self.bottom[:,1] = temp
            self.right = np.rot90(self.right,-1)
            
        elif move == 8:
            temp = [i for i in self.front[:,1]]
            self.front[:,1] = self.bottom[:,1]
            self.bottom[:,1] = np.flipud(self.back[:,0])
            self.back[:,0] = np.flipud(self.top[:,1])
            self.top[:,1] = temp
            self.right = np.rot90(self.right)
    
    
        elif move == 9:
            
            temp = [i for i in self.top[0]]
            self.top[0] = self.right[:,0]
            self.right[:,0] = self.bottom[0]
            self.bottom[0] = self.left[:,0]
            self.left[:,0] = temp
            self.back = np.rot90(self.back,-1)
            
        elif move == 10 :
        
            temp = [i for i in self.top[0]]
            self.top[0] = self.left[:,0]
            self.left[:,0] = self.bottom[0]
            self.bottom[0] = self.right[:,0]
            self.right[:,0] = temp
            self.back = np.rot90(self.back,1)
            
        elif move == 11:
            
            temp = [i for i in self.top[1]]
            self.top[1] = self.right[:,1]
            self.right[:,1] = self.bottom[1]
            self.bottom[1] = self.left[:,1]
            self.left[:,1] = temp
            self.front = np.rot90(self.front,-1)
            
        elif move == 12:
        
            temp = [i for i in self.top[1]]
            self.top[1] = self.left[:,1]
            self.left[:,1] = self.bottom[1]
            self.bottom[1] = self.right[:,1]
            self.right[:,1] = temp
            self.front = np.rot90(self.front,1)
        
        self.cube = np.column_stack([self.front,self.top,self.left,self.right,self.bottom,self.back])
    
        return self
            


 