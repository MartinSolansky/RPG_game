import random


class Bestiary:
    def __init__(self, name, level: int, hp_coefficient: int, attack_info: list, armor='nothing'):
        self.name = name
        self.level = level
        self.max_hp = hp_coefficient*level
        self.actual_hp = self.max_hp
        self.dmg_reduction = self.get_armor_reduction(armor)
        self.attack_info = self.get_attack_info(attack_info)

    def get_attack_info(self, attack_info):
        '''Take attack name, max_attack value. Return list [name, base_att, max_att]'''
        attack_name, max_attack, *_ = attack_info
        return [attack_name, max_attack//2, max_attack]

    @staticmethod
    def get_armor_reduction(armor) -> float:
        if isinstance(armor, str):
            armor_possibilities = {'nothing': 0, 'leather': 0.1, 'chain mail': 0.2, 'plate': 0.4}
            return armor_possibilities.get(armor)
        elif isinstance(armor, str):
            pass

        else:
            raise TypeError(f'This armor <{armor}> is not allowed.')


class Human(Bestiary):
    def __init__(self, name, level):
        HP_COEFICIENT = 15
        weapons = {'dager': 4, 'sword': 6}
        armor = random.choice(['nothing', 'leather', 'chain mail', 'plate'])
        attack_info = random.choice(list(weapons.items()))
        super().__init__(name, level, HP_COEFICIENT, attack_info, armor=armor)



class Beast(Bestiary):
    pass

class Undead(Bestiary):
    pass

if __name__ == '__main__':
    attacker1 = Human('Thug', 1)
    attacker2 = Human('Thug', 1)

    print(attacker1.name)
    print(attacker1.dmg_reduction)
    print(attacker1.attack_info)