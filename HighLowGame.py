import random

#Easy Level:
highest_val = 10
lowest_val = 1
print("Hi, welcome to the High Low Game!\nThis is the easy level!\nI am gonna guess your number from {} to {}."
      .format(lowest_val, highest_val))
input("To get started please press ENTER !")

guesses = 1

while True:
    guess = lowest_val + (highest_val - lowest_val)//2
    H_L = input("I think your number is {}. Tell me should I go higher, lower, or I am correct:".format(guess)).casefold()

    if H_L == "higher":
        lowest_val = guess + 1
    elif H_L == "lower":
        highest_val = guess - 1
    elif H_L == "correct":
        print("I got your number in {} guesses!".format(guesses))
        break

    else:
        print("Please write Higher, Lower or correct!")
    guesses = guesses + 1
print("")

#Medium Level:
highest_val = 100
lowest_val = 1
print("Hi, welcome to the High Low Game!\nThis is the medium level!\nI am gonna guess your number from {} to {}."
      .format(lowest_val, highest_val))
input("To get started please press ENTER !")

guesses = 1

while True:
    guess = lowest_val + (highest_val - lowest_val)//2
    H_L = input("I think your number is {}. Tell me should I go higher, lower, or I am correct:".format(guess)).casefold()

    if H_L == "higher":
        lowest_val = guess + 1
    elif H_L == "lower":
        highest_val = guess - 1
    elif H_L == "correct":
        print("I got your number in {} guesses!".format(guesses))
        break

    else:
        print("Please write Higher, Lower or correct!")
    guesses = guesses + 1
print("")

#Hard Level:
highest_val = 500
lowest_val = 1
print("Hi, welcome to the High Low Game!\nThis is the hard level!\nI am gonna guess your number from {} to {}."
      .format(lowest_val, highest_val))
input("To get started please press ENTER !")

guesses = 1

while True:
    guess = lowest_val + (highest_val - lowest_val)//2
    H_L = input("I think your number is {}. Tell me should I go higher, lower, or I am correct:".format(guess)).casefold()

    if H_L == "higher":
        lowest_val = guess + 1
    elif H_L == "lower":
        highest_val = guess - 1
    elif H_L == "correct":
        print("I got your number in {} guesses!".format(guesses))
        break

    else:
        print("Please write Higher, Lower or correct!")
    guesses = guesses + 1
print("")

#Legendary Level:
highest_val = 1000
lowest_val = 1
print("Hi, welcome to the High Low Game!\nThis is the legendary level!\nI am gonna guess your number from {} to {}."
      .format(lowest_val, highest_val))
input("To get started please press ENTER !")

guesses = 1

while True:
    guess = lowest_val + (highest_val - lowest_val)//2
    H_L = input("I think your number is {}. Tell me should I go higher, lower, or I am correct:".format(guess)).casefold()

    if H_L == "higher":
        lowest_val = guess + 1
    elif H_L == "lower":
        highest_val = guess - 1
    elif H_L == "correct":
        print("I got your number in {} guesses!".format(guesses))
        break

    else:
        print("Please write Higher, Lower or correct!")
    guesses = guesses + 1
print("")
print("THE END!")