print("Let's play rock paper scissors!")
while True:
    move =input("pick rock paper or scissors:")
    possible_act = ["rock","paper","scissors" ]
    if move == possible_act:
        print(f"It is a tie! you chose {move} and the computer chose {possible_act}")
    elif move == "rock":
        if possible_act == "scissors":
            print(f"You won! you picked {move} and the computer chose {possible_act}")
        else:
            print(f"You lost! you picked {move} and the computer chose {possible_act}")
    elif move == "scissors":
        if possible_act == "paper":
            print(f"You won! you picked {move} and the computer chose {possible_act}")
        else:
            print(f"You lost! you picked {move} and the computer chose {possible_act}")
    elif move == "paper":
        if possible_act == "rock":
            print(f"You won! you picked {move} and the computer chose {possible_act}")
        else:
            print(f"You lost! you picked {move} and the computer chose {possible_act}")
    else:
        print("try again")
    play_again = input("play_again?")
    if play_again != "yes":
        break
    
