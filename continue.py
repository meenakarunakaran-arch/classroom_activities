var = int(input("Enter a number greater than 5"))
while var > 0:
    var -=1
    if var == 5:
        continue
    print(f"\ncurrent varaiable value:{var}")
print("\ngood bye")