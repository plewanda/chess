import random

import chess
import chess.polyglot

from engine.syzygy_move_generator import find_syzygy_move


def get_next_move(board, bot):
    try:
        with chess.polyglot.open_reader("./resources/komodo.bin") as reader:
            move = random.choice(list(reader.find_all(board))).move
    except IndexError:
        if piece_count(board) < 6:
            move = find_syzygy_move(board)
        else:
            move = bot.get_move(board)
    return move


def piece_count(board):
    return len(board.piece_map())
