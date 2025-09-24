import time
import hashlib

def main():
    salt = "qzyelonm"
    val = 0
    keys_found = 0
    while True:
        h = md5(str(val), salt)
        repeating_count = 0
        curr_repeating = ""
        for c in h:
            if c == curr_repeating:
                repeating_count += 1
                if repeating_count == 3:
                    break
            else:
                curr_repeating = c
                repeating_count = 1
        if repeating_count == 3:
            for i in range(val+1, val+1001):
                h2 = md5(str(i), salt)
                if curr_repeating*5 in h2:
                    print(f"Found key {val} with hash {h.lower()}")
                    keys_found += 1
                    if keys_found == 64:
                        print(f"64th key: {val}")
                        return
                    break
        val += 1

def md5(s: str, salt: str) -> str:

    return hashlib.md5((salt + s).encode()).hexdigest()

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
