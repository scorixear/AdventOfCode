import os, sys
import time

class PriceChange:
    def __init__(self):
        self.changes: dict[tuple[int, int, int, int], int] = {}
        self.prices: list[int] = []
    def add(self, change: int, price: int):
        self.prices.append(change)
        if len(self.prices) >= 4:
            new_price_changes: tuple[int, int, int, int] = (self.prices[-4], self.prices[-3], self.prices[-2], self.prices[-1])
            if new_price_changes not in self.changes:
                self.changes[new_price_changes] = price
                
    def get(self, change: tuple[int, int, int, int]) -> int:
        return self.changes.get(change, 0)
            
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    price_changes: list[PriceChange] = []
    for line in lines:
        number = int(line)
        mod_10 = number % 10
        current_prices = PriceChange()
        for _ in range(2000):
            new_number = gen(number)
            new_mod_10 = new_number % 10
            current_prices.add(new_mod_10 - mod_10, new_mod_10)
            number = new_number
            mod_10 = new_mod_10
        price_changes.append(current_prices)
    best = 0
    
    for a in range(-9, 10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    #print(a, b, c, d)
                    current = 0
                    for changes in price_changes:
                        current += changes.get((a, b, c, d))
                    best = max(best, current)
    print(best)

def find_price(guard, changes):
    for i in range(0, len(changes) - len(guard)):
        if [c[0] for c in changes[i:i+len(guard)]] == guard:
            return changes[i+len(guard)-1][1]
    return 0

def gen(number):
    # multiply by 64
    r1 = number << 6
    number ^= r1
    number %= 1<<24
    # divide by 32
    r2 = number >> 5
    number ^= r2
    number %= 1<<24
    # multiply by 2048
    r3 = number << 11
    number ^= r3
    number %= 1<<24
    return number

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
