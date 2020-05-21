import random
import sys

import hero
import bestiary


class GameMechanism:
    @classmethod
    def dice_roll(cls, size: int):
        """Return ..."""
        possibilities = list(range(1, size+1))
        return random.choice(possibilities)

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


    # @classmethod
    # def hero_check(self, hero):
    #     for person in self.participants:
    #         if hero.__repr__() == person.__repr__():
    #             return person.get_status()

class Combat:
    def __init__(self, *args):
        self.round = 1
        self.moves_per_round = len(args)
        self.participants = random.sample(list(args), self.moves_per_round)

    def death_check(self):
        """Function will remove all combat participants with actual_hp < 0"""
        for entity in self.participants:
            if entity.actual_hp <= 0:
                print("entity", entity, "removed")
                self.participants.remove(entity)

    # ATTACK RELATED METHODS
    @classmethod
    def check_attack_success(cls, attacker, defender):
        return True

    def hero_check(self, current_hero):
        for person in self.participants:
            if current_hero == person:
                return person.get_status()

    def ui_attack(self, attacker: bestiary.Bestiary):
        targets = [player for player in self.participants if isinstance(player, (hero.Warrior, hero.Mage, hero.Rogue))]

        if len(targets) >= 2:
            target = targets[1]
        else:
            target = random.choice(targets)

        attack_name, min_att, max_att = attacker.get_attack_info(attacker.attack_info)
        attack_num = random.randint(min_att, max_att)
        for participant in self.participants:
            if participant == target:
                target.actual_hp -= attack_num
                print(f'{attacker.name} did {attack_num} by {attack_name} to {target.name}. And he got {target.actual_hp} HP remaining')

            if participant.actual_hp <= 0:
                print(f'Attack of {attacker.name} had killed {target.name}.') # !!!! Vyřešit - píše se stále dokola při mrtvém enemy


    def hero_attack(self, current_hero):
        possible_targets = [creature for creature in self.participants if issubclass(type(creature), bestiary.Bestiary)]
        if len(possible_targets) == 1:
            i = 1
            print(f'({0}){possible_targets[0].name} - {possible_targets[0].actual_hp}')
            print(f"({i})Nothing - (Regenerate energy)")
        else:
            for i, mob in enumerate(possible_targets):
                print(f'({i}){mob.name} - {mob.actual_hp}')
            print(f"({i+1})Nothing - (Regenerate energy)")

        while True:
            choice = input('Who you want to attack?: ')
            try:
                choice = int(choice)
                if choice == (i + 1) or (len(possible_targets) == 1 and choice == 1):
                    regen = current_hero.attack_possibilities["nothing"][1] # Calculate how much energy regenerate from "nothing" action in hero.SubClass attack_possibilities
                    current_hero.actual_energy -= regen
                    print(f"Player {current_hero.name} is waiting and regenerate ")
                    return None
                elif choice in range(i + 1):
                    target = possible_targets[choice]
                break
            except IndexError:
                print("Target number out of range.")
                continue
            except ValueError:
                print("Wrong typo, m8!")
                continue

        attack_name, min_att, max_att, energy_usage = current_hero.get_attack_info()
        actual_dmg = random.randint(min_att, max_att)

        if len(possible_targets) == 1:
            possible_targets[0].actual_hp -= actual_dmg
        else:
            for poos, participant in enumerate(self.participants):
                if target == participant:
                    self.participants[poos].actual_hp -= actual_dmg

        for poos, participant in enumerate(self.participants):
            if participant == current_hero:
                self.participants[poos].actual_energy -= energy_usage
        print(f'Attack by {attack_name} from {current_hero.name} did {actual_dmg} to {target.name}.')


    def one_round(self, round_num):
        """Function defining events of one round of combat"""
        print(f'Round {round_num} has begin.')
        for participant in self.participants:
            if issubclass(type(participant), hero.Hero):
                print(self.hero_check(participant))
                self.hero_attack(participant)
            else:
                self.ui_attack(participant)
        print(f'END OF ROUND {self.round}')
        self.round += 1

    def round_check(self):
        """"Return tuple of count (hero, enemy) remaining in combat"""
        heroes_count = 0
        enemy_count = 0
        for participant in self.participants:
            if issubclass(type(participant), hero.Hero):
                heroes_count += 1
            elif issubclass(type(participant), bestiary.Bestiary):
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


if __name__ == '__main__':
    user_1 = GameMechanism.hero_creation()

    attacker1 = bestiary.Human('Thug', 1)
    attacker2 = bestiary.Human('Thug', 1)
    # attacker3 = bestiary.Human('Thug', 1)
    cmb1 = Combat(user_1, attacker1, attacker2)
    combat = True
    while combat:
        while len(cmb1.participants) > 1:
            cmb1.one_round(cmb1.round)
            cmb1.death_check()
            combat = cmb1.combat_end(cmb1.round_check())

