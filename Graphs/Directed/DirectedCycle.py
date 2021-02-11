from Digraph import Digraph

class DirectedCycle:

    # Cycle finding constructor
    def __init__(self, G):
        self.marked = [None] * G.num_vertices()
        self.onStack = [False] * G.num_vertices()  # Vertices on the recursive call stack
        self.isCycle = False  

        for v in range(G.num_vertices()):
            self.dfs(G, v)

    def dfs(self, G, v):
        
        self.marked[v] = True

        # Current vertex is on the stack
        self.onStack[v] = True

        node = G.adj(v)

        while node:

            # If we ever find a directed edge v->w to a vertex w that is on that stack, we have found a cycle
            if self.onStack[node.v]: 
                self.isCycle = True
            if not self.marked[node.v]:
                self.dfs(G, node.v)
            
            node = node.next
        
        # reset
        self.onStack[v] = False

    # Does G have a directed cycle?
    def hasCycle(self):
        return self.isCycle



# Test
myGraph = Digraph(None, 'tinyDG.txt')
myGraph2 = Digraph(None, 'tinyDAG.txt')

directed_cycle = DirectedCycle(myGraph)
directed_cycle2 = DirectedCycle(myGraph2)

print(directed_cycle.hasCycle())
print(directed_cycle2.hasCycle())
