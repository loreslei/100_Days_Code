from logo import logo_art

bidders = {}

print(logo_art[0])

looping = True

#First loop

while looping:

    name = input("What is your name? ").capitalize()
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    loop = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if(loop == "no"):
        looping = False
    else:
        print("\n" * 100)
        

#Second loop
winner_name = ""
winner_bid = 0

for bidder in bidders:
    if(bidders[bidder] > winner_bid):
        winner_name = bidder
        winner_bid = bidders[bidder]


print(f"The winner is {winner_name} with a bid of ${winner_bid}.")