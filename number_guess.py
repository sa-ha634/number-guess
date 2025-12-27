import random

number=random.randint(1,100)
attempts=0

print("Welcome to number guessing game...!")
print("Guess a number between 1 to 100")

while True:
    guess= int(input("enter your guess: "))
    attempts +=1

    if guess>number:
        print("too high!")
    elif guess<number:
        print("too low!")
    else:
        print("congratulations!!!! you guessed it right")
        print("total attempts: ",attempts)
        break