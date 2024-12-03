class Character:
    def __init__(self, name, strength, health=100):
        self.name = name
        try:
            with open(f"{self.name}.txt", "r") as file:
                self.health = int(file.readline().strip())
                self.strength = int(file.readline().strip())
        except FileNotFoundError:
            self.health = health
            self.strength = strength
    def __str__(self):
        return f"name: {self.name}, health: {self.health}"
    def attack(self, other):
        other.health -= self.strength
        other.save()
    def save(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(f"{self.health}\n")
            file.write(f"{self.strength}\n")

jc = Character(name="jean", strength=10)
bienve = Character(name="bienve", strength=10)
# jc.attack(bienve)
print(jc)
print(bienve)


# try:
#     # with open("test.txt", "r") as file:
#     #     print(file.read())
#     print(1 / 0)
# except FileNotFoundError:
#     print("file does not exist")
# except ZeroDivisionError:
#     print("cant divide by zero")
# except Exception as e:
#     print(e)
