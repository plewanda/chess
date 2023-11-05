import random


def get_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)
