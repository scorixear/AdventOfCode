import os, sys
import time

class Node():
    def __init__(self, name):
        self.name = name
        self.neighbours: set["Node"] = set()
    
    def add_neighbour(self, neighbour: "Node"):
        self.neighbours.add(neighbour)
        neighbour.neighbours.add(self)
    
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)
    


def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    nodes: dict[str, Node] = {}

    for line in lines:
        node_name1, node_name2 = line.split("-")
        if node_name1 in nodes:
            node1 = nodes[node_name1]
        else:
            node1 = Node(node_name1)
            nodes[node_name1] = node1
        if node_name2 in nodes:
            node2 = nodes[node_name2]
        else:
            node2 = Node(node_name2)
            nodes[node_name2] = node2
        
        node1.add_neighbour(node2)
    
    largest = bron_kerbosch(set(nodes.values()))
    largest = list(largest)
    largest.sort(key=lambda x: x.name)
    print(",".join([node.name for node in largest]))


def bron_kerbosch(P: set[Node], R: set[Node] = set(), X: set[Node] = set()):
    if len(P) == 0 and len(X) == 0:
        #print(R)
        return R
    p_and_u = P.union(X)
    pivot = next(iter(p_and_u))
    largest = R
    for node in P - pivot.neighbours:
        new_r = bron_kerbosch(P.intersection(node.neighbours), R.union({node}), X.intersection(node.neighbours))
        if len(new_r) > len(largest):
            largest = new_r
        P.remove(node)
        X.add(node)
    return largest

    

       
        

    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
