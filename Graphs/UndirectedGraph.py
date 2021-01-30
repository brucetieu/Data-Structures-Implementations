

class UndirectedGraph:

    class  AdjNode:
        '''This represents all the adjacent nodes a vertex is adjacent to in the adjacency list'''
        def __init__(self, V):
            self.V = V  # Value of vertex
            self.next = None # Pointer to the next node adjacent to the current vertex

    def __init__(self, V=None, file=None):
        if V:
            self.V = V  # Number of vertices
            self.E = 0  # Number of edges
            self.undirectedGraph = [None] * V
        
        elif file:
            
            f = open(file, 'r')
            self.__init__(int(f.readline()))
            self.E = int(f.readline())


