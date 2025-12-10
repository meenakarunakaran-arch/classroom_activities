print("Select your ride:")
print("1. car")
print("2. bike")
choice = int(input("enter your choice:"))
if choice == 1:
    print("what type? \\1. sedan \\2. XUV")
    choice2 = int(input("what type?:"))
    if choice2 == 1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")
elif choice == 2:
    print("what type? \n1. scooter \n2. scooty")
    choice3 = int(input("what type?:"))
    if choice3 ==1:
        print("you have selected scooter")
    else:
        print("you have selected scooty")
else:
    print("wrong choice")