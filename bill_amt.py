def total_calc(bill_amt, tip_perc):
    print("The bill amount is:", bill_amt)
    total = bill_amt *(1+ 0.01*tip_perc)
    print("Total amount to be paid is:", round(total,2))
    
total_calc(50, 10)