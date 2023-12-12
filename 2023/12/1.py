import os, sys
import time

def permute(configuration: str, char_index: int, numbers: list[int], number_index: int, current_block: int):
    # if we reached the end of the configuration, check if it is valid
    if char_index == len(configuration):
        return 1 if (current_block == 0 and number_index >= len(numbers)) or (number_index == len(numbers) - 1 and current_block == numbers[number_index]) else 0
    # if the char is a known, and is working spring
    if configuration[char_index] == ".":
        # the current block must end, and the next block must start
        if number_index >= len(numbers) or current_block == numbers[number_index]:
            return permute(configuration, char_index + 1, numbers, number_index + 1, 0)
        # the current block hasn't begun, we begin it later
        if current_block == 0:
            return permute(configuration, char_index + 1, numbers, number_index, current_block)
        # the current block is not enough, this permutation is not valid
        return 0
    # if the char is a known, and is broken spring
    if configuration[char_index] == "#":
        # the current block must be less than the number
        if number_index < len(numbers) and current_block < numbers[number_index]:
            return permute(configuration, char_index + 1, numbers, number_index, current_block + 1)
        # the current block is too much, this permutation is not valid
        return 0
    # if the char is unknown
    # first case, we set the unknown to be a working spring
    # the current block ends, we move to the next block
    if number_index >= len(numbers) or current_block == numbers[number_index]:
        # defaultdict sets this automatically
        first_perm = permute(configuration, char_index + 1, numbers, number_index+1, 0)
    # the current block hasn't begun, we begin it later
    elif current_block == 0:
        first_perm = permute(configuration, char_index + 1, numbers, number_index, 0)
    # the current block is not enough, this permutation is not valid
    else:
        first_perm = 0
        
    # second case, we set the unknown to be a broken spring
    # the current block is less than the number
    if number_index < len(numbers) and current_block < numbers[number_index]:
        second_perm = permute(configuration, char_index + 1, numbers, number_index, current_block + 1)
    # the current block is more then the number, this permutation is not valid
    else:
        second_perm = 0
    return first_perm + second_perm
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total_configurations = 0
    for line in lines:
        configuration, numbers = line.split(" ")
        numbers = [int(n) for n in numbers.split(",")]
        total_configurations += permute(configuration, 0, numbers, 0, 0)
    print(total_configurations)
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
