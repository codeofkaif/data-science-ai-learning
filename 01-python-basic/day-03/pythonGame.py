# Simple guessing Game in python
import random
print("Welcome to guessing number")
print("you have to choose a number between 1 to 100. can you guess it?")
n=0
guess=random.randint(1,100)
while True:

    val = (input("Enter your guess (or 'q' to quit): "))
    if val == "q":
        break
    val = int(val)
    if val>guess:
        n+=1
        print("Too high! Try again")
    elif val<guess:
        n+=1
        print("Too low! Try again")
    elif val==guess:
        n+=1
        print(f"Congrats! You guessed the number {n}!")
print("Game over")

