class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = self
        
        
class UnionFind:
    def __init__(self):
        self.nodes = {}
    
        
    def make_set(self, value):
        node = TreeNode(value)
        self.nodes[value] = node
        
        
    def find_set(self, value):
        u = self.nodes[value]
        return self.path_compression(u)
    
    
    def path_compression(self, u):
        if u != u.parent:
            u.parent = self.path_compression(u.parent)  #path compression
        return u.parent 
        
    
    def union(self, u, v):
        u_root = self.find_set(u)
        v_root = self.find_set(v)
        if u_root != v_root:
            u_root.parent = v_root

        
    def connected_components(self, graph):
        for node in graph.nodes:
            self.make_set(node)
        for u, neighbours in enumerate(graph.adjacency_list):
            for v in neighbours:
                u_root = self.find_set(u)
                v_root = self.find_set(v)
                if u_root != v_root:
                    u_root.parent = v_root
    
        
    def print_connected_components(self):
        components = {}
        for value in self.nodes:
            root = self.find_set(value).value
            if root not in components:
                components[root] = []
            components[root].append(value)
        print("Connected components: ")
        for component in components.values():
            print(component)
