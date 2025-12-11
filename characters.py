string = input("enter the word:")
char = input("enter the character you want to count:")
i = 0
count = 0
while (i<len(string)):
    if string[i] == char:
        count = count + 1
    i = i + 1
print("the number of characters is:", count)