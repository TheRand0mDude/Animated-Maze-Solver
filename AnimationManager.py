#Animation_Manager

import matplotlib.pyplot as plt
import numpy as np
  
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
cmap = ListedColormap(["blue", "purple", "yellow", "black", "red",])


class Animation_Manager():

    def __init__(self): #Init animation manager
        
                            
        self.grid = None
        self.gen_steps = []
        self.steps = []
        self.times = []
        
    

    def animate_generation(self,grid,steps,times,optimal_steps,optimal_times):

        self.steps = steps #Sets these values so we could take them from A_Star()
        self.times = times
        self.optimal_steps = optimal_steps
        self.optimal_times = optimal_times

        if not hasattr(self, "fig"): #Init fig only once (if fig doesn't have a value already)
            self.fig, self.axis = plt.subplots(1,2,figsize = (4,4),dpi = 100) #Init both subplots

            #maze
            self.axis[0].axis("off")

            #Performance Graph
            self.axis[1].grid()
            self.axis[1].set_title("Steps vs Time ratio") 
            self.axis[1].set_ylabel("Steps")
            self.axis[1].set_xlabel("Time (seconds)")
            

            #Set limits
            self.axis[1].set_xlim(-0.001, max(times) * 1.1)  
            self.axis[1].set_ylim(-0.001, max(steps) * 1.1)

            #Improve subplot spacings 
            self.fig.tight_layout() 

            #Plot
            (self.algorithm_path_line,)=self.axis[1].plot([], [], label="A* path", color="Black")
            (self.optimal_path_line,)=self.axis[1].plot([], [], label="Best path", color="orange")
            
            self.img = self.axis[0].imshow(grid, cmap=cmap, vmin=0, vmax=4)
        
        def update(frame):
            '''This is our update function that runs every frame. It updates both the maze and the performance graph'''

            #Update maze
            self.img.set_data(self.gen_steps[frame])
            
            #If A* did not finish - Draw A* path
            if frame < len(self.steps):
                self.algorithm_path_line.set_data(self.times[:frame], self.steps[:frame])

            if frame >= len(self.steps): #If A* finished - Draw best path
                optimal_frame = frame - len(self.times)
                if optimal_frame < len(self.optimal_steps):
                    self.optimal_path_line.set_data(self.optimal_times[:optimal_frame], self.optimal_steps[:optimal_frame]) 
            '''
            Note: Notice the jagged graph. Because our time measurements are so accuratly small (as they need to be), we update our
            times as quickly as possible.
            '''
            #Ajust Axis
            self.axis[1].relim()
            self.axis[1].autoscale_view()
            
            #Force canvas to update
            self.fig.canvas.draw_idle()
            self.fig.canvas.flush_events()
            
            

            return[self.img]
        

        '''Animate!'''
        animation = FuncAnimation(self.fig,update, frames=range(0,len(self.gen_steps),len(self.grid)//10+1), blit=True,interval = 25, repeat = False)

        #animation.save("MazeSolver.gif", writer='FFMpegWriter',fps=10) #Remove '#' to init gif, slow process.

        plt.show()


#update every frame