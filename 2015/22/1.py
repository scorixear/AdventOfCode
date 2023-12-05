from collections import defaultdict
import math
import os, sys
from typing import Optional
from xml.etree.ElementTree import SubElement

class Spell:
    def __init__(self, name: str, mana: int, damage: int, armor: int, heal: int, effect: int, effect_damage: int, effect_armor: int, effect_mana: int):
        self.name = name
        self.mana = mana
        self.damage = damage
        self.armor = armor
        self.heal = heal
        self.effect = effect
        self.effect_damage = effect_damage
        self.effect_armor = effect_armor
        self.effect_mana = effect_mana
    def calculate_effects(self, cool_down: int, boss_health: int, player_mana: int, player_armor: int):
        # if no effect, return values
        if self.effect == 0:
            return boss_health, player_mana, player_armor
        # if effect just turned on, update armor
        if cool_down == self.effect:
            player_armor += self.effect_armor
        # update values
        player_mana += self.effect_mana
        boss_health -= self.effect_damage
        return boss_health, player_mana, player_armor
    def __hash__(self) -> int:
        return hash(self.name)
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.name

memorized = dict()

def battle(boss_health: int, boss_damage: int, player_health: int, player_mana: int, player_armor: int, spells: list[Spell]) -> Optional[int]:
    global memorized
    # minimum mana spent to win
    mana_spent = 0
    # for each spell cast
    effects: dict[Spell, int] = defaultdict(int)
    casted_spells = []
    for spell in spells:
        # for each effect currently active
        for effect_spell, effect_cooldown in effects.items():
            # if effect is not active, disregard
            if effect_cooldown == 0:
                continue
            # and update the values
            boss_health, player_mana, player_armor = effect_spell.calculate_effects(effect_cooldown, boss_health, player_mana, player_armor)
            effects[effect_spell] -= 1
            if effect_cooldown == 1 and effect_spell.effect_armor > 0:
                player_armor -= effect_spell.effect_armor
            
        # if the effects killed the boss with no turn made
        # we won, return mana spent
        if boss_health <= 0:
            memorized[tuple(casted_spells)] = mana_spent
            return mana_spent
        
        # player turn
        # is spell is possible to cast and no effect is running
        if spell.mana <= player_mana and (spell.effect == 0 or effects[spell] == 0):
            casted_spells.append(spell)
            # update values
            boss_health -= spell.damage
            player_health += spell.heal
            player_mana -= spell.mana
            mana_spent += spell.mana
            if spell.effect != 0:
                effects[spell] = spell.effect
        else:
            # if we can't cast the spell, we lose
            memorized[tuple(casted_spells)] = math.inf
            return math.inf
        # if this turn killed the boss
        # we won with the current spell mana spent
        if boss_health <= 0:
            memorized[tuple(casted_spells)] = mana_spent
            return mana_spent
        
        # otherwise boss turn
        # for each effect currently active
        for effect_spell, effect_cooldown in effects.items():
            # if effect is not active, disregard
            if effect_cooldown == 0:
                continue
            # and update the values
            boss_health, player_mana, player_armor = effect_spell.calculate_effects(effect_cooldown, boss_health, player_mana, player_armor)
            effects[effect_spell] -= 1
            if effect_cooldown == 1 and effect_spell.effect_armor > 0:
                player_armor -= effect_spell.effect_armor
        # if the effects killed the boss with no turn made
        # we won with the current spell mana spent
        if boss_health <= 0:
            memorized[tuple(casted_spells)] = mana_spent
            return mana_spent
        # otherwise boss deals damage
        # update player health (boss turn)
        player_health -= max(1, boss_damage - player_armor)
        # if the player died, this combination is not successful
        # therefore we return infinity
        if player_health <= 0:
            memorized[tuple(casted_spells)] = math.inf
            return math.inf
    # if we reached this point, the boss didn't die and we ran out of spells
    # therefore we return infinity
    memorized[tuple(casted_spells)] = math.inf
    return math.inf


def iterate_spells(spells: list[Spell], max_spells: int, casted_spells: list[Spell], values: tuple[int, int, int, int, int]):
    if len(casted_spells) == max_spells:
        boss_health, boss_damage, player_health, player_mana, player_armor = values
        result = battle(boss_health, boss_damage, player_health, player_mana, player_armor, casted_spells)
        print(f"{casted_spells} => {result}")
        return result
        
    mana_spent = math.inf
    for spell in spells:
        casted_spells.append(spell)
        sub_sequence_spells = []
        found_memorized = False
        for sub_spell in casted_spells:
            sub_sequence_spells.append(sub_spell)
            if tuple(sub_sequence_spells) in memorized:
                mana_spent = min(mana_spent, memorized[tuple(sub_sequence_spells)])
                found_memorized = True
                if len(sub_sequence_spells) < len(casted_spells):
                    return mana_spent
                break
        if not found_memorized:
            mana_spent = min(mana_spent, iterate_spells(spells, max_spells, casted_spells.copy(), values))
        casted_spells.pop()
    return mana_spent

def main():

    spells = [
        Spell("M", 53, 4, 0, 0, 0, 0, 0, 0),
        Spell("D", 73, 2, 0, 2, 0, 0, 0, 0),
        Spell("S", 113, 0, 0, 0, 6, 0, 7, 0),
        Spell("P", 173, 0, 0, 0, 6, 3, 0, 0),
        Spell("R", 229, 0, 0, 0, 5, 0, 0, 101),
    ]

    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    player_health = int(lines[0].split(": ")[1])
    player_mana = int(lines[1].split(": ")[1])
    player_armor = 0
    boss_health = int(lines[2].split(": ")[1])
    boss_damage = int(lines[3].split(": ")[1])
    
    print(iterate_spells(spells, 10, [], (boss_health, boss_damage, player_health, player_mana, player_armor)))
    #print(battle(boss_health, boss_damage, player_health, player_mana, player_armor, [spells[4], spells[2], spells[1], spells[3], spells[0]]))


    
    

if __name__ == "__main__":
    main()
