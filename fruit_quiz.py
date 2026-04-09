# 1) Import the `random` module to randomly pick items for the quiz.

# 2) Create a class named `FruitQuiz`.

# 3) Define the constructor `__init__(self)`:
#    a) Create a dictionary `self.fruits` where:
#       - keys are fruit names
#       - values are the corresponding fruit colors

# 4) Define a method `quiz(self)` to run the quiz game.

# 5) Inside `quiz()`, start an infinite loop using `while(True)`:
#    (This keeps the quiz running until the user decides to stop.)

# 6) Randomly pick one fruit-color pair from the dictionary:
#    a) Convert `self.fruits.items()` into a list.
#    b) Use `random.choice(...)` to select one (fruit, color) pair.
#    c) Store them in `fruit` and `color`.

# 7) Ask the quiz question:
#    a) Print "What is the color of <fruit>".

# 8) Take the user's answer as input and store it in `user_answer`.

# 9) Check the answer:
#    a) Convert the user answer to lowercase using `user_answer.lower()`.
#    b) If it matches `color`, print "Correct answer".
#    c) Otherwise, print "Wrong answer".

# 10) Ask the user if they want to play again:
#     a) Take input as an integer `option`.
#     b) If `option` is 1 (true), stop the loop using `break`.
#        (If option is 0, the loop continues and another question is asked.)

# 11) Print a welcome message: "welcome to fruit quiz ".

# 12) Create an object `fq` of the class `FruitQuiz`.

# 13) Call `fq.quiz()` to start the fruit quiz game.

import random
class fruit_quiz:
    def __init__(self):
        self.fruits = { "apple":"red","banana":"yellow", "orange":"orange" }
    def quiz(self):
        while(True):
            fruit,colour = random.choice(list(self.fruits.items()))
            print("what is the colour of <fruit>")
            user_ans = input("enter the answer:")
            user_ans.lower()
            if user_ans == colour:
                print("correct answer")
            else:
                print("wrong answer")
            print("do you want to play again?")
            option = int(input("0 to play again and 1 to stop"))
            if option == 1:
                break
            for i in fruit,colour:
                    print(">",i)
            print("welcome to fruit quiz")
            