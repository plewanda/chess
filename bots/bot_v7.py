from engine.alpha_beta import iterative_deepening_alpha_beta_search
from engine.evaluation import naive_zobrist_evaluation


def get_move(board):
    time_limit = 200
    maximizing_player = board.turn

    best_move = iterative_deepening_alpha_beta_search(board, maximizing_player,
                                                      naive_zobrist_evaluation, time_limit)

    return best_move
