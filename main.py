"""
Library install with pip
pip install python-chess
pip install PyQt5

"""

import chess
import time
import scoreboard

ListOfScoreBoards = scoreboard.getScoreBoards() #Get scoreboards for black and white pieces

def squareValueForPiece(piece):
    print("Evalulating square value for ", piece)

def findmove(): #Find available moves in sorted order
    # Sort order:
    # Start with last best moves follow up
    # Prioritize capture of last moved piece
    # Killer moves: capture threatining pieces
    # Other captures: if you can capture do it
    # Pawn promotion: try to promte pawn
    # Castling
    # All other moves
    # En passant

    return list(board.legal_moves)


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
    king = 20000        #6
    pieces = [0,pawn,knight,bishop,rook,queen,king]
    
    diff = 0    
    for j in range(1,7):                                        #Go through each piece type
        for i in board.pieces(j,player):                        #Your piecec are goooood
            diff += pieces[j]*len(board.attacks(i))+pieces[j]
        for i in board.pieces(j,not player):                    #Enemy pieces not so much
            diff -= pieces[j]*len(board.attacks(i))+pieces[j]
        #diff += len(board.pieces(j,player))*pieces[j]
        #diff -= len(board.pieces(j,not player))*pieces[j]
    
    #If game is over and you didn't win, it's bad for else you will commit suicide. Winning is good.
    if board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_stalemate(): diff*=-king
    elif board.is_checkmate():
        if board.turn is player: diff*=-king
        if board.turn is not player: diff*=king
    return diff

def alphabeta(alpha, beta, depth, player):
    if depth == 0 or board.is_game_over(): return score(player, depth)
    if board.turn == player:
        a=alpha
        for val in findmove():
            if a>=beta: break
            board.push(val)
            v=alphabeta(a,beta,depth-1, player)
            a = max(v,a)
            board.pop()
        return a
    else:
        b=beta
        for val in findmove():
            if alpha>=b: break
            board.push(val)
            v=alphabeta(alpha,b,depth-1, player)
            b = min(v,b)
            board.pop()
        return b


def ab(depth, player):
    a=-1000
    b=-a
    poss=findmove()
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
        if board.turn: print("Player white Wins")
        else: print("Player black Wins")
    else: print("It was a tie")
#'''


if __name__ == "__main__":
    board = chess.Board()
    #board._set_board_fen("r7/1k2N1p1/3R4/3R4/2Q5/8/1K6/8")
    board._set_board_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNp")
    #print(ab(6,True))
    autoplay(4)
    print(board.is_insufficient_material())
    print(board.is_stalemate())
    print(board.is_fivefold_repetition())
    print(board.is_seventyfive_moves())
    print(c)

    #BITBOARDS
    bitboard = board.transform()
