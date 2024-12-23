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
    
    known = set()
    for node in nodes.values():
        for node2 in node.neighbours:
            for node3 in node2.neighbours:
                if node3 == node:
                    continue
                if node3 in node.neighbours:
                    node_list = [node, node2, node3]
                    node_list.sort(key=lambda x: x.name)
                    known.add(tuple(node_list))
    print(len(known))
    counter = 0
    for node_list in known:
        if node_list[0].name[0] == "t" or node_list[1].name[0] == "t" or node_list[2].name[0] == "t":
            counter += 1
    print(counter)
        

    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
