import random

import chess
import chess.polyglot
import chess.syzygy

tablebase = chess.syzygy.open_tablebase("./resources/tablebases/3-4-5/")


def evaluate_board(board):
    try:
        with chess.polyglot.open_reader("./resources/komodo.bin") as reader:
            move = random.choice(list(reader.find_all(board))).move
    except IndexError:
        if piece_count(board) < 6:
            move = find_best_move(board)
        else:
            legal_moves = list(board.legal_moves)
            move = random.choice(legal_moves)
    return move


def piece_count(board):
    return len(board.piece_map())


def find_best_move(board):
    wdl = tablebase.probe_wdl(board)

    best_move = None
    if wdl > 0:
        best_dtz = float('-inf')
    elif wdl < 0:
        best_dtz = 0
    elif wdl == 0:
        best_dtz = float('inf')

    for move in board.legal_moves:
        new_board = board.copy()
        new_board.push(move)
        new_dtz = tablebase.probe_dtz(new_board)
        if wdl > 0 > new_dtz and (best_move is None or new_dtz > best_dtz):
            best_move = move
            best_dtz = new_dtz
        elif wdl < 0 and (new_dtz == 0 or (best_move is None or new_dtz < best_dtz)):
            best_move = move
            best_dtz = new_dtz
        elif wdl == 0 and new_dtz < best_dtz:
            best_move = move
            best_dtz = new_dtz
    return best_move
