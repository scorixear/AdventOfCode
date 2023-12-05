import functools
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    signals = {}
    for line in lines:
        line = line.split(" -> ")
        signals[line[1]] = line[0]
@functools.lru_cache(maxsize=None)
def get_signal(signal: str):
    if signal.isdigit():
        return int(signal)
    signal = signals[signal]
    if signal.isdigit():
        return int(signal)
    if "AND" in signal:
        signal = signal.split(" AND ")
        return (get_signal(signal[0]) & get_signal(signal[1]))%65536
    if "OR" in signal:
        signal = signal.split(" OR ")
        return (get_signal(signal[0]) | get_signal(signal[1]))%65536
    if "LSHIFT" in signal:
        signal = signal.split(" LSHIFT ")
        return (get_signal(signal[0]) << get_signal(signal[1]))%65536
    if "RSHIFT" in signal:
        signal = signal.split(" RSHIFT ")
        return (get_signal(signal[0]) >> get_signal(signal[1]))%65536
    if "NOT" in signal:
        signal = signal.replace("NOT ", "")
        return (~get_signal(signal))%65536
    return get_signal(signal)

signals["b"] = "3176"
print(get_signal("a"))
    
