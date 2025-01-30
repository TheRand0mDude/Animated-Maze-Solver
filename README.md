# Animated-Maze-Solver
An Animated maze solver program that solves randomly generated perfect mazes using A* algorithm.

This is my very first project on github, feedback would be appreciated :D

## Features:
- Generates a random perfect maze using Depth-first search (DFS) algorithm
- User-ajustable Maze sizes
- Solves said maze with A* algorithm
- Visualised solving process
- A* marks the best possible path for the maze
- A performance graph that compares steps vs running times for both the path A* takes and the best possible path  
![MazeSolver](https://github.com/user-attachments/assets/6a9356ce-70e8-4aab-bcfd-aab71c8ceac3)


## How it works - in depth explaination :

Our program consists of the following py files:

│── main.py         # Entry point of the program
│── DfsMaze.py         # Maze generation 
│── AStar.py       # BFS solving algorithm
│── AnimationManager.py    # Handles visualization

**About DFS:**
The maze is generated using a randomized recursive backtracking algorithm called **Depth-First-Search (DFS)**. The process starts with an empty grid, progressively carving out paths while ensuring there’s a single connected solution. Each iteration of the algorithm loop, DFS carves out paths in random directions, and each time a grid square is added to a stack. If DFS reaches a state where from a cell there are no valid
nodes to continue, it removes cells from the stack until a cell with valid paths is found. Once the stack is empty, The algorithm stops.

**About the Animation Manager:**
The animation is managed using matplotlib.animation.FuncAnimation. Every time a cell in the maze grid is modified (during solving), a copy of the current grid state is stored as a frame update. These frames are then rendered sequentially, creating a smooth real-time visualization of the maze's progress. This ensures that each step of the algorithm is visually represented without skipping important transitions.

**More about A Star**:

***A Star is an informed search Pathfinding algorithm**, that aims to find a path to a given node that has the lowest cost possible.
Specifically, A* selects the path that minimizes:
        
        f(n)=g(n)+h(n)
 where:

        g(n)- is the cost from the start node to the current node.
        h(n)- is the estimated cost from the current node to the goal (heuristic).
And this is done together with an open-set (priority queue), that it uses to
perform the repeated selection of minimum (estimated) cost nodes to expand.

Each iteration, The item with the lowest f(n) in the open-set is removed, and the F,G values of its neighbors are updated.
This is until a removed node is a goal node.


Our maze is made of of a numpy 2D array that contains different numbers that represents walls, paths, ect.
We display the maze using ```plt.imshow``` with the following colormap:  

        0 - blue - empty paths
        1 - purple - walls
        4 - orange - Start/End
        3 - black - checked path by A*
        2 - yellow - Best possible path

![image](https://github.com/user-attachments/assets/0e459892-7278-489e-b1d1-b0fc0bb48c17)
![image](https://github.com/user-attachments/assets/ebc93868-fa4e-4eab-b9f8-65bcbf9a073f)


### Performance Graph Explained
Alongside the animation, we display a performace graph that compares steps VS running time for both A* and the best optimal path.
Here's an example of how the graph might look like:

![image](https://github.com/user-attachments/assets/bf38c49a-434d-41d8-9868-3c613ee019cc)

#### Graph Key:
        The black line - Entirety of A*
        The orange line - Best path only        

#### Key takeaways:
- **Notice the jagged lines**. This is because we measure really, really small time increments for both paths. A* is a _fast_ Algorithm.
  The jagged shape is a product of this: as we try to update the graph as much as possible, because A* is so fast there's already a big difference in the amount of steps recorded,
  hence the jagged shape.
  
- **Notice the orange line is much shorter, and steeper then the black**. This is due that computing the best path possible takes considerably less computing power then A* itself (relative to A*, sometimes just 10%!)
  Of course, there's no way for to know ahead of time what the best path is, and we need to apply A* to calulate that.
  The optimal solution always takes less steps then A*.
  
  Another thing worth mentioning is that our time calculation excludes the computing time for the animation process. For every value we change to 'Best path' (2) on the grid, we save the current grid state as a frame.
  Including this process our time calculation results in a best path that takes more time to calculate then A*, (A longer orange line then black) which is not ideal.

### how to install
You need to have python 3.12+ installed.
make sure you have matplotlib, numpy installed.
if not, write in terminal " ```--pip install matplotlib``` " and ```--pip install numpy```

## Final thoughts

This was a very fun project to work on! :D, I learned alot, and after a few months of not programming, it got me back up to speed!
In the future, id like to add an option to animate the maze generation process itself, and to implament that in the performance graph. This change
shouldn't even take too long.

Thank you for reading!

