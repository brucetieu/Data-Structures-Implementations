

class UndirectedGraph:

    class  AdjNode:
        '''This represents all the adjacent nodes a vertex is adjacent to in the adjacency list'''
        def __init__(self, V):
            self.V = V  # Value of vertex
            self.next = None # Pointer to the next node adjacent to the current vertex

    def __init__(self, V=None, file=None):
        if V:
            self.V = V  # Number of vertices
            self.E = 0  # Number of edges
            self.undirectedGraph = [None] * V  # Represent empty graph as empty list with V number of vertices
        
        elif file:
            

            f = open(file, 'r')

            # Create an empty graph with the number of vertices in the first line
            self.__init__(int(f.readline()))

            # Number of edges is in the second line
            self.E = int(f.readline())

            # Add edge to each vertex
            for i in range(self.E):
                v, w = map(int, f.readline().split())
                self.addEdge(v, w)


    # Add edge v-w (each edge appears twice)
    def addEdge(self, v, w):

        # Add w to v.
        node = self.AdjNode(w)

        if self.undirectedGraph[v] is None:
            self.undirectedGraph[v] = node
        else:
            temp = self.undirectedGraph[v]

            while temp.next != None:
                temp = temp.next
            temp.next = node

        # Add v to w.
        node = self.AdjNode(v)

        if self.undirectedGraph[w] is None:
            self.undirectedGraph[w] = node
        else:
            temp = self.undirectedGraph[w]

            while temp.next != None:
                temp = temp.next
            temp.next = node
        

        self.E += 1

    # String representation of the adjacency lists
    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.undirectedGraph[i]
            while temp:
                print(" -> {}".format(temp.V), end="")
                temp = temp.next
            print(" \n")

    # Number of vertices
    def num_vertices(self):
        return self.V

    # Number of edges (there should be 2x as much b/c there's an edge from v->w and w->v)
    def num_edges(self):
        return self.E



myGraph = UndirectedGraph(None, 'tinyG.txt')
myGraph.print_graph()

print(myGraph.num_edges())
print(myGraph.num_vertices())
