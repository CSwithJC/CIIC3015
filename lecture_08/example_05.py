# TODO: Implement Inheritance to characters.

class Character:
    def __init__(self, name):
        self.name = name

    def perform_action(self):
        print('i have no action to perform')

class SkyCharacter(Character):
    def perform_action(self):
        print("I can fly!")

class OceanCharacter(Character):
    def perform_action(self):
        print("I can swim!")

class GroundCharacter(Character):
    def perform_action(self):
        print("I can run!")

sky = SkyCharacter('Sky')
ocean = OceanCharacter('Ocean')
ground = GroundCharacter('Ground')

print(sky.name)
print(ocean.name)
print(ground.name)
sky.perform_action()
ocean.perform_action()
ground.perform_action()