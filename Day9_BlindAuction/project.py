from art import logo as logo
print (logo)
game_over = False
bids = {}

while game_over == False:
    name = input("Type your name: ")
    price = int(input("Type your bid: $"))
    bids = {name: price}

    print("Are there any other bidders? Type 'yes' or 'no'.")
    user_decision = input()
    if user_decision == "yes":
        print("\n" * 20)
    else:
        game_over = True

winner = max(bids, key=lambda x: bids[x])
print(f"The winner is {winner}, with price: ${bids[winner]}")



