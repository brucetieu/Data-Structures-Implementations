from Digraph import Digraph

class DirectedCycle:

    # Cycle finding constructor
    def __init__(self, G):
        self.marked = [None] * G.num_vertices()
        self.onStack = [False] * G.num_vertices()  # Vertices on the recursive call stack
        self.cycles = []  # Store the cycles

    def dfs(self, G, v):
        pass
    
    # Does G have a directed cycle?
    def hasCycle(self):
        return len(self.cycles) > 0

    # An iterable containing all vertices on the cycle
    def cycle(self):
        return self.cycles
