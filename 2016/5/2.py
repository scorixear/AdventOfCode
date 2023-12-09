import os, sys
import time
# import md5
from hashlib import md5

def get_hash(text):
    return md5(text.encode("utf-8")).hexdigest()

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        i = 0
        password = [None] * 8
        
        while any(x is None for x in password):
            hash = get_hash(text + str(i))
            
            if hash.startswith("00000"):
                if hash[5].isdigit() and int(hash[5]) < 8 and password[int(hash[5])] is None:
                    password[int(hash[5])] = hash[6]
                    
            i += 1
        print("".join(password))

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
