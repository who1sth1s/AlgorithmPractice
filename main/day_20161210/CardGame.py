import random


class Dealer:

    def __init__(self):

        self.cards = [
            'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
            'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
            'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13'
        ]

    def assign_card_to_player(self):

        player_cards = random.sample(self.cards, 7)
        self.remove_selected_cards(player_cards)

        return player_cards

    def remove_selected_cards(self, selected_cards):

        for selected_card in selected_cards:
            self.cards.remove(selected_card)

    def make_winner_list(self, player_score_inventory):

        maximum_score = max(player_score_inventory.values())
        winner_list = list()

        for player_index in player_score_inventory.keys():

            if player_score_inventory.get(player_index) == maximum_score:

                winner_list.append((player_index + 1, player_score_inventory.get(player_index)))

        return winner_list

    def check_winner_number(self, winner_list):

        return len(winner_list) == 1


class Player:

    def __init__(self):
        self.CARD_SCORE_INDEX = 1
        pass

    def calculate_single_player_score(self, player):
        player_scores = list()

        for player_selected_card in player:
            player_scores.append(int(player_selected_card[self.CARD_SCORE_INDEX:]))

        return sum(player_scores)


def kangwonland():

    while True:

        dealer = Dealer()

        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()

        player1s_card = dealer.assign_card_to_player()
        player2s_card = dealer.assign_card_to_player()
        player3s_card = dealer.assign_card_to_player()
        player4s_card = dealer.assign_card_to_player()

        player1_score = player1.calculate_single_player_score(player1s_card)
        player2_score = player2.calculate_single_player_score(player2s_card)
        player3_score = player3.calculate_single_player_score(player3s_card)
        player4_score = player4.calculate_single_player_score(player4s_card)

        player_score_inventory = assemble_players_score(player1_score, player2_score, player3_score, player4_score)

        winner_list = dealer.make_winner_list(player_score_inventory)

        if dealer.check_winner_number(winner_list):

            return 'Winner is Player' + str(winner_list[0][0])


def assemble_players_score(*players_score):

    player_score_inventory = dict()

    for player_index, player_score in enumerate(players_score):

        player_score_inventory[player_index] = player_score

    return player_score_inventory
