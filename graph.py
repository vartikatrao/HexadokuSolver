
class Node : 
    
    def __init__(self, idx, data = 0) : # Constructor   
        """
        Constructor for the Node class that initializes the node's ID, data, and an empty dictionary to store its neighbors.
        """
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self, neighbour , weight = 0) :
        """
        Adds a neighbor to the node's dictionary of neighbors with an optional weight value.
        neighbour : Node Object
        weight : Default Value = 0
        adds the (neightbour_id : wt) pair into the dictionary
        """
        if neighbour.id not in self.connectedTo.keys() :  
            self.connectedTo[neighbour.id] = weight

    # setter
    def setData(self, data) : 
        #
        self.data = data 

    #getter
    def getConnections(self) : 
        # Getter method for the node's dictionary of neighbor IDs
        return self.connectedTo.keys()

    def getID(self) : 
        #Getter method for the node's ID
        return self.id
    
    def getData(self) :
        #Getter method for the node's data 
        return self.data

    def getWeight(self, neighbour) : 
        #Getter method for the weight value of a neighbor
        return self.connectedTo[neighbour.id]

    def __str__(self) : 
        #Returns a string representation of the node's data and its connected neighbors.
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connectedTo])

class Graph : 

    totalV = 0 # total vertices in the graph
    
    def __init__(self) : 
        """
        Constructor for the Graph class that initializes an empty dictionary to store nodes.
        """
        self.allNodes = dict()

    def addNode(self, idx) : 
        """ Adds a node with the given ID to the graph. """
        if idx in self.allNodes : 
            return None
        
        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data) : 
        """ Sets the data value of a node with the given ID """
        if idx in self.allNodes : 
            node = self.allNodes[idx]
            node.setData(data)
        else : 
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt = 0) : 
        """
        Adds edge between 2 nodes
        Undirected graph

        src = node_id = edge starts from
        dst = node_id = edge ends at
        """
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)
    
    def isNeighbour(self, u, v) : 
        """
        checks if neighbour exists or not
        """
        if u >=1 and u <= 256 and v >=1 and v<= 256 and u !=v : 
            if v in self.allNodes[u].getConnections() : 
                return True
        return False



    def printEdges(self) : 
        """ print all edges """
        for idx in self.allNodes :
            node =  self.allNodes[idx]
            for con in node.getConnections() : 
                print(node.getID(), " --> ", 
                self.allNodes[con].getID())
    
    # getter
    def getNode(self, idx) : 
        """ Returns the node with the given ID."""
        if idx in self.allNodes : 
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self) : 
        """ Returns a list of all the node IDs in the graph."""
        return self.allNodes.keys()