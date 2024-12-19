import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    stripes = lines[0].split(", ")
    patterns = lines[2:]
    
    counter = 0
    dp: dict[str, int] = {}
    for pattern in patterns:
        counter += find_path(stripes, pattern, dp)
    print(counter)
    
def find_path(stripes: list[str], pattern: str, dp: dict[str, int]) -> int:
    if len(pattern) == 0:
        return 1
    if pattern in dp:
        return dp[pattern]
    total = 0
    for stripe in stripes:
        if pattern.startswith(stripe):
            total += find_path(stripes, pattern[len(stripe):], dp)
    dp[pattern] = total
    return total
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
