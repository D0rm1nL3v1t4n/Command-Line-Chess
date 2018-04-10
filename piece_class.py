class Piece(object):
    def __init__(self, name, colour, pieceCode):
        self.name = name
        self.colour = colour
        self.pieceCode = pieceCode
    
    def returnMe(self):
        return self.pieceCode
    
    
EMPTY_PIECE = Piece(".",".","  ")



class King(Piece):
    def __init__(self, canMove, legalMove):
        self.canMove = canMove
        self.legalMove = legalMove
        
        
    def CanMove(self):