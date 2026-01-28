valid = False
while not False:
    try:
        value = int(input("Enter a number"))
        while value%2 == 0:
            print("bye")
        valid = True
    except ValueError:
        print("invalid")
        
