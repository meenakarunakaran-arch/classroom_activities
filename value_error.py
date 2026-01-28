try: 
    value = int(input("Enter the code:"))
except ValueError as v:
    print("Incorrect", v)
try:
    num1,num2 = eval(input("enter 2 numbers seperated by commas"))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("division by zero is not allowed")
except SyntaxError:
    print("Commas are missing. enter numbers serperater by commas")
except:
    print("wrong input")
else:
    print("there is no exception")
finally:
    print("this will execute no matter what")