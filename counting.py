a = int(input("Enter the amount you want to withdraw:"))
note1 = a//100
note2 = (a%100)//50
note3 = ((a%100)%50)//10
print ("notes of 100 are:", note1, "\n notes of 50 are:", note2, "\n notes of 10 are:", note3)