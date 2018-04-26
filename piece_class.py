class Piece(object):
    def __init__(self, name, colour, pieceCode):
        self.name = name
        self.colour = colour
        self.pieceCode = pieceCode
    
    def ReturnMe(self):
        return self.pieceCode
    
EMPTY_PIECE = Piece(".",".","  ")