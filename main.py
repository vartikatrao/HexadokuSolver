from sudoku_connections import SudokuConnections
import os, sys
class SudokuBoard : 
    def __init__(self, filename) : 
        self.filename= filename
        self.board = self.getBoard(filename)
        self.sudokuGraph = SudokuConnections()
        self.mappedGrid = self.__getMappedMatrix() # Maps all the ids to the position in the matrix

    def __getMappedMatrix(self) : 

        matrix = [[0 for cols in range(16)] 
        for rows in range(16)]

        count = 1
        for rows in range(16) : 
            for cols in range(16):
                matrix[rows][cols] = count
                count+=1
        return matrix

    def getBoard(self, filename) : 
        board = []
        with open(filename, 'r') as f:
            for line in f:
                row = []
                for c in line.strip().split():
                    if c.isdigit():
                        row.append(int(c))
                    else:
                        row.append(ord(c) - 55)
                if len(row)>16 or len(row)<16:
                    print("Error: Invalid board size")
                    exit(0)
                board.append(row)
        if (len(board)>16 or len(board)<16):
            print("Error: Invalid board size")
            exit(0)
       
        return board
    
    

    def printBoard(self) : 
        
        for i in range(len(self.board)) : 
            if i%4 == 0  :
                print("  - - - - - - - - - - - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])) : 
                if j %4 == 0 :
                    print(" |  ", end = "")
                if j == 15 :
                    print(self.board[i][j] if self.board[i][j] <= 9 else chr(55+self.board[i][j])," | ")
                else : 
                    print(f"{ self.board[i][j] if self.board[i][j] <= 9 else chr(55+self.board[i][j]) } ", end="")
        print("  - - - - - - - - - - - - - - - - - - - - - - - - ")

    def is_Blank(self) : 
        
        for row in range(len(self.board)) :
            for col in range(len(self.board[row])) : 
                if self.board[row][col] == 0 : 
                    return (row, col)
        return None

    def graphColoringInitializeColor(self):
        """
        fill the already given colors
        """
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] # list of all the ids whos value is already given. Thus cannot be changed
        for row in range(len(self.board)) : 
            for col in range(len(self.board[row])) : 
                if self.board[row][col] != 0 : 
                    #first get the idx of the position
                    idx = self.mappedGrid[row][col]
                    #update the color
                    color[idx] = self.board[row][col] # this is the main imp part
                    given.append(idx)
        return color, given

    def solveGraphColoring(self, m =16) : 
        
        color, given = self.graphColoringInitializeColor()
        if self.__graphColorUtility(m =16, color=color, v =1, given=given) is None :
            print("No solution exists")
            sys.exit(0)
            return False
        count = 1
        for row in range(16) : 
            for col in range(16) :
                self.board[row][col] = color[count]
                count += 1
        return color
    
    def __graphColorUtility(self, m, color, v, given) :
        
        if v == self.sudokuGraph.graph.totalV+1  : 
            return True
        for c in range(1, m+1) : 
            if self.__isSafe2Color(v, color, c, given) == True :
                color[v] = c
                if self.__graphColorUtility(m, color, v+1, given) : 
                    return True
            if v not in given : 
                color[v] = 0

    def __isSafe2Color(self, v, color, c, given) : 
        
        if v in given and color[v] == c: 
            return True
        elif v in given : 
            return False

        for i in range(1, self.sudokuGraph.graph.totalV+1) :
            if color[i] == c and self.sudokuGraph.graph.isNeighbour(v, i) :
                return False
        return True

def validate_args(argv):
    # check correct number of arguments
    if len(argv) < 2 or len(argv) > 2:
        sys.exit('Requires exactly one argument (filename)')

    # check that argument ends in '.txt'
    if not argv[1].endswith('.txt'):
        sys.exit('Must supply plain text file (using .txt extension)')

    # check that argument is reference to valid file
    if not os.path.isfile(argv[1]):
        sys.exit('File not found: ' + argv[1])

def main(argv) : 
    validate_args(argv)
    filename= argv[1]
    print("Getting puzzle from "+filename)
    s = SudokuBoard(filename)
    print("BEFORE SOLVING ...")
    print("\n\n")
    s.printBoard()
    print("\nSolving ...")
    print("\n\n\nAFTER SOLVING ...")
    print("\n\n")
    s.solveGraphColoring(m=16)
    s.printBoard()

if __name__ == "__main__" : 
    main(sys.argv)
