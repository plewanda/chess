import chess.syzygy

tablebase = chess.syzygy.open_tablebase("./resources/tablebases/3-4-5/")


def find_syzygy_move(board):
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
