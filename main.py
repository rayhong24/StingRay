import numpy as np

letter2index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
board = np.matrix([["r", "n", "b", "q", "k", "b", "n", "r"],
                   ["p","p","p","p","p","p","p","p"],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   ["P","P","P","P","P","P","P","P"],
                   ["R", "N", "B", "Q", "K", "B", "N", "R"]])

def print_board(board):
    print(board)


def query_board(pos):
    """return the piece at the given coordinate"""
    row, col = chess_to_matrix(pos)
    print(board[row, col])


def chess_to_matrix(pos):
    """convert chess notaion to matrix notation"""
    row = 8 - int(pos[1])
    col = letter2index.get(pos[0])
    return row, col


def pawn_move(move):
    bob = query_board(move)
    print("bob")
    if bob == " ":
        print("bob")


pawn_move("e3")
print_board(board)
query_board("e2")
