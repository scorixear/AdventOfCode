import os, sys
import time

def is_zero_sequence(sequence: list[int]) -> bool:
    return all(x == 0 for x in sequence)

def extrapolate(line: str) -> int:
    sequences = [[int(x) for x in line.split()]]
    while (not is_zero_sequence(sequences[-1])):
        sequences.append([sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)])
    sequences[-1].insert(0,0)
    for i in range(len(sequences)-2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
    return sequences[0][0]
    
    

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    result = 0
    for line in lines:
        result += extrapolate(line)
    print(result)
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
