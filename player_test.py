from player import Player

def getNewBoard():
    a=[]
    for row in range(8): a += [[None]*8]
    return a


def main():
    board = getNewBoard()
    w = Player("white", board)
    b = Player("black", board)

    w.setBoard()
    b.setBoard()

    print(board)
