from piece_class import Piece

class Knight(Piece):
    def CanMove(self,source,destination):
        xCoordChange = source[0] - source[1]
        yCoordChange = destination[0] - destination[1]
        illegalMoves = 0

        if not ((abs(xCoordChange) == 2 and abs(yCoordChange) == 1) or (abs(xCoordChange) == 1 or abs(yCoordChange) == 2)):
            illegalMoves += 1
            print("The Knight cannot move there!")

        if destination[2] == self.colour:
            illegalMoves += 1
            print("That is an illegal move, you already have a piece there!")

        if illegalMoves > 0:
            return False
        elif illegalMoves == 0:
            return True