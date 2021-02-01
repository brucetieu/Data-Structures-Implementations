from UndirectedGraph import UndirectedGraph

class DepthFirstSearch:
    '''Perform a dfs to search in a connected graph. 
    Algorithm:
        1. When visiting a vertex, mark it as visited
        2. Visit (recursively) all the vertices that are adjacent to it and that have not yet been marked.
    '''

    # Find the vertices in the graph that are connected to the source. 
    def __init__(self, G, source):
        self.marked = [False] * G.num_vertices()  # A list of booleans which tells us if a vertex is connected to an edge
        self.vertices_connected_to_source = 0    # Tells us how many vertices are connected to the source

        self.dfs(G, source)

    # Is there a path between the source vertex and the vertex v?
    def visited(self, v):
        return self.marked[v]

    # Returns the number of vertices connected to the source vertex
    def count(self):

        # If the number of vertices connected to the source != total number of vertices in the graph, then the graph is disconnected (ie consists of a set of connected components, which are maximal connected subgraphs.)
        return self.vertices_connected_to_source

    # Depth first search from v
    def dfs(self, G, v):

        # Mark vertex as visited
        self.marked[v] = True
        
        self.vertices_connected_to_source += 1

        # For each vertex you visited, get the adjacent nodes
        node = G.adj(v)

        # Do a dfs on that adjacent node (vertex), if it has not yet been visited
        while node is not None:
            if self.marked[node.V] is False:
                self.dfs(G, node.V)
            
            node = node.next



myGraph = UndirectedGraph(None, 'tinyG.txt')
search = DepthFirstSearch(myGraph, 0)

for v in range(myGraph.num_vertices()):
    if search.visited(v):
        print(v, " ", end="")

print("\n")
print("Number of vertices connected to the source:", search.count())



        


