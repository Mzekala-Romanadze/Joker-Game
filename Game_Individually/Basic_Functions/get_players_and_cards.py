# The program of Joker Game

# This file includes the following functions:
#                    1. Constant variables
#                    2. choose_game_type()
#                    3. get_player_names()
#                    4. get_players_order()
#                    5. create_and_shuffle_cards()
#


import random
from Game_Individually.Basic_Functions.rearrange_players_order import rearrange_players_order_for_next_hand

NUMBER_OF_PLAYERS = 4
DECK_OF_CARDS = {
    "Spade": ["Ace of Spade", "King of Spade", "Queen of Spade", "Jack of Spade", "10 of Spade",
              "9 of Spade", "8 of Spade", "7 of Spade", "Joker of Spades"],
    "Club": ["Ace of Club", "King of Club", "Queen of Club", "Jack of Club", "10 of Club",
             "9 of Club", "8 of Club", "7 of Club", "Joker of Clubs"],
    "Heart": ["Ace of Heart", "King of Heart", "Queen of Heart", "Jack of Heart", "10 of Heart",
              "9 of Heart", "8 of Heart", "7 of Heart", "6 of Heart"],
    "Diamond": ["Ace of Diamond", "King of Diamond", "Queen of Diamond", "Jack of Diamond", "10 of Diamond",
                "9 of Diamond", "8 of Diamond", "7 of Diamond", "6 of Diamond"]
}
SUITS = ["Heart", "Diamond", "Spade", "Club"]
RANKS = ["Joker", "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6"]
RANK_VALUES = {"Joker": 20, "Ace": 14, "King": 13, "Queen": 12, "Jack": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6}

WORDS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
MATCH = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

CALL_MATCH_POINTS = {"0": 50,
                     "1": 100,
                     "2": 150,
                     "3": 200,
                     "4": 250,
                     "5": 300,
                     "6": 350,
                     "7": 400,
                     "8": 450,
                     "9": 900,
                     "No match": 10,
                     "Fine": -500}

TRUMP = ['H', 'D', 'S', 'C', 'N']
TOTAL_ROUND_CALL = 9


def choose_game_type():
    user_choice = input("Do you want to play individually (I) or in a pair (P)? ").upper()
    while user_choice != "I" and user_choice != "P":
        user_choice = input("Enter valid Symbol: if you want to play individually - I or in a pair - P? ").upper()
    if user_choice == "I":
        return "Individually"
    else:
        return "In Pairs"


def get_player_names() -> list:
    players = ["Mzekala", "Luka", "Victoria", "Sebastian"]
    # for i in range(1, NUMBER_OF_PLAYERS + 1):
    #     player_name = input(f"Enter name of Player {i}: ").capitalize()
    #     while player_name in players:
    #         player_name = input(f"This name is already taken. Enter another name for Player {i}: ").capitalize()
    #         if player_name in players:
    #             continue
    #     while not player_name:
    #         player_name = input(f"Please enter name for Player {i}: ").capitalize()
    #     players.append(player_name)
    return players


def get_players_order(hand_number):
    players = get_player_names()
    first_card_dealer = random.choice(players)
    temp_list_1 = []
    temp_list_2 = []
    for player in players:
        if player == first_card_dealer:
            index = players.index(player)
            temp_list_1.append(players[index + 1:])
            temp_list_2.append(players[:index + 1])

    combine_lists = temp_list_1 + temp_list_2

    if hand_number == 0:
        players_order = [player for sublist in combine_lists for player in sublist]
        return players_order


def create_and_shuffle_cards():
    deck_of_cards = []
    for suit in SUITS:
        deck_of_cards += DECK_OF_CARDS[suit]
    random.shuffle(deck_of_cards)

    return deck_of_cards


def main():
    pass
    # game_type = choose_game_type()
    # players_order = get_players_order()
    # deck_of_cards = create_and_shuffle_cards()
    #
    # print(game_type)
    # print(players_order)
    # print(deck_of_cards)


if __name__ == '__main__':
    main()
