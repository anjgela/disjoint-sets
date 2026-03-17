import test
import graph

nodes = [50, 500, 1000, 1500, 2000, 3000, 4000, 6000, 8000, 10000, 15000]
edges_nodes_ratio = [1, 10, 20]
algorithms = ['Linked lists', 'Weighted union', 'Rooted trees']

ITERATIONS = 30

for r in edges_nodes_ratio:
    data_n = {algorithm : [] for algorithm in algorithms}
    
    for n in nodes:
        lists_time = 0
        weighted_time = 0
        trees_time = 0
        
        for i in range(ITERATIONS):
            g = graph.Graph(n, n*r)
            lists_time += test.test_lists(g)
            weighted_time += test.test_weighted_lists(g)
            trees_time += test.test_trees(g)
            
        lists_time /= ITERATIONS
        weighted_time /= ITERATIONS
        trees_time /= ITERATIONS
            
        data_n[algorithms[0]].append(lists_time)
        data_n[algorithms[1]].append(weighted_time)
        data_n[algorithms[2]].append(trees_time)
    
    test.create_plot(data_n, nodes, 'Number of nodes (n)', f'Varying n, fixed r={r}')
        