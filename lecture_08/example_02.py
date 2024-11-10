class Character:
    """This class models a simple Character.

    Attributes:
       name: A string of the character's name.
       strength: A int representing the strength stat of a character.
       defense: A int representing the defense stat of a character.
   """
    def __init__(self, name, strength, defense):
        """Initializes the instance based on the Character's attributes.

        Args:
            name: A string of the character's name.
            strength: A int representing the strength stat of a character.
            defense: A int representing the defense stat of a character.
        """
        self.health = 100
        self.name = name
        self.strength = strength
        self.defense = defense

    def introduce(self):
        """Prints the character's name and stats."""
        print(f"Hi, my name is {self.name}, my stats are: Strength: {self.strength}, Defense: {self.defense}")

# Create two new characters.
woodie = Character(name='Woodie', strength=15, defense=7)
pickie = Character(name='Pickie', strength=12, defense=8)

# Update the attributes of the characters.
woodie.strength = 20
pickie.defense = 5

# Let the characters introduce themselves again with the updated data.
woodie.introduce()
pickie.introduce()