from engine.alpha_beta import iterative_deepening_alpha_beta_search
from engine.evaluation import evaluate_material_tapered_position


def get_move(board):
    time_limit = 200
    maximizing_player = board.turn

    best_move = iterative_deepening_alpha_beta_search(board, maximizing_player,
                                                      evaluate_material_tapered_position, time_limit)

    return best_move
