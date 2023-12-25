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
    # find all edges with highest betweeness centrality
    # the betweeness centrality of an edge is the fraction of shortest paths between two verticies
    # that pass through that edge
    # a high centrality means, a lot of paths between two verticies depend on this edge
    # therefore, this edge is important for the connectivity of the graph
    betweeness_edges = nx.edge_betweenness_centrality(graph)
    # sort edges by betweeness centrality
    # no idea why pyhton complains about this
    betweeness_edges = sorted(betweeness_edges, key=betweeness_edges.get) # type: ignore
    # remove the 3 edges with the highest betweeness centrality
    betweeness_edges = betweeness_edges[-3:]
    graph.remove_edges_from(betweeness_edges)
    # find all connected components
    connected_components = nx.connected_components(graph)
    # and multiply their sizes
    result = 1
    for component in connected_components:
        result *= len(component)
    print(result)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
