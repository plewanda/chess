import chess
from tqdm import tqdm

from bots import bot_v1, bot_v4, bot_v5, bot_v6, bot_v7
from consts import ZOBRIST_DICT
from engine.move_generator import get_next_move


def simulate_match():
    player_1 = bot_v7
    player_2 = bot_v6

    p1_score = 0
    p2_score = 0
    draws = 0

    for x in tqdm(range(100)):
        if x % 2:
            white = 'player_1'
            black = 'player_2'
        else:
            white = 'player_2'
            black = 'player_1'
        board = chess.Board()
        current_player = white

        while not board.is_game_over():
            if current_player == 'player_1':
                next_move = get_next_move(board, player_1)
                board.push(next_move)
                current_player = 'player_2'
            else:
                next_move = get_next_move(board, player_2)
                board.push(next_move)
                current_player = 'player_1'

        result = board.result()
        if result == '1-0':
            if white == 'player_1':
                p1_score += 1
            else:
                p2_score += 1
        elif result == '0-1':
            if black == 'player_2':
                p2_score += 1
            else:
                p1_score += 1
        else:
            draws += 1
        print('-'.join([str(p1_score), str(draws), str(p2_score)]))
        ZOBRIST_DICT.clear()


simulate_match()

