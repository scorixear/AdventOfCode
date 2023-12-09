import os

YEAR = "2016"
for day in range(1, 26):
    if os.path.isdir(os.path.join(YEAR, str(day))):
        continue
    os.mkdir(os.path.join(YEAR, str(day)))
    with open(os.path.join(YEAR, str(day), "input.txt"), "w") as f:
        pass
    with open(os.path.join(YEAR, str(day), "example.txt"), "w") as f:
        pass
    with open(os.path.join(YEAR, str(day), "1.py"), "w") as f:
        f.write("""import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\\n")

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
""")
    with open(os.path.join(YEAR, str(day), "2.py"), "w") as f:
        f.write("""import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\\n")

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
""")
    