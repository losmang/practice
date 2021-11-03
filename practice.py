import random

number = random.randrange(1 , 100)
count = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1

        if guess == number:
            print("You\'ve guessed the number...woo hoo! It only took {} tries".format(count))
        elif guess > number:
            print("Too High")
        else:
            print("Too Low")
    except ValueError:
        print("You didn\'t enter a number you silly butt!")
