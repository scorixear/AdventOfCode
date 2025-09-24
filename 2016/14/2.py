import time
import hashlib
from functools import lru_cache

def main():
    salt = "qzyelonm"
    val = 0
    keys_found = 0
    
    while True:
        h = get_stretched_md5(val, salt)
        
        # Find first triplet more efficiently
        triplet_char = find_triplet(h)
        
        if triplet_char:
            # Check next 1000 hashes for quintuplet
            quintuplet = triplet_char * 5
            for i in range(val + 1, val + 1001):
                h2 = get_stretched_md5(i, salt)
                if quintuplet in h2:
                    print(f"Found key {val} with hash {h.lower()}")
                    keys_found += 1
                    if keys_found == 64:
                        print(f"64th key: {val}")
                        return
                    break
        val += 1

@lru_cache(maxsize=10000)
def get_stretched_md5(index, salt):
    """Cached version of MD5 with key stretching"""
    h = hashlib.md5((salt + str(index)).encode()).hexdigest()
    for _ in range(2016):
        h = hashlib.md5(h.encode()).hexdigest()
    return h

def find_triplet(h):
    """Find the first character that appears 3 times consecutively"""
    for i in range(len(h) - 2):
        if h[i] == h[i+1] == h[i+2]:
            return h[i]
    return None

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
