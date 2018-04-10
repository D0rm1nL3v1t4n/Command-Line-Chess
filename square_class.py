from piece_class import EMPTY_PIECE

class Square(object):
    
    def __init__(self, name):
        self.name = name
        self.piece = EMPTY_PIECE;
    
    #Printing the specific code name for that piece
    def returnMe(self):
        return self.piece.pieceCode
   
    #Placing a Piece in a Square
    def putPiece(self, piece):
        self.piece = piece
    
    #Clearing the Piece by putting it equal to the constant EMPTY PIECE  
    def clear(self):
        self.piece = EMPTY_PIECE
        
        
        
