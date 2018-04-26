from piece_class import EMPTY_PIECE

class Square(object):
    def __init__(self, name):
        self.name = name
        self.piece = EMPTY_PIECE;
    
    def ReturnMe(self):
        return self.piece.pieceCode
   
    def PutPiece(self, piece):
        self.piece = piece
    
    def Clear(self):
        self.piece = EMPTY_PIECE