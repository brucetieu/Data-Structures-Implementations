from Digraph import Digraph

class DirectedDFS:

    def __init__(self, G, source=None, sources=None):
        self.marked = [False] * G.num_vertices()

        # Single source reachability: find all vertices in G that are reachable from s
        if source is not None:
            self.source = source
            self.dfs(G, self.source)

        # Multiple source reachability: find vertices in G that are reachable from a set of sources
        elif sources is not None:
            self.sources = sources

            for s in self.sources:
                if not self.marked[s]:
                    self.dfs(G, s)

    def visited(self, v):
        return self.marked[v]

    def dfs(self, G, s):
        self.marked[s] = True

        node = G.adj(s)

        while node != None:
            if not self.marked[node.v]:
                self.dfs(G, node.v)
            node = node.next


# test client

myDG = Digraph(None, "tinyDG.txt")
source = DirectedDFS(myDG, 1, None)
sources = DirectedDFS(myDG, None, [1,2,6])

# Print out the nodes that can be reached from the source
for v in range(myDG.num_vertices()):
    if sources.visited(v):
        print("{} ".format(v), end="")
print("\n")