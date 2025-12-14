import os, sys
import time


class Present:
    def __init__(self, index: int, blocked: list[tuple[int, int]]):
        self.index = index
        self.blocked = blocked
        self.original_blocked = []
        self.max_x = 0
        self.max_y = 0
        self.rotations = []
        self.horizontal_flipped_rotations = []
        self.vertical_flipped_rotations = []
        self.flipped_rotations = []

    def generate(self):
        self.original_blocked = self.blocked.copy()
        self.max_x = max(bx for (bx, by) in self.blocked)
        self.max_y = max(by for (bx, by) in self.blocked)
        self.rotations = self.generate_rotations(self.blocked)
        self.horizontal_flipped_rotations = self.generate_rotations(
            self.horizontal_flip(self.blocked)
        )
        self.vertical_flipped_rotations = self.generate_rotations(
            self.vertical_flip(self.blocked)
        )
        self.flipped_rotations = self.generate_rotations(
            self.horizontal_flip(self.vertical_flip(self.blocked))
        )

    def generate_rotations(
        self, blocked: list[tuple[int, int]]
    ) -> list[list[tuple[int, int]]]:
        rotations = [blocked.copy()]
        for _ in range(3):
            rotations.append(self.rotate_right(rotations[-1]))
        return rotations

    def rotate_right(self, blocked: list[tuple[int, int]]) -> list[tuple[int, int]]:
        return [(by, self.max_x - bx) for (bx, by) in blocked]

    def horizontal_flip(self, blocked: list[tuple[int, int]]) -> list[tuple[int, int]]:
        return [(self.max_x - bx, by) for (bx, by) in blocked]

    def vertical_flip(self, blocked: list[tuple[int, int]]) -> list[tuple[int, int]]:
        return [(bx, self.max_y - by) for (bx, by) in blocked]

    def translate(
        self, blocked: list[tuple[int, int]], x: int, y: int
    ) -> list[tuple[int, int]]:
        return [(bx + x, by + y) for (bx, by) in blocked]

    def reset(self):
        self.blocked = self.original_blocked.copy()

    def apply_transform(
        self,
        rotation: int,
        horizontal_flipped: bool,
        vertical_flipped: bool,
        translation: tuple[int, int],
    ) -> None:
        if horizontal_flipped and vertical_flipped:
            self.blocked = self.flipped_rotations[rotation]
        elif horizontal_flipped:
            self.blocked = self.horizontal_flipped_rotations[rotation]
        elif vertical_flipped:
            self.blocked = self.vertical_flipped_rotations[rotation]
        else:
            self.blocked = self.rotations[rotation]
        self.blocked = self.translate(self.blocked, translation[0], translation[1])

    def overlaps(self, other: "Present") -> bool:
        for bx, by in self.blocked:
            for obx, oby in other.blocked:
                if bx == obx and by == oby:
                    return True
        return False

    def copy(self) -> "Present":
        new_present = Present(self.index, self.blocked.copy())
        return new_present

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Present(index={self.index}, blocked={self.blocked})"


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    presents = []
    present_readin = False
    region_readin = False
    curr_present = []
    total = 0
    for i, line in enumerate(lines):
        if line == "":
            blocked = []
            for by, present_line in enumerate(curr_present):
                for bx, char in enumerate(present_line):
                    if char == "#":
                        blocked.append((bx, by))
            present = Present(i, blocked)
            present.generate()
            presents.append(present)
            present_readin = False
            curr_present = []
            continue
        if not present_readin:
            if line.endswith(":"):
                present_readin = True
                continue
            else:
                region_readin = True
        if present_readin:
            curr_present.append(line)
        if region_readin:
            parts = line.split(":")
            x, y = map(int, parts[0].strip().split("x"))
            amounts = [int(i) for i in parts[1].strip().split(" ")]
            print("Solving for region", x, "x", y, "with amounts", amounts)
            if solve_region(presents, x, y, amounts, []):
                total += 1
    print(total)


def solve_region(
    presents: list[Present],
    region_x: int,
    region_y: int,
    amounts: list[int],
    other_presents: list[Present],
) -> bool:
    found_present = None
    found_index = -1
    # print(amounts)
    for i, amount in enumerate(amounts):
        if amount > 0:
            found_present = presents[i]
            found_index = i
            break
    if found_present is None:
        return True
    for rotation in range(4):
        for horizontal_flipped in [False, True]:
            for vertical_flipped in [False, True]:
                for x in range(region_x - found_present.max_x):
                    for y in range(region_y - found_present.max_y):
                        overlap = False
                        found_present.reset()
                        found_present.apply_transform(
                            rotation, horizontal_flipped, vertical_flipped, (x, y)
                        )
                        for other in other_presents:
                            does_overlap = other.overlaps(found_present)
                            if does_overlap:
                                overlap = True
                                break
                        if not overlap:
                            found_solution = solve_region(
                                presents,
                                region_x,
                                region_y,
                                [
                                    amounts[j] - (1 if j == found_index else 0)
                                    for j in range(len(amounts))
                                ],
                                other_presents + [found_present.copy()],
                            )
                            if found_solution:
                                return True
    return False


def print_presents(presents: list[Present], region_x: int, region_y: int) -> None:
    grid = [["." for _ in range(region_x)] for _ in range(region_y)]
    for present in presents:
        for bx, by in present.blocked:
            grid[by][bx] = "#"
    for line in grid:
        print("".join(line))
    print()


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
