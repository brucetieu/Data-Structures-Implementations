from UndirectedGraph import UndirectedGraph

class GraphProcessingClient:
    ''' Include common graph processing problems
    1. degree(Graph, v): Compute the degree of v
    2. maxDegree(Graph): Compute the max degree of Graph
    3. averageDegree(Graph): Compute average degree of a Graph
    4. numberOfSelfLoops(Graph): Count the number of self loops (An edge of a graph which starts and ends at the same vertex) of a Graph
    5. print_graph: Print a string representation of the adjacency list
    '''

    def degree(self, G, v):
        pass

    def maxDegree(self, G):
        pass

    def averageDegree(self, G):
        pass

    def numberOfSelfLoops(self, G):
        pass

    def print_graph(self):
        pass


graph_client = GraphProcessingClient()
myGraph = UndirectedGraph(None, 'tinyG.txt')
myGraph.print_graph()

