import os, sys
import time
import networkx as nx

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    graph = nx.Graph()
    for line in lines:
        first, second = line.split(": ")
        second = second.split()
        for other in second:
            if graph.has_edge(first, other):
                continue
            graph.add_edge(first, other)
    betweeness_edges = nx.edge_betweenness_centrality(graph)
    betweeness_edges = sorted(betweeness_edges, key=betweeness_edges.get) # type: ignore
    betweeness_edges = betweeness_edges[-3:]
    graph.remove_edges_from(betweeness_edges)
    connected_components = nx.connected_components(graph)
    result = 1
    for component in connected_components:
        result *= len(component)
    print(result)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
