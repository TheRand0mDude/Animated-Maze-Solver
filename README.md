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


## How it works:
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
        
  

        0 - blue - empty paths
        1 - purple - walls
        4 - orange - Start/End
        3 - black - checked path by A*
        2 - yellow - Best possible path
![image](https://github.com/user-attachments/assets/0e459892-7278-489e-b1d1-b0fc0bb48c17)


## how to install

insert explanation to use -pip install matplotlib and numpy

### lessons learned:

text here haha
