import os, sys
import time

class SpringConfig:
    def __init__(self, numbers: list[int], configuration: str) -> None:
        self.numbers = numbers
        self.configuration = configuration
        self.dp: dict[(int, int, int), int] = {}

    def permute(self, char_index: int,  number_index: int, current_block: int):
        # dp check
        if (char_index, number_index, current_block) in self.dp:
            return self.dp[(char_index, number_index, current_block)]

        # if we reached the end of the configuration, check if it is valid
        if char_index == len(self.configuration):
            result = 1  if (current_block == 0 and number_index >= len(self.numbers)) \
                        or (number_index == len(self.numbers) - 1 and current_block == self.numbers[number_index]) \
                        else 0
            self.dp[(char_index, number_index, current_block)] = result
            return result
        # if the char is a known, and is working spring
        if self.configuration[char_index] == ".":
            # the current block must end, and the next block must start
            if number_index >= len(self.numbers) or current_block == self.numbers[number_index]:
                result = self.permute(char_index + 1, number_index + 1, 0)
                self.dp[(char_index, number_index, current_block)] = result
                return result
            # the current block hasn't begun, we begin it later
            if current_block == 0:
                result = self.permute(char_index + 1, number_index, current_block)
                self.dp[(char_index, number_index, current_block)] = result
                return result
            # the current block is not enough, this permutation is not valid
            self.dp[(char_index, number_index, current_block)] = 0
            return 0
        # if the char is a known, and is broken spring
        if self.configuration[char_index] == "#":
            # the current block must be less than the number
            if number_index < len(self.numbers) and current_block < self.numbers[number_index]:
                result = self.permute(char_index + 1, number_index, current_block + 1)
                self.dp[(char_index, number_index, current_block)] = result
                return result
            # the current block is too much, this permutation is not valid
            self.dp[(char_index, number_index, current_block)] = 0
            return 0
        # if the char is unknown
        # first case, we set the unknown to be a working spring
        # the current block ends, we move to the next block
        if number_index >= len(self.numbers) or current_block == self.numbers[number_index]:
            first_perm = self.permute(char_index + 1, number_index+1, 0)
        # the current block hasn't begun, we begin it later
        elif current_block == 0:
            first_perm = self.permute(char_index + 1, number_index, 0)
        # the current block is not enough, this permutation is not valid
        else:
            first_perm = 0
        # second case, we set the unknown to be a broken spring
        # the current block is less than the number
        if number_index < len(self.numbers) and current_block < self.numbers[number_index]:
            second_perm = self.permute(char_index + 1, number_index, current_block + 1)
        # the current block is more then the number, this permutation is not valid
        else:
            second_perm = 0
        self.dp[(char_index, number_index, current_block)] = first_perm + second_perm
        return first_perm + second_perm
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total_configurations = 0
    for line in lines:
        configuration, numbers = line.split(" ")
        configuration = "?".join([configuration for _ in range(5)])
        numbers = ",".join([numbers for _ in range(5)])
        numbers = [int(n) for n in numbers.split(",")]
        config = SpringConfig(numbers, configuration)
        total_configurations += config.permute(0, 0, 0)
    print(total_configurations)
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
