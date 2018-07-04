import string
from pieces import Rook, Knight, Bishop, King, Queen, Pawn

def moveToString(move):
    result = ""
    result += string.ascii_lowercase[move[0]]
    rank = move[1] + 1 
    result += str(rank)
    return result

def getNewBoard():
    a=[]
    for row in range(8): a += [[None]*8]
    return a

def main():
    board = getNewBoard()
    piecesList = []

    # white pieces
    wr1 = Rook("white", (0, 0))
    wn1 = Knight("white", (1, 0))
    wb1 = Bishop("white", (2, 0))
    wq = Queen("white", (3, 0))
    wk = King("white", (4, 0))
    wb2 = Bishop("white", (5, 0))
    wn2 = Knight("white", (6, 0))
    wr2 = Rook("white", (7, 0))

    # adding pieces to piecesList
    piecesList.append(wr1)
    piecesList.append(wn1)
    piecesList.append(wb1)
    piecesList.append(wq)
    piecesList.append(wk)
    piecesList.append(wb2)
    piecesList.append(wn2)
    piecesList.append(wr2)

    # black pieces
    br1 = Rook("black", (0, 7))
    bn1 = Knight("black", (1, 7))
    bb1 = Bishop("black", (2, 7))
    bq = Queen("black", (3, 7))
    bk = King("black", (4, 7))
    bb2 = Bishop("black", (5, 7))
    bn2 = Knight("black", (6, 7))
    br2 = Rook("black", (7, 7))

    # adding pieces to piecesList
    piecesList.append(br1)
    piecesList.append(bn1)
    piecesList.append(bb1)
    piecesList.append(bq)
    piecesList.append(bk)
    piecesList.append(bb2)
    piecesList.append(bn2)
    piecesList.append(br2)

    # adding pawns for both colors
    for color in ["white", "black"]:
        for file in range(0, 8):
            if color == "white":
                p = Pawn(color, (file, 1))
            else:
                p = Pawn(color, (file, 6))
            piecesList.append(p)

    # putting all the pieces on the board
    for piece in piecesList:
        (currFile, currRank) = piece.currentSquare
        board[currRank][currFile] = piece


    # testing the pieces
    for rank in range(len(board)):
        for file in range(len(board)):
            if(board[rank][file] != None):
                p = board[rank][file]
                p.getPossibleMoves(board)
                print(p.toString() + ":")
                if(p.possibleMoves != None):
                    for move in list(p.possibleMoves):
                        print("\t" + moveToString(move))



