import random

from king_class import King



def players(number):
    player = input("Player", number, "Name: ")
    return player

def playerStarting(playerOne, playerTwo):
    randInt = random.randint(0,1)
    if randInt == 0:
        print(playerOne, "is white,\n", playerTwo, "is black.")
        white = playerOne
    else:
        print(playerOne, "is black,\n", playerTwo, "is white.")
        white = playerTwo
    
    
    print(white, "is white and therefore starts, good luck! :^)")


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

                        dstSqr[1].putPiece(srcSqr[1].piece)

                        srcSqr[1].clear()




def main():
    
    
    
    chessBoard = [["a1",a1],["a2",a2],["a3",a3],["a4",a4],["a5",a5],["a6",a6],["a7",a7],["a8",a8],
                  ["b1",b1],["b2",b2],["b3",b3],["b4",b4],["b5",b5],["b6",b6],["b7",b7],["b8",b8],
                  ["c1",c1],["c2",c2],["c3",c3],["c4",c4],["c5",c5],["c6",c6],["c7",c7],["c8",c8],
                  ["d1",d1],["d2",d2],["d3",d3],["d4",d4],["d5",d5],["d6",d6],["d7",d7],["d8",d8],
                  ["e1",e1],["e2",e2],["e3",e3],["e4",e4],["e5",e5],["e6",e6],["e7",e7],["e8",e8],
                  ["f1",f1],["f2",f2],["f3",f3],["f4",f4],["f5",f5],["f6",f6],["f7",f7],["f8",f8],
                  ["g1",g1],["g2",g2],["g3",g3],["g4",g4],["g5",g5],["g6",g6],["g7",g7],["g8",g8],
                  ["h1",h1],["h2",h2],["h3",h3],["h4",h4],["h5",h5],["h6",h6],["h7",h7],["h8",h8]]
    
    playerOne = players("1")
    playerTwo = players("2")
    playerStarting(playerOne,playerTwo)
    
    gameStart(players, chessBoard)
    
    
main()






from piece_class import Piece
from square_class import Square

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
kingWhite = Piece("King","White","Kw")
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
kingBlack = Piece("King","Black","Kb")
queenBlack = Piece("Queen","Black","Qb")

pawnBlack_a = Piece("Pawn","Black","Pb")
pawnBlack_b = Piece("Pawn","Black","Pb")
pawnBlack_c = Piece("Pawn","Black","Pb")
pawnBlack_d = Piece("Pawn","Black","Pb")
pawnBlack_e = Piece("Pawn","Black","Pb")
pawnBlack_f = Piece("Pawn","Black","Pb")
pawnBlack_g = Piece("Pawn","Black","Pb")
pawnBlack_h = Piece("Pawn","Black","Pb")



a1.putPiece(rookWhite_a)
b1.putPiece(knightWhite_a)
c1.putPiece(bishopWhite_a)
d1.putPiece(kingWhite)
e1.putPiece(queenWhite)
f1.putPiece(bishopWhite_b)
g1.putPiece(knightWhite_b)
h1.putPiece(rookWhite_b)

a2.putPiece(pawnWhite_a)
b2.putPiece(pawnWhite_b)
c2.putPiece(pawnWhite_c)
d2.putPiece(pawnWhite_d)
e2.putPiece(pawnWhite_e)
f2.putPiece(pawnWhite_f)
g2.putPiece(pawnWhite_g)
h2.putPiece(pawnWhite_h)

a8.putPiece(rookBlack_a)
b8.putPiece(knightBlack_a)
c8.putPiece(bishopBlack_a)
d8.putPiece(kingBlack)
e8.putPiece(queenBlack)
f8.putPiece(bishopBlack_b)
g8.putPiece(knightBlack_b)
h8.putPiece(rookBlack_b)

a7.putPiece(pawnBlack_a)
b7.putPiece(pawnBlack_b)
c7.putPiece(pawnBlack_c)
d7.putPiece(pawnBlack_d)
e7.putPiece(pawnBlack_e)
f7.putPiece(pawnBlack_f)
g7.putPiece(pawnBlack_g)
h7.putPiece(pawnBlack_h)