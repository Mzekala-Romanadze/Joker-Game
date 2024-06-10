# The program of playing 1 hand (9 tricks, 36 cards)

from play_one_trick import play_one_trick
from Game_Individually.Basic_Functions.players_calls_functions import player_calls

players_and_one_hand_scores = {}


def play_one_hand():
    global players_and_one_hand_scores

    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()
    print(f"Bidding:\n\n{players_calls}\n")

    for i in range(9):
        play_one_trick()


def main():
    # play_one_hand()
    # print(players_and_one_hand_scores)
    pass


if __name__ == '__main__':
    main()
