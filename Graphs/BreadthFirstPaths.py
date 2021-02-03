from UndirectedGraph import UndirectedGraph

class BreadthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False] * G.num_vertices()
        self.edgeTo = [None] * G.num_vertices()
        self.s = s
        self.bfs(G, s)


    def bfs(self, G, s):
        pass


    def hasPathTo(self, v):
        pass

    def pathTo(self, v):
        pass
    

    