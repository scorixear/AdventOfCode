import os, sys
import time
import timeit
from typing import Iterable

class StringHashMap:
    def __init__(self, elements: Iterable[tuple[str, int]]=None, size: int = 256):
        self.size = size
        self.table: list[list[tuple[str, int]]] = [list[tuple[str, int]]() for _ in range(size)]
        if elements is not None:
            for elem in elements:
                self.add_or_set(elem[0], elem[1])
    def add_or_set(self, key: str, value: int):
        # get the bucket
        curr_hash = self._hash(key)
        # for each pair in the bucket
        for i, pair in enumerate(self.table[curr_hash]):
            # if the key matches set the focus power
            if pair[0] == key:
                self.table[curr_hash][i] = (key, value)
                return
        # no key matched, add the lense
        self.table[curr_hash].append((key, value))

    def remove(self, key: str):
        # get the bucket
        curr_hash = self._hash(key)
        # for each pair in the bucket
        for i, pair in enumerate(self.table[curr_hash]):
            # if the key matches remove the lense
            if pair[0] == key:
                del self.table[curr_hash][i]
                return

    def get_focus_power(self) -> int:
        total = 0
        # for each bucket
        for i, bucket in enumerate(self.table):
            # for each pair in the bucket
            for j, pair in enumerate(bucket):
                # add bucket_index * pair_index * focus_power (1-indexed)
                total += (i+1) * (j+1) * pair[1]
        return total
    
    def _hash(self, sequence: str) -> int:
        curr = 0
        for c in sequence:
            curr += ord(c)
            curr *= 17
            curr %= self.size
        return curr
def main(do_print: bool = False):
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    sequences = text.split(",")
    lenses = StringHashMap()
    # for each sequence given
    for sequence in sequences:
        # if sequence is a removal
        if sequence.endswith("-"):
            # remove specified label
            lenses.remove(sequence[:-1])
        # else add or set the focus power at that label
        else:
            lenses.add_or_set(sequence.split("=")[0], int(sequence.split("=")[1]))
    result = lenses.get_focus_power()
    if do_print:
        print(result)

if __name__ == "__main__":
    before = time.perf_counter()
    main(True)
    print(f"Time: {time.perf_counter() - before:.6f}s")
    
    print(f"Avg: {timeit.timeit(main, number=1000)/1000:.6f}s")
