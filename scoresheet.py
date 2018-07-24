import string
import utils

class ScoreSheet(object):
    def __init__(self):
        self.whiteMoves = None
        self.blackMoves = None

    # takes in file of score from game
    def getMoves(self, scoreFile):
        count = 0
        self.whiteMoves, self.blackMoves = [], []
        with open(scoreFile, "rt") as f:
            records = f.read()

            for record in records.split("\n"):
                moves = record.split(" ")

                for move in moves:
                    move = self.convertMove(move)
                    if(count%2 == 0):
                        self.whiteMoves.append(move)
                    else: 
                        self.blackMoves.append(move)
                    count = count + 1



                