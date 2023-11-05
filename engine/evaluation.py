import chess
from chess import Board
from chess.polyglot import zobrist_hash

from consts import PIECE_VALUES, PAWN_SQUARE_TABLE, KNIGHT_SQUARE_TABLE, BISHOP_SQUARE_TABLE, ROOK_SQUARE_TABLE, \
    QUEEN_SQUARE_TABLE, KING_SQUARE_TABLE_MG, KING_SQUARE_TABLE_EG, PIECE_PHASE_VALUES, TOTAL_PHASE, ZOBRIST_DICT


def naive_zobrist_evaluation(board: Board):
    zhash = zobrist_hash(board)
    if zhash not in ZOBRIST_DICT:
        ZOBRIST_DICT[zhash] = evaluate_material_tapered_position(board)
    return ZOBRIST_DICT[zhash]


def evaluate_material_tapered_position(board: Board):
    return material_evaluation(board) + position_evaluation(board) + king_evaluation(board)


def evaluate_material_position(board: Board):
    return material_evaluation(board) + position_evaluation(board)


def material_evaluation(board: Board):
    if board.is_checkmate():
        if board.turn:
            return float('-inf')
        else:
            return float('inf')
    score = 0

    for (piece, value) in PIECE_VALUES.items():
        score += len(board.pieces(piece, chess.WHITE)) * value
        score -= len(board.pieces(piece, chess.BLACK)) * value

    return score


def position_evaluation(board: Board):
    score = 0

    for square in range(64):
        piece = board.piece_at(square)
        if piece:
            square = convert_to_square_table(square if piece.color else 63 - square)
            if piece.piece_type == chess.PAWN:
                score += PAWN_SQUARE_TABLE[square] * [-1, 1][piece.color]
            if piece.piece_type == chess.KNIGHT:
                score += KNIGHT_SQUARE_TABLE[square] * [-1, 1][piece.color]
            if piece.piece_type == chess.BISHOP:
                score += BISHOP_SQUARE_TABLE[square] * [-1, 1][piece.color]
            if piece.piece_type == chess.ROOK:
                score += ROOK_SQUARE_TABLE[square] * [-1, 1][piece.color]
            if piece.piece_type == chess.QUEEN:
                score += QUEEN_SQUARE_TABLE[square] * [-1, 1][piece.color]

    return score


def king_evaluation(board: Board):
    score = 0
    white_eval = 0
    black_eval = 0

    phase = TOTAL_PHASE
    for (piece, value) in PIECE_PHASE_VALUES.items():
        phase -= len(board.pieces(piece, chess.WHITE)) * value
        phase -= len(board.pieces(piece, chess.BLACK)) * value

    phase = (phase * TOTAL_PHASE + (TOTAL_PHASE / 2)) / TOTAL_PHASE

    for square in range(64):
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.KING and piece.color:
            square = convert_to_square_table(square)
            white_eval = ((KING_SQUARE_TABLE_MG[square] * (TOTAL_PHASE - phase)) + (KING_SQUARE_TABLE_EG[square] * phase)) / TOTAL_PHASE
        if piece and piece.piece_type == chess.KING and not piece.color:
            square = convert_to_square_table(63 - square)
            black_eval = ((KING_SQUARE_TABLE_MG[square] * (TOTAL_PHASE - phase)) + (KING_SQUARE_TABLE_EG[square] * phase)) / TOTAL_PHASE
    return score + white_eval - black_eval


def convert_to_square_table(num):
    rank_size = 8
    rank = num // rank_size
    file = num % rank_size

    inverted_rank = (rank_size - 1) - rank
    converted = inverted_rank * rank_size + file

    return converted
