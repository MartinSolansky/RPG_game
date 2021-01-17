import random

from character import Character


class Beast(Character):
    def __init__(self, name, level, hp_coefficient, attack_info, mana=0, armor='nothing'):
        self.max_hp = hp_coefficient * level
        super().__init__(level, self.max_hp, mana)
        self.actual_hp = self.max_hp
        self.armor = armor
        self.dmg_reduction = self.get_armor_reduction()
        self.name = name
        self.attack_possibilities = attack_info


class Human(Beast):
    def __init__(self, name, level):
        HP_COEFICIENT = 30
        weapons = {'dagger': 4, 'sword': 6}
        armor = random.choice(['nothing', 'cloth', 'leather', 'chain mail', 'plate'])
        weapon = random.choice(list(weapons.items()))
        super().__init__(name, level, HP_COEFICIENT, weapon, mana=0, armor=armor)


class Animal(Beast):
    pass


class Undead(Beast):
    pass
