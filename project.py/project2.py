print("welcome to the tip calculator!")
bill = float(input("what was the total bill?$"))
tip = float(input("what percentage tip would you like to give? 10 12 15"))
people =int(input("how many people to split the bill?"))
bill_with_tip = tip/100*bill+bill
print(bill_with_tip)