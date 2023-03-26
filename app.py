import random
from art import logo


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(player_card):
    if sum(player_card) == 21 and len(player_card) == 2:
        return 0

    if 11 in player_card and sum(player_card) > 21:
        player_card.remove(11)
        player_card.append(1)

    return sum(player_card)


def compare(user_score, computer_score):
    """Decides final score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins with a blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over. Computer wins!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"


def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards} current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            draw_card = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if draw_card == "y":
                user_cards.append(deal_cards())
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do You want to play a game of blackjack Type 'y' or 'n': ") == "y":
    play_game()
