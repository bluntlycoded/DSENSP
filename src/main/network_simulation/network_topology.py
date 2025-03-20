class NetworkTopology:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node):
        self.nodes[node.node_id] = node
    
    def update_topology(self):
        for node in self.nodes.values():
            node.neighbors = [n for n in self.nodes.values() if n.node_id != node.node_id]
    
    def get_topology(self):
        return {node.node_id: [n.node_id for n in node.neighbors] for node in self.nodes.values()}
