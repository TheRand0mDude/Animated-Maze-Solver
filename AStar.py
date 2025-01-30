#A_Star algorithm
import numpy as np
import random
import time 
import matplotlib.pyplot as plt
from queue import PriorityQueue

class Astar():

    def __init__(self): #Init class, get grid from DfsMaze and gen_steps for animation
        
        
        self.grid = None
        self.gen_steps = []    

    def h(self,cell1,cell2): #For A*, manhattan distance between 2 cells
        x1,y1 = cell1
        x2, y2 = cell2

        return abs(x1-x2) + abs(y1-y2)
    
    def get_end(self):
        # Randomly select an end point, making sure it's not a wall and not the start (0,0)
        while True:
            self.end_x = random.randrange(1, self.grid.shape[0] - 1)
            self.end_y = random.randrange(1, self.grid.shape[1] - 1)
            
            # Check if the selected endpoint is not a wall (does not have a value of 1) and if its not equal to the starting point
            if self.grid[self.end_x, self.end_y] == 0 and (self.end_x, self.end_y) != (1, 0):
                break
        self.grid[self.end_x,self.end_y] = 4 #Set end value to be 4        
        return self.end_x, self.end_y
    

    def A_star(self,):
        '''
        A* is an informed search Pathfinding algorithm, that aims to find a path to a given node that has the lowest cost possible.
        Specifically, A* selects the path that minimizes:
        f(n)=g(n)+h(n)

        where:

        g(n)- is the cost from the start node to the current node.
        h(n)- is the estimated cost from the current node to the goal (heuristic).

        And this is done together with an open-set (priority queue), that it uses to
        perform the repeated selection of minimum (estimated) cost nodes to expand.

        Each iteration, The item with the lowest f(n) in the open-set is removed, and the F,G values of its neighbors are updated.
        this is until a removed node is a goal node.
        
        Also, A* makes the grid consist of:

        0 - empty paths
        1 - walls
        4 - Start/End
        3 - checked path by A*
        2- Best possible path

        '''
        ##update_callback = None
        
        start = (1,0) #Set start X,Y values
        self.get_end() #Get random end X,Y values
        end = (self.end_x,self.end_y)

        self.steps = [0]   #Init steps, times as 0 - this will be later used for the performance graph
        self.times = [0.0]

        self.optimal_steps = []
        self.optimal_times = [] 
        #self.grid[self.end_x,self.end_y] = 0

        step = 0
        '''for every cell in the grid that is not equal to one we assign a dictionary value of infinite!'''
        self.g_score = {cell:np.inf for cell in np.ndindex(self.grid.shape) if self.grid[cell] == 0 or self.grid[cell] == 4}
        self.g_score[start]=0 # G score increases every step taken

        '''same thing as g_score'''
        self.f_score = {cell:np.inf for cell in np.ndindex(self.grid.shape) if self.grid[cell] == 0 or self.grid[cell] == 4}
        self.f_score[start]=self.h(start,end) #manhattan distance between start & end 

        open = PriorityQueue() #Setup priority queue
        open.put((self.h(start,end)+0,self.h(start,end),start)) # (f + g cost of start (g=0), huristic cost, start X,Y)

        reverse_path ={} #Stores parents refrence for backtracking
        checked_path = [] 

        
        start_time = time.time() #Start timing the search process
        while not open.empty():
            currentCell = open.get()[2] # Get the node with the lowest F-score
            step += 1 # Increment step counter
            checked_path.append(currentCell)

            if currentCell == end:
                
                print("Path solved!")
                break

            #Store performance metrics
            self.steps.append(step)
            self.times.append(time.time() - start_time)

            
            # Define valid movement directions (N, S, W, E)
            neighbors = [
                (currentCell[0] + dx, currentCell[1] + dy)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= currentCell[0] + dx < self.grid.shape[0]
                and 0 <= currentCell[1] + dy < self.grid.shape[1]
                and self.grid[currentCell[0] + dx, currentCell[1] + dy] == 0 or self.grid[currentCell[0] + dx, currentCell[1] + dy] == 4 #ensure valid move
            ]
            for neighbor in neighbors:
                temp_g_score = self.g_score[currentCell]+1 #Calculate new G_score 
                temp_f_score = self.g_score[currentCell]+self.h(neighbor,end) #Calculate new F_score
                
                if temp_f_score < self.f_score[neighbor]: #If found a better path:
                    self.g_score[neighbor] = temp_g_score
                    self.f_score[neighbor] = temp_f_score
                    open.put((temp_f_score,self.h(neighbor,end),neighbor)) #Add to priority queue
                    reverse_path[neighbor] = currentCell #Store path information
                    
        #Mark as visited cells for the animation
        for cell in checked_path:
            if self.grid[cell] != 2:
               self.grid[cell] = 3 #Mark as visited
            self.gen_steps.append(np.copy(self.grid)) #Store updated grid state
            
        forward_path = {}
        cell = end
        backtrack_time = time.time()
        self.grid[start] = 4 #Mark start
        self.grid[end] = 4 #Mark en

        while cell != start:
            self.optimal_steps.append(len(forward_path)) #Store optimal path step count
            
            forward_path[reverse_path[cell]] = cell 
            cell = reverse_path[cell] #Move to parent node          
            self.grid[cell] = 2 #Mark optimal path 


            '''Pause_time exists so we could get that accurate time for the optimal path taken.
            This is due to that storing the updated grid state for the animation
            slows the optimal time by a few miliseconds, enough that the optimal path will compute slower 
            Then the actual path A* takes '''

            pause_time = time.time()
            self.gen_steps.append(np.copy(self.grid)) #Store updated grid state
            backtrack_time += (time.time() - pause_time)
            self.optimal_times.append(time.time() - backtrack_time)
            #update_callback(self.grid)
            



        self.gen_steps.append(np.copy(self.grid))
        #Finalize grid markings
        self.grid[start] = 4 #Mark start
        self.grid[end] = 4 #Mark end
        
        #Checks for debugging
        print("A* Steps taken: ",step)
        print("Best path steps taken: ",len(forward_path))
        print("A* calulating time: ",self.times[-1])
        print("Best path calculating time: ",self.optimal_times[-1])
        
       
        
        return forward_path, self.grid,self.steps, self.times, self.optimal_steps, self.optimal_times #return for later use
    
    