#
# Superclas Character
#
class Character:
    """Superclass with common attributes for all characters.

    Attributes:
       name: A string of the character's name.
       strength: A int representing the strength stat of a character.
       defense: A int representing the defense stat of a character.
   """
    def __init__(self, name, strength, defense):
        self.health = 100
        self.name = name
        self.strength = strength
        self.defense = defense

    def perform_action(self):
        """This method says what action is being executed by this character. This is a
        generic character, so there is no specific action to it."""
        pass


#
# Subclasses of Character.
#
class OceanCharacter(Character):
    """An ocean Character that can swim. It inherits all attributes from Character.
    """
    def perform_action(self):
        """The implemented perform_action of Character which denotes that this character can swim."""
        print("I can swim!")

class GroundCharacter(Character):
    """A ground Character that can run. It inherits all attributes from Character.
    """
    def perform_action(self):
        """The implemented perform_action of Character which denotes that this character can run."""
        print("I can run!")

class SkyCharacter(Character):
    """A sky Character that can fly. It inherits all attributes from Character
    and also has an extra attribute sky_points.

    Attributes:
       sky_points: A int representing the sky stat of a character.
   """
    def __init__(self, name, strength, defense):
        """SkyCharacter also needs a sky_points attribute, so it must call the Character.__init_ method and then
        add the sky_points attribute separately so that it doesn't just override the __init__ method from Character.
        """
        Character.__init__(self, name, strength, defense)
        self.sky_points = 1000

    def perform_action(self):
        """The implemented perform_action of Character which denotes that this character can fly."""
        print("I can fly!")

# Create three separate characters.
sky = SkyCharacter(name='Sky', strength=15, defense=7)
ocean = OceanCharacter(name='Ocean', strength=15, defense=7)
ground = GroundCharacter(name='Ground', strength=15, defense=7)

# All characters have the attributes that come from the Character class and each implement the perform_action()
# method differently.
print(ocean.name)
print(ocean.strength)
print(ground.name)
print(ground.health)
ocean.perform_action()
ground.perform_action()

# The sky character has all the attributes from Character and also has an extra attribute sky_points.
print(sky.name)  # Prints "Sky"
print(sky.strength)  # Prints 15
print(sky.defense)  # Prints 7
print(sky.sky_points)  # Prints 1000
sky.perform_action()  # Prints "I can fly!"


# Method that prints all attributes of a character, regardless of the type.
def print_all_attributes(character):
    print("")
    print(character.name)  # Prints "Sky"
    print(character.strength)  # Prints 15
    print(character.defense)  # Prints 7
    if isinstance(character, SkyCharacter):
        print(character.sky_points)  # Prints 1000
    character.perform_action()  # Prints "I can fly!"

print_all_attributes(sky)
print_all_attributes(ocean)
print_all_attributes(ground)
