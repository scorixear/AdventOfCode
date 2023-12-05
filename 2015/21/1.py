boss_health = 109
boss_damage = 8
boss_armor = 2

player_health = 100
player_damage = 0
player_armor = 0

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]
    
def fight(boss_health, boss_damage, boss_armor, player_health, player_damage, player_armor):
    player = player_health
    boss = boss_health
    while True:
        boss -= max(1, player_damage - boss_armor)
        if boss <= 0:
            return True
        player -= max(1, boss_damage - player_armor)
        if player <= 0:
            return False

def main():
    min_cost = 1000000
    max_cost = 0
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2 and ring1[0] != 0:
                        continue
                    cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                    damage = weapon[1] + armor[1] + ring1[1] + ring2[1]
                    resistance = weapon[2] + armor[2] + ring1[2] + ring2[2]
                    if fight(boss_health, boss_damage, boss_armor, player_health, damage, resistance):
                        min_cost = min(cost, min_cost)
    print(min_cost)
if __name__ == '__main__':
    main()