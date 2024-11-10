class Character:
    def __init__(self, char_name, str_score, def_score):
        self.health = 100
        self.name = char_name
        self.strength = str_score
        self.defense = def_score

    """Lets us define when using the == operator on 
    two separate Character objects returns True."""
    def __eq__(self, other):
        return self.name == other.name

    """Lets us define the string version of this object, which includes what shows up
    when you print it."""
    def __str__(self):
        return (f"\nName: {self.name}\n"
                f"Health: {self.health}\n"
                f"Strength: {self.strength}\n"
                f"Defense: {self.defense}")

player_1 = Character("Woodie", 15, 7)
player_2 = Character("Woodie", 15, 7)
player_3 = Character("Pickie", 15, 7)

# The implementation of the __eq__ method determines when two separate
# objects of Character return True when comparing them using "=="
print(player_1 == player_2)  # Returns True because both players are called "Woodie"
print(player_1 == player_3)  # Returns False because player 3 is called "Pickie"

# The implementation of the __eq__ method determines the string value of that class,
# which also means that it is what gets printed when you print the object.
print(player_1)
print(player_3)
