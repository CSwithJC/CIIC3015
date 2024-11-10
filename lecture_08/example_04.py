class Character:
    def __init__(self, name, strength, defense):
        self.health = 100
        self.name = name
        self.strength = strength
        self.defense = defense

    def attack(self, character_2):
        """Attacks a different character based on self character's strength. Also
        updates the health of the different character after the attack.

        Args:
            character_2: A Character that being attacked by self.
        """
        damage = self.strength - character_2.defense
        if damage > 0:
          character_2.health = character_2.health - damage

# Create the characters.
woodie = Character(name="Woodie", strength=15, defense=7)
pickie = Character(name="Pickie", strength=12, defense=8)
print(pickie.health) # Prints 100

# Make the characters attack each other and show their updated healths.
woodie.attack(pickie)
pickie.attack(woodie)
print(pickie.health) # Prints 93
print(woodie.health) # Prints 95