import random

class Weapon:
    def __init__(self, name, damage, durability=100):
        self.name = name
        self.damage = damage
        self.durability = durability

    def still_works(self):
        return self.durability > 0

    def attack(self):
        if self.still_works():
            self.durability -= 50
            print(f"This {self.name}'s durability is now {self.durability}.")
            return self.damage
        else:
            print(f"This {self.name} is broken.")
            return 0


class Character:
    def __init__(self,
                 name,
                 strength,
                 defense,
                 weapon,
                 accuracy=50,
                 critical_hit_accuracy=0):
        self.health = 100
        self.name = name
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.accuracy = accuracy
        self.critical_hit_accuracy = critical_hit_accuracy

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def attack(self, other):
        #time.sleep(1)
        if not self.is_alive():
            print(f"{self} is dead, so he cant attack.")
        elif not other.is_alive():
            print(f"{other} is dead, so he cant be attacked.")
        else:
            did_attack_work = random.randint(1, 100)
            if did_attack_work <= self.accuracy:
                print(f"\n{self} is going to attack {other}")
                multiplier = 1
                if did_attack_work <= self.critical_hit_accuracy:
                    multiplier += 1
                    print(f"{self} got a critical hit!")
                other.health -= (self.strength + self.weapon.attack()) * multiplier
                print(f"{other}'s new health is: {other.health}")
            else:
                print(f"\n{self}'s attack is not very effective (lol)!")

class GameBattle:
    def __init__(self, char_1, char_2):
        self.winners = []
        self.char_1 = char_1
        self.char_2 = char_2

    def battle(self):
        self.char_1.health = 100
        self.char_2.health = 100
        while self.char_1.is_alive() and self.char_2.is_alive():
            char_1_attacks_first = random.randint(0, 1) == 0
            if char_1_attacks_first:
                self.char_1.attack(self.char_2)
                self.char_2.attack(self.char_1)
            else:
                self.char_2.attack(self.char_1)
                self.char_1.attack(self.char_2)
        print()
        if self.char_1.is_alive():
            self.winners.append(self.char_1.name)
            return self.char_1.name
        self.winners.append(self.char_2.name)
        return self.char_2.name

    def run_battles(self, num_battles):
        for _ in range(num_battles):
            self.battle()
        winner_scores = { self.char_1.name: 0, self.char_2.name: 0 }
        for winner in self.winners:
            winner_scores[winner] += 1
        print(winner_scores)
        #print(f"{self.char_1}: {winner_scores[self.char_1.name]}")

pistol = Weapon(name="pistol", damage=30)
lapiz = Weapon(name="lapiz", damage=0.7)
bienve = Character(name="Bienve",
                   strength=10,
                   defense=10,
                   weapon=pistol,
                   accuracy=50,
                   critical_hit_accuracy=5)
jc = Character(name="Jean",
               strength=10,
               defense=10,
               weapon=pistol,
               accuracy=50,
               critical_hit_accuracy=5)

game_battle = GameBattle(char_1=bienve, char_2=jc)
game_battle.run_battles(5000)