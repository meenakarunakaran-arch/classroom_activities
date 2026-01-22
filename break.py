a = input("Enter a word:")
for i in a.lower():
    if i == "a":
        print("a is found")
        break
else:
    print("a is not found")