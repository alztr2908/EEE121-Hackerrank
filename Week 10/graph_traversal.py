class Graph(object):
    """
    This graph implements an undirected graph using an adjacency list.
    Note that the implementation assumes that vertex identifiers are positive
    numbers; thus the first element of the adjacency list (which has index 0)
    is not used and has an arbitrary placeholder None.
    """
    # ---------- DO NOT MODIFY CODE BELOW ----------
    def __init__(self):
        """
        Initializer method that initializes the member variables of the class.
        """
        self.V = 0      # number of vertices
        self.E = 0      # number of directed edges
        self.adjacency_list = [None] # index 0 is not used

        # Traversal
        self.visited_node = [False]
        self.visited = []

    def add_edge(self, src, dst, cost):
        """
        This function adds a directed edge in the graph.
        
        Parameters
        ----------
        v1 : int
            Source vertex.
        v2 : int
            Destination vertex.
        cost : int
            Weight associated with directed edge from the source vertex to the 
            destination vertex.
        """
        self.E = self.E + 1
        self.adjacency_list[src].append((dst, cost))
    
    def show_graph(self):
        """
        This function prints a formatted adjacency list representation of 
        the weighted graph.
        """
        print(f'|V| = {self.V},  |E| = {self.E}')
        for n in range(1, self.V+1):
            print(f'[{n}] -> {self.adjacency_list[n]}')

    def add_vertex(self):
        """
        This function adds a vertex in the graph.
        """
        self.visited_node += [False]
        self.V = self.V + 1
        self.adjacency_list.append(list())          
    # ---------- DO NOT MODIFY CODE ABOVE ----------


    def initialize_graph(self, V, edge_list):
        """
        This function initializes an empty graph using the number of vertices
        and the list of directed edges by making use of available methods.

        Parameters
        ----------
        V : int
            The number of vertices to be added to the graph.
        edge_list : list of tuples
            A list of dircted edges with format (src, dst, cost) to be
            added to the graph.
        """
        # ---------- INSERT CODE BELOW ----------
        for _ in range(V):
          self.add_vertex()
        
        for node in edge_list:
          self.add_edge(node[0],node[1],node[2])

        # ---------- INSERT CODE ABOVE ----------

    ## Traversal
    def clear_visited(self):
      self.visited_node = [False]*self.V
      
    def traverse(self, root):
      self.visited.append(root)
      self.visited_node[root] = True
      greedy = float('inf') # close to inf
      neighbor = 0

      # Checking every neighbors and its costs
      for cost in self.adjacency_list[root]:
        if cost[1] < greedy and not self.visited_node[cost[0]]:
          neighbor, greedy = cost[0],cost[1]
      
      # Base case
      if neighbor == 0:
        return 0
      return greedy + self.traverse(neighbor)

def read_input(E):
    """
    This function reads the input starting from the second line until the last
    line and returns the list of parsed directed edges and commands.

    Parameters
    ----------
    E : int
        The total number of directed edges to be read.
    C : int
        The total number of commands to be read.

    Returns
    -------
    edge_list : list (tuple)
        A list of directed edges in the format (src,dst,cost).
    command_list : list (str)
        A list of commands containing the a python statement using the
        graph methods on graph g.
    """
    # ---------- INSERT CODE BELOW ----------
    edge_list = []

    for _ in range(E):
       src, dst, cost = input('').rstrip('\r\n').split()
       edge_list.append((int(src),int(dst),int(cost)))
    
    return edge_list
    # ---------- INSERT CODE ABOVE ----------



# ---------- DO NOT MODIFY CODE BELOW ----------
if __name__ == '__main__':
    
    # Reads the first line of the input
    V, E, C = input('').rstrip('\r\n').split()
    V, E, C = int(V), int(E), int(C)

    # Create a graph instance
    g = Graph()
    
    # Parse the remaining input into two lists.
    edge_list= read_input(E)

    # Initialize the graph using the value of V and/or the edge_list.
    if V > 0 or E > 0:
        g.initialize_graph(V, edge_list)

    
    # Generate the required formatted output.
    # g.show_graph()
    total = g.traverse(C)
    print(g.visited[-1],total)

# ---------- DO NOT MODIFY CODE ABOVE ----------