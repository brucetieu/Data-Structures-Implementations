from UndirectedGraph import UndirectedGraph

class DepthFirstSearch:
    '''Perform a dfs to search in a connected graph. 
    Algorithm:
        1. When visiting a vertex, mark it as visited
        2. Visit (recursively) all the vertices that are adjacent to it and that have not yet been marked.
    '''

    # Find the vertices in the graph that are connected to the source. 
    def __init__(self, G, source, method):
        self.marked = [False] * G.num_vertices()  # A list of booleans which tells us if a vertex is connected to an edge
        self.vertices_connected_to_source = 0    # Tells us how many vertices are connected to the source
        self.method = method

        if self.method == "recursive":
            self.dfs(G, source)
        elif self.method == "iterative":
            self.dfs_iterative(G, source)

    # Is there a path between the source vertex and the vertex v?
    def visited(self, v):
        return self.marked[v]

    # Returns the number of vertices connected to the source vertex
    def count(self):

        if self.method == "recursive":

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

    # Depth first search from v using a stack (non recursive)
    def dfs_iterative(self, G, v):
        stack = []

        # Push source node to stack
        stack.append(v)

        while stack:

            # Pop last element in stack and mark it as visited
            vertex = stack.pop()
        
            if self.marked[vertex] is False:
                self.marked[vertex] = True

            # Then, obtain all adjacent vertices to that vertex
            node = G.adj(vertex)
            
            # If their nodes haven't been visited before, add them to the stack so that they can be visited
            while node is not None:
                if self.marked[node.V] is False:
                    stack.append(node.V)
                
                node = node.next



myGraph = UndirectedGraph(None, 'tinyG.txt')
search = DepthFirstSearch(myGraph, 9, "recursive")
search2 = DepthFirstSearch(myGraph, 0, "iterative")

print("Recursive")
# Find the vertices in the graph that are connected to the source.
for v in range(myGraph.num_vertices()):
    if search.visited(v):
        print(v, " ", end="")

print("\n")
print("Number of vertices connected to the source:", search.count())

print("\n" + "Iterative")
for v in range(myGraph.num_vertices()):
    if search2.visited(v):
        print(v, " ", end="")

print("\n")





        


