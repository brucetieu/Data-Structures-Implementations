from UndirectedGraph import UndirectedGraph

class ConnectedComponents:
    '''Find the connected components of a graph'''

    # Preprocessing constructor
    def __init__(self, G):
        self.marked = [False] * G.num_vertices()
        self.id = [None] * G.num_vertices()
        self.num_cc = 0

        for v in range(G.num_vertices()):
            if not self.marked[v]:
                self.dfs(G, v)
                self.num_cc += 1
    
    
    # Are v and w connected?
    def connected(self, v, w):
        return self.id[v] == self.id[w]

    # Number of connected components
    def count(self):
        return self.num_cc

    # Component identifier for v (between 0 and count() - 1)
    def id(self, v):
        return self.id[v]

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.num_cc

        node = G.adj(v)

        while node is not None:
            if not self.marked[node.V]:
                self.dfs(G, node.V)

            node = node.next


myGraph = UndirectedGraph(None, 'tinyG.txt')
cc = ConnectedComponents(myGraph)

for v in range(myGraph.num_vertices()):
    print("{}: {}".format(v, cc.id[v]))

print("Number of connected components:", cc.count())