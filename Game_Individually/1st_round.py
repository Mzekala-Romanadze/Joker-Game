# The program of 1st round

from part_3 import player_calls


def play_first_round():
    players_order, players_and_cards, players_calls, total_round_score, chosen_trump = player_calls()
    print(f"Bidding: {players_calls}")

    players_scores = {}

    while players_and_cards.values():
        table_cards = []
        for player, cards in players_and_cards.items():
            print(cards)
            player_choice_card = input("Which card do you want to be led? ")
            while player_choice_card not in cards:
                player_choice_card = input("You do not have this card. Choose another which you want to be led: ")

            # if chosen_trump != "N":
            #     if player_choice_card.split()[-1] != chosen_trump:
            #         player_choice_card = input("You can not lead this card. Choose another which you want to be led: ")

            table_cards.append(player_choice_card)
            index = cards.index(player_choice_card)
            cards.pop(index)
        print(table_cards)


def main():
    play_first_round()


if __name__ == '__main__':
    main()
