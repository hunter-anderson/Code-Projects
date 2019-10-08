#Beginner chess board program
#Date - 10/4/2019
###################
# R H B K Q B H R #
# P P P P P P P P #
#                 #
#                 #
#                 #
#                 #
# P P P P P P P P #
# R H B Q K B H R #
###################

#class Chessboard that will be an 8x8 array that contains chess piece objects
class ChessBoard:
    def __init__(self):
        self.chessboard = self.createChessBoard()

    def createChessBoard(self):
        #initialize 8x8 array of .
        return [['.']*8 for _ in range(8)]

    def printChessBoard(self):
        for row in self.chessboard:
            for piece in row:
                print(piece, end=" ")
            print()

class chessPiece:
    def __init__(self, type=None, team=None):
        self.piece = type
        self.side = team

    def getPiece(self):
