class DepthFirstSearch:
    '''Perform a dfs to search in a connected graph. 
    Algorithm:
        1. When visiting a vertex, mark it as visited
        2. Visit (recursively) all the vertices that are adjacent to it and that have not yet been marked.
    '''

    # Find the vertices in the graph that are connected to the source. 
    def __init__(self, G, source):
        self.marked = [False] * G.num_vertices()  # A list of booleans which tells us if a vertex is connected to an edge
        self.count = 0    # Tells us how many vertices are connected to the source

        self.dfs(G, source)


    def marked(self, v):
        return self.marked[v]

    def count(self):
        return self.count

    def dfs(self, G, v):
        self.marked[v] = True
        
        self.count += 1

        for w in range(G.adj(v)):
            if self.marked[w] is False:
                self.dfs(G, w)
        


