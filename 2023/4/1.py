import os, sys


def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total_sum = 0
    for card in lines:
        winning, having = card.split(": ")[1].split(" | ", 1)
        winning = winning.split(" ")
        having = having.split(" ")
        matches = 0
        for h in having:
            if h.strip() != "":
                if h in winning:
                    matches += 1
        if matches > 0:
            total_sum += 2 ** (matches-1)
    print(total_sum)

if __name__ == "__main__":
    main()