import os, sys
import time
import timeit
from RangeClasses import SortedRangeList

class SeedMap:
    def __init__(self, off: str, to: str):
        self.off = off
        self.to = to
        # tuple of (source, max_source, target)
        # source is inclusive, max_source is exclusive
        self.map_values: list[tuple[int, int, int]] = []
    # add a mapping to the list
    # ranges are non-overlapping
    def add(self, target: int, source: int, offset: int):
        self.map_values.append((source, source + offset, target))
    def sort(self):
        self.map_values.sort(key=lambda x: x[0])
    def get_destination(self, ranges: SortedRangeList) -> SortedRangeList:
        new_ranges = SortedRangeList()
        # for each range of seeds
        for start, end in ranges:
            # if we fully mapped the range, we can continue with next range
            found_mapping = False
            # for each mapping range
            for source, max_source, target in self.map_values:
                # if start is before range
                if start < source:
                    # if end is before range
                    if end < source:
                        # we can add this range
                        # ---- start -- end -- source -- max_source ----
                        new_ranges.add(start, end)
                        found_mapping = True
                        break
                    # else if end is in between range
                    if end <= max_source:
                        # we add only until source
                        # ---- start -- source -- end -- max_source ----
                        new_ranges.add(start, source)
                        # and map the rest
                        # ---- target -- target + (end - source) -- target + (max_source - source) ----
                        new_ranges.add(target, target + (end - source))
                        found_mapping = True
                        break
                    # else if end is after range
                    # we add only until source
                    # ---- start -- source -- max_source -- end ----
                    new_ranges.add(start, source)
                    # and map in between
                    # ---- target -- target + (max_source - source) ----
                    new_ranges.add(target, target + (max_source - source))
                    # we continue with the rest of the range
                    start = max_source
                # else if start is in between map range
                elif source <= start < max_source:
                    # if end is in between range
                    if end <= max_source:
                        # we map all
                        # ---- source -- start -- end -- max_source ----
                        # ---- target -- target + (start - source) -- target + (end - source) -- target + (max_source - source) ----
                        new_ranges.add(target + (start - source), target + (end - source))
                        found_mapping = True
                        break
                    # else if end is after this range
                    # we map until max_source
                    # ---- source -- start -- max_source -- end ----
                    # ---- target -- target + (start - source) -- target + (max_source - source) -- target + (end - source) ----
                    new_ranges.add(target + (start - source) , target + (max_source - source))
                    # we continue with the rest of the range
                    start = max_source
                # else if start is after range
                # we continue with the rest of the range
            # if we didn't find a mapping, we add the remaining range
            if not found_mapping:
                new_ranges.add(start, end)
        # we merge the ranges, so they are non-overlapping
        return new_ranges
    def __str__(self) -> str:
        return f"{self.off} => {self.to}"
    def __repr__(self) -> str:
        return self.__str__()

def main():
    with open(os.path.join(sys.path[0],"example.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")
    # split seeds
    # example input "seeds: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
    seed_range = lines[0].split(": ")[1].split(" ")
    # example output ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", ...]
    seeds = SortedRangeList()
    # for each pair of seed inputs
    for i in range(0, len(seed_range), 2):
        # add the range to the list
        seeds.add(int(seed_range[i]), int(seed_range[i]) + int(seed_range[i+1]))
    # create list of seed maps
    seed_maps: list[SeedMap] = []
    # start reading first map
    current_map = None
    # for each line after seeds
    for line in lines[1:]:
        # skip empty lines
        if line == "":
            continue
        # if new map declaration begins
        if line.endswith("map:"):
            # get from and to strings (just for printing)
            off, to = line.split(" ")[0].split("-to-", 1)
            # create new map
            current_map = SeedMap(off, to)
            # and add it to the list
            seed_maps.append(current_map)
        else:
            if(current_map is None):
                raise Exception("No map declaration")
            # if not new map declaration, add the mapping
            current_map.add(*[int(s) for s in line.split(" ")])
    # we sort seed map ranges, so they are ascending
    # seed map ranges are not overlapping
    # later on, we can early break out as later ranges will start further than the current seed
    for seed_map in seed_maps:
        seed_map.sort()
    
    # for each mapping
    for seed_map in seed_maps:
        # map all seed ranges to new destination
        seeds = seed_map.get_destination(seeds)
        print(seeds)
    
    # print the minimum location, which will be the start of a range
    print(min(start for start, _ in seeds))
            

if __name__ == "__main__":
    
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f} seconds")
    # total_time = timeit.timeit(main, number=500)
    # print(f"Average time: {total_time/500:.6f} seconds")
