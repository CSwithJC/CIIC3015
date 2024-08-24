# Basic examples
print("Basic examples:")
a = True
b = False

a_and_b = a and b
a_or_b = a or b
not_a = not a

print("a and b is", a_and_b)
print("a ir b is", a_or_b)
print("not a is", not_a)

# Combining logical operators (Examples from slides)
print("\nCombining logical operators (Examples from slides):")
print(True and not False)  # True
print((False or True) and False)  # False
print(not (True or False) or True)  # True

# Animals on a farm!
print("\nAnimals on a farm!:")
dog = False
chicken = True
sheep = True

print(not dog or not chicken and sheep)
print(chicken and dog or not sheep)
print(not chicken or not sheep or dog)
print(dog and not sheep or chicken )

