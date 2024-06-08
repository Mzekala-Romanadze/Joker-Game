# The program of 1st round

from part_1 import RANK_VALUES
from part_3 import player_calls
SUITS = ["Heart", "Diamond", "Spade", "Club"]


def play_first_round():
    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()
    print(f"Bidding: {players_calls}")

    players_scores = {f"{player}": [] for player in players_order}

    while players_and_cards:
        table_cards = []
        for player, cards in players_and_cards.items():
            print(f"Player {player}'s Cards: {cards}")
            player_choice_card = None
            joker_choice = None
            middle_player_joker_choice = []
            want_suit = None
            take_suit = None

            if not table_cards:
                player_choice_card = input("Which card do you want to be led? ")
                while player_choice_card not in cards:
                    player_choice_card = input("You do not have this card. Choose another which you want to be led: ")
                if player_choice_card.split()[0] == "Joker":
                    player_action = input("Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ")
                    while player_action != "WANT" and player_action != "TAKE":
                        player_action = input("Wrong input. Choose: Want Highest ('WANT') or Don't Want ('TAKE')? ")
                    joker_choice = player_action

                    if player_action == "WANT":
                        want_suit = input("Which suit of cards do you want with highest ranks? ")
                        while want_suit not in SUITS:
                            want_suit = input("Enter valid suit. Which suit of cards do you want with highest ranks? ")

                    if player_action == "TAKE":
                        take_suit = input("Which suit of card do you want to take? ")
                        while take_suit not in SUITS:
                            take_suit = input("Enter valid suit. Which suit of card do you want to take? ")
            else:
                if joker_choice == "WANT":
                    player_cards_suits = [card.split()[-1] for card in cards]

                    player_choice_card = input("Which card do you want to be led? ")
                    while player_choice_card not in cards:
                        player_choice_card = input(
                            "You do not have this card. Choose another which you want to be led: ")

                    while player_choice_card.split()[0] == "Joker":
                        if want_suit in player_cards_suits:
                            middle_player_joker_choice.append(player_choice_card)
                        else:
                            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
                            while player_joker_choice != "YES" and player_joker_choice != "NO":
                                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                                            "cards by Joker or not? (YES/NO) ").upper()
                            if player_joker_choice == "YES":
                                middle_player_joker_choice.append(player_choice_card)
                            break

                    while want_suit in player_cards_suits and player_choice_card.split()[-1] != want_suit:
                        player_choice_card = input("You have to lead card with wanted suit. "
                                                   "Which card do you want to be led? ")
                        while player_choice_card not in cards:
                            player_choice_card = input(
                                "You do not have this card. Choose another which you want to be led: ")
                        highest_card = find_highest_suit_card(cards, want_suit)
                        while player_choice_card != highest_card:
                            player_choice_card = input("You have to lead highest card with wanted suit. ")
                        break

                    while (want_suit != chosen_trump and want_suit not in player_cards_suits and chosen_trump
                            in player_cards_suits and player_choice_card.split()[-1] != chosen_trump):
                        player_choice_card = input("You have to lead card of chosen suit when you do not "
                                                   "have wanted suit. Which card do you want to be led? ")
                        while player_choice_card not in cards:
                            player_choice_card = input(
                                "You do not have this card. Choose another which you want to be led: ")
                        break

                if joker_choice == "TAKE":
                    player_cards_suits = [card.split()[-1] for card in cards]

                    player_choice_card = input("Which card do you want to be led? ")
                    while player_choice_card not in cards:
                        player_choice_card = input(
                            "You do not have this card. Choose another which you want to be led: ")

                    while player_choice_card.split()[0] == "Joker":
                        if take_suit in player_cards_suits:
                            middle_player_joker_choice.append(player_choice_card)
                        else:
                            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
                            while player_joker_choice != "YES" and player_joker_choice != "NO":
                                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                                            "cards by Joker or not? (YES/NO) ").upper()
                            if player_joker_choice == "YES":
                                middle_player_joker_choice.append(player_choice_card)
                            break

                    while take_suit in player_cards_suits and player_choice_card.split()[-1] != want_suit:
                        player_choice_card = input("You have to lead take suit card. "
                                                   "Which card do you want to be led? ")
                        while player_choice_card not in cards:
                            player_choice_card = input(
                                "You do not have this card. Choose another which you want to be led: ")
                        highest_card = find_highest_suit_card(cards, take_suit)
                        while player_choice_card != highest_card:
                            player_choice_card = input("You have to lead highest card with take suit. ")
                        break

                    while (take_suit != chosen_trump and take_suit not in player_cards_suits and chosen_trump
                            in player_cards_suits and player_choice_card.split()[-1] != chosen_trump):
                        player_choice_card = input("You have to lead card of chosen suit when you do not "
                                                   "have take suit. Which card do you want to be led? ")
                        while player_choice_card not in cards:
                            player_choice_card = input(
                                "You do not have this card. Choose another which you want to be led: ")
                        break

                if joker_choice is None:
                    player_cards_suits = [card.split()[-1] for card in cards]

                    player_choice_card = input("Which card do you want to be led? ")
                    while player_choice_card not in cards:
                        player_choice_card = input("You do not have this card. "
                                                   "Choose another which you want to be led: ")

                    while (table_cards[0].split()[-1] in player_cards_suits and player_choice_card.split()[-1] !=
                            table_cards[0].split()[-1]):
                        if player_choice_card.split()[0] == "Joker":
                            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
                            while player_joker_choice != "YES" and player_joker_choice != "NO":
                                player_joker_choice = input("Enter YES or NO. "
                                                            "Do you want to take cards by Joker or not? (YES/NO) ").upper()
                            if player_joker_choice == "YES":
                                middle_player_joker_choice.append(player_choice_card)

                            break

                        player_choice_card = input("You have to lead card with same suit. "
                                                   "Choose another which you want to be led: ")

                    if table_cards[0].split()[-1] not in player_cards_suits:
                        if player_choice_card.split()[0] == "Joker":
                            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
                            while player_joker_choice != "YES" and player_joker_choice != "NO":
                                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                                            "cards by Joker or not? (YES/NO) ").upper()
                            if player_joker_choice == "YES":
                                middle_player_joker_choice.append(player_choice_card)
                            break

                        while chosen_trump in player_cards_suits and player_choice_card.split()[0] != chosen_trump:
                            player_choice_card = input("You have to lead card with trump suit. "
                                                       "Choose another which you want to be led: ")
                            while player_choice_card not in cards:
                                player_choice_card = input(
                                    "You do not have this card. Choose another which you want to be led: ")

                        if chosen_trump not in player_cards_suits:
                            player_choice_card = input("Which card do you want to be led? ")
                            while player_choice_card not in cards:
                                player_choice_card = input(
                                    "You do not have this card. Choose another which you want to be led: ")

            table_cards.append(player_choice_card)
            index = cards.index(player_choice_card)
            cards.pop(index)

        print(f"Set's Cards: {table_cards} ")
        winner_card = find_highest_card_in_set(table_cards, chosen_trump)
        print(winner_card)


def find_highest_suit_card(cards, wanted_suit):
    player_suit_cards = [card for card in cards if wanted_suit in card]

    highest_card = None
    highest_rank_value = -1

    for card in player_suit_cards:
        rank = card.split(' of ')[0]
        rank_value = RANK_VALUES[rank]
        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    # print("The highest card is:", highest_card)
    return highest_card


def find_highest_card_in_set(table_cards, chosen_trump):
    highest_card = None
    highest_rank_value = -1

    for card in table_cards:
        rank, suit = card.split(' of ')

        if rank == "Joker":  # I should add function to deal with case when in the set are 2 jokers
            highest_card = card
            break

        if suit == chosen_trump:
            rank_value = RANK_VALUES[rank] + 100
        else:
            rank_value = RANK_VALUES[rank]

        if rank_value > highest_rank_value:
            highest_rank_value = rank_value
            highest_card = card

    # print("The highest card is:", highest_card)
    return highest_card


def main():
    play_first_round()


if __name__ == '__main__':
    main()
