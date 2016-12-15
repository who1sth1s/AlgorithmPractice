import random


class Dealer:

    def __init__(self):

        self.cards = [
            'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
            'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
            'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13',
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13'
        ]

    def distribute_card_to_player(self):

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

                winner_list.append((player_index, player_score_inventory.get(player_index)))

        return winner_list

    def check_winner_number(self, winner_list):

        return len(winner_list) == 1


class Player:

    def __init__(self, player_cards, player_number):
        self.CARD_SCORE_INDEX = 1
        self.player_cards = player_cards
        self.player_number = player_number
        self.player_scores = 0
        pass

    def __str__(self):
        return 'Player' + str(self.player_number) + ' : ' + str(self.player_cards) + ' ' + str(self.player_scores)

    def calculate_single_player_score(self):
        player_scores = list()

        for player_selected_card in self.player_cards:
            player_scores.append(int(player_selected_card[self.CARD_SCORE_INDEX:]))

        self.player_scores = sum(player_scores)


def card_game():

    while True:

        dealer = Dealer()

        player1 = Player(dealer.distribute_card_to_player(), 1)
        player2 = Player(dealer.distribute_card_to_player(), 2)
        player3 = Player(dealer.distribute_card_to_player(), 3)
        player4 = Player(dealer.distribute_card_to_player(), 4)

        player1.calculate_single_player_score()
        player2.calculate_single_player_score()
        player3.calculate_single_player_score()
        player4.calculate_single_player_score()

        player_score_inventory = assemble_players_score(player1, player2, player3, player4)

        winner_list = dealer.make_winner_list(player_score_inventory)

        if dealer.check_winner_number(winner_list):

            print(player1)
            print(player2)
            print(player3)
            print(player4)
            print('Winner is Player' + str(winner_list[0][0]))

            return 'Winner is Player' + str(winner_list[0][0])


def assemble_players_score(*players):

    player_score_inventory = dict()

    for player in players:

        player_score_inventory[player.player_number] = player.player_scores

    return player_score_inventory
