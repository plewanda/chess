from engine.alpha_beta import alpha_beta_search
from engine.evaluation import evaluate_material_position


def get_move(board):
    alpha = float('-inf')
    beta = float('inf')
    depth = 2
    maximizing_player = board.turn

    best_score, best_move = alpha_beta_search(board, depth, alpha, beta, maximizing_player, evaluate_material_position)

    return best_move
