import time
import matplotlib.pyplot as plt
import linked_lists
import forest

def test_lists(graph):
    union_find = linked_lists.UnionFind()
    start = time.perf_counter()
    union_find.connected_components(graph)
    end = time.perf_counter()
    return end - start


def test_weighted_lists(graph):
    union_find = linked_lists.UnionFind()
    start = time.perf_counter()
    union_find.weighted_connected_components(graph)
    end = time.perf_counter()
    return end - start


def test_trees(graph):
    union_find = forest.UnionFind()
    start = time.perf_counter()
    union_find.connected_components(graph)
    end = time.perf_counter()
    return end - start 
    
    
def create_plot(data, x_values, xlabel, title):
    plt.figure(figsize=(10,6))
    for label, y_values in data.items():
        plt.plot(x_values, y_values, label=label, marker='o', linestyle='-', linewidth=2)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Time (s)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, ls='--', alpha=0.5)
    plt.legend(frameon=True, shadow=True)
    plt.tight_layout()
    plt.show()
    