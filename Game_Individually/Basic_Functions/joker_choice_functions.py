# The program of Joker Game

# This file includes the following functions:
#                    1. joker_is_want()
#                    2. joker_is_take()
#


def joker_is_want(joker_choice, cards, joker_case, want_suit, chosen_trump, trump_joker_case):
    if joker_choice == "WANT":
        player_cards_suits = [card.split()[-1] for card in cards]

        player_choice_card = input("Which card do you want to be led? ")
        while player_choice_card not in cards:
            player_choice_card = input("You do not have this card. Choose another which "
                                       "you want to be led: ")

        while player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        highest_card = find_highest_suit_card(cards, want_suit)
        while (want_suit in player_cards_suits and player_choice_card.split()[-1] !=
               want_suit and player_choice_card != highest_card):
            while player_choice_card.split()[-1] != want_suit:
                player_choice_card = input("You have to lead card with wanted suit. "
                                           "Which card do you want to be led? ")
                while player_choice_card not in cards:
                    player_choice_card = input(
                        "You do not have this card. Choose another which you want to be led: ")

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
            trump_joker_case.append(player_choice_card)
            break


def joker_is_take(joker_choice, cards, joker_case, take_suit, chosen_trump):
    if joker_choice == "TAKE":
        player_cards_suits = [card.split()[-1] for card in cards]

        player_choice_card = input("Which card do you want to be led? ")
        while player_choice_card not in cards:
            player_choice_card = input("You do not have this card. Choose another "
                                       "which you want to be led: ")

        while player_choice_card.split()[0] == "Joker":
            player_joker_choice = input("Do you want to take cards by Joker or not? (YES/NO) ").upper()
            while player_joker_choice != "YES" and player_joker_choice != "NO":
                player_joker_choice = input("Enter YES or NO. Do you want to take "
                                            "cards by Joker or not? (YES/NO) ").upper()
            if player_joker_choice == "YES":
                joker_case.append(player_choice_card)
            break

        while take_suit in player_cards_suits and player_choice_card.split()[-1] != take_suit:
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


def main():
    pass


if __name__ == '__main__':
    main()
