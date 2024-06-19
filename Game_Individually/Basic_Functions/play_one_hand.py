"""
The program of Joker Game. This file includes the following functions:
            1. play_one_hand() => playing 1 hand (9 tricks, 36 cards)

"""

from Game_Individually.Basic_Functions.players_calls_functions import player_calls
from Game_Individually.Basic_Functions.play_one_trick import play_one_trick
from Game_Individually.Basic_Functions.get_players_scores_functions import calculate_hand_scores


def play_one_hand(set_scores, hand_number, temp_players_order):
    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = (
        player_calls(hand_number, temp_players_order))
    print(f"Bidding:\n\n{players_calls}\n")

    player_take_scores = {f"{player}": 0 for player in players_order}
    trick_winner_player = None
    for _ in range(2):
        trick_winner_player, player_take_scores = play_one_trick(players_order, players_and_cards,
                                                                 chosen_trump, trick_winner_player,
                                                                 player_take_scores)
    players_and_hand_scores = calculate_hand_scores(players_calls, player_take_scores)
    print(f"Players' Scores: {players_and_hand_scores}")
    set_scores.append(players_and_hand_scores)

    return players_order, set_scores


def main():
    pass


if __name__ == '__main__':
    main()
