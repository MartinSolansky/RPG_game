import random
import sys

import bestiary
import hero

class Game:
    def __init__(self):
        self.heroes = []

    def game_end(self):
        print('You have failed in your adventure!')
        _ = input('Press any key to shut down program.')
        sys.exit()


    def hero_creation(self):
        print('1-Warrior: master of weapons')
        print('2-Rogue: silent killer who hide in shadows')
        print('3-Mage: Master of arcane (f)arts')
        choice = int(input('Choose your spec(1-3): '))
        choices = ['nothing', hero.Warrior, hero.Rogue, hero.Mage]
        return choices[choice]()

    # def register_player(self, player: hero.Hero):
    #     self.heroes.append(player)

# class GameMechanic:
#     def dice_roll(self, choice):
#         dices = [4, 6, 8, 10, 12, 100]
#         if choice in dices:
#             return random.randint(1, choice)
#         raise ValueError('This dice is not in dice options!')

class Combat:
    def __init__(self, *args):
        self.round = 1
        self.moves_per_round = len(args)
        self.participants = random.sample(list(args), self.moves_per_round)


    # ATTACK RELATED METHODS
    def check_attack_succes(self, attacker, defender) -> bool:
        return True

    def hero_check(self, hero):
        for person in self.participants:
            if hero.__repr__() == person.__repr__():
                return person.get_status()


    def ui_attack(self, attacker: bestiary.Bestiary):
        targets = [player for player in self.participants if isinstance(player, (hero.Warrior, hero.Mage, hero.Rogue))]
        for c in self.participants:
            if isinstance(c, hero.Hero):
                targets.append(c)
        if len(targets) == 2:
            target = targets[1]
        else:
            target = random.choice[targets]
        target_id = target.__repr__()
        attack_name, min_att, max_att = attacker.get_attack_info(attacker.attack_info)
        attack_num = random.randint(min_att, max_att)
        for poos, participant in enumerate(self.participants):
            if participant.__repr__ == target_id:
                print(target_id)
                print(participant.__repr__)
                self.participants[poos].actual_hp -= attack_num
                print(f'{attacker.name} did {attack_num} by {attack_name} to {target.name}. And he got {self.participants[poos].actual_hp} HP remaining')

            if participant.actual_hp <= 0:
                print(f'Attack of {attacker.name} had killed {target.name}.')


    def hero_attack(self, hero):
        possible_targets = [creature for creature in self.participants if isinstance(creature, bestiary.Bestiary)]
        for i, mob in enumerate(possible_targets):
            print(f'({i}){mob.name} - {mob.actual_hp}')
        choice = int(input('Who you want to attack?: '))
        target = possible_targets[choice]
        target_id = target.__repr__()

        attack_name, min_att, max_att, energy_usage = hero.get_attack_info()
        actual_dmg = random.randint(min_att, max_att)

        for poos, participant in enumerate(self.participants):
            if target_id == participant.__repr__():
                self.participants[poos].actual_hp -= actual_dmg

        for poos, participant in enumerate(self.participants):
            if participant.__repr__() == hero.__repr__():
                self.participants[poos].actual_energy -= energy_usage
        print(f'Attack by {attack_name} from {hero.name} did {actual_dmg} to {target.name}.')


    def one_round(self, round_num):
        print(f'Round {round_num} has begin.')
        for participant in self.participants:
            if isinstance(participant, (hero.Warrior, hero.Mage, hero.Rogue)):
                print(self.hero_check(participant))
                self.hero_attack(participant)
            else:
                self.ui_attack(participant)
        print(f'END OF ROUND {self.round}')
        self.round += 1


if __name__ == '__main__':
    game = Game()
    user_1 = game.hero_creation()

    attacker1 = bestiary.Human('Thug', 1)
    attacker2 = bestiary.Human('Thug', 1)
    attacker3 = bestiary.Human('Thug', 1)
    cmb1 = Combat(user_1, attacker1, attacker2, attacker3)
    while len(cmb1.participants) > 1:
        cmb1.one_round(cmb1.round)







