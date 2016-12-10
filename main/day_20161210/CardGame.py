import random


CARD_SCORE_INDEX = 1


def random_card_game(player_number):
    cards = [
        'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13'
    ]

    while True:

        make_players = [assign_card_to_player(cards) for _ in range(player_number)]
        winner = choose_winner(make_players)

        if check_winner_count(winner):

            return 'Winner is ' + winner[0]


def check_winner_count(winner):

    return len(winner) == 1


def assign_card_to_player(cards):

    player_cards = random.sample(cards, 7)
    remove_selected_cards(cards, player_cards)

    return player_cards


def remove_selected_cards(not_selected_cards, selected_cards):

    for selected_card in selected_cards:
        not_selected_cards.remove(selected_card)

    return not_selected_cards


def choose_winner(players):

    (player_indexes, players_scores) = calculate_players_score(players)
    mapping_player_score_information = dict()

    for index in range(4):
        mapping_player_score_information[player_indexes[index]] = players_scores[index]

    finally_winner = make_winner_list(players_scores, mapping_player_score_information)

    return finally_winner


def make_winner_list(players_scores, mapping_player_score_information):

    finally_winner = list()
    max_score = max(players_scores)

    for key in mapping_player_score_information.keys():

        if mapping_player_score_information.get(key) == max_score:
            finally_winner.append('Player' + str(key + 1))

    return finally_winner


def calculate_players_score(players):

    player_indexes = list()
    players_scores = list()

    for (player_index, player) in enumerate(players):
        player_indexes.append(player_index)
        player_scores = calculate_single_player_score(player)

        players_scores.append(sum(player_scores))

    return player_indexes, players_scores


def calculate_single_player_score(player):
    player_scores = list()

    for player_selected_card in player:
        player_scores.append(int(player_selected_card[CARD_SCORE_INDEX:]))

    return player_scores
