
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.size = 1
        self.head = node
        self.tail = node


class UnionFind:
    def __init__(self):
        self.sets = {}
    
    
    def make_set(self, value):
        node = ListNode(value)
        linked_list = LinkedList(node)
        self.sets[value] = linked_list
    
    
    def find_set(self, value):
        return self.sets[value].head


    def union(self, u, v):
        if self.find_set(u) != self.find_set(v):
            self.sets[u].size += self.sets[v].size
            u_tail = self.sets[u].tail
            u_tail.next = self.sets[v].head #or self.find_set(v)
            self.sets[u].tail = self.sets[v].tail
            node = self.sets[v].head #or self.find_set(v)
            while node is not None:
                self.sets[node.value] = self.sets[u]
                node = node.next
    
    def weighted_union(self, u, v):
        if self.sets[u].size < self.sets[v].size:
            self.union(v,u)
        else:
            self.union(u,v)
    
            
    def connected_components(self, graph):
        for node in graph.nodes:
            self.make_set(node)
        for u, neighbours in enumerate(graph.adjacency_list):
            for v in neighbours:
                if self.find_set(u) != self.find_set(v):
                    self.union(u,v)
                    
    
    def weighted_connected_components(self, graph):
        for node in graph.nodes:
            self.make_set(node)
        for u, neighbours in enumerate(graph.adjacency_list):
            for v in neighbours:
                if self.find_set(u) != self.find_set(v):
                    self.weighted_union(u,v)

    
    def print_connected_components(self):
        components = {}
        for value in self.sets:
            linked_list = self.sets[value]
            head = linked_list.head.value
            if head not in components:
                components[head] = []
            components[head].append(value)
        print("Connected components: ")
        for component in components:
            print(component)