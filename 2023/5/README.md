# Day 5: Mapping Slapping
Now this, this is a puzzle worth explaining. Day 5 really increased the difficulty and was the first day most of the questions on reddit were about.

But first, lets start easy with Part 1. We are given multiple mapping ranges.
Each range is given as target start, source start and source offset.

For example, a mapping range of `1 2 3` would mean that numbers in the range `[2,5)` are mapped to `[1,4)`. The notation for ranges are `[start, end)` while `[` denotes inclusive and `)` denotes exclusive.

When working with ranges, you should always strive to use inclusive starts and exclusive ends, as adding, merging and subtracting ranges follow the standard rules of normal numbers.
But generally speaking, as long as you are consistent, any notation will work.

Each mapping range is assigned to a certain map and there are 7 maps in total.
Our goal is now to map certain numbers through all the maps and determine the final result.
If a given mapping range applies to this number, it gets mapped. If no mapping range applies, the number stays the same.

It wasn't clear from the description of the puzzle, but all mapping ranges are non-overlapping making our job a lot easier.

For day 1, this sounds as straight forward as you might think.
I pulled out the logic for the actual "mapping" part into a separate class that looks like this:

```python
class SeedMap:
    def __init__(self, off: str, to: str):
        self.off = off
        self.to = to
        # mapping values
        # tuple represents (source, max_source, target)
        # source is inclusive, max_source is exclusive
        self.map_values: list[tuple[int, int, int]] = []
    def add(self, target: int, source: int, offset: int):
        self.map_values.append((source, source + offset, target))
    def get_destination(self, given: int):
        # for each mapping range
        for source, max_source, target in self.map_values:
            # if given is in between range
            if source <= given < max_source:
                # map it
                return target + (given - source)
        # if no range was found,
        # return value unchanged
        return given
```

We parse in the input:
```python	
 # parse first line to get all seeds
seeds = [int(s) for s in lines[0].split(": ")[1].split(" ")]
# create seed maps
seed_maps: list[SeedMap] = []
current_map: Optional[SeedMap] = None
# for each other line except 1st line
for line in lines[1:]:
    # skip empty lines
    if line == "":
        continue
    # if new map declaration start
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
        # the * will unpack the list into 3 arguments
        current_map.add(*[int(s) for s in line.split(" ")])
```

and then iterate over each seed (which is the number we should map), and map it through all seven maps. After that, the minimum number is the result.

```python
min_location = math.inf
# for each seed
for seed in seeds:
    # map it through all seed maps
    for seed_map in seed_maps:
        seed = seed_map.get_destination(seed)
    # and update the minimum location
    min_location = min(min_location, seed)
print(min_location)
```

# Part 2
Part 2 is where this approach doesn't work anymore. We still search for the lowest number after mapping all numbers, but now we are given number ranges.
These ranges include so many numbers, that a brute force approach like part 1 probably takes the age of the universe to complete. Also, the start of seed ranges, as I will call them from now, do not necessarily end at the lowest point after mapping, as mapping ranges might split them apart.

After considering several speedup approaches, I decided to put in the work and actually rewrite my part 1 solution to work with ranges. For that, I added a new class called `SortedRangeList` which is a list of ranges. This sorted range list as several advantages.
First of all, the ranges are sorted by default, meaning the start of ranges are always in ascending orders. Secondly, ranges are not overlapping.

If a new range is added, and it overlaps with an already included range, it gets merged into that range. And if two ranges are adjacent, they get merged to.
This level of complexity is certainly not needed for this part, as it only decreases runtime by about 10ms, but I figured having a class that can deal with ranges might be usefull for future puzzles.

