units = int(input("please enter the number of units used:"))
if units <=50:
    charge = units * 3
    surcharge = 10
else:
    if units <=100:
        charge = units * 4
        surcharge = 20
    elif units <=200:
        charge = units * 5
        surcharge = 30
    elif units >=200:
        charge = units * 6
        surcharge = 40
total = charge + surcharge
print("your total is:", total)
