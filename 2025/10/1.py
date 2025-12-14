import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    answ = 0
    for line in lines:
        parts = line.split(" ")
        indicators = [True if c == "#" else False for c in parts[0][1:-1]]
        buttons = [[int(x) for x in p[1:-1].split(",")] for p in parts[1:-1]]
        joltages = [int(x) for x in parts[-1][1:-1].split(",")]
        result = try_buttons(buttons, 0, indicators, [False] * len(indicators), [])
        print(f"Indicators: {indicators}, Buttons: {buttons}, Result: {result}")
        answ += result[0]
    print(answ)


def try_buttons(
    buttons: list[list[int]],
    index: int,
    indicators: list[bool],
    state: list[bool],
    pressed: list[int],
) -> tuple[int, list[int]]:
    if index >= len(buttons):
        is_equal = all(state[i] == indicators[i] for i in range(len(indicators)))
        return (len(pressed), pressed) if is_equal else (-1, [])
    pressResult, pressButtons = try_buttons(
        buttons,
        index + 1,
        indicators,
        toggle_state(state, buttons[index]),
        pressed + [index],
    )
    noPressResult, noPressButtons = try_buttons(
        buttons, index + 1, indicators, state, pressed
    )
    if noPressResult != -1 and (pressResult == -1 or noPressResult < pressResult):
        return (noPressResult, noPressButtons)
    return (pressResult, pressButtons)


def toggle_state(state: list[bool], button: list[int]) -> list[bool]:
    new_state = state.copy()
    for idx in button:
        new_state[idx] = not new_state[idx]
    return new_state


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
