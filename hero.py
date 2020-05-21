import random


class Hero:
    def __init__(self, name, level: int, hp_coefficient: float, armor, attack_possibilities: dict,
                 energy_coefficient: (float, str), hero='hero'):
        self.name = name
        self.hero_type = hero
        self.level = level
        self.base_hp = 100
        self.base_energy = 50
        self.hp_coefficient = hp_coefficient
        self.energy_coefficient = energy_coefficient
        self._max_hp = self.get_max_hp()
        self._max_energy = self.get_max_energy()
        self.armor = armor
        self.attack_possibilities = attack_possibilities
        # self.attack_range = self.get_attack_range(self.chose_attack_type(attack_possibilities))
        self.dmg_reduction = self.get_armor_reduction(armor)

        self.actual_hp = self._max_hp
        self.actual_energy = self._max_energy


    def get_max_hp(self):
        '''Determine highest HP possible according to lvl and spec'''
        return int(float(self.base_hp * self.level) * self.hp_coefficient)

    def get_max_energy(self):
        '''Determine highest energy possible according to lvl and spec'''
        return self.energy_coefficient*self.level*self.base_energy

    def hp_depletion(self, value: int):
        '''Deplete actual_hp by given value'''
        self.actual_hp -= value

    def energy_depletion(self, value: int):
        '''Deplete actual_energy by given value'''
        self.actual_energy -= value

    def chose_attack_type(self, attack_possibilities: dict) -> list:
        '''Give player choice which action to perform. Return list[action, action value, energy_cost]'''
        attacks = ''
        for att, value in attack_possibilities.items():
            attacks += f'{att}--<{value[0]} dmg/{value[1]} energy>\n'
        print(attacks.strip('\n'))
        while True:
            chosen_attack = input('Which attack you want to perform? ')
            print(chosen_attack)
            try:
                result = attack_possibilities[chosen_attack]
                return [chosen_attack, result[0], result[1]]
            except KeyError:
                print('You may misspelled attack. Please type is once more.')
                continue

    def get_attack_info(self):
        '''Take partial attack info from chose_attack_type method. Return list[min_att, max_att]'''
        attack_name, max_attack, energy_usage = self.chose_attack_type(self.attack_possibilities)
        return [attack_name, max_attack//2, max_attack, energy_usage]

    @staticmethod
    def get_armor_reduction(armor) -> float:
        '''Method take armor. Return dmg reduction for hero armor.'''
        if isinstance(armor, str):
            armor_possibilities = {'nothing': 0, 'cloth': 0, 'leather': 0.1, 'chain mail': 0.2, 'plate': 0.4}
            return armor_possibilities.get(armor)
        else:
            raise TypeError(f'This armor <{armor}> is not allowed.')

    def check_death(self):
        '''Return True if hero is dead. Otherwise return False'''
        if self.actual_hp <= 0:
            print(f'{self.name} is DEAD!')
            return True
        return False

    def check_energy(self, energy_usage):
        '''Return bool value of energy usage per ability.'''
        if self.actual_energy >= energy_usage:
            return True
        return False

    def get_status(self):
        return f'{self.name} <{self.hero_type}> | HP:{self._max_hp}/{self.actual_hp:<5}| Energy:{self._max_energy}/{self.actual_energy:<} |'

class Warrior(Hero):
    def __init__(self):
        name = input('Chose your name: ')
        hp_coefficent = 2
        armor = 'plate'
        energy_coefficient = 1
                                    # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -2],
                                     'sword': [10, 5],
                                     'kick': [8, 2],
                                     'punch': [5, 1]}

        super().__init__(name, 1, hp_coefficent, armor, self.attack_possibilities, energy_coefficient, hero='Warrior')


class Mage(Hero):
    def __init__(self):
        name = input('Chose your name: ')
        hp_coefficent = 1
        armor = 'cloth'
        energy_coefficient = 2.0
                                        # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -5],
                                     'fireball': [20, 15],
                                     'blast': [10, 10],
                                     'dagger': [3, 3]}
        super().__init__(name, 1, hp_coefficent, armor, self.attack_possibilities, energy_coefficient, hero='Mage')


class Rogue(Hero):
    def __init__(self):
        name = input('Chose your name: ')
        hp_coefficent = 1.2
        armor = 'cloth'
        energy_coefficient = 1.35
                                        # [dmg, energy_cost]
        self.attack_possibilities = {'nothing': [0, -3],
                                     'sword': [10, 6],
                                     'bow': [10, 8],
                                     'dagger': [5, 3]}

        super().__init__(name, 1, hp_coefficent, armor, self.attack_possibilities, energy_coefficient, hero='Rogue')


if '__main__' == __name__:
    user = Warrior()
    print(user)

    attack_name, min_attack, max_attack, energy_usage = user.get_attack_info()

    while user.check_energy(energy_usage):
        actual_attack = random.randint(min_attack, max_attack)
        user.energy_depletion(energy_usage)
        print(f'{user.name} did {actual_attack} damage by {attack_name} for {energy_usage} hp and have {user.actual_energy} left')

