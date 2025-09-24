import os, sys
import time

class Instruction:
    def __init__(self, low_target, high_target, low_is_output, high_is_output):
        self.low_target = low_target
        self.low_is_output = low_is_output
        self.high_target = high_target
        self.high_is_output = high_is_output

class Bot:
    def __init__(self, bot_id):
        self.id = bot_id
        self.holding: list[int] = []
        self.instructions: list[Instruction] = []
    def can_give(self):
        return len(self.holding) == 2 and len(self.instructions) > 0
    def can_receive(self):
        return len(self.holding) < 2
    def give(self, bots: dict[int, "Bot"]) -> list[tuple[int, int]]:
        if not self.can_give():
            return []
        low, high = sorted(self.holding)
        if low == 17 and high == 61:
            print(f"Bot {self.id} is responsible for comparing 17 and 61")
        for inst in self.instructions:
            if inst.low_is_output and inst.high_is_output:
                self.holding = []
                return [(inst.low_target, low), (inst.high_target, high)]
            if inst.low_is_output:
                if not bots[inst.high_target].can_receive():
                   continue
                bots[inst.high_target].holding.append(high)
                self.holding = []
                return [(inst.low_target, low)]
            if inst.high_is_output:
                if not bots[inst.low_target].can_receive():
                    continue
                bots[inst.low_target].holding.append(low)
                self.holding = []
                return [(inst.high_target, high)]
            if not bots[inst.low_target].can_receive() or not bots[inst.high_target].can_receive():
                continue
            bots[inst.low_target].holding.append(low)
            bots[inst.high_target].holding.append(high)
            self.holding = []
            return []
        return []
            
        
    

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    bots: dict[int, Bot] = {}
    outputs: dict[int, int] = {}
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "value":
            value = int(parts[1])
            bot_id = int(parts[5])
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            if not bots[bot_id].can_receive():
                raise Exception("Bot cannot receive more values")
            bots[bot_id].holding.append(value)
        else:
            bot_id = int(parts[1])
            low_target = int(parts[6])
            low_is_output = parts[5] == "output"
            high_target = int(parts[11])
            high_is_output = parts[10] == "output"
            if bot_id not in bots:
                bots[bot_id] = Bot(bot_id)
            bots[bot_id].instructions.append(Instruction(low_target, high_target, low_is_output, high_is_output))
    bot_action = True
    while bot_action:
        bot_action = False
        for bot in bots.values():
            if bot.can_give():
                result = bot.give(bots)
                for target, value in result:
                    if target not in outputs:
                        outputs[target] = value
                    else:
                        raise Exception("Output already has a value")
                bot_action = True
    print(outputs[0]*outputs[1]*outputs[2])
                

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
