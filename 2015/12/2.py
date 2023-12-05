import json
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    json_object = json.loads(text)

def sum_numbers(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, list):
        return sum([sum_numbers(item) for item in obj])
    elif isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum([sum_numbers(item) for item in obj.values()])
    else:
        return 0
print(sum_numbers(json_object))
            
    
