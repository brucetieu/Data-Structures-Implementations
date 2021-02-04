from UndirectedGraph import UndirectedGraph
import queue

class BreadthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False] * G.num_vertices()
        self.edgeTo = [None] * G.num_vertices()
        self.s = s
        self.bfs(G, self.s)


    def bfs(self, G, s):

        # Use a queue to perform bfs.
        q = queue.Queue(G.num_vertices())

        # Mark source as visited.
        self.marked[s] = True

        # Source goes first in the queue.
        q.put(s)

        while not q.empty():
            vertex = q.get()

            # Get first adjacent vertex to v.
            node = G.adj(vertex)

            while node is not None:

                if not self.marked[node.V]:
                    q.put(node.V)
                    self.marked[node.V] = True
                    self.edgeTo[node.V] = vertex  # save last edge on a shortest path

                node = node.next

        
    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        stack = []

        while v != self.s:
            stack.append(v)
            v = self.edgeTo[v]

        stack.append(self.s)

        return stack


myGraph = UndirectedGraph(None, 'tinyCG.txt')
s = 0
search = BreadthFirstPaths(myGraph, s)


# Find the paths from s to every other vertex, if any path exists.
for i in range(myGraph.num_vertices()):
    print("{} to {}: ".format(s, i), end="")

    # Use [::-1] to reverse the stack.
    for w in search.pathTo(i)[::-1]:
        if search.hasPathTo(w):
            print("{}-".format(w), end="")
    print()





    