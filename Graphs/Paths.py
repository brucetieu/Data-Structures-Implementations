# Given a graph and a source vertex s, support queries of the
# form Is there a path from s to a given target vertex v? If so, find such a path.

class Paths:

    # Find paths in G from source s.
    def __init__(self, G, s):
        self.marked = [False] * G.num_vertices()
        self.edgeTo = [None] * G.num_vertices()
        self.s = s
        self.dfs(G, self.s)


    # Is there a path from s to v?
    def hasPathTo(self, v):
        return self.marked[v]
    
    # Path from s to v; null if no such path.
    def pathTo(self, v):

        stack = []

        while v != self.s:
            stack.append(v)
            v = self.edgeTo[v]

        stack.append(self.s)

        return stack
        

    # Depth first search from v and remember the edge that takes us to each vertex the first time.
    def dfs(self, G, v):
        
        self.marked[s] = True

        node = G.adj(v)

        while node is not None:
            if not self.marked[node.V]:
                self.edgeTo[node.V] = v
                self.dfs(node.V)

            node = node.next


