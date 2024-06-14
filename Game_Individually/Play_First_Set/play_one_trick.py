# The program of playing 1 trick (4 cards)

from Game_Individually.Basic_Functions.joker_choice_functions import joker_is_want, joker_is_take
from Game_Individually.Basic_Functions.joker_card_options import joker_is_first, joker_is_not_first
from Game_Individually.Basic_Functions.find_card_functions import find_winner_card_of_trick
from Game_Individually.Basic_Functions.check_card import check_card

from Game_Individually.Basic_Functions.players_calls_functions import player_calls
from Game_Individually.Basic_Functions.rearrange_players_order import rearrange_players_order_for_next_trick

players_and_one_hand_scores = {}


def play_one_trick(players_order, players_and_cards, chosen_trump, trick_winner_player):
    global players_and_one_hand_scores

    players_and_cards, players_order = rearrange_players_order_for_next_trick(trick_winner_player, players_order, players_and_cards)

    players_and_table_card = {}
    table_cards = []

    trump_joker_case = []
    joker_case = []

    joker_choice = None  # WANT or TAKE
    want_suit = None  # Which suit with highest ranks the player wants to get?
    take_suit = None  # Which suit with highest ranks the player wants to take the cards?
    player_choice_card = None

    for player, cards in players_and_cards.items():
        print(joker_choice)
        print(f"Player {player}'s Cards: {cards}")
        player_cards_suits = [card.split()[-1] for card in cards]
        # joker_choice = None  # WANT or TAKE
        # want_suit = None  # Which suit with highest ranks the player wants to get?
        # take_suit = None  # Which suit with highest ranks the player wants to take the cards?

        if not table_cards:
            player_choice_card = input("Which card do you want to be led? ")
            while player_choice_card not in cards:
                player_choice_card = input("You do not have this card. Choose another which you want to be led: ")
            if player_choice_card.split()[0] == "Joker":
                joker_choice, want_suit, take_suit = joker_is_first(player_choice_card, joker_choice, joker_case, want_suit, take_suit)

        else:
            if joker_choice == "WANT":
                player_choice_card = input("Which card do you want to be led? ")
                check_card(player_choice_card, cards)
                joker_is_want(player_choice_card, cards, player_cards_suits, joker_case, want_suit, chosen_trump, trump_joker_case)

            elif joker_choice == "TAKE":
                player_choice_card = input("Which card do you want to be led? ")
                check_card(player_choice_card, cards)
                joker_is_take(player_choice_card, cards, player_cards_suits, joker_case, take_suit, chosen_trump)

            else:
                player_choice_card = input("Which card do you want to be led? ")
                check_card(player_choice_card, cards)

                while table_cards[0].split()[-1] in player_cards_suits:
                    if player_choice_card.split()[0] == "Joker":
                        joker_is_not_first(player_choice_card, joker_case)
                        break
                    if player_choice_card.split()[-1] != table_cards[0].split()[-1]:
                        player_choice_card = input("You have to lead card with same suit. "
                                                   "Choose another which you want to be led: ")
                        check_card(player_choice_card, cards)
                    else:
                        break

                while table_cards[0].split()[-1] not in player_cards_suits:
                    if player_choice_card.split()[0] == "Joker":
                        joker_is_not_first(player_choice_card, joker_case)
                        break

                    if chosen_trump in player_cards_suits and player_choice_card.split()[-1] != chosen_trump:
                        player_choice_card = input("You have to lead card with trump suit. "
                                                   "Choose another which you want to be led: ")
                        check_card(player_choice_card, cards)
                    if chosen_trump in player_cards_suits and player_choice_card.split()[-1] == chosen_trump:
                        break
                    if chosen_trump not in player_cards_suits:
                        break
        players_and_table_card[player] = player_choice_card
        table_cards.append(player_choice_card)
        cards.pop(cards.index(player_choice_card))

    print(f"Set's Cards: {table_cards} ")
    print(players_and_table_card)

    winner_card = find_winner_card_of_trick(joker_case, trump_joker_case, chosen_trump, table_cards)
    print(f"Winner Card: {winner_card} ")

    for player, card in players_and_table_card.items():
        if card == winner_card:
            players_and_one_hand_scores[player] += 1
            trick_winner_player = player

    print(trick_winner_player)

    print(players_and_one_hand_scores)
    return trick_winner_player


def main():
    global players_and_one_hand_scores
    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()

    players_and_one_hand_scores = {f"{player}": 0 for player in players_order}
    print(f"Bidding:\n\n{players_calls}\n")

    trick_winner_player = None
    for i in range(9):
        trick_winner_player = play_one_trick(players_order, players_and_cards, chosen_trump, trick_winner_player)

    # pass


if __name__ == '__main__':
    main()
