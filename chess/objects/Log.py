from persistent import Persistent

class Log(Persistent):
    def __init__(self,turnNo,board,pieces,time,nextMove, gameId):
        self.turnNo = turnNo
        self.board = board
        self.pieces = pieces
        self.time = time
        self.nextMove = nextMove
        self.gameId = gameId





