#DFS_maze

import numpy as np
import random

class dfsMaze():
    def __init__(self,size): #Init maze
        self.size = size
        
        self.grid = None
        self.gen_steps = []
        
        


    

    def GenerateMaze(self):

        '''
        Generates a random perfect maze using Depth First Search (DFS)
        The final maze consists of a matrix made of:
        0 - empty paths
        1 - walls
        4 - Start/End

        Later, with A_star we add:
        3 - checked path by A*
        2- Best possible path


        '''
        self.grid = np.ones((2*self.size+1,2*self.size+1),dtype=int) #Init maze as matrix of walls (1), 
        x, y = (0, 0)
        self.grid[2*x+1, 2*y+1] = 0 #modifications to the maze dimentions ensure an odd sized grid so every pathway is surrounded by walls
        stack = [(x,y)] #init backtracking stack             
        self.gen_steps.append(self.grid.copy()) #Copy the current state of the maze, for future animation

        while len(stack) > 0:
            x,y = stack [-1] #Get last element from stack
            directions = [(0,-1),(0,1),(1,0),(-1,0)] #All four directions for the neighboring cells (South-North-East-West)
            random.shuffle(directions) #Shuffle directions to create random pathways
            for dx, dy in directions:
                nx, ny = x+dx, y+dy #get neighbor X,Y

                '''If neighbor is inside maze limits and is a wall:'''
                if nx >= 0 and ny >= 0 and nx < self.size and ny < self.size and self.grid[2*nx+1, 2*ny+1] == 1: 
                    self.grid[2*nx+1, 2*ny+1] = 0 #Make cell a path
                    self.grid[2*x+1+dx, 2*y+1+dy] = 0
                    stack.append((nx, ny)) #Add to backtracking stack

                    #self.gen_steps.append(self.grid.copy()) #remove the first '#' to enable maze generating animation. decided to omit this feature for now, as it causes the performance graph and the maze animation to go out of sync (both not activating on the same time)
                    break
            else:
                stack.pop() #remove item from stack
            
        
        
            #self.gen_steps.append(self.grid.copy())
        
        print("Maze Generated successfully!")    
        return self.grid
    
