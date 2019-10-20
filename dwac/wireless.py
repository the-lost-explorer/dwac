"""@author Vimal Venugopal."""
class environment:  
    """Class to realize the wireless environment."""

    def __init__(self):
        """Initialize a new environment object with an empty list of nodes."""
        self.list_of_nodes=[]

    def add_node(self,device):
        """Add a node to the list of nodes."""
        self.list_of_nodes.append(device)