import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    discs: list[tuple[int, int]] = []
    for line in lines:
        parts = line.split(" ")
        discs.append((int(parts[3]), int(parts[11][:-1])))
    
    print(f"Discs (modulus, start_pos): {discs}")
    
    # For each disc, we need: (start_position + wait_time + disc_number) % modulus == 0
    # Rearranging: wait_time ≡ -(start_position + disc_number) (mod modulus)
    constraints = []
    for i, (modulus, start_pos) in enumerate(discs):
        # Disc i+1 is reached at time (wait_time + i + 1)
        # We need (start_pos + wait_time + i + 1) % modulus == 0
        # So wait_time ≡ -(start_pos + i + 1) (mod modulus)
        target_remainder = (-start_pos - i - 1) % modulus
        constraints.append((modulus, target_remainder))
        print(f"Disc {i+1}: need wait_time ≡ {target_remainder} (mod {modulus})")
    
    result = solve_timing(constraints)
    print(f"Result: {result}")
    
    return result

def solve_timing(constraints: list[tuple[int, int]]) -> int:
    """
    Solve the timing problem using a simple iterative approach
    """
    if not constraints:
        return 0
    
    # Start with the first constraint
    modulus, remainder = constraints[0]
    
    # For each additional constraint, find when both are satisfied
    for next_mod, next_rem in constraints[1:]:
        # Find the smallest t >= remainder such that:
        # t ≡ remainder (mod modulus) and t ≡ next_rem (mod next_mod)
        
        t = remainder
        while True:
            if t % next_mod == next_rem:
                # Found a solution
                remainder = t
                # New modulus is LCM of current modulus and next_mod
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a
                
                modulus = modulus * next_mod // gcd(modulus, next_mod)
                break
            t += modulus
    
    return remainder

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
