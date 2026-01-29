import random
print("i am going to pick a number from 0 to 20. Try and guess it")
while True:
    guess = input("Guess the number:")
    num = str(random.randint(0,20))
    if guess == num:
        print("you guessed it!")
        break
    else:
        print("Try again")