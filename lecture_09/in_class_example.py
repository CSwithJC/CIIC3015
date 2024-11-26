class Character:
    def __init__(self, name):
        try:
            game_state_file = open("character.txt", "r")
            saved_name = game_state_file.readline().rstrip("\n")
            saved_health = game_state_file.readline().rstrip("\n")
            self.name = saved_name
            self.health = int(saved_health)
            game_state_file.close()
        except FileNotFoundError:
            self.health = 100
            self.name = name

    def save(self):
        file = open("character.txt", "w")
        file.write(self.name + "\n")
        file.write(str(self.health))
        file.close()

bienve = Character("Bienve")
print(bienve.name)
print(bienve.health)