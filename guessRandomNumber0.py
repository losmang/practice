import random

number = random.randrange(1,10)
count = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    count += 1
    if guess == number:
        print("You\'ve guessed it!! I took {} tries to get the answer!".format(count))
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
