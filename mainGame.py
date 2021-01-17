#!/usr/bin/python3
import random
import sys

import hero
import bestiary
from AttackMechanics import Combat


class GameMechanism:
    @classmethod
    def dice_roll(cls, size: int, repetition=1):
        """Return dice roll on given dice and roll repetition"""
        possibilities = list(range(1, size+1))
        result = 0
        for i in range(repetition):
            result += random.choice(possibilities)
        return result

    @classmethod
    def hero_creation(cls):
        """Function prompt creation of hero from hero classes."""
        print('1-Warrior: master of weapons')
        print('2-Rogue: silent killer who hide in shadows')
        print('3-Mage: Master of arcane (f)arts')
        choice = int(input('Choose your spec(1-3): '))
        choices = ['nothing', hero.Warrior, hero.Rogue, hero.Mage]
        return choices[choice]()

    @classmethod
    def game_end(self):
        """"Function execution result in the end of game"""
        print('You have failed in your adventure!')
        _ = input('Press any key to shut down program.')
        sys.exit()


if __name__ == '__main__':
    user_1 = GameMechanism.hero_creation()

    attacker1 = bestiary.Human('Thug', 1)
    attacker2 = bestiary.Human('Thug', 1)
    cmb1 = Combat(user_1, attacker1, attacker2)
    combat = True
    while combat:
        while len(cmb1.participants) > 1:
            cmb1.one_round(cmb1.round)
            cmb1.death_check()
            combat = cmb1.combat_end(cmb1.round_check())

