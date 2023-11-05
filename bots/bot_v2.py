import random

from engine.evaluation import material_evaluation


def get_move(board):
    legal_moves = list(board.legal_moves)
    best_eval = float('-inf')
    best_move = random.choice(legal_moves)
    for move in legal_moves:
        new_board = board.copy()
        new_board.push(move)
        new_eval = material_evaluation(board) * [1, -1][board.turn]
        if new_eval > best_eval:
            best_eval, best_move = new_eval, move
    return best_move
