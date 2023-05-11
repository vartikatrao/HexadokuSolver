from graph import Graph

class SudokuConnections : 
    def __init__(self) :  # constructor

        self.graph = Graph() # Graph Object

        self.rows = 16
        self.cols = 16
        self.total_blocks = self.rows*self.cols 

        self.__generateGraph() # Generates all the nodes
        self.connectEdges() # connects all the nodes acc to sudoku constraints

        self.allIds = self.graph.getAllNodesIds() # storing all the ids in a list

        

    def __generateGraph(self) : 
        """
        Generates nodes with id from 1 to 256
        Both inclusive
        """
        for idx in range(1, self.total_blocks+1) : 
            _ = self.graph.addNode(idx)

    def connectEdges(self) : 
        """
        Connect nodes according to Sudoku Constraints : 

        # ROWS

       from start of each id number connect all the 
       successive numbers till you reach a multiple of 16


        # COLS 

        from start of id number. +16 for each connection
        till you reach a number >= 241 and <= 256

        # BLOCKS
        Connect all the elements in the block which do not 
        come in the same column or row.
        1   2   3    4
        17  18  19   20
        33  34  35   36
        49  50  51   52

        1 -> 18,19,20,34,35,26,50,51,52
        similarly for all other elements 

        """
        matrix = self.__getGridMatrix()
       
        head_connections = dict() # head : connections

        for row in range(16) :
            for col in range(16) : 
                
                head = matrix[row][col] #id of the node
                connections = self.__whatToConnect(matrix, row, col)
                
                head_connections[head] = connections
        # connect all the edges

        self.__connectThose(head_connections=head_connections)
        
    def __connectThose(self, head_connections) : 
        for head in head_connections.keys() : #head is the start idx
            connections = head_connections[head]
            for key in connections :  #get list of all the connections
                for v in connections[key] : 
                    self.graph.addEdge(src=head, dst=v)

 
    def __whatToConnect(self, matrix, rows, cols) :

        """
        matrix : stores the id of each node representing each cell

        returns dictionary

        connections - dictionary
        rows : [all the ids in the rows]
        cols : [all the ids in the cols]
        blocks : [all the ids in the block]
        
        ** to be connected to the head.
        """
        connections = dict()

        row = []
        col = []
        block = []

        # ROWS
        for c in range(cols+1, 16) : 
            row.append(matrix[rows][c])
        
        connections["rows"] = row

        # COLS 
        for r in range(rows+1, 16):
            col.append(matrix[r][cols])
        
        connections["cols"] = col

        # BLOCKS
        
        if rows%4 == 0 : 

            if cols%4 == 0 :
                
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+2][cols+3])
                block.append(matrix[rows+3][cols+1])
                block.append(matrix[rows+3][cols+2])
                block.append(matrix[rows+3][cols+3])

            elif cols%4 == 1 :
                
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+3][cols-1])
                block.append(matrix[rows+3][cols+1])
                block.append(matrix[rows+3][cols+2])

                
            elif cols%4 == 2 :
                
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])                
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])                
                block.append(matrix[rows+3][cols-2])
                block.append(matrix[rows+3][cols-1])
                block.append(matrix[rows+3][cols+1])  

            elif cols%4 == 3 :
                
                block.append(matrix[rows+1][cols-3])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])                
                block.append(matrix[rows+2][cols-3])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])                
                block.append(matrix[rows+3][cols-3])
                block.append(matrix[rows+3][cols-2])
                block.append(matrix[rows+3][cols-1])  
        
        elif rows%4 == 1 :
            
            if cols%4 == 0 :
                
                
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+2][cols+3])

            elif cols%4 == 1 :
                
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])

                
            elif cols%4 == 2 :
                
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])

        elif rows%4 == 2 :
            
            if cols%4 == 0 :
                
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-2][cols+3])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])

            elif cols%4 == 1 :
                
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                
            elif cols%4 == 2 :
                
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])

            elif cols%4 == 3 :
                block.append(matrix[rows-2][cols-3])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-3])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-3])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
        
        elif rows%4 == 3 :
            
            if cols%4 == 0 :
                
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-3][cols+2])
                block.append(matrix[rows-3][cols+3])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-2][cols+3])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])

            elif cols%4 == 1 :
                
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-3][cols+2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                
            elif cols%4 == 2 :
                
                block.append(matrix[rows-3][cols-2])
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])

            elif cols%4 == 3 :
                block.append(matrix[rows-3][cols-3])
                block.append(matrix[rows-3][cols-2])
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-2][cols-3])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-3])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
        
        connections["blocks"] = block
        return connections

    def __getGridMatrix(self) : 
        matrix = [[0 for cols in range(self.cols)] 
        for rows in range(self.rows)]

        count = 1
        for rows in range(16) :
            for cols in range(16):
                matrix[rows][cols] = count
                count+=1
        return matrix

