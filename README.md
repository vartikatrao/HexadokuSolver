# HexadokuSolver
A 16x16 Sudoku solver made using graph coloring technique. <br>
Reference: https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072

## Graph Coloring
Graph Coloring is the assignment of colours to vertices of a graph such that no
two adjacent vertices have the same colour. Although a graph can have more
than one possible colouring, the goal is to use the minimum number of colours
possible.

## Method 
A Sudoku puzzle (nxn) can be thought of as a undirected graph with n
2 vertices,one for each cell, and two vertices are connected by an edge if they cannot be
assigned the same value, i.e., all cells in the same row, column or block will have
edges between their corresponding vertices. <br>
#### Goal:
to assign colours to each vertex, which correspond to the numbers from 1
to n, such that no two adjacent vertices have the same colour.
The optimal solution in the case of the Sudoku puzzle is to find a colouring using
only n colours (each number representing a colour).<br>
#### Proposed solution:
Initialize the possible colours for each vertex based on the
constraints of the Sudoku puzzle (where some spaces are prefilled), and then use
a backtracking algorithm to assign colours to each vertex one at a time. If it
encounters a vertex where no valid colour can be assigned, it backtracks to the
previous vertex and tries a different colour. The process continues until all
vertices have been assigned a valid colour, or until it exhausts all possible
combinations of colours without finding a valid solution. Once a valid solution is
found, the colours assigned to the vertices correspond to the correct numbers
to fill in each cell of the Sudoku grid.
However, not all Sudoku puzzles can be solved using graph colouring. Some
puzzles require more advanced techniques such as guessing or trial and error.
This might happen as the algorithm cannot find a colouring that uses only nine
colours.
<br><br> 
An example sudoku puzzle in graph form: (source:
https://networkx.org/nx-guides/content/generators/sudoku.html)
![image](https://github.com/vartikatrao/HexadokuSolver/assets/100116788/5e11c61e-65eb-472f-9f33-49f2bf5ae93c)
