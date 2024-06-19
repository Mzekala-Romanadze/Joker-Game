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
#
perfect_match_scores = {f"{player}": [] for player in original_players_order}


def calculate_hand_scores(players_calls, player_take_scores):
    global perfect_match_scores
    player_scores = {}

    for player, call in players_calls.items():
        take = player_take_scores.get(player, 0)

        if call == take:
            score = CALL_MATCH_POINTS[str(call)]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(1)
        elif take == 0 and call > 0:
            score = CALL_MATCH_POINTS["Fine"]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(0)
        else:
            score = take * CALL_MATCH_POINTS["No match"]
            if player not in perfect_match_scores:
                perfect_match_scores[player] = []
            perfect_match_scores[player].append(0)

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
#
#
# def create_game_scores_table():
#     """
#     Combines and summarizes 4 sets scores in 4 columns and rows.
#     For 4 sets and sum of 16 hands scores in each set
#     :return: The final scores of the game
#     """
#     #
#     pass


def find_perfect_match_player(perfect_match):
    player_succeed_in_set = []

    for player, trick_win in perfect_match.items():
        if sum(trick_win) == 4:
            player_succeed_in_set.append(player)

    if not player_succeed_in_set:
        return None
    else:
        return player_succeed_in_set


def create_final_set_scores(players_and_set_scores, perfect_match):
    players_and_final_set_scores = {}
    other_player_scores = []

    for player, score in players_and_set_scores.items():
        if player not in perfect_match:
            scores_to_sum = []
            for i in score:
                if i > 0:
                    scores_to_sum.append(i)
            other_player_scores.append(sum(scores_to_sum))

    bonus_point = max(other_player_scores)
    for player, scores in players_and_set_scores.items():
        if player not in perfect_match:
            players_and_final_set_scores[player] = sum(scores)
        if player in perfect_match:
            players_and_final_set_scores[player] = sum(scores) + bonus_point

    return players_and_final_set_scores


def main():
    pass


if __name__ == '__main__':
    main()
