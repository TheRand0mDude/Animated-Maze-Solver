'''Hi! this is my very first github project. Feedback would be appreciated! '''
from DfsMaze import dfsMaze
from AStar import Astar
from AnimationManager import Animation_Manager

               
        
if __name__ == "__main__": #Ensure the program runs when executed

    #Allow user to dictate maze size
    C = dfsMaze(int(input("Insert Maze Size: (Example - 100) "))//2-1) 
    grid = C.GenerateMaze()


    #Set as object class 
    A = Astar()

    #Share parameters between class objects
    A.grid = C.grid
    A.gen_steps = C.gen_steps

    A.A_star()
    
    Am = Animation_Manager()
    Am.grid = A.grid
    Am.gen_steps = A.gen_steps

    #Init Animation manager with all the parameters needed from A_star()
    Am.animate_generation(grid,steps=A.steps,times=A.times,optimal_steps=A.optimal_steps,optimal_times=A.optimal_times)




