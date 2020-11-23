"""
Library install with pip
pip install python-chess
pip install PyQt5

"""

import chess
import time
import scoreboard
from collections import OrderedDict

ListOfScoreBoards = scoreboard.getScoreBoards() # Get scoreboards for black and white pieces

def findmove(): 
    # Find available moves in sorted order
    l=[]
    # Start with last best moves follow up              ✓

    #''' With current scoring, this is slower
    # Prioritize capture of last moved piece            ✓
    if len(board.move_stack)>0:
        last = board.peek()
        piece = chess.parse_square((str(last)[2:]))
        froms = board.attackers(board.turn,piece)
        move = [chess.Move(i,piece) for i in froms]
        l.extend(move)
    ours = [board.pieces(j,board.turn) for j in range(1,7)]
    for ptypes in ours:
        for froms in ptypes:
            # Killer moves: capture threatining pieces  ✓
            attackers = board.attackers(not board.turn,froms)
            attacks = board.attacks(froms)
            moves = [chess.Move(froms,to) for to in attacks if attackers.__contains__(to)]
            # Other captures: if you can capture do it  ✓
            moves.extend([chess.Move(froms,to) for to in attacks if not attackers.__contains__(to)])
            l.extend([move for move in moves if board.is_legal(move)])
    # Pawn promotion: try to promte pawn                ✓/✓
    if board.turn: moves = [chess.Move(pawn,pawn-8) for pawn in ours[0] if pawn<8*2]
    else: moves = [chess.Move(pawn,pawn-8) for pawn in ours[0] if pawn >=8*7]
    l.extend([m for m in moves if board.is_legal(m)])
    # if len([item for sublist in ours for item in sublist])<8:
    if board.turn: moves = [chess.Move(pawn,pawn-8) for pawn in ours[0]]
    else: moves = [chess.Move(pawn,pawn-8) for pawn in ours[0]]
    l.extend([m for m in moves if board.is_legal(m)])
    
    # Castling        X
    # for pie in ours[3]:#Rook = 4 for 1 indexed array
    #     if(board.castling_rights & pie): print("castling",pie, [o for o in ours[5]][0])
    #'''
    # All other moves ✓
    ll = list(board.legal_moves)
    l.extend(ll)
    l = list(OrderedDict.fromkeys(l))
    # En passant      X (Alredy in "capture if possible")

    #if len(l) is not len(ll): print("Illigal move detected",len(ll),len(l))
    return l

centerManhattanDistance =  [[6,5,4,3,3,4,5,6],
                            [5,4,3,2,2,3,4,5],
                            [4,3,2,1,1,2,3,4],
                            [3,2,1,0,0,1,2,3],
                            [3,2,1,0,0,1,2,3],
                            [4,3,2,1,1,2,3,4],
                            [5,4,3,2,2,3,4,5],
                            [6,5,4,3,3,4,5,6]]

def scoreForPiece(player, piecetype, position): #Takes the number indicating the piece type and the piece location
    pawnRow = [0,0,-1,0,2,14,30,0]
    if player: pawnLine = [-2,-2,1,5,4,3,0,-2]
    else:pawnLine = [-2,0,3,4,5,1,-2,-2]
    
    switcher = { #Dictionary used like a switch statement
        0: pawnRow[position//8] + pawnLine[position%8]*((position//8)/2),
        1: 3.0*(4 - centerManhattanDistance[position//8][position%8]),
        2: 2.0*len(board.attacks(position)),
        3: 1.5*len(board.attacks(position)),
        4: 1.0*len(board.attacks(position)),
        5: -centerManhattanDistance[position//8][position%8]
    }
    return switcher.get(piecetype, 0) #Returns extra score for the given piece


c=0
def score(player,depth):
    
    global c
    c += 1
                        #piecetype
    pawn = 100          #1
    knight = 305        #2
    bishop = 333        #3
    rook = 563          #4
    queen = 950         #5
    king = 20000       #6
    pieceScore = [pawn,knight,bishop,rook,queen,king]
    
    threatenedPieces = 0
    diff = 0    
    
    if player:mul=1 
    else: mul=-1
    
    for j in range(6):                                            #Go through each piece type
        for i in board.pieces(j+1,player):                        #Your pieces are goooood
            pieceBoard = ListOfScoreBoards[player][j]
            for k in board.attackers(not player, i):
                if board.piece_at(k).piece_type == 2 or board.piece_at(k).piece_type == 3:
                    threatenedPieces += 1
            
            diff += mul*(pieceBoard[i//8][i%8]+pieceScore[j]+scoreForPiece(player,j,i)) #TODO FIX
    
    if threatenedPieces==1:
        diff -= mul*10
    elif threatenedPieces>1:
        diff -= mul*50
    else:
        diff += mul*2
    
    #If game is over and you didn't win, it's bad for else you will commit suicide. Winning is good.
    if board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_stalemate(): diff*=-king
    elif board.is_checkmate():
        if board.turn is player: diff*=-king
        if board.turn is not player: diff*=king
    return diff


def alphabeta(alpha, beta, depth, player):
    if depth <= 0 or board.is_game_over(): return score(player, depth)
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
    a=-1000000
    b=-a
    poss=findmove()
    if not poss: return -1
    mov=poss[0]
    for i in range(1,depth+1):
        board.push(mov)
        v = alphabeta(a,b,i,player)
        if a < v: a=v
        board.pop()    
        for val in poss:
            board.push(val)
            v = alphabeta(a, b, i, player)
            board.pop()
            if a < v:
                a=v
                mov=val
    return mov


def play(player): #FIXME Outdated
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
        board.push(ab(depth, board.turn))
        print(board.unicode(invert_color=True, borders=False, empty_square="⭘"),'\n') #Print the board where white is at the bottom of the board. Forms for empty squares: ⭘, ☐
    if not board.is_stalemate():
        if not board.turn: print("White wins!") #Since the game changes turn after we call board.push() white wins when it's blacks turn and vice versa.
        else: print("Black wins!")
    else: print("It was a tie")



if __name__ == "__main__":
    board = chess.Board("rnkq1bnr/2p1pN2/p2pN2p/1p5Q/8/4P3/PPPP1PPP/R1B1KB1R w KQkq - 0 1")
    #board._set_board_fen("r7/1k2N1p1/3R4/3R4/2Q5/8/1K6/8")
    #board._set_board_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    autoplay(4)
    
    print(board.is_insufficient_material())
    print(board.is_stalemate())
    print(board.is_fivefold_repetition())
    print(board.is_seventyfive_moves())
    print(c)
