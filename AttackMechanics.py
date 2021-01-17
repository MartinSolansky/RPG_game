import os
import random
from time import sleep

import helpers
import hero
import bestiary


class Combat:
    def __init__(self, *args):
        self.round = 1
        self.moves_per_round = len(args)
        self.participants = random.sample(list(args), self.moves_per_round)

    def death_check(self):
        """Function will remove all combat participants with actual_hp < 0"""
        for entity in self.participants:
            if entity.actual_hp <= 0:
                print("entity", entity.name, "removed")
                self.participants.remove(entity)

    # ATTACK RELATED METHODS
    @classmethod
    def check_attack_success(cls, attacker, defender):
        return True

    def hero_check(self, current_hero):
        for person in self.participants:
            if current_hero == person:
                return person.get_status()

    def ui_attack(self, attacker: bestiary.Beast):
        targets = [player for player in self.participants if isinstance(player, (hero.Warrior, hero.Mage, hero.Rogue))]
        target = random.choice(targets)

        # TODO: FUNCTION - same as hero_attack
        attack_name, min_att, max_att, _ = attacker.get_attack_info()
        attack_num = random.randint(min_att, max_att)
        target.actual_hp -= attack_num
        self.print_attack_info(attacker, attack_num, attack_name, target)

        if target.actual_hp <= 0:
            print(f'Attack of {attacker.name} had killed {target.name}.')
            self.participants.remove(target)

    def hero_attack(self, current_hero):
        possible_targets = [creature for creature in self.participants if issubclass(type(creature), bestiary.Beast)]

        # TODO: Maybe use counting from 1
        for i, mob in enumerate(possible_targets):
            print(f'({i}){mob.name} - {mob.actual_hp}')
        print(f"({len(possible_targets)})Nothing - (Regenerate mana)")

        while True:
            try:
                choice = int(input('Who you want to attack?: '))
                if choice == len(possible_targets):
                    current_hero.actual_mana -= current_hero.battle_regen
                    print(f"Player {current_hero.name} is waiting and regenerate mana.")
                    return None
                target = possible_targets[choice]
                break
            except IndexError:
                print("Target number out of range.")
                continue
            except ValueError:
                print("Wrong typo, m8!")
                continue

        attack_name, min_att, max_att, mana_usage = current_hero.get_attack_info()
        actual_dmg = random.randint(min_att, max_att)

        target.actual_hp -= actual_dmg
        current_hero.mana_change(-mana_usage)
        self.print_attack_info(current_hero, actual_dmg, attack_name, target)

        if target.actual_hp <= 0:
            self.participants.remove(target)

    @staticmethod
    def print_attack_info(attacker, dmg, attack, target):
        helpers.slow_print(f'{attacker.name} did {dmg} dmg by {attack} to {target.name}. ' + target.hp_remaining())

    def one_round(self, round_num):
        """Function defining events of one round of combat"""
        os.system('cls' if os.name == 'nt' else 'clear')
        helpers.blick_print(f'Round {round_num} has begin.')
        for participant in self.participants:
            if issubclass(type(participant), hero.Hero):
                print(self.hero_check(participant))
                self.hero_attack(participant)
            else:
                self.ui_attack(participant)
        helpers.blick_print(f'END OF ROUND {self.round}')
        sleep(5)
        self.round += 1

    def round_check(self):
        """"Return tuple of count (hero, enemy) remaining in combat"""
        heroes_count = 0
        enemy_count = 0
        for participant in self.participants:
            if issubclass(type(participant),
                          hero.Hero):
                heroes_count += 1
            elif issubclass(type(participant), bestiary.Beast):
                enemy_count += 1
        return heroes_count, enemy_count

    def combat_end(self, round_check: tuple):
        """Check if there are remaining enemy or hero in combat"""
        hero_count, enemy_count = round_check
        if hero_count >= 1 and enemy_count == 0:
            print("Combat ends. All enemies are slain.")
            return False
        elif hero_count == 0:
            print("All heroes are dead!")
            return False
        return True
