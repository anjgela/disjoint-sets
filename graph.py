import random

class Graph:
    def __init__(self, num_nodes, num_edges):
        self.nodes = [i for i in range(num_nodes)]
        self.num_edges = num_edges 
        self.adjacency_list = [[] for _ in range(num_nodes)]
        
        edges = 0;
        while edges < num_edges:
            u = random.choice(self.nodes)
            v = random.choice(self.nodes)
            if u != v and v not in self.adjacency_list[u]:
                self.adjacency_list[u].append(v)
                self.adjacency_list[v].append(u) #undirected graph
                edges += 1