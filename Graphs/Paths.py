from UndirectedGraph import UndirectedGraph

# Given a graph and a source vertex s, support queries of the
# form Is there a path from s to a given target vertex v? If so, find such a path.

class Paths:

    # Find paths in G from source s.
    def __init__(self, G, s):
        self.marked = [False] * G.num_vertices()
        self.edgeTo = [0] * G.num_vertices()
        self.s = s
        self.dfs(G, self.s)


    # Is there a path from s to v?
    def hasPathTo(self, v):
        return self.marked[v]
    
    # Path from s to v; null if no such path.
    def pathTo(self, v):

        # Maintain a stack which will contain the path to get from s to a specific vertex.
        stack = []

        while v != self.s:
            stack.append(v)
            v = self.edgeTo[v]

        # Top of the stack is the source, bottom of the stack is v.
        stack.append(self.s)

        return stack
        

    # Depth first search from v and remember the edge that takes us to each vertex the first time.
    def dfs(self, G, v):
        
        self.marked[v] = True

        node = G.adj(v)

        while node is not None:
            if not self.marked[node.V]:

                # To get to this vertex, we had to come from v. Think of s being the root of a tree, and it's branches are paths which all connect to s.
                self.edgeTo[node.V] = v
                self.dfs(G, node.V)

            node = node.next


myGraph = UndirectedGraph(None, 'tinyCG.txt')
s = 0
search = Paths(myGraph, s)


# Find the paths from s to every other vertex, if any path exists.
for i in range(myGraph.num_vertices()):
    print("{} to {}: ".format(s, i), end="")

    # Use [::-1] to reverse the stack.
    for w in search.pathTo(i)[::-1]:
        if search.hasPathTo(w):
            print("{}-".format(w), end="")
    print()


