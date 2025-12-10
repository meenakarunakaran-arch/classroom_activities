medical_cause = input("do you have any medical cause Y or N:")
attendence = int(input("enter student's attendance:"))
if medical_cause == Y:
    print("You are allowed")
else:
    if attendence >= 75:
        print ("Allowed")
    else:
        print("not allowed")