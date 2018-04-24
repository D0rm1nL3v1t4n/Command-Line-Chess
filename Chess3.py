from square_class import Square
from piece_class import Piece
from king_class import King
import random



def players(number):
    player = input("Player " + number + " Name: ")
    return player

def playerStarting(playerOne, playerTwo):
    randInt = random.randint(0,1)
    if randInt == 0:
        print("\n"+playerOne, "is white,\n" + playerTwo, "is black.\n")
        white = playerOne
    else:
        print("\n"+playerOne, "is black,\n" + playerTwo, "is white.\n")
        white = playerTwo
    
    
    print(white, "is white and therefore starts, good luck! :^)\n\n")


def gameStart(player, chessBoard):
    
    validInput = False
    while validInput == False:
        pieceSelected = input("\n>>>Select a piece to move: ")

        if len(pieceSelected) == 2:
            validInput = True
        else:
            print("That input is not accepted!")
            validInput = False


    repeat = False

    validInput = False
    while validInput == False:
        pieceDestination = input("\n>>>Place the piece: ")

        if len(pieceDestination) == 2:
            validInput = True
        else:
            print("That input is not accepted!")
            validInput = False


    if repeat == False:

        for srcSqr in chessBoard:
            if pieceSelected.lower() == srcSqr[0]:

                for dstSqr in chessBoard:
                    if pieceDestination.lower() == dstSqr[0]:

                        """
                        Need to pass function in Piece Subclass to check canMove() for specific Piece type --> canMove() varies depending on Piece
                        dstSqr[1].CanMove()
                        
                        
                        DESTINATION:
                        # 1 = X Coordinate
                        # 2 = Y Coordinate
                        # 3 = Destination Square code


                        # 4 = Colour of piece in 3
                        OR 3 is entered as an array with all properties for that Square --> and therefore Piece colour (if present)                        
                        
                        """
                        
                        dstSqr[1].PutPiece(srcSqr[1].piece)

                        srcSqr[1].Clear()


    showBoard()


def showBoard():
    print("8|"+a8.ReturnMe()+"|"+b8.ReturnMe()+"|"+c8.ReturnMe()+"|"+d8.ReturnMe()+"|"+e8.ReturnMe()+"|"+f8.ReturnMe()+"|"+g8.ReturnMe()+"|"+h8.ReturnMe()+"|")
    print("7|"+a7.ReturnMe()+"|"+b7.ReturnMe()+"|"+c7.ReturnMe()+"|"+d7.ReturnMe()+"|"+e7.ReturnMe()+"|"+f7.ReturnMe()+"|"+g7.ReturnMe()+"|"+h7.ReturnMe()+"|")
    print("6|"+a6.ReturnMe()+"|"+b6.ReturnMe()+"|"+c6.ReturnMe()+"|"+d6.ReturnMe()+"|"+e6.ReturnMe()+"|"+f6.ReturnMe()+"|"+g6.ReturnMe()+"|"+h6.ReturnMe()+"|")
    print("5|"+a5.ReturnMe()+"|"+b5.ReturnMe()+"|"+c5.ReturnMe()+"|"+d5.ReturnMe()+"|"+e5.ReturnMe()+"|"+f5.ReturnMe()+"|"+g5.ReturnMe()+"|"+h5.ReturnMe()+"|")
    print("4|"+a4.ReturnMe()+"|"+b4.ReturnMe()+"|"+c4.ReturnMe()+"|"+d4.ReturnMe()+"|"+e4.ReturnMe()+"|"+f4.ReturnMe()+"|"+g4.ReturnMe()+"|"+h4.ReturnMe()+"|")
    print("3|"+a3.ReturnMe()+"|"+b3.ReturnMe()+"|"+c3.ReturnMe()+"|"+d3.ReturnMe()+"|"+e3.ReturnMe()+"|"+f3.ReturnMe()+"|"+g3.ReturnMe()+"|"+h3.ReturnMe()+"|")
    print("2|"+a2.ReturnMe()+"|"+b2.ReturnMe()+"|"+c2.ReturnMe()+"|"+d2.ReturnMe()+"|"+e2.ReturnMe()+"|"+f2.ReturnMe()+"|"+g2.ReturnMe()+"|"+h2.ReturnMe()+"|")
    print("1|"+a1.ReturnMe()+"|"+b1.ReturnMe()+"|"+c1.ReturnMe()+"|"+d1.ReturnMe()+"|"+e1.ReturnMe()+"|"+f1.ReturnMe()+"|"+g1.ReturnMe()+"|"+h1.ReturnMe()+"|\n")



