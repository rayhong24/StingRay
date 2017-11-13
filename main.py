import numpy as np

board = np.matrix([["r", "n", "b", "q", "k", "b", "n", "r"],
                   ["p","p","p","p","p","p","p","p"],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   [" "," "," "," "," "," "," "," "],
                   ["P","P","P","P","P","P","P","P"],
                   ["R", "N", "B", "Q", "K", "B", "N", "R"][)

def print_board(board):
    print(board)

print_board(board)