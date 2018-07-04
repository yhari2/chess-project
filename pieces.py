import string 

class Piece(object):
    def __init__(self, name, color, currentSquare):
        self.name = name
        self.color = color
        self.currentSquare = currentSquare
        self.hasMoved = False
        self.possibleMoves = None
        self.directions = []

    def getPossibleMoves(self, board):
        return None

    def __repr__(self):
        return self.toString()

    # checks if either file/rank is on the board
    def isInBounds(self, elem):
        return 0 <= elem and elem < 8

    def getFileLetter(self):
        return string.ascii_lowercase[self.currentSquare[0]]


    def getPieceAbbreviation(self):
        return self.name[0]


    def toString(self):
        result = ""
        result += self.getPieceAbbreviation()
        result += self.getFileLetter()
        result += (str) (self.currentSquare[1] + 1)
        return result


    def isValidMove(self, newSquare, board):
        (newFile, newRank) = newSquare

        if(not self.isInBounds(newFile) or not self.isInBounds(newRank)): 
            return False

        # now we know that the newSquare is safely on the board
        if(board[newRank][newFile] == None): return True
        return False


    def isValidCapture(self, newSquare, board):
        (newFile, newRank) = newSquare

        if(not (self.isInBounds(newFile) and 
                self.isInBounds(newRank))): 
            return False

        # now we know that the newSquare is safely on the board
        if(board[newRank][newFile].color != self.color): 
            return True
            
        return False

    
    def moveToString(self, move):
        result = ""
        result += string.ascii_lowercase[move[0]]
        rank = move[1] + 1 
        result += str(rank)
        return result

    """ 
    WARNING: The only check that this code makes is that the new square is on the board.
    It is on the client to check this works.
    """
    def move(self, newSquare):
        if(self.isInBounds(newSquare[0]) and 
            self.isInBounds(newSquare[1])):
            self.hasMoved = True
            self.currentSquare = newSquare


    def getPossibleMoves(self, board):
        result = []
        (currFile, currRank) = self.currentSquare

        for direction in self.directions:
            (dFile, dRank) = direction

            for scale in range(1, 8):
                newFile, newRank = currFile + scale*dFile, currRank + scale*dRank
                if(not (self.isInBounds(newRank) and 
                    self.isInBounds(newFile))): 
                    break

                if(self.isInBounds(newRank) and 
                    self.isInBounds(newFile) and
                    board[newRank][newFile] != None and 
                    board[newRank][newFile].color == self.color):
                    break
                elif(self.isValidMove((newFile, newRank), board)):
                    result.append((newFile, newRank))
                elif(self.isValidCapture((newFile, newRank), board)):
                    result.append((newFile, newRank))
                    break
                else:
                    break

        self.possibleMoves = set(result)

class Pawn(Piece):
    def __init__(self, color, currentSquare):
        super().__init__("Pawn", color, currentSquare)
        if(self.color == "white"): 
            self.directions = [(0, 1), (0, 2)]
        else:
            self.directions = [(0, -1), (0, -2)]

    def getPieceAbbreviation(self):
        return ""

    def getPossibleMoves(self, board):
        result = []
        (currFile, currRank) = self.currentSquare

        if(self.hasMoved and self.color == "white"): 
            self.directions = [(0, 1)]
        elif(self.hasMoved and self.color == "white"):
            self.directions = [(0, -1)]

        for newDirection in self.directions:
            newFile, newRank = currFile + newDirection[0], currRank + newDirection[1]
            if(self.isValidMove((newFile, newRank), board)):
                result.append((newFile, newRank))
            else:
                # we no longer can consider any of these moves
                break

        captureDirections = [(-1, 1), (1, 1)]
        for newCapDir in captureDirections:
            newFile, newRank = currFile + newCapDir[0], currRank + newCapDir[1]

            if(self.isValidMove((newFile, newRank), board) and 
                board[newRank][newFile] != None and
                board[newRank][newFile].color != self.color):
                result.append((newFile, newRank))

        self.possibleMoves = set(result)


class Rook(Piece):
    def __init__(self, color, currentSquare):
        super().__init__("Rook", color, currentSquare)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Knight(Piece):
    def __init__(self, color, currentSquare):
        super().__init__("Knight", color, currentSquare)
        self.directions = [(-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2), (1, -2),
                            (-1, 2), (-1, -2)]


    def getPieceAbbreviation(self):
        return "N"

    def getPossibleMoves(self, board):
        result = []
        (currFile, currRank) = self.currentSquare

        for direction in self.directions:
            (dFile, dRank) = direction
            newFile, newRank = currFile + dFile, currRank + dRank
            if(self.isValidMove((newFile, newRank), board)):
                result.append((newFile, newRank))
            elif(self.isValidCapture((newFile, newRank), board)):
                result.append((newFile, newRank))
           
        self.possibleMoves = set(result)


class Bishop(Piece):
    def __init__(self, color, currentSquare):
        super().__init__("Bishop", color, currentSquare)
        self.directions = [(1, 1), (-1, -1), (-1, 1), (-1, -1)]


class King(Piece):
    def __init__(self, color, currentSquare, name = "King"):
        super().__init__(name, color, currentSquare)
        self.directions = [(1, 1), (-1, -1), (-1, 1), (-1, -1), 
                            (1, 0), (-1, 0), (0, 1), (0, -1)]
        self.isInCheck = False

    
    def getPossibleMoves(self, board):
        result = []
        (currFile, currRank) = self.currentSquare

        for direction in self.directions:
            (dFile, dRank) = direction
            newFile, newRank = currFile + dFile, currRank + dRank
            if(self.isValidMove((newFile, newRank), board)):
                result.append((newFile, newRank))
            elif(self.isValidCapture((newFile, newRank), board)):
                result.append((newFile, newRank))
                break
            else:
                break

        self.possibleMoves = set(result)

class Queen(King):
    def __init__(self, color, currentSquare, name = "Queen"):
        super().__init__(color, currentSquare, name)

    def getPossibleMoves(self, board):
        result = []
        (currFile, currRank) = self.currentSquare

        for direction in self.directions:
            (dFile, dRank) = direction

            for scale in range(1, 8):
                newFile, newRank = currFile + scale*dFile, currRank + scale*dRank

                if(self.isInBounds(newRank) and 
                    self.isInBounds(newFile) and
                    board[newRank][newFile] != None and 
                    board[newRank][newFile].color == self.color):
                    break
                elif(self.isValidMove((newFile, newRank), board)):
                    result.append((newFile, newRank))
                elif(self.isValidCapture((newFile, newRank), board)):
                    result.append((newFile, newRank))
                    break
                else:
                    break

        self.possibleMoves = set(result)
