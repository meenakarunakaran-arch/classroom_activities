actual_cost = float(input("please enter the actual product price:"))
sale_amount = float(input("please enter the sales amount:"))
if (sale_amount>actual_cost):
    amount = sale_amount - actual_cost
    #print ("total profit = {0}".format(amount))
    print (f"total profit = {amount}")
else:
    print("no profit")
    