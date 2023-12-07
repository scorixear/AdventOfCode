import os, sys
import time
import timeit
from functools import cmp_to_key


card_to_value = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_highest_groups(hand):
    card_apperance = {}
    highest_hit = 0 
    highest_hit_card = ""
    second_highest_hit = 0
    card_values = []
    joker_count = 0
    for c in hand:
        card_values.append(card_to_value[c])
        if c in card_apperance:
            card_apperance[c] += 1
        else:
            card_apperance[c] = 1
        if c == "J":
            joker_count += 1
        elif card_apperance[c] > highest_hit:
            if highest_hit_card != c:
                second_highest_hit = highest_hit
                highest_hit_card = c
            highest_hit = card_apperance[c]
        elif card_apperance[c] > second_highest_hit:
            second_highest_hit = card_apperance[c]
    return highest_hit + joker_count, second_highest_hit, card_values

def compare_cards(card1, card2):
    highest_hit1, second_highest_hit1, card_values1 = get_highest_groups(card1[0])
    highest_hit2, second_highest_hit2, card_values2 = get_highest_groups(card2[0])
    
    if highest_hit1 > highest_hit2:
        return 1
    if highest_hit1 < highest_hit2:
        return -1
    if second_highest_hit1 > second_highest_hit2:
        return 1
    if second_highest_hit1 < second_highest_hit2:
        return -1
    for a, b in zip(card_values1, card_values2):
        if a > b:
            return 1
        if a < b:
            return -1
    return 0
    
        
            
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")
    
    cards = []
    for line in lines:
        hand, bid = line.split(" ",1)
        cards.append((hand, bid))
    
    cards.sort(key=cmp_to_key(compare_cards))
    
    total_won = 0
    for i, card in enumerate(cards):
        total_won += (i+1) * int(card[1])
    print(total_won)
    
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
    
    # print(f"Avg time: {timeit.timeit(main, number=1000)/1000:.6f}s")
