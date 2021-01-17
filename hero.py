import random

from character import Character
#level, hp_coef, mana_coef


class Hero(Character):
    def __init__(self, base_hp, base_mana, hp_per_lvl: int, mana_per_lvl: int):
        #Stat related
        self.level = 1
        self.hp_per_lvl = hp_per_lvl
        self.mana_per_lvl = mana_per_lvl
        self.base_hp = base_hp
        self.base_mana = base_mana
        self.max_hp = self.get_max_hp()
        self.max_mana = self.get_max_energy()
        super().__init__(self.level, self.max_hp, self.max_mana)
        
        # Avatar related
        self.name = input('Chose your name: ')
        self.experience = 0
        self.hero_type = ''
        self.battle_regen = mana_per_lvl

        
    def check_experience(self):
        """Check experience adn if ready than level up"""
        pass

    def raise_lvl(self):
        """Raise stats according to lvl"""
        self.level += 1
        # Raise hp
        if self.actual_hp == self.max_hp:
            self.actual_hp = self.get_max_hp()
        self.max_hp = self.get_max_hp()

        # Raise mana
        if self.actual_mana == self.max_mana:
            self.actual_mana = self.max_mana
        self.max_mana = self.get_max_energy()

    def meditate(self):
        """For meditation to replenish hp/mana"""

        
    def get_max_hp(self):
        # TODO: Make debufs count
        """Determine highest HP possible according to lvl and spec"""
        max_hp = (self.hp_per_lvl * self.level) + self.base_hp
        return max_hp

    def get_max_energy(self):
        # TODO: Make debufs count
        """Determine highest energy possible according to lvl and spec"""
        max_mana = (self.mana_per_lvl * self.level) + self.base_mana
        return max_mana

    def get_status(self):
        return f'{self.name} <{self.hero_type}> | HP:{self.actual_hp}/{self.max_hp:<5}| Energy:{self.actual_mana}/{self.max_mana:<} |'


class Warrior(Hero):
    def __init__(self):
        base_hp, base_mana, hp_per_lvl, mana_per_lvl= [100, 30, 4, 2]
        super().__init__(base_hp, base_mana, hp_per_lvl, mana_per_lvl)
        self.hero_type = "warrior"
                                            # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -2],
                                     'sword': [10, 5],
                                     'kick': [8, 2],
                                     'punch': [5, 1]}


class Mage(Hero):
    def __init__(self):
        base_hp, base_mana, hp_per_lvl, mana_per_lvl= [50, 100, 2, 4]
        super().__init__(base_hp, base_mana, hp_per_lvl, mana_per_lvl)
        self.hero_type = "mage"
                                            # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -5],
                                     'fireball': [20, 15],
                                     'blast': [10, 10],
                                     'dagger': [3, 3]}


class Rogue(Hero):
    def __init__(self):
        base_hp, base_mana, hp_per_lvl, mana_per_lvl = [70, 70, 3, 3]
        super().__init__(base_hp, base_mana, hp_per_lvl, mana_per_lvl)
        self.hero_type = "rogue"
                                            # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -3],
                                     'sword': [10, 6],
                                     'bow': [10, 8],
                                     'dagger': [5, 3]}
