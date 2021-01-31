from UndirectedGraph import UndirectedGraph

class GraphProcessingClient:
    ''' Include common graph processing problems
    1. degree(Graph, v): Compute the degree of v (number of edges connected to v)
    2. maxDegree(Graph): Compute the max degree of Graph
    3. averageDegree(Graph): Compute average degree of a Graph (The average number of edges per node in the graph)
    4. numberOfSelfLoops(Graph): Count the number of self loops (An edge of a graph which starts and ends at the same vertex of a Graph)
    5. print_graph: Print a string representation of the adjacency list
    '''

    def degree(self, G, v):
        return G.adj(v)

    def maxDegree(self, G):
        max = 0

        for i in range(G.num_vertices()):
            deg = self.degree(G, i)

            if deg > max:
                max = deg
        
        return max

    def averageDegree(self, G):

        # Total Edges/Total Nodes=Average Degree
        return G.num_edges() // G.num_vertices()
 
    def numberOfSelfLoops(self, G):
        self_loops = 0

        for v in range(G.num_vertices()):
            for w in range(G.adj(v)):
                if v == w:
                    self_loops += 1

        return self_loops // 2


graph_client = GraphProcessingClient()
myGraph = UndirectedGraph(None, 'tinyG.txt')

print("Degree:", graph_client.degree(myGraph, 1))
print("Max degree:", graph_client.maxDegree(myGraph))
print("Average degree:", graph_client.averageDegree(myGraph))
print("Self loops:", graph_client.numberOfSelfLoops(myGraph))


