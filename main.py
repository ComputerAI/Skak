"""
Library install with pip
pip install python-chess
pip install PyQt5

"""


import chess
import chess.svg
import time

def evaluate():
    print("Evaluating board")



c=0

def score(player,depth):
    return 0

def alphabeta(alpha, beta, depth, player):
    global c
    c += 1
    if depth == 0 or board.is_game_over: return score(player, depth)
    if board.turn == player:
        a=alpha
        for val in list(board.legal_moves):
            if a>=beta: break
            board.push_san(val)
            v=alphabeta(a,beta,depth-1, player)
            a = max(v,a)
            board.pop()
        return a
    else:
        b=beta
        for val in list(board.legal_moves):
            if alpha>=b: break
            board.push_san(val)
            v=alphabeta(alpha,b,depth-1, player)
            b = min(v,b)
            board.pop()
        return b


def ab(depth, player):
    a=-1000
    b=-a
    poss=list(board.legal_moves)
    if not poss: return -1
    mov=poss[0]
    print(poss[0])
    for val in poss:
        board.push_san(val)
        v = alphabeta(a, b, depth - 1, player)
        #print(v,val)
        if a < v:
            a=v
            mov=val
    return mov

'''
def play(Game, player):
    if player is 'X': E='O'
    else: E = 'X'
    while not Game.done():
        if Game.turn == player:
            T.printBoard(Game.board)
            Game.move(input("Your move"))
        else: Game.move(ab(Game, 9, E))
    if T.won(Game.board):
        if Game.turn != player: print(f"Player {player} Wins")
        else: print(f"Player {E} Wins")
    else: print("It was a tie")
'''


if __name__ == "__main__":
    board = chess.Board()
    
    legalMoves = list(board.legal_moves)
    #board.push(legalMoves[0])
    print(legalMoves[0])
    print(ab(1,True))