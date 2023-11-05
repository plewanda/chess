import time


def iterative_deepening_alpha_beta_search(board, maximizing_player, eval_function, time_limit):
    alpha = float('-inf')
    beta = float('inf')
    best_move = None
    start_time = time.time()
    depth = 1

    while (time.time() - start_time) * 1000 < time_limit:
        max_val, move = alpha_beta_search(board, depth, alpha, beta, maximizing_player, eval_function)
        if max_val is not None:
            best_move = move
        depth += 1

    return best_move


def alpha_beta_search(board, depth, alpha, beta, maximizing_player, eval_function):
    if depth == 0 or board.is_game_over():
        return eval_function(board), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in board.legal_moves:
            new_board = board.copy()
            new_board.push(move)
            evaluation, _ = alpha_beta_search(new_board, depth - 1, alpha, beta, False, eval_function)
            if evaluation >= max_eval:
                max_eval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in board.legal_moves:
            new_board = board.copy()
            new_board.push(move)
            evaluation, _ = alpha_beta_search(new_board, depth - 1, alpha, beta, True, eval_function)
            if evaluation <= min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval, best_move