```python
class SortedRangeList(List):
    """Represents a list of ranges.

    Args:
        List (_type_): _description_
    """

    def __init__(self, ranges: Optional[Iterable[Tuple[int, int]]] = None):
        """Initializes the list of ranges.
        
        Args:
            ranges (Iterable[Tuple[int, int]], optional): The ranges to add to the list. Defaults to None.
            Must be sorted and non-overlapping! Given as [start, end) interval. Inclusive start, exclusive end!
        """
        self.ranges: List[Tuple[int, int]] = []
        if ranges is not None:
            ranges = list(ranges)
    def add_tuple(self, r: Tuple[int, int]) -> None:
        """Adds a range tuple to the list. Runtime is O(N). Space is O(1).

        Args:
            r (Tuple[int, int]): The range to add. Given as [start, end) interval.
            Inclusive start, exclusive end!
        """
        self.add(r[0], r[1])
    def add(self, range_start: int, range_end: int) -> None:
        """Adds a range tuple to the list. Runtime is O(N). Space is O(1).

        Args:
            range_start (int): inclusive start of the range
            range_end (int): exclusive end of the range
        """
        # for each already added range
        for i, (s, e) in enumerate(self.ranges):
            # if start is before range
            if range_start < s:
                # if end is before range
                if range_end < s:
                    # ---- start -- end -- s -- e ----
                    # if previous range is right next to this range
                    if i > 0 and self.ranges[i-1][1] == range_start:
                        # we merge the two ranges
                        self.ranges[i-1] = (self.ranges[i-1][0], range_end)
                        return
                    # else we add the range
                    self.ranges.insert(i, (range_start, range_end))
                    return
                # else if end is in between range
                if range_end <= e:
                    # we add only until s
                    # ---- start -- s -- end -- e ----
                    # if previous range is right next to this range
                    if i > 0 and self.ranges[i-1][1] == range_start:
                        # we merge the two ranges
                        self.ranges[i-1] = (self.ranges[i-1][0], e)
                        del self.ranges[i]
                        i -= 1
                        return
                    # else we expand the range
                    self.ranges[i] = (range_start, e)
                    return
                # else if end is after range
                # ---- start -- s -- e -- end ----

                # if previous range is right next to this range
                if i > 0 and self.ranges[i-1][1] == range_start:
                    # we merge the two ranges
                    self.ranges[i-1] = (self.ranges[i-1][0], e)
                    del self.ranges[i]
                    i -= 1
                    # we continue with the rest of the range
                    range_start = e
                    continue

                # else we expand the range
                self.ranges[i] = (range_start, e)
                # we continue with the rest of the range
                range_start = e
                continue
            # else if start is in between range
            if range_start <= s <= range_end:
                # if end is in between range
                if range_end <= e:
                    # we already have this range
                    # ---- s -- start -- end -- e ----
                    return
                # else if end is after this range
                # we continue with the rest of the range
                # ---- s -- start -- e -- end ----
                range_start = e
            # else if start is after range
            # we continue with the rest of the range
            # ---- s -- e -- start -- end ----
        # if we haven't returned yet, we add the remaining range
        # if previous range is right next to this range
        if len(self.ranges) > 0 and self.ranges[-1][1] == range_start:
            # we merge the two ranges
            self.ranges[-1] = (self.ranges[-1][0], range_end)
            return
        # else we add the range
        self.ranges.append((range_start, range_end))
    @override
    def __str__(self) -> str:
        return "["+", ".join([f"({s}, {e-s})" for s, e in self.ranges])+"]"
    @override
    def __repr__(self) -> str:
        return repr(self.ranges)
    @override
    def __iter__(self):
        return iter(self.ranges)
    @override
    def __len__(self):
        return len(self.ranges)
    @override
    def __getitem__(self, i: int):
        return self.ranges[i]
    @override
    def __delitem__(self, i: int):
        del self.ranges[i]
    @override
    def __add__(self, other: Iterable[Tuple[int, int]]):
        new_range_list = SortedRangeList(self.ranges.copy())
        for r in other:
            new_range_list.add_tuple(r)
        return new_range_list
    @override
    def __iadd__(self, other: Iterable[Tuple[int, int]]):
        for r in other:
            self.add_tuple(r)
        return self
    @override
    def __contains__(self, r: Tuple[int, int]):
        for s, e in self.ranges:
            if s <= r[0] < r[1] <= e:
                return True
        return False
    @override
    def __eq__(self, other):
        return self.ranges == other.ranges
    @override
    def __ne__(self, other):
        return self.ranges != other.ranges
    @override
    def __lt__(self, other):
        return self.ranges < other.ranges
    @override
    def __le__(self, other):
        return self.ranges <= other.ranges
    @override
    def __gt__(self, other):
        return self.ranges > other.ranges
    @override
    def __ge__(self, other):
        return self.ranges >= other.ranges
    @override
    def __hash__(self):
        return hash(self.ranges)
    @override
    def __format__(self, format_spec):
        return format(self.ranges, format_spec)
```

Having this sorted range list also allows for some neat shortcuts when comparing ranges.
For example, if a given range that needs to be inserted is before a range already in the list, than this range is definitly not included, as all following ranges come after the given range.

Now, lets adjust the `SeedMap` to work with ranges aswell.
```python
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
```

The `get_destination` function now takes a `SortedRangeList` as input and returns a `SortedRangeList` as output. This part now consideres 6 cases.
1. The seed range is entirely before the mapping range
2. The seed range starts before the mapping range and ends in between the mapping range
3. The seed range starts before the mapping range and ends after the mapping range
4. The seed range starts in between the mapping range and ends in between the mapping range
5. The seed range starts in between the mapping range and ends after the mapping range
6. The seed range is entirely after the mapping range

If part of the seed range is mapped, the non-mapped part must be tried again for all other mapping ranges. And if the seed range is fully mapped, we can exit early.
Sorting the mapping ranges gives the opportunity to exit early, as we can apply the same logic as above that if case 1 or 2 apply, the left over range will definitly not be mapped by any mapping range.

As there aren't that many mapping ranges per map, this doesn't really increase the performance that much, but it's a nice extension.

If after trying each mapping range there still exists a left over seed range, this seed range is taken as is and added to the new now mapped seed ranges.
Our implementation of the `SortedRangeList` class ensures that the resulting ranges are non-overlapping, fully merged and minimal, so we can just continue with the next seed map.

The rest of the code is the same as in part 1.