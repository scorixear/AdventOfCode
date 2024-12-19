import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    stripes = lines[0].split(", ")
    patterns = lines[2:]
    
    counter = 0
    for pattern in patterns:
        if find_path(stripes, pattern):
            counter += 1
    print(counter)
    
def find_path(stripes: list[str], pattern: str) -> bool:
    if len(pattern) == 0:
        return True
    for stripe in stripes:
        if pattern.startswith(stripe):
            if find_path(stripes, pattern[len(stripe):]):
                return True
    return False
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
