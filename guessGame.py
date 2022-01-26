# Basic game
import random
number = random.randint(0,10)
print(number)

counter = 1
while counter <= 3 :
    chance = int(input("Guess the number :"))
    if chance == number:
        print("You guessed right")
        break
    else:
        print("You guessed wrong")
    counter = counter + 1