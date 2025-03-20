class Node:
    def __init__(self, node_id, node_type="legitimate"):
        self.node_id = node_id
        self.node_type = node_type
        self.status = "active"
        self.neighbors = []
    
    def add_neighbor(self, neighbor_node):
        if neighbor_node not in self.neighbors:
            self.neighbors.append(neighbor_node)
    
    def simulate_activity(self):
        if self.node_type == "adversarial":
            return "attack"
        return "normal"
