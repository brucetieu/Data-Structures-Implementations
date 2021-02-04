from UndirectedGraph import UndirectedGraph

class ConnectedComponents:

    # Preprocessing constructor
    def __init__(self, G):
        self.marked = [False] * G.num_vertices()
        self.id = [None] * G.num_vertices()
        self.count = 0

        for v in range(G.num_vertices()):
            if not self.marked[v]:
                self.dfs(G, v)
                self.count += 1
    

    
    # Are v and w connected?
    def connected(self, v, w):
        pass

    # Number of connected components
    def count(self):
        pass

    # Component identifier for v (between 0 and count() - 1)
    def id(self, v):
        pass

    def dfs(self, G, v):
        pass
