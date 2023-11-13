import random

def print_blackjack_logo():
    logo = '''
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
          |  \\/ K|                            _/ |                
          `------'                           |__/
    '''
    print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len (cards) == 2:
        return 0
    
    if 11 in cards and sum (cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum (cards)

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif user_score == 0:
        return "win"
    elif user_score > 21:
        return "lose"
    elif computer_score == user_score:
        return "draw"
    elif computer_score == 0:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif computer_score > user_score:
        return "you lose"

def play_again():
    print_blackjack_logo()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards:{user_cards}, current score:{user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True

        else:
            draw_another = input("draw another card? type y for yes and n for no \n")
            if draw_another == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"final score user{user_score}, final card user{user_cards}")
    print(f"final score computer{computer_score}, final card computer{computer_cards}")

    print(compare_score(user_score, computer_score))

while (playagain := input("Play BlackJack? (y or n): ")) == "y":
    play_again()
else:
    is_game_over = True
   

