import random

num = random.randint(1,1000000)

print("I am thinking of a number between 1 and 100000. Can you guess what it is?")

guess = int(input())

while guess != num:
    if guess > num:
        print("lower")
    else:
        print("higher")
    guess = int(input())

print("You guessed it! The number is", num)
