from UndirectedGraph import UndirectedGraph

class GraphProcessingClient:
    ''' Include common graph processing problems
    1. degree(Graph, v): Compute the degree of v (number of edges connected to v)
    2. maxDegree(Graph): Compute the max degree of Graph
    3. averageDegree(Graph): Compute average degree of a Graph
    4. numberOfSelfLoops(Graph): Count the number of self loops (An edge of a graph which starts and ends at the same vertex) of a Graph
    5. print_graph: Print a string representation of the adjacency list
    '''

    def degree(self, G, v):
        degree = 0

        for i in range(G.adj(v)):
            degree += 1

        return degree


    def maxDegree(self, G):
        max = 0

        for i in range(G.num_vertices()):
            deg = self.degree(G, i)

            if deg > max:
                max = deg
        
        return max

    def averageDegree(self, G):
        pass

    def numberOfSelfLoops(self, G):
        pass

    def print_graph(self):
        pass


graph_client = GraphProcessingClient()
myGraph = UndirectedGraph(None, 'tinyG.txt')

print(graph_client.degree(myGraph, 1))
print(graph_client.maxDegree(myGraph))


