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
        self.adjacency_matrix = [] # index 0 is not used

        # Traversal
        self.visited_node = [False]
        self.dist = [float('inf')]
        self.prev_node = [None]

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
        self.adjacency_matrix[src][dst] = cost
        self.adjacency_matrix[dst][src] = cost

    def add_vertex(self):
        """
        This function adds a vertex in the graph.
        """
        self.visited_node += [False]
        self.dist.append(float('inf'))
        self.prev_node.append(None)
        self.V = self.V + 1
    # ---------- DO NOT MODIFY CODE ABOVE ----------

    def show_graph(self):
      """
      This function prints a formatted adjacency list representation of 
      the weighted graph.
      """
      print(f'|V| = {self.V},  |E| = {self.E}')
      for n in range(self.V+1):
        print(f'{self.adjacency_matrix[n]}')

    def initialize_matrix(self,V):
      for i in range(V+1):
        sub_matrix= []
        for j in range(V+1):
          sub_matrix.append(0)
        self.adjacency_matrix.append(sub_matrix)

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
        
        self.initialize_matrix(V)

        for node in edge_list:
          self.add_edge(node[0],node[1],node[2])

        # ---------- INSERT CODE ABOVE ----------

    ## Traversal for finding shortest path
    def clear_visited(self):
      self.visited_node = [False]*(self.V+1)
      self.dist = [float('inf')]*(self.V+1)
      self.prev_node = [None]*(self.V+1)

    ## Compare shortest distance on the current self.dist
    def minDistance(self, dist, sptSet):
  
        # Initilaize minimum distance for next node
        min = float('inf')
  
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(1,self.V+1):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
  
        return min_index


    ## Main function for finding comparing shortest paths
    def djikstra(self, root, target):
      ## Reset for new entrance
      self.clear_visited()

      
      self.dist[root] = 0

      ## Loop won't stop until the target node is not visited
      while self.visited_node[target] == False:

        ## For getting the shortest distance on the index
        smol = self.minDistance(self.dist,self.visited_node)

        self.visited_node[smol] = True

        for n in range(1,self.V+1):
          temp = self.adjacency_matrix[smol][n]

          ## If
          ## 1. The element on the graph is 0
          ## 2. element on dist is less than
          ## 3. Visited
          ## Then path won't relax
          if temp > 0 and self.dist[n] > (temp + self.dist[smol]) and (self.visited_node[n] == False):
            self.dist[n] = self.dist[smol] + temp
            self.prev_node[n] = smol
      

    ## Setup function for comparing entrances
    def shortestPath(self,gates,X):
      temp1 = float('inf')
      temp2 = 0
      tempnode = []

      for x in gates:
        self.djikstra(int(x),X)
        ## Compare which specs will be printed
        if temp1 > self.dist[X]:
          temp1 = self.dist[X]
          temp2 = int(x) 
          tempnode = self.prev_node
      
      print(temp2)
      print(temp1)
      print(self.foo(tempnode,X))

    
    ## Traverse the shortest path by recursion
    def foo(self,nodes,x):
      if nodes[x] is None:
        return str(x)
      else:
        return self.foo(nodes,nodes[x]) + ' ' + str(x)
        

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
    En, E, V, X = input('').rstrip('\r\n').split()
    En, E, V, X = int(En), int(E), int(V), int(X)
    Gates = list(input('').rstrip('\r\n').split())
    
    # Create a graph instance
    g = Graph()
    
    # Parse the remaining input into two lists.
    edge_list= read_input(E)

    # Initialize the graph using the value of V and/or the edge_list.
    if E > 0 or V > 0:
      g.initialize_graph(V, edge_list)

    
    # Generate the required formatted output.
    # g.show_graph()
    g.shortestPath(Gates,X)

# ---------- DO NOT MODIFY CODE ABOVE ----------