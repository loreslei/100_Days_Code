import random
from art import logo

def deal_card():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Returns the total score of a hand. """
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score


def compare(u_score, compt_score):
    """ Determines the winner of the game. """
    if u_score == compt_score:
        return "It's a draw!"
    elif u_score == 0:
        return "You win!"
    elif compt_score == 0:
        return "Computer wins!"
    elif u_score > 21:
        return "Computer wins!"
    elif compt_score > 21:
        return "You win!"
    elif u_score > compt_score:
        return "You win!"
    else:
        return "Computer wins!"

def blackjack():
    
    print(logo[0])
    
    your_hand = []
    computer_hand = []

    computer_score = -1
    user_score = -1

    is_game_over = False


    for _ in range(2):
        your_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(your_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your cards: {your_hand} = {user_score}")
        print(f"Computer first card: {computer_hand[0]}")


        if user_score == 0 and computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
            if user_should_deal == "y":
                your_hand.append(deal_card())
            else:
                is_game_over = True
                    
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
            
    print(f"Your final hand: {your_hand} = {user_score}")
    print(f"Computer final hand: {computer_hand} = {computer_score}")      
    print(compare(compt_score=computer_score, u_score=user_score))


while input("Wanna play blackjack? Type 'y' or 'n': \n").lower() ==  "y":
    print("\n" * 20)
    blackjack()
    
    