from art import logo
import random
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def draw():
    return random.choice(cards)

def get_score(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ("J", "Q", "K"):
            total += 10
        elif card == "A":
            aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def display_state(user_hand, dealer_hand):
    print(f"Dealer's first card: {dealer_hand[0]}")
    print(f"Your cards: {user_hand}, current score {get_score(user_hand)}")


def play(user_hand, dealer_hand):
    user_hand.append(draw())
    dealer_hand.append(draw())
    display_state(user_hand, dealer_hand)

def find_winner(user_hand, dealer_hand):
    user_score = get_score(user_hand)
    dealer_score = get_score(dealer_hand)
    print(f"user score: {user_score}, dealer score: {dealer_score}")
    if user_score > 21:
        print("You lose!!")
    elif dealer_score > 21:
        print("You win!!")
    elif user_score > dealer_score:
        print("You win!!")
    elif user_score < dealer_score:
        print("You lose!!")
    else:
        print("Draw!!")

def start_game(should_continue):
    user_hand = [draw()]
    dealer_hand = [draw()]
    while should_continue == 'y':
        play(user_hand, dealer_hand)
        if get_score(user_hand) > 21:
            print("You lose!!")
            should_continue = "n"
            break
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == "n":
            find_winner(user_hand, dealer_hand)
if __name__ == "__main__":
    should_start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print(logo)
    start_game(should_start_game)