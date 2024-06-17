# The program of Joker Game

# This file includes the following functions:
#                    1. calculate_hand_scores()
#                    2. create_set_scores_table()
#                    3. create_game_scores_table()
#                    4. ()
#                    5. ()
#

from Game_Individually.Basic_Functions.get_players_and_cards import CALL_MATCH_POINTS
from Game_Individually.Basic_Functions.get_players_and_cards import get_players_order

original_players_order = get_players_order(hand_number=0)

perfect_match = {f"{player}": [] for player in original_players_order}


def calculate_hand_scores(players_calls, player_take_scores):
    global perfect_match
    player_scores = {}

    for player, call in players_calls.items():
        take = player_take_scores.get(player, 0)

        if call == take:
            score = CALL_MATCH_POINTS[str(call)]
            if player not in perfect_match:
                perfect_match[player] = []
            perfect_match[player].append(1)
        elif take == 0 and call > 0:
            score = CALL_MATCH_POINTS["Fine"]
            if player not in perfect_match:
                perfect_match[player] = []
            perfect_match[player].append(0)
        else:
            score = take * CALL_MATCH_POINTS["No match"]
            if player not in perfect_match:
                perfect_match[player] = []
            perfect_match[player].append(0)

        player_scores[player] = score

    return player_scores


def create_set_scores_table(set_scores):
    """
    Creates scores table for 1 set, 4 hands.
    :return: players and set scores
    """

    players_and_set_scores = {}

    for game_set in set_scores:
        for player, score in game_set.items():
            if player not in players_and_set_scores:
                players_and_set_scores[player] = []
            players_and_set_scores[player].append(score)

    return players_and_set_scores


def create_game_scores_table():
    """
    Combines and summarizes 4 sets scores in 4 columns and rows.
    For 4 sets and sum of 16 hands scores in each set
    :return: The final scores of the game
    """
    #
    pass


def find_perfect_match_player():
    # გადავცეთ 4-ვე ხელის ნათქვამი და აღებული კარტების ლექსიკონები - perfect_match dict and at the end of set
    # find which player has all 1s in the list and if any of them calculate scores:
    #                             1. თუ ერთზე მეტია ყველა პრემიაზე გასულის ლისთი დააბრუნოს.
    #                             2. თუ გამოვლინდა ერთი მაინც, ახალი ფუნქცია შევქმნა სადაც დაითვლის
    #                             სხვა მოთამაშეების ქულებს სეტში და ვისიც ყველაზე მაღალი იქნება იმას დააბრუნებს.
    #                             3. დაბრუნებულ მაღალ ქულას ეს ფუნქცია დაუმატებს პრემიაზე გასულ(ებ)ს და დააბრუნებს
    #                             ერთ დიქშენარის ყველა მოთამაშის ქულების ჯამით სეტში.
    # თუ გამოავლენს პრემიაზე გასულ მოთამაშეს (თუ იქნება ასეთი), მის ქულებს დააჯამებს - ამისთვის გადავცეთ სეტის ქულები.
    pass


def main():
    pass


if __name__ == '__main__':
    main()
