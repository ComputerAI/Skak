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

'''
import copy #for stack implementation, make Game a global variable, and delete the copy.
import time
c=0


def alphabeta(Game, alpha, beta, depth, p):
    global c
    c += 1
    if depth == 0 or Game.done(): return Game.score(p, depth)
    if Game.turn == p:
        a=alpha
        for val in T.valid(Game.board):
            if a>=beta: break
            g = copy.deepcopy(Game)
            g.move(val)
            if T.won(g.board): return 100+depth
            v=alphabeta(g,a,beta,depth-1, p)
            a = max(v,a)
        return a
    else:
        b=beta
        for val in T.valid(Game.board):
            if alpha>=b: break
            g = copy.deepcopy(Game)
            g.move(val)
            v=alphabeta(g,alpha,b,depth-1, p)
            b = min(v,b)
        return b


def ab(Game, depth, p):
    a=-1000
    b=-a
    poss=T.valid(Game.board)
    if not poss: return -1
    mov=poss[0]
    for val in poss:
        g = copy.deepcopy(Game)
        g.move(val)
        v = alphabeta(g, a, b, depth - 1, p)
        #print(v,val)
        if a < v:
            a=v
            mov=val
    global c
    #print(c)
    c=0
    return mov


def play(Game, p):
    if p is 'X': E='O'
    else: E = 'X'
    while not Game.done():
        if Game.turn == p:
            T.printBoard(Game.board)
            Game.move(input("Your move"))
        else: Game.move(ab(Game, 9, E))
    if T.won(Game.board):
        if Game.turn != p: print(f"Player {p} Wins")
        else: print(f"Player {E} Wins")
    else: print("It was a tie")
'''


if __name__ == "__main__":
    board = chess.Board()
    print(board)
    evaluate()
    alphabeta(1,2)