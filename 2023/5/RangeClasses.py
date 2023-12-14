from typing import Iterable, List, Tuple, override

class SortedRangeList(List):
    """Represents a list of ranges.

    Args:
        List (_type_): _description_
    """

    def __init__(self, ranges: Iterable[Tuple[int, int]] = None):
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
    def __copy__(self):
        return SortedRangeList(self.ranges.copy())
    @override
    def __bool__(self):
        return bool(self.ranges)
    @override
    def __bytes__(self):
        return bytes(self.ranges)
    @override
    def __format__(self, format_spec):
        return format(self.ranges, format_spec)
