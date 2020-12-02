"""
Library install with pip
pip install python-chess
pip install PyQt5

"""

import chess
import scoreboard
from collections import OrderedDict
import threading

stop = False
ListOfScoreBoards = scoreboard.getScoreBoards() # Get scoreboards for black and white pieces

def findmove(): 
    # Find available moves in sorted order
    l=[]
    # Start with last best moves follow up              ✓

    # With current scoring, this is slower
    # Prioritize capture of last moved piece            ✓
    if len(board.move_stack)>0:
        last = str(board.peek())
        piece = chess.parse_square(last[2:4])
        froms = board.attackers(board.turn,piece)
        move = [chess.Move(i,piece) for i in froms]
        l.extend([m for m in move if board.is_legal(m)])

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
    if board.turn: moves = [chess.Move(pawn,pawn+8,5) for pawn in ours[0] if pawn>=8*6]
    else: moves = [chess.Move(pawn,pawn-8,5) for pawn in ours[0] if pawn <8*2]
    l.extend([m for m in moves if board.is_legal(m)])

    # All other moves ✓
    ll = list(board.legal_moves)
    l.extend(ll)
    l = list(OrderedDict.fromkeys(l))

    if len(l) is not len(ll): # Checks if list has illegal moves
        print("Illigal move detected",len(ll),len(l))
        l = [i for i in l if board.is_legal(i)]
    return l

centerManhattanDistance =  [[6,5,4,3,3,4,5,6],
                            [5,4,3,2,2,3,4,5],
                            [4,3,2,1,1,2,3,4],
                            [3,2,1,0,0,1,2,3],
                            [3,2,1,0,0,1,2,3],
                            [4,3,2,1,1,2,3,4],
                            [5,4,3,2,2,3,4,5],
                            [6,5,4,3,3,4,5,6]]

#centerDistance =           [[3,3,3,3,3,3,3,3],
#                            [3,2,2,2,2,2,2,3],
#                            [3,2,1,1,1,1,2,3],
#                            [3,2,1,0,0,1,2,3],
#                            [3,2,1,0,0,1,2,3],
#                            [3,2,1,1,1,1,2,3],
#                            [3,2,2,2,2,2,2,3],
#                            [3,3,3,3,3,3,3,3]]

