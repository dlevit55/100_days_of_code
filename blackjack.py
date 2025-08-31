#!/usr/bin/env python3

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
pc_chosen_cards = []
user_chosen_cards = []

def is_blackjack():
    return (user_chosen_cards[0] == 11 and user_chosen_cards[1] == 10 ) or (user_chosen_cards[0] == 10 and user_chosen_cards[1]  == 11)

another_card = ""
keep_playing = True
while keep_playing:
    another_card_user = True
    for _ in range(2):
        user_chosen_cards.append(random.choice(cards))
        pc_chosen_cards.append(random.choice(cards))

    print(f"your chosen cards are: {user_chosen_cards} and the sum is: {sum(user_chosen_cards)}")
    print(f"Computer's first hand is: {pc_chosen_cards[0]}")
    black_jack = is_blackjack()
    if black_jack:
        print("you have blackjack! you win!")
        another_card_user = False

    while another_card_user:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_chosen_cards.append(random.choice(cards))
            print(f"your chosen cards are: {user_chosen_cards} and the sum is: {sum(user_chosen_cards)}")
            print(f"Computer's first hand is: {pc_chosen_cards[0]}")
            if sum(user_chosen_cards) > 21:
                print("you went over! you lose!!")
                another_card_user = False
        else:
            another_card_user = False


    if another_card == "n":
        while sum(pc_chosen_cards) < 16:
            pc_chosen_cards.append(random.choice(cards))
        if sum(pc_chosen_cards) > 21:
            print("Computer went over. you win!")

        elif sum(pc_chosen_cards) > sum(user_chosen_cards):
            print("you lose!")

        elif sum(pc_chosen_cards) < sum(user_chosen_cards):
            print("you win!")

        elif sum(pc_chosen_cards) == sum(user_chosen_cards):
            print("Draw")


    print(f"your chosen cards are: {user_chosen_cards} and the sum is: {sum(user_chosen_cards)}")
    print(f"Computer's cards are: {pc_chosen_cards} and the sum is: {sum(pc_chosen_cards)}")

    print('\n' * 2)
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == "n":
        print("Thank you for playing :) ")
        keep_playing = False
    if play_again == "y":
        pc_chosen_cards.clear()
        user_chosen_cards.clear()

