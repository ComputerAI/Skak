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
    global c
    c += 1
                        #piecetype
    pawn = 1.0          #1
    knight = 3.05       #2
    bishop = 3.33       #3
    rook = 5.63         #4
    queen = 9.5         #5
    king = 200          #6
    pieces = [0,pawn,knight,bishop,rook,queen,king]

    mul = 1
    color = player
    diff = 0
    for _ in range(2):
        for j in range(1,7):
            diff += mul*len(board.pieces(j,color))*pieces[j]
        color = not color
        mul = -1
    
    return diff

def alphabeta(alpha, beta, depth, player):
    if depth == 0 or board.is_game_over(): return score(player, depth)
    if board.turn == player:
        a=alpha
        for val in list(board.legal_moves):
            if a>=beta: break
            board.push(val)
            v=alphabeta(a,beta,depth-1, player)
            a = max(v,a)
            board.pop()
        return a
    else:
        b=beta
        for val in list(board.legal_moves):
            if alpha>=b: break
            board.push(val)
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
    for val in poss:
        board.push(val)
        v = alphabeta(a, b, depth - 1, player)
        board.pop()
        #print(v,val)
        if a < v:
            a=v
            mov=val
    return mov


def play(player):
    E = not player
    while not board.is_game_over():
        if board.turn == player:
            print(board.unicode())
            print([str(i) for i in board.legal_moves])
            print()
            board.push_san(input("Your move: \n"))
        else: board.push(ab(3, E))
    
    if not board.is_stalemate():
        if board.turn != player: print(f"Player {player} Wins")
        else: print(f"Player {E} Wins")
    else: print("It was a tie")

def autoplay(depth):
    while not board.is_game_over():
        if board.turn == True: board.push(ab(depth, True))
        else: board.push(ab(depth, False))
        print(board.unicode(),'\n')
    if not board.is_stalemate():
        if board.turn: print(f"Player white Wins")
        else: print(f"Player black Wins")
    else: print("It was a tie")
#'''


if __name__ == "__main__":
    board = chess.Board()
    #board._set_board_fen("r7/1k2N1p1/3R4/3R4/2Q5/8/1K6/8")
    #print(ab(6,True))
    autoplay(3)
    print(c)