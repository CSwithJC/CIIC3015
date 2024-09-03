# Weather report based on temperature
temperature = int(input("What is the temperature outside?"))

if temperature < 50:
    print("It's freezing! Wear a coat and scarf.")
elif temperature < 70:
    print("It's chilly. A sweater would be nice.")
else:
    print("It's hot! Wear shorts and a t-shirt.")


# Final letter grade based on numerical grade
grade = int(input("What was your numerical grade this semester"))

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
else:
    print("You need to study more.")
