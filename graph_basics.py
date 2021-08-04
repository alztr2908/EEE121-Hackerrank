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


    def remove_edge(self, src, dst):
        """
        This function removes the directed edge from vertex src to vertex dst.

        Parameters
        ----------
        src : int
            Source vertex of directed edge to be removed.
        dst : int
            Destination vertex of directed edge to be removed.
        """
        # ---------- INSERT CODE BELOW ----------
        for i in self.adjacency_list[src]:
          if i[0] == dst:
            self.adjacency_list[src].remove(i)
            self.E = self.E - 1

        # ---------- INSERT CODE ABOVE ----------


    def remove_vertex(self, v):
        """
        This function removes a vertex in the graph and all its associated
        directed edges.

        Parameters
        ----------
        v : int
            The vertex to be removed.
        """
        # ---------- INSERT CODE BELOW ----------
        
        # This will remove the v as dist on every vertex
        for i in range(1,self.V):
          self.remove_edge(i,v)
        
        # Remove the remaining edges of that soon-will-be-remove vertex
        self.E = self.E - len(self.adjacency_list[v])

        # POP!!
        self.adjacency_list.pop()
        self.V = self.V - 1

        # ---------- INSERT CODE ABOVE ----------

def read_input(E, C):
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
    command_list = []

    for _ in range(E):
       src, dst, cost = input('').rstrip('\r\n').split()
       edge_list.append((int(src),int(dst),int(cost)))
    
    for _ in range(C):
      command_list.append(f'g.{input()}')

    return edge_list, command_list
    # ---------- INSERT CODE ABOVE ----------



# ---------- DO NOT MODIFY CODE BELOW ----------
if __name__ == '__main__':
    
    # Reads the first line of the input
    V, E, C = input('').rstrip('\r\n').split()
    V, E, C = int(V), int(E), int(C)

    # Create a graph instance
    g = Graph()
    
    # Parse the remaining input into two lists.
    edge_list, command_list = read_input(E, C)

    # Initialize the graph using the value of V and/or the edge_list.
    if V > 0 or E > 0:
        g.initialize_graph(V, edge_list)

    # Runs the elements in command_list as python statements.
    if C > 0:
        for command in command_list:
            exec(command)
            
    # Generate the required formatted output.
    g.show_graph()   
# ---------- DO NOT MODIFY CODE ABOVE ----------