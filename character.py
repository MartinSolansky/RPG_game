
class Character:
    def __init__(self, level: int, hp, mana):
        self.name = ""
        self.level = level
        self.max_hp = hp
        self.max_mana = mana
        self.actual_hp = hp
        self.actual_mana = mana
        self.armor = 'nothing'
        self.armor_reduction = self.get_armor_reduction()
        self.attack_possibilities = {}

    def hp_change(self, hp: int):
        if hp < 0:
            hp = hp + (hp * self.armor_reduction)

        self.actual_hp += hp
        if self.actual_hp > self.max_hp:
            self.actual_hp = self.max_hp

    def mana_change(self, mana: int):
        self.actual_mana += mana
        if self.actual_mana > self.max_mana:
            self.actual_mana = self.max_mana

    def check_death(self):
        """Return True if character is dead. Otherwise return False"""
        if self.actual_hp <= 0:
            print(f'{self.name} is DEAD!')
            return True
        return False

    def get_armor_reduction(self):
        """Method take armor. Return dmg reduction for hero armor."""
        if isinstance(self.armor, str):
            armor_possibilities = {'nothing': 0, 'cloth': 0, 'leather': 0.1, 'chain mail': 0.2, 'plate': 0.4}
            return armor_possibilities.get(self.armor)
        else:
            raise TypeError(f'This armor <{self.armor}> is not allowed.')

    def check_energy(self, energy_usage):
        """Return bool value of energy usage per ability."""
        if self.actual_mana >= energy_usage:
            return True
        return False

    def attack_info(self):
        """Show possible attacks"""
        attacks = ''
        for att, value in self.attack_possibilities.items():
            attacks += f'{att}--<{value[0]} dmg/{value[1]} energy>\n'
        print('attack--<dmg done/energy cost>')
        print(attacks.strip('\n'))

    def chose_attack_type(self):
        """Give player choice which action to perform. Return list[action, action value, energy_cost]"""
        attacks = ''
        for att, value in self.attack_possibilities.items():
            attacks += f'{att}--<{value[0]} dmg/{value[1]} energy>\n'
        print('attack--<dmg done/energy cost>')
        print(attacks.strip('\n'))
        while True:
            chosen_attack = input('Which attack you want to perform?\n')
            try:
                max_attack, mana_usage = self.attack_possibilities[chosen_attack]
                if mana_usage > self.actual_mana:
                    print("Sorry you dont have enough mana.")
                    continue
                return [chosen_attack, max_attack, mana_usage]
            except KeyError:
                print('You may misspelled attack. Please type is once more.')
                continue

    def is_hero(self):
        """Check if self is Hero class or not"""
        for classname in self.__class__.__bases__:
            if classname.__name__ == 'Hero':
                return True
        return False

    def get_attack_info(self) -> list:
        """Take partial attack info from chose_attack_type method.
        Return list[att_name, min_att, max_att, mana_usage]"""

        if self.is_hero():
            attack_name, max_attack, mana_usage = self.chose_attack_type()
        else:
            attack_name, max_attack = self.attack_possibilities
            mana_usage = 0
        return [attack_name, max_attack // 2, max_attack, mana_usage]

    def hp_remaining(self, capture=False):
        """Print HP remaining"""
        if capture:
            print(f"{self.name} have {self.actual_hp} HP remaining.")
        return f"And he got {self.actual_hp} HP remaining."
