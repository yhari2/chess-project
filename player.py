from pieces import Pawn, Rook, Knight, Bishop, King, Queen

class Player(object):
    
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.piecesNameList = ["r", "n", "b", "q", "k", "p"]
        self.possibleMoves = None # dictionary mapping all the pieces on board to their possible moves

    def setBoard(self):
        backRank, nextRank = 0, 1

        if(self.color == "black"):
            backRank = 7
            nextRank = 6

        for piece in self.piecesNameList:
            if(piece == "r"):
                self.board[backRank][0] = Rook(self.color, (0, backRank))
                self.board[backRank][7] = Rook(self.color, (7, backRank))
            elif(piece == "n"):
                self.board[backRank][1] = Knight(self.color, (1, backRank))
                self.board[backRank][6] = Knight(self.color, (6, backRank))
            elif(piece == "b"):
                self.board[backRank][2] = Bishop(self.color, (2, backRank))
                self.board[backRank][5] = Bishop(self.color, (5, backRank))
            elif(piece == "q"):
                self.board[backRank][3] = Queen(self.color, (3, backRank))
            elif(piece == "k"):
                self.board[backRank][4] = King(self.color, (4, backRank))
            else:
                for file in range(0, 8):
                    self.board[nextRank][file] = Pawn(self.color, 
                        (file, nextRank))


    def setPossibleMoves(self):
        result = dict()

        for rank in self.board:
            for file in self.board[rank]:
                if(self.board[rank][file] != None):
                    # found a piece
                    result[self.board[rank][file]] = self.board[rank][file].possibleMoves

        self.possibleMoves = result





