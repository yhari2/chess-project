import string

class ScoreSheet(object):
    def __init__(self):
        self.whiteMoves = None
        self.blackMoves = None


    # translate the algebraic notation to MRN - machine readable notation
    def convertMove(self, move):
        piece = ""
        for char in move:



    # takes in file of score from game
    def getMoves(self, scoreFile):
        count = 0
        self.whiteMoves, self.blackMoves = [], []
        with open(scoreFile, "rt") as f:
            for record in f.split("\n"):
                moves = record.split(" ")
                for move in moves:
                    move = self.convertMove(move)
                    if(count%2 == 0):
                        self.whiteMoves.append(move)
                    else: 
                        self.blackMoves.append(move)
                    count++



                