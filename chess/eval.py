import random

import chess


def evaluate_board(game):
    legal_moves = list(game.legal_moves)

    random_move = random.choice(legal_moves)

    return random_move
