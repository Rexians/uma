import json

class Nodes:

    def __init__(self):
        self.node_id = None
        self.node_name = None
        self.node_info = None
        self.error = None

    def read_all_nodes(self):
        
        """
        Read all nodes
        """
        try:
            with open('./files/nodes/nodes.json', 'r') as f:
                all_nodes = json.load(f)
            return all_nodes
        except FileNotFoundError:
            self.error = f'File not found. Please report the bug'
            raise FileNotFoundError

    def read_node(self, node_id):
        """
        Read single node
        Parameters: node_id
        """
        try:
            with open('./files/nodes/nodes.json', 'r') as f:
                all_nodes = json.load(f)

            node = all_nodes['data'][node_id]
            self.node_id = node_id
            self.node_name = node['node_name']
            self.node_info = node['node_info']
        except FileNotFoundError:
            self.error = f'File not found. Please report the bug'
            raise FileNotFoundError
        except KeyError:
            self.error = f'Node id {node_id} not found in the file'
            raise KeyError