def main(chessBoard):
    
    playerOne = players("1")
    playerTwo = players("2")
    playerStarting(playerOne,playerTwo)
    
    showBoard()
    
    gameStart(players, chessBoard)
    



a1 = Square("a1")
a2 = Square("a2")
a3 = Square("a3")
a4 = Square("a4")
a5 = Square("a5")
a6 = Square("a6")
a7 = Square("a7")
a8 = Square("a8")

b1 = Square("b1")
b2 = Square("b2")
b3 = Square("b3")
b4 = Square("b4")
b5 = Square("b5")
b6 = Square("b6")
b7 = Square("b7")
b8 = Square("b8")

c1 = Square("c1")
c2 = Square("c2")
c3 = Square("c3")
c4 = Square("c4")
c5 = Square("c5")
c6 = Square("c6")
c7 = Square("c7")
c8 = Square("c8")

d1 = Square("d1")
d2 = Square("d2")
d3 = Square("d3")
d4 = Square("d4")
d5 = Square("d5")
d6 = Square("d6")
d7 = Square("d7")
d8 = Square("d8")

e1 = Square("e1")
e2 = Square("e2")
e3 = Square("e3")
e4 = Square("e4")
e5 = Square("e5")
e6 = Square("e6")
e7 = Square("e7")
e8 = Square("e8")

f1 = Square("f1")
f2 = Square("f2")
f3 = Square("f3")
f4 = Square("f4")
f5 = Square("f5")
f6 = Square("f6")
f7 = Square("f7")
f8 = Square("f8")

g1 = Square("g1")
g2 = Square("g2")
g3 = Square("g3")
g4 = Square("g4")
g5 = Square("g5")
g6 = Square("g6")
g7 = Square("g7")
g8 = Square("g8")

h1 = Square("h1")
h2 = Square("h2")
h3 = Square("h3")
h4 = Square("h4")
h5 = Square("h5")
h6 = Square("h6")
h7 = Square("h7")
h8 = Square("h8")



rookWhite_a = Piece("Rook","White","Rw")
rookWhite_b = Piece("Rook","White","Rw")
knightWhite_a = Piece("Knight","White","Nw")
knightWhite_b = Piece("Knight","White","Nw")
bishopWhite_a = Piece("Bishop","White","Bw")
bishopWhite_b = Piece("Bishop","White","Bw")
kingWhite = King("King","White","Kw")
queenWhite = Piece("Queen","White","Qw")

pawnWhite_a = Piece("Pawn","White","Pw")
pawnWhite_b = Piece("Pawn","White","Pw")
pawnWhite_c = Piece("Pawn","White","Pw")
pawnWhite_d = Piece("Pawn","White","Pw")
pawnWhite_e = Piece("Pawn","White","Pw")
pawnWhite_f = Piece("Pawn","White","Pw")
pawnWhite_g = Piece("Pawn","White","Pw")
pawnWhite_h = Piece("Pawn","White","Pw")

rookBlack_a = Piece("Rook","Black","Rb")
rookBlack_b = Piece("Rook","Black","Rb")
knightBlack_a = Piece("Knight","Black","Nb")
knightBlack_b = Piece("Knight","Black","Nb")
bishopBlack_a = Piece("Bishop","Black","Bb")
bishopBlack_b = Piece("Bishop","Black","Bb")
kingBlack = King("King","Black","Kb")
queenBlack = Piece("Queen","Black","Qb")

