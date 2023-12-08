import os, sys
import time

class NodeCycle:
    """Represents all cycles of starting node to all ending nodes
    """
    def __init__(self, first_reach: int, ending_node_cycles: list[int], repeat_index: int) -> None:
        # first_reach: the first time the starting node reaches an ending node
        self.first_reach = first_reach
        # ending_node_cycles: the cycle lengths from the last ending node to the next ending node
        self.ending_node_cycles = ending_node_cycles
        # if the last ending node is reached, where to start again to get the next cycle
        # the last entry in ending_node_cycles represents the path taken from the last ending node to the first ending node
        self.repeat_index = repeat_index
        # current cycle index, starting at -1 to represent the first_reach
        self.start_index = -1
        # the current cycle index we are on
        self.current_cycle = 0
    def get_next_cycle(self) -> int:
        """returns the length of nodex from the current ending (or starting) node to the next ending node
        does automatic wrap around

        Returns:
            int: the length of the next cycle
        """
        # if we are at the starting node, we need to return the first_reach
        if self.start_index == -1:
            # and begin the cycle
            self.start_index = 0
            self.current_cycle = self.first_reach
        else:
            # if we reached the last ending node, we need to wrap around
            if self.start_index >= len(self.ending_node_cycles):
                self.start_index = self.repeat_index
            self.current_cycle += self.ending_node_cycles[self.start_index]
            # increment the index
            self.start_index += 1
        return self.current_cycle


def get_cycle_counters(starting_node: str, instructions: str, nodes: dict[str, tuple[str, str]]):
    """Generates NodeCycle objects

    Args:
        starting_node (str): the starting node
        instructions (str): the instructions to follow
        nodes (dict[str, tuple[str, str]]): the adjacency list of nodes

    Returns:
        NodeCycle: the corresponding NodeCycle object
    """
    # holds all seen ending nodes in order
    ending_nodes = []
    # holds the cycle lengths from the last ending node to the next ending node
    ending_node_cycles = []
    # the number of cycles we have seen so far
    cycle_counter = 0
    # the first time we reach an ending node
    first_reach = 0
    # the index of the first ending node we see again
    repeat_integer = 0
    # the current node we are on
    curr_node = starting_node
    while True:
        # for each instruction
        for i in instructions:
            # if we reach an ending node
            if curr_node.endswith("Z"):
                # if we have not seen an ending node yet
                if len(ending_nodes) == 0:
                    # add the current node
                    ending_nodes.append(curr_node)
                    # set the first_reach
                    first_reach = cycle_counter
                    # reset the cycle_counter
                    cycle_counter = 0
                # if we have seen an ending node
                else:
                    # if we have not seen this ending node yet
                    if curr_node not in ending_nodes:
                        # add the current node
                        ending_nodes.append(curr_node)
                        # add the cycle_counter
                        ending_node_cycles.append(cycle_counter)
                        # reset the cycle_counter
                        cycle_counter = 0
                    # if we have seen this ending node
                    else:
                        # get the index of the first time we saw this ending node
                        repeat_integer = ending_nodes.index(curr_node)
                        # add the cycle_counter
                        ending_node_cycles.append(cycle_counter)
                        # return the NodeCycle object
                        return NodeCycle(first_reach, ending_node_cycles, repeat_integer)
            # increment the cycle_counter
            cycle_counter += 1
            # get next node
            left, right = nodes[curr_node]
            if i == "L":
                curr_node = left
            else:
                curr_node = right

def get_cycle_length(starting_node: str, instructions: str, nodes: dict[str, tuple[str, str]]):
    """Under the assumption that every starting node has only one end node
    and every end node has only one starting node
    and every cycle is the same as the starting node to the end node length
    we simply return the cycle length of the starting node to the end node

    Args:
        starting_node (str): the starting node
        instructions (str): the instructions to follow
        nodes (dict[str, tuple[str, str]]): the adjacency list of nodes

    Returns:
        int: the cycle length
    """
    cycle_counter = 0
    curr_node = starting_node
    while True:
        for i in instructions:
            if curr_node.endswith("Z"):
                return cycle_counter
            cycle_counter += 1
            left, right = nodes[curr_node]
            if i == "L":
                curr_node = left
            else:
                curr_node = right

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")
    instructions = lines[0]
    
    nodes = {}
    starting_nodes: set[str] = set()
    for line in lines[2:]:
        node, neighbours = line.split(" = ", 1)
        neighbours = neighbours.split(", ")
        nodes[node] = (neighbours[0][1:], neighbours[1][:-1])
        if node.endswith("A"):
            starting_nodes.add(node)
    
    # given the assumptions of get_cycle_lengths()
    # we can simplify the problem to finding the cycle length of each starting node
    # by computing the lcm of each cycle length
    # cycle_lengths = []
    # for starting_node in starting_nodes:
    #     cycle_lengths.append(get_cycle_length(starting_node, instructions, nodes))
    
    # current_lcm = 1
    # for cycle_length in cycle_lengths:
    #     current_lcm = lcm(current_lcm, cycle_length)
    # print(current_lcm)
    # return;    
    
    # with no assumptions
    # this code runs around 100_000 iterations of the while loop
    # in 0.14s, time estimate will be around 51 minutes until completion
    # since final target is around 22_000_000_000_000 and we increase by 1_000_000_000 each iteration
    cycles: list[NodeCycle] = []
    for starting_node in starting_nodes:
        cycles.append(get_cycle_counters(starting_node, instructions, nodes))
    # get the first cycle length
    cycle_lengths = [cycle.get_next_cycle() for cycle in cycles]
    # and count distinct cycle lengths
    cycle_length_sets = set(cycle_lengths)
    # only for debugging
    print_counter = 0
    current_time = time.perf_counter()
    # while we haven't found a cycle length that is the same for all starting nodes
    while len(cycle_length_sets) > 1:
        # get the min and max cycle length
        min_cycle = min(cycle_length_sets)
        max_cycle = max(cycle_length_sets)
        # only for debugging
        if (print_counter % 100000 == 0):
            print_counter = 0
            print(f"Min Cycle: {min_cycle}, time: {time.perf_counter() - current_time:.6f}s")
            current_time = time.perf_counter()
        print_counter += 1
        # for each cycle length
        for i, cycle_length in enumerate(cycle_lengths):
            # if the cycle length is the min cycle length
            if cycle_length == min_cycle:
                # get the next cycle length until is is equal or greater than the max cycle length
                current_cycle_length = cycle_length
                while(current_cycle_length < max_cycle):
                    current_cycle_length = cycles[i].get_next_cycle()
                # and override the cycle length
                cycle_lengths[i] = current_cycle_length
        # update distinct cycle lengths
        cycle_length_sets = set(cycle_lengths)
    print(cycle_lengths.pop())

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
