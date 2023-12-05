import os, sys


def main():
    with open(os.path.join(sys.path[0],"example2"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    card_matches = []
    for card in lines:
        winning, having = card.split(": ")[1].split(" | ", 1)
        winning = winning.split(" ")
        having = having.split(" ")
        matches = 0
        for h in having:
            if h.strip() != "":
                if h in winning:
                    matches += 1
        card_matches.append(matches)
    card_count = [1] * len(card_matches)
    for i, matches in enumerate(card_matches):
        for j in range(i+1, min(i+matches+1, len(card_matches))):
            card_count[j] += card_count[i]
    print(sum(card_count)) 
            

if __name__ == "__main__":
    main()