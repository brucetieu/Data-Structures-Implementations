from UndirectedGraph import UndirectedGraph
import queue

class BreadthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False] * G.num_vertices()
        self.edgeTo = [None] * G.num_vertices()
        self.s = s
        self.bfs(G, self.s)


    def bfs(self, G, v):

        # Use a queue to perform bfs.
        q = queue.Queue(G.num_vertices())

        # Mark source as visited.
        self.marked[v] = True

        # Source goes first in the queue.
        q.put(v)

        while not q.empty():
            vertex = q.get()

            # Get first adjacent vertex to v.
            node = vertex.adj(v)

            # Enqueue remaining adjacent vertices, mark them as visited if they haven't yet been visited, and remember where they came from.
            while node is not None:

                if not self.marked[node.V]:
                    q.put(node.V)
                    self.marked[node.V] = True
                    self.edgeTo[node.V] = v

                node = node.next

        



    def hasPathTo(self, v):
        pass

    def pathTo(self, v):
        pass


    