def scoreForPiece(player, piecetype, position): # Takes the player, number indicating the piece type and the piece location
    pawnRow = [0,0,-1,0,2,14,30,0]
    if player: pawnLine = [-2,-2,1,5,4,3,0,-2]
    else:pawnLine = [-2,0,3,4,5,1,-2,-2]
    
    switcher = { # Dictionary used like a switch statement
        0: pawnRow[position%8] + pawnLine[position//8]*((position%8)/2),
        1: 3.0*(4 - centerManhattanDistance[position//8][position%8]),
        2: 2.0*len(board.attacks(position)),
        3: 1.5*len(board.attacks(position)),
        4: 1.0*len(board.attacks(position)),
        5: centerManhattanDistance[position//8][position%8]*5
    }
    return switcher.get(piecetype) # Returns extra score for the given piece


def score(player, depth):
                        #piecetype
    pawn = 100          #1
    knight = 305        #2
    bishop = 333        #3
    rook = 563          #4
    queen = 950         #5
    king = 20000        #6
    pieceScore = [pawn,knight,bishop,rook,queen,king]
	
    currentPlayer = player
    currentDiff =      [0,0] # Current score for white (first element) and black (second element).
    threatenedPieces = [0,0] # Threatened pieces score for white (first element) and black (second element).
	
    for l in range(2): 
        for j in range(6): # For every piece type
            for i in board.pieces(j+1,currentPlayer): # For every current players piece on the board
                pieceBoard = ListOfScoreBoards[currentPlayer][j]
                for k in board.attackers(not currentPlayer, i):
                    if board.piece_at(k).piece_type < board.piece_at(i).piece_type: # If a minor piece attacks the current piece
                        threatenedPieces[currentPlayer] += 1

                if currentPlayer:currentDiff[currentPlayer] += pieceBoard[i//8][i%8]+pieceScore[j]+scoreForPiece(currentPlayer,j,i)
                else:            currentDiff[currentPlayer] -= pieceBoard[i//8][i%8]+pieceScore[j]+scoreForPiece(currentPlayer,j,i)

        if   threatenedPieces[currentPlayer] == 1:
            if    currentPlayer: currentDiff[currentPlayer] -= 10
            else:                currentDiff[currentPlayer] += 10
        elif threatenedPieces[currentPlayer] > 1:
            if    currentPlayer: currentDiff[currentPlayer] -= 50
            else:                currentDiff[currentPlayer] += 50
        else:
            if    currentPlayer: currentDiff[currentPlayer] += 2
            else: currentDiff[currentPlayer] -= 2

        currentPlayer = not player # We have done the calculations for one player, now we have to do it for the other so we can compare
    if player: diff =   currentDiff[0]+currentDiff[1]
    else:      diff = -(currentDiff[0]+currentDiff[1])
    
    # If game is over and you didn't win, it's bad for else you will commit suicide. Winning is good.
    if board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_stalemate(): diff+=-king
    elif board.is_checkmate():
        if board.turn is     player: diff+=-king
        if board.turn is not player: diff+=king+depth*king
    return diff


def alphabeta(alpha, beta, depth, player):
    global stop
    if depth <= 0 or board.is_game_over() or stop: return score(player, depth)
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
    global mov, stop
    poss=findmove()
    if not poss: return -1
    mov=poss[0]
    for i in range(2,depth+1,2):
        a=-1000000
        b=-a
        board.push(mov)
        v = alphabeta(a,b,i-1,player)
        if a < v: a=v
        board.pop()
        for val in poss:
            board.push(val)
            v = alphabeta(a, b, i-1, player)
            board.pop()
            if stop:
                print(f"depth:{i}",f"value:{a}")
                return mov
            if a < v:
                a=v
                mov=val
    return mov

def threadded(depth,player,time):
    global mov, stop
    stack = len(board.move_stack)
    p = threading.Thread(target=ab, args=(depth,player))
    p.start()
    p.join(time)
    if p.is_alive():
        stop=True
        p.join()
    for _ in range(len(board.move_stack)-stack): board.pop()
    stop=False
    return mov

def play(player,depth,time):
    E = not player
    while not board.is_game_over():
        if board.turn == player:
            print(board.unicode(invert_color=True, borders=True))
            print([str(i) for i in board.legal_moves],'\n')
            
            inCorrect = True
            while (inCorrect):
                move = input("Your move: \n")
                for i in board.legal_moves:
                    if str(move) == str(i):
                        board.push_uci(move)
                        inCorrect = False
                        break
                if inCorrect:
                    print("Invalid move try again.")
            
        else: board.push(threadded(depth, E, time))
    print(board.unicode(invert_color=True, borders=True))
    if not board.is_stalemate():
        if not board.turn: print("White wins!") # Since the game changes turn after we call board.push() white wins when it's blacks turn and vice versa.
        else: print("Black wins!")
    else: print("It was a tie")

def autoplay(depth,time):
    while not board.is_game_over():
        board.push(threadded(depth, board.turn,time))
        print(board.unicode(invert_color=True, borders=False, empty_square="⭘"),'\n') # Print the board where white is at the bottom of the board. Forms for empty squares: ⭘, ☐
    if not board.is_stalemate():
        if not board.turn: print("White wins!") # Since the game changes turn after we call board.push() white wins when it's blacks turn and vice versa.
        else: print("Black wins!")
    else: print("It was a tie")



if __name__ == "__main__":
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    
    # If you want to test with AI vs AI uncomment next line and comment the code following
    #autoplay(20,10)
    
    print("Welcome to a game of chess versus an AI")
    color = input("Please choose a color (white or black)\n")
    if color == "white":
        play(True, 25,29)
    elif color == "black":
        play(False, 25,29)
    else:
        print("Not a real color. Exiting...")
