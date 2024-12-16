print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, 15?"))
tip = 1 + (tip/100)

ppl = int(input("How many people to split the bill?"))
score = round(((bill * tip) / ppl), 2)

print(f"Each person should pay: {score}")