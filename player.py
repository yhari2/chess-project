from pieces import Pawn, Rook, Knight, Bishop, King, Queen

class Player(object):
    
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.piecesNameList = ["r", "n", "b", "q", "k", "p"]
        self.possibleMoves = None
        self.piecesOnBoard = []

    def setBoard(self):
        backRank, nextRank = 0, 1

        if(self.color == "black"):
            backRank = 7
            nextRank = 6

        for piece in self.piecesNameList:
            if(piece == "r"):
                self.board[backRank][0] = Rook(self.color, (0, backRank))
                self.board[backRank][7] = Rook(self.color, (7, backRank))
                self.piecesOnBoard.append(self.board[backRank][0])
                self.piecesOnBoard.append(self.board[backRank][7])
            elif(piece == "n"):
                self.board[backRank][1] = Knight(self.color, (1, backRank))
                self.board[backRank][6] = Knight(self.color, (6, backRank))
                self.piecesOnBoard.append(self.board[backRank][1])
                self.piecesOnBoard.append(self.board[backRank][6])
            elif(piece == "b"):
                self.board[backRank][2] = Bishop(self.color, (2, backRank))
                self.board[backRank][5] = Bishop(self.color, (5, backRank))
                self.piecesOnBoard.append(self.board[backRank][2])
                self.piecesOnBoard.append(self.board[backRank][5])
            elif(piece == "q"):
                self.board[backRank][3] = Queen(self.color, (3, backRank))
                self.piecesOnBoard.append(self.board[backRank][3])
            elif(piece == "k"):
                self.board[backRank][4] = King(self.color, (4, backRank))
                self.piecesOnBoard.append(self.board[backRank][4])
            else:
                for file in range(0, 8):
                    self.board[nextRank][file] = Pawn(self.color, 
                        (file, nextRank))
                    self.piecesOnBoard.append(self.board[nextRank][file])


    def setPossibleMoves(self):
        result = dict()

        for rank in self.board:
            for file in self.board[rank]:
                if(self.board[rank][file] != None):
                    self.board[rank][file].getPossibleMoves()
                    result[self.board[rank][file]] = self.board[rank][file].possibleMoves

        self.possibleMoves = result





