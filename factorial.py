def factorial(x):
    if x == 0 or x ==1:
        return 1
    else:
        return x* factorial(x-1)
print("the factorial of 8 is:", factorial(8))