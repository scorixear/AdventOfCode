import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    base_floors: list[list[str]] = []
    for i, line in enumerate(lines):
        items = line.split(" contains ")[1].replace(" and ", ", ").replace("a ", "").replace("an ", "").replace(".", "").split(", ")
        floor = []
        for item in items:
            item = item.strip().replace(",", "").replace("-compatible", "")
            if item == "nothing relevant":
                continue
            floor.append(item.replace(" microchip", "-M").replace(" generator", "-G"))
        base_floors.append(floor)
    initial_state: tuple[int, tuple[tuple[str,...],...]] = (0, tuple(tuple(sorted(floor)) for floor in base_floors))
    seen = set()
    states = {initial_state: 0}
    min_steps = None
    while states:
        new_states = {}
        for state, steps in states.items():
            if min_steps is not None and steps >= min_steps:
                continue
            elevator, floors = state
            if all(len(floor) == 0 for floor in floors[:-1]):
                if min_steps is None or steps < min_steps:
                    min_steps = steps
                continue
            current_floor = list(floors[elevator])
            for i in range(len(current_floor)):
                item1 = current_floor[i]
                # Move one item
                for direction in [-1, 1]:
                    new_elevator = elevator + direction
                    if new_elevator < 0 or new_elevator >= len(floors):
                        continue
                    new_floors = [list(floor) for floor in floors]
                    new_floors[elevator].remove(item1)
                    new_floors[new_elevator].append(item1)
                    if not is_valid_floor(new_floors[elevator]) or not is_valid_floor(new_floors[new_elevator]):
                        continue
                    new_state = (new_elevator, tuple(tuple(sorted(floor)) for floor in new_floors))
                    if new_state in seen:
                        continue
                    seen.add(new_state)
                    if new_state not in new_states or steps + 1 < new_states[new_state]:
                        new_states[new_state] = steps + 1
                # Move two items
                for j in range(i + 1, len(current_floor)):
                    item2 = current_floor[j]
                    for direction in [-1, 1]:
                        new_elevator = elevator + direction
                        if new_elevator < 0 or new_elevator >= len(floors):
                            continue
                        new_floors = [list(floor) for floor in floors]
                        new_floors[elevator].remove(item1)
                        new_floors[elevator].remove(item2)
                        new_floors[new_elevator].append(item1)
                        new_floors[new_elevator].append(item2)
                        if not is_valid_floor(new_floors[elevator]) or not is_valid_floor(new_floors[new_elevator]):
                            continue
                        new_state = (new_elevator, tuple(tuple(sorted(floor)) for floor in new_floors))
                        if new_state in seen:
                            continue
                        seen.add(new_state)
                        if new_state not in new_states or steps + 1 < new_states[new_state]:
                            new_states[new_state] = steps + 1
        states = new_states
    print(min_steps)

def is_valid_floor(floor: list[str]) -> bool:
    generators = {item[:-2] for item in floor if item.endswith("-G")}
    for item in floor:
        if item.endswith("-M"):
            element = item[:-2]
            if element not in generators and generators:
                return False
    return True

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
