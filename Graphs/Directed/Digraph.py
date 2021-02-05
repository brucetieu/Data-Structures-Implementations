class Digraph:
    
    class AdjNode:
        pass

    # Create a V-vertex digraph with no edges
    def __init__(self, V=None, file=None):
        pass

    # Number of vertices in the digraph
    def num_vertices(self):
        pass

    # Number of edges in the digraph
    def num_edges(self):
        pass

    # Add directed edge v->w to digraph
    def addEdge(self, v, w):
        pass

    # Vertices connected to v by edges pointing FROM v
    def adj(self, v):
        pass

    # Reverse of this digraph
    def reverse(self):
        pass

    # Print adjacency list representation of graph
    def print_graph(self):
        pass