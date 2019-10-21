"""@author Vimal Venugopal."""
class wireless:  
    """Class to realize the wireless environment."""

    def __init__(self):
        """Initialize a new environment object with an empty list of nodes."""
        self.collection_of_nodes={}

    def add_node(self,peerno,device):
        """Add a node to the list of nodes."""
        self.collection_of_nodes[peerno] = device
        