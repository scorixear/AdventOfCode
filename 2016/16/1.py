import time

def main():
    initial = "01111001100111011"
    target = 272
    while len(initial) < target:
        new = initial + "0" + initial[::-1].replace('0', 'x').replace('1', '0').replace('x', '1')
        initial = new
    initial = initial[:target]
    print(f"Initial length: {len(initial)}")
    print(f"Initial: {initial}")
    result = checksum(initial)
    print(f"Checksum: {result}")
    while len(result) % 2 == 0:
        result = checksum(result)
        print(f"Checksum: {result}")
    print(f"Result: {result}")

def checksum(data: str) -> str:
    result = ""
    for i in range(0, len(data)-1, 2):
        pair = data[i:i+2]
        result += '1' if pair[0] == pair[1] else '0'
    return result

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
