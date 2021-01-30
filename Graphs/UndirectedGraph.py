

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
            self.undirectedGraph = [None] * V
        
        elif file:
            
            f = open(file, 'r')
            self.__init__(int(f.readline()))
            self.E = int(f.readline())

            for i in range(self.E):
                v, w = map(int, f.readline().split())
                self.addEdge(v, w)


    def addEdge(self, v, w):
        node = self.AdjNode(w)

        if self.undirectedGraph[v] is None:
            self.undirectedGraph[v] = node
        else:
            temp = self.undirectedGraph[v]

            while temp.next != None:
                temp = temp.next
            temp.next = node

        node = self.AdjNode(v)

        if self.undirectedGraph[w] is None:
            self.undirectedGraph[w] = node
        else:
            temp = self.undirectedGraph[w]

            while temp.next != None:
                temp = temp.next
            temp.next = node
        

        self.E += 1

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.undirectedGraph[i]
            while temp:
                print(" -> {}".format(temp.V), end="")
                temp = temp.next
            print(" \n")



myGraph = UndirectedGraph(None, 'tinyG.txt')
myGraph.print_graph()