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