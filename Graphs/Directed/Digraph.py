class Digraph:
    
    class AdjNode:
        def __init__(self, v):
            self.v = v  # Value of vertex
            self.next = None  # Points to the next adjacent vertex

    # Create a V-vertex digraph with no edges
    def __init__(self, V=None, file=None):
        if V:
            self.V = V
            self.E = 0
            self.digraph = [None] * self.v

        elif file:
            f = open(file, 'r')
            self.__init__(int(f.readline()))
            E = int(f.readline())
            for i in range(E):
                v, w = map(int, f.readline())
                self.addEdge(v, w)
                


    # Number of vertices in the digraph
    def num_vertices(self):
        return self.E

    # Number of edges in the digraph
    def num_edges(self):
        return self.E

    # Add directed edge v->w to digraph
    def addEdge(self, v, w):
        node = self.AdjNode(w)

        if self.digraph[v] is None:
            self.digraph[v] = node
        else:
            temp = self.digraph[v]
            while temp.next is not None:
                temp = temp.next

            temp.next = node

    # Vertices connected to v by edges pointing FROM v
    def adj(self, v):
        pass

    # Reverse of this digraph
    def reverse(self):
        pass

    # Print adjacency list representation of graph
    def print_graph(self):
        pass