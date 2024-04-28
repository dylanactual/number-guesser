import random

#get user input and check if its valid 
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
while lower >= upper:
    print("Upper bound must be greater than lower bound.\n")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

#picks a number and first guess
number = random.randint(lower, upper)
print("Picking a number between " + str(lower) + " and " + str(upper) + "inclusive \n")
guess = int(input("Try and guess the number: "))

#game loop
while guess != number:
    if guess > number:
        print("Your guess was too high!")
    else: print("Your guess was too low")
    guess = int(input("Please guess again: "))

print("You got it! The number was " + str(guess))
