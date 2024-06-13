# The program of playing first set (4 hands (4 * 9 tricks)

from play_one_hand import play_one_hand
from Game_Individually.Basic_Functions.players_calls_functions import player_calls

players_and_first_set_scores = {}


def play_four_hands():
    global players_and_first_set_scores

    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()

    players_and_first_set_scores = {f"{player}": 0 for player in players_order}
    print(f"Bidding:\n\n{players_calls}\n")

    for _ in range(4):
        play_one_hand(players_order, players_and_cards, chosen_trump)
        players_order = get_card_dealer(players_order)
        print(players_order)


def get_card_dealer(players_order):
    players_order = players_order[1:] + [players_order[0]]
    return players_order


def main():
    play_four_hands()
    # print(players_and_first_set_scores)
    # pass


if __name__ == '__main__':
    main()
