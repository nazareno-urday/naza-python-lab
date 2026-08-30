import art
print(art.logo)
print("Welcome to the secret Auction Program.")
auction = {}
in_game = True
max_bid = 0
winner = ""

while in_game:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    auction[name] = price
    for i in auction:
        if auction[i] > max_bid:
            max_bid = auction[i]
            winner = name

    decision = input("Are there any other bidders?, Type 'yes' or 'no'.").lower()
    if decision == "yes":
        print("\n" * 20)
    else:
        print(f"The winner is {winner} with a bid of {max_bid}.")
        in_game = False