pawnBlack_a = Piece("Pawn","Black","Pb")
pawnBlack_b = Piece("Pawn","Black","Pb")
pawnBlack_c = Piece("Pawn","Black","Pb")
pawnBlack_d = Piece("Pawn","Black","Pb")
pawnBlack_e = Piece("Pawn","Black","Pb")
pawnBlack_f = Piece("Pawn","Black","Pb")
pawnBlack_g = Piece("Pawn","Black","Pb")
pawnBlack_h = Piece("Pawn","Black","Pb")



a1.PutPiece(rookWhite_a)
b1.PutPiece(knightWhite_a)
c1.PutPiece(bishopWhite_a)
d1.PutPiece(kingWhite)
e1.PutPiece(queenWhite)
f1.PutPiece(bishopWhite_b)
g1.PutPiece(knightWhite_b)
h1.PutPiece(rookWhite_b)

a2.PutPiece(pawnWhite_a)
b2.PutPiece(pawnWhite_b)
c2.PutPiece(pawnWhite_c)
d2.PutPiece(pawnWhite_d)
e2.PutPiece(pawnWhite_e)
f2.PutPiece(pawnWhite_f)
g2.PutPiece(pawnWhite_g)
h2.PutPiece(pawnWhite_h)

a8.PutPiece(rookBlack_a)
b8.PutPiece(knightBlack_a)
c8.PutPiece(bishopBlack_a)
d8.PutPiece(kingBlack)
e8.PutPiece(queenBlack)
f8.PutPiece(bishopBlack_b)
g8.PutPiece(knightBlack_b)
h8.PutPiece(rookBlack_b)

a7.PutPiece(pawnBlack_a)
b7.PutPiece(pawnBlack_b)
c7.PutPiece(pawnBlack_c)
d7.PutPiece(pawnBlack_d)
e7.PutPiece(pawnBlack_e)
f7.PutPiece(pawnBlack_f)
g7.PutPiece(pawnBlack_g)
h7.PutPiece(pawnBlack_h)



chessBoard = [["a1",a1,1,1],["a2",a2,1,2],["a3",a3,1,3],["a4",a4,1,4],["a5",a5,1,5],["a6",a6,1,6],["a7",a7,1,7],["a8",a8,1,8],
              ["b1",b1,2,1],["b2",b2,2,2],["b3",b3,2,3],["b4",b4,2,4],["b5",b5,2,5],["b6",b6,2,6],["b7",b7,2,7],["b8",b8,2,8],
              ["c1",c1,3,1],["c2",c2,3,2],["c3",c3,3,3],["c4",c4,3,4],["c5",c5,3,5],["c6",c6,3,6],["c7",c7,3,7],["c8",c8,3,8],
              ["d1",d1,4,1],["d2",d2,4,2],["d3",d3,4,3],["d4",d4,4,4],["d5",d5,4,5],["d6",d6,4,6],["d7",d7,4,7],["d8",d8,4,8],
              ["e1",e1,5,1],["e2",e2,5,2],["e3",e3,5,3],["e4",e4,5,4],["e5",e5,5,5],["e6",e6,5,6],["e7",e7,5,7],["e8",e8,5,8],
              ["f1",f1,6,1],["f2",f2,6,2],["f3",f3,6,3],["f4",f4,6,4],["f5",f5,6,5],["f6",f6,6,6],["f7",f7,6,7],["f8",f8,6,8],
              ["g1",g1,7,1],["g2",g2,7,2],["g3",g3,7,3],["g4",g4,7,4],["g5",g5,7,5],["g6",g6,7,6],["g7",g7,7,7],["g8",g8,7,8],
              ["h1",h1,8,1],["h2",h2,8,2],["h3",h3,8,3],["h4",h4,8,4],["h5",h5,8,5],["h6",h6,8,6],["h7",h7,8,7],["h8",h8,8,8]]


main(chessBoard)
