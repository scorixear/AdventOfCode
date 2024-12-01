import os

YEAR = "2024"
for day in range(1, 26):
    if not os.path.isdir(os.path.join(YEAR, str(day))):
        os.mkdir(os.path.join(YEAR, str(day)))
    if not os.path.isfile(os.path.join(YEAR, str(day), "input.txt")):
        with open(os.path.join(YEAR, str(day), "input.txt"), "w", encoding="UTF-8") as f:
            pass
    if not os.path.isfile(os.path.join(YEAR, str(day), "example.txt")):
        with open(os.path.join(YEAR, str(day), "example.txt"), "w", encoding="UTF-8") as f:
            pass
    if not os.path.isfile(os.path.join(YEAR, str(day), "1.py")):
        with open(os.path.join(YEAR, str(day), "1.py"), "w", encoding="UTF-8") as f:
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
    if not os.path.isfile(os.path.join(YEAR, str(day), "2.py")):
        with open(os.path.join(YEAR, str(day), "2.py"), "w", encoding="UTF-8") as f:
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
    