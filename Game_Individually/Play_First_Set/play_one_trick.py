# The program of playing 1 trick (4 cards)

from Game_Individually.Basic_Functions.joker_choice_functions import joker_is_want, joker_is_take
from Game_Individually.Basic_Functions.joker_card_options import joker_is_first, joker_is_not_first
from Game_Individually.Basic_Functions.find_card_functions import (find_highest_suit_card, find_highest_value_card,
                                                                   find_winner_card_of_trick)
from Game_Individually.Basic_Functions.players_calls_functions import player_calls
from Game_Individually.Basic_Functions.check_card import check_card


def play_one_trick():
    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()

    players_trick_scores = {f"{player}": 0 for player in players_order}

    players_and_table_card = {}
    table_cards = []

    trump_joker_case = []
    joker_case = []

    joker_choice = None  # WANT or TAKE
    want_suit = None  # Which suit with highest ranks the player wants to get?
    take_suit = None  # Which suit with highest ranks the player wants to take the cards?

    for player, cards in players_and_cards.items():
        print(f"Player {player}'s Cards: {cards}")
        player_choice_card = None

        if not table_cards:
            player_choice_card = input("Which card do you want to be led? ")
            while player_choice_card not in cards:
                player_choice_card = input("You do not have this card. Choose another which you want to be led: ")
            if player_choice_card.split()[0] == "Joker":
                joker_is_first(player_choice_card, joker_choice, joker_case)
        else:
            if joker_choice == "WANT":
                joker_is_want(joker_choice, cards, joker_case, want_suit, chosen_trump, trump_joker_case)
            if joker_choice == "TAKE":
                joker_is_take(joker_choice, cards, joker_case, take_suit, chosen_trump)
            if joker_choice is None:
                player_cards_suits = [card.split()[-1] for card in cards]

                player_choice_card = input("Which card do you want to be led? ")
                check_card(player_choice_card, cards)
                while (table_cards[0].split()[-1] in player_cards_suits and player_choice_card.split()[-1] !=
                       table_cards[0].split()[-1]):
                    if player_choice_card.split()[0] == "Joker":
                        joker_is_not_first(player_choice_card, joker_case)
                        break
                    player_choice_card = input("You have to lead card with same suit. "
                                               "Choose another which you want to be led: ")
                    check_card(player_choice_card, cards)

                if table_cards[0].split()[-1] not in player_cards_suits:
                    while player_choice_card.split()[0] == "Joker":
                        joker_is_not_first(player_choice_card, joker_case)
                        break

                    while chosen_trump in player_cards_suits and player_choice_card.split()[0] != chosen_trump:
                        player_choice_card = input("You have to lead card with trump suit. "
                                                   "Choose another which you want to be led: ")
                        check_card(player_choice_card, cards)
                        break

                    while chosen_trump not in player_cards_suits:
                        player_choice_card = input("Which card do you want to be led? ")
                        check_card(player_choice_card, cards)

        players_and_table_card[player] = player_choice_card
        table_cards.append(player_choice_card)
        cards.pop(cards.index(player_choice_card))

    print(f"Set's Cards: {table_cards} ")

    print(players_and_cards)
    print(players_and_table_card)

    winner_card = find_winner_card_of_trick(joker_case, trump_joker_case, chosen_trump, table_cards)
    print(f"Winner Card: {winner_card} ")

    for player, card in players_and_table_card.items():
        if card == winner_card:
            players_trick_scores[player] += 1

    print(players_trick_scores)


def main():
    play_one_trick()


if __name__ == '__main__':
    main()
