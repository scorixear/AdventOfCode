import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")
    instructions = lines[0]
    
    nodes = {}
    for line in lines[2:]:
        node, neighbours = line.split(" = ", 1)
        neighbours = neighbours.split(", ")
        nodes[node] = (neighbours[0][1:], neighbours[1][:-1])
    curr_node = "AAA"
    steps = 0
    while (curr_node != "ZZZ"):
        for i in instructions:
            if curr_node == "ZZZ":
                break
            steps += 1
            left, right = nodes[curr_node]
            if i == "L":
                curr_node = left
            else:
                curr_node = right
    print(steps)
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
