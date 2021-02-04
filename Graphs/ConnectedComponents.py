from UndirectedGraph import UndirectedGraph

class ConnectedComponents:
    '''Find the connected components of a graph'''

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
        return self.id[v] == self.id[w]

    # Number of connected components
    def count(self):
        return self.count

    # Component identifier for v (between 0 and count() - 1)
    def id(self, v):
        return self.id[v]

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count

        node = G.adj(v)

        while node is not None:
            if not self.marked[node.V]:
                self.dfs(node.V)

            node = node.next
