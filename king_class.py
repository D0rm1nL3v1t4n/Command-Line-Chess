from piece_class import Piece

class King(Piece):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def CanMove(self):
        xCoordChange = self.source[0] - self.destination[0]
        yCoordChange = self.source[1] - self.destination[1]
                
        illegalMoves = 0
        
        if abs(xCoordChange) > 1 or self.destination[0] > 8 or self.destination[0] < 1:
            illegalMoves += 1
        if abs(yCoordChange) > 1 or self.destination[1] > 8 or self.destination[1] < 1:
            illegalMoves += 1
            
        if illegalMoves > 0:
            print("The King cannot move to that spot!")
            
        
    
        if self.destination[3] != "  ":
            illegalMoves += 1
            print("That is an illegal move, there is already a piece there!")
            
        if illegalMoves > 0:
            canMove = False
        elif illegalMoves == 0:
            canMove = True
            
            
        return canMove