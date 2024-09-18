import random

# Cashier example that keeps track of the total per item and prints out the
# total after you are done scanning everything.
total_price = 0
item_number = 1

while True:
    price = float(input(f"Please enter the price of item {item_number}: "))
    item_number += 1
    total_price += price

    have_more_items = input("Do you have more items to scan? (y/n) ")
    if have_more_items == "n":
        break

print(f"Your total price is {total_price}.")

# Create a calculator that receives a number, an operand and a second number and returns the result
# of the two numbers and the operator. Ask the user after every iteration if they want to continue,
# and break out of the loop if they are done.
def calculate_value(num_1, operator, num_2):
    if operator == "+":
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1 * num_2)
    elif operator == "/":
        if num_2 == 0:
            print("Cannot divide by 0.")
        else:
            print(num_1 / num_2)
    else:
        print("Invalid operator.")

while True:
    first_number = float(input("Enter the first number: "))
    op = input("Enter an operator (+, -, /, *): ")
    second_number = float(input("Enter the second number: "))
    calculate_value(first_number, op, second_number)

    try_again = input("Do you want to try again? (y/n) ")
    if try_again == "n":
        print("Thank you for using this calculator. See you again soon!")
        break

# Play the guessing a random number game again, but now implement a limited number of tries.
random_number = random.randint(1, 1000)
tries_left = 5
while True:
    user_guess = int(input("Guess a number! "))
    if user_guess == random_number:
        print("You guessed right! You win!")
        break
    elif user_guess < random_number:
        print("You are close but the random number is a bit larger than ", user_guess)
        tries_left -= 1
    else:
        print("You are close but the random number is a bit smaller than ", user_guess)
        tries_left -= 1

    if tries_left == 0:
        print(f"You don't have any tries left. The random number was {random_number}. You lose!")
        break

    print(f"You have {tries_left} tries left.")

# Play the rock-paper-scissors game, but now implement an ongoing score and first to five wins.
user_score = 0
cpu_score = 0
winning_score = 5
print(f"Welcome to rock paper scissors agains the CPU! First to {winning_score} wins")
while True:
    user_command = input("rock, paper or scissors? ")
    # 1 = rock, 2 = paper, 3 = scissors
    cpu_command = random.randint(1, 3)

    if user_command == "rock":
        if cpu_command == 1:
            print("Tie!")
        elif cpu_command == 2:
            print("CPU scores!")
            cpu_score += 1
        else:
            print("User scores!")
            user_score += 1
    elif user_command == 'paper':
        if cpu_command == 1:
            print("User scores!")
            user_score += 1
        elif cpu_command == 2:
            print("Tie!")
        else:
            print("CPU scores!")
            cpu_score += 1
    elif user_command == 'scissors':
        if cpu_command == 1:
            print("CPU scores!")
            cpu_score += 1
        elif cpu_command == 2:
            print("User scores!")
            user_score += 1
        else:
            print("Tie!")
    else:
        print(f'the command "{user_command}" is not valid, please try again.')

    if user_score == winning_score:
        print(f"You got to 5 first! You win!")
        break

    if cpu_score == winning_score:
        print(f"The CPU got to 5 first! You lose!")
        break

    print(f"the current score of the game is: User: {user_score}, CPU: {cpu_score}")
