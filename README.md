# disjoint-sets
Disjoint sets implementation comparison: linked lists (with and without weighted union heuristics) VS disjoint sets forests with path compression.

This experiment compares different ways to implement data strucutures for disjoint sets (chapter 21 of the book):
- through linked lists (with and without the weighted union heuristic)
- through forests of disjoint sets (with path compression)
The comparison of the implementation will be based on the connected components algorithm in undirected graphs.

Prerequisites:
- Python: Version 3.8.10
- Libraries: (standards) random for graph generation and time for performance tracking
	     (extenral) matplotlib to visualise results

Configuration:
Test parameters are defined in main.py. To reproduce the results discussed in the report, these are the needed values:
- graph dimensions (nodes): [50,500,1000,1500,2000,3000,4000,6000,8000,10000,15000]
- graph densities (edge_nodes_ratio): [1, 10, 20]
- average (ITERATIONS): 30

Execution:
To run the tests and generate the results, execute the main.py script from terminal:
python main.py
