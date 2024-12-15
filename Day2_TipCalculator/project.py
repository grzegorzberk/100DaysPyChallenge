print("Welcome to Tip Calculator")
bill = input("What was the total bill? $")
bill = float(bill)

tip = input("How much tip would you like to give? 10, 12, 15?")
tip = int(tip)
tip = 1 + (tip/100)

ppl = input("How many people to split the bill?")
ppl = int(ppl)

score = round(((bill * tip) / ppl), 2)

print(f"Each person should pay: {score}")