from Digraph import Digraph

class DirectedDFS:

    def __init__(self, G, source=None, sources=None):
        
        # Single source reachability
        if source:
            self.marked = [False] * G.num_vertices()
            self.dfs(G, source)

        # Multiple source reachability
        elif sources:
            self.marked = [False] * G.num_vertices()
            
            for s in sources:
                if not self.marked[s]:
                    self.dfs(G, s)

    def visited(self):
        pass

    def dfs(self, G, s):
        pass