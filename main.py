"""
Library install with pip
pip install python-chess
pip install PyQt5

"""


import chess
import chess.svg

def evaluate():
    print("Evaluating board")

def alphabeta(alpha, beta):
    print("Running AlphaBeta algorithm")

if __name__ == "__main__":
    board = chess.Board()
    print(board)
    evaluate()
    alphabeta(1,2)