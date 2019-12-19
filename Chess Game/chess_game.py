#Beginner chess board program
#Date - 10/4/2019
#######BLACK#######
# R H B K Q B H R #
# P P P P P P P P #
#                 #
#                 #
#                 #
#                 #
# P P P P P P P P #
# R H B Q K B H R #
#######WHITE#######

from colorama import Fore, Back, Style
#class Chessboard that will be an 8x8 array that contains chess piece objects
class ChessBoard:
    def __init__(self):
        self.chessboard = self.createChessBoard()
        self.turn = None

    #initialize an 8x8 array to hold piece objects
    def createChessBoard(self):
        chessboard = [[None] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                #ROOK
                if (i == 0 or i == 7) and (j == 0 or j == 7):
                    if i == 0:
                        chessboard[i][j] = chessRook("rook", "white", (j, i))
                    else:
                        chessboard[i][j] = chessRook("rook", "black", (j, i))

                #KNIGHT
                elif (i == 0 or i == 7) and (j == 1 or j == 6):
                    if i == 0:
                        chessboard[i][j] = chessKnight("knight", "white", (j, i))
                    else:
                        chessboard[i][j] = chessKnight("knight", "black", (j, i))

                #BISHOP
                elif (i == 0 or i == 7) and (j == 2 or j == 5):
                    if i == 0:
                        chessboard[i][j] = chessBishop("bishop", "white", (j, i))
                    else:
                        chessboard[i][j] = chessBishop("bishop", "black", (j, i))

                #KING
                elif (i == 0 and j == 3) or (i == 7 and j == 4):
                    if i == 0:
                        chessboard[i][j] = chessKing("king", "white", (j, i))
                    else:
                        chessboard[i][j] = chessKing("king", "black", (j, i))

                #QUEEN
                elif (i == 0 and j == 4) or (i == 7 and j == 3):
                    if i == 0:
                        chessboard[i][j] = chessQueen("queen", "white", (j, i))
                    else:
                        chessboard[i][j] = chessQueen("queen", "black", (j, i))

                #PAWN
                elif i == 1 or i == 6:
                    if i == 1:
                        chessboard[i][j] = chessPawn("pawn", "white", (j, i))
                    else:
                        chessboard[i][j] = chessPawn("pawn", "black", (j, i))

                else:
                    chessboard[i][j] = ""
        return chessboard

    #Helper method to print state of chess board to terminal
    def printChessBoard(self):
        s = "        1          2          3          4" + \
            "          5          6          7          8      "
        print(Back.RED + Fore.BLACK + '\n\n\n' + s)

        i = 0
        y_axis = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H']
        for row in self.chessboard:
            print(Back.RED + Fore.BLACK + "   " + "-"*89)
            print(Back.RED + Fore.BLACK + y_axis[i] + " ", end="")
            for piece in row:

                if piece != "" and piece.side == "white":
                    print(Back.RED + Fore.BLACK + "| " +
                        Back.RED + Fore.WHITE + str(piece).center(8) \
                        + " ", end="")

                elif piece != "" and piece.side == "black":
                    print(Back.RED + Fore.BLACK + "| " + str(piece).center(8) \
                        + " ", end="")

                else:
                    print(Back.RED + Fore.BLACK + "| " + str(piece).center(8) \
                        + " ", end="")

            print(Back.RED + Fore.BLACK + "|")

            i += 1

        print(Back.RED + Fore.BLACK + "   " + "-"*89 + '\n\n')

    #method to detect if input is a valid location
    def validLocation(self, location: str) -> bool:
        #first check and make sure length is correct
        if len(location) != 2:
            return False

        #check if location is valid for (A1 -> H8)
        if location[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False
        elif location[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return False

        return True

    #method to convert location to coordinate, ie "A5" to (0,6)
    def convertLocation(self, location: str) -> tuple:
        #split string into x and y coordinate
        y = location[0]
        x = location[1]

        #grab lowercase and convert into index from 0 to 7
        y = ord(y.lower()) - 97
        x = int(x) - 1

        #return coordinate as tuple
        return (x,y)

    #method to return piece at specified location (x,y)
    def getPiece(self, location):
        return chessboard[location[1]][location[0]]

    #method to return whether move is legal or not
    def legalMove(self, start_loc: tuple, end_loc: tuple) -> bool:
        piece = getPiece(start_loc)
        return piece.move(end_loc)

#Class chessPiece is overall basic class for any piece that holds information on
#the type of piece, black or white side, and whether the piece is alive/taken
class chessPiece:
    def __init__(self, type=None, team=None, position=None):
        self.piece = type
        self.side = team
        self.life = True
        self.pos = position

    def __str__(self):
        return self.piece

    #returns the piece type
    def getType(self):
        return self.piece

    #returns the piece's state on the board
    def isAlive(self):
        return self.life

    def kill(self, otherLoc, board):
        x,y = self.pos
        otherPiece = board[otherLoc[1]][otherLoc[0]]

        #if no piece exists there
        if otherPiece == "":
            self.pos = (otherLoc[0], otherLoc[1])
            board[otherLoc[1]][otherLoc[0]] = self
            board[y][x] = ""

        elif otherPiece.side == self.side:
            return -1
            
        #take out the piece and set it as dead
        else:
            otherPiece.pos = (-1, -1)
            otherPiece.life = False
            self.pos = (otherLoc[0], otherLoc[1])
            board[otherLoc[1]][otherLoc[0]] = self
            board[y][x] = ""

        return

    def checkPieces(self, otherLoc, board):
        """
        checks if pieces exist between the selected pieces
        return true if none exist (move possible)
        """
        return self.checkPath(self.pos, otherLoc, board)

    def checkPath(self, start, end, board):

        #if we reached otherPiece, return true
        if start == end:
            return True

        if self.piece == "rook":
            if board[start[1]][start[0]] == "" or self.pos == start:
                #moving vertically
                if start[0] - end[0] == 0:
                    i = int((end[1] - start[1]) / abs(end[1] - start[1]))
                    return self.checkPath((start[0], start[1]+i), end, board)

                #moving horizontally
                elif start[1] - end[1] == 0:
                    i = int((end[0] - start[0]) / abs(end[0] - start[0]))
                    return self.checkPath((start[0]+i, start[1]), end, board)

        elif self.piece == "bishop":
            if board[start[1]][start[0]] == "" or self.pos == start:
                #four possible directions to move, NW NE SW SE
                i = int((end[0] - start[0]) / abs(end[0] - start[0]))
                j = int((end[1] - start[1]) / abs(end[1] - start[1]))
                return self.checkPath((start[0]+i, start[1]+j), end, board)

        return False


class chessPawn(chessPiece):
    def move(self, otherLoc, board):
        """
        Pawns can only move north/south depending on team/start point and
        diagonal if there is a piece that exist there it can take
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]
        #white is the top side
        if self.side == "white" and board.turn.lower() == "white":

            #piece is moving 1 down, take whatever is there
            if otherLoc[1]-y == 1:
                if otherLoc[0] == x:
                    if otherPiece == "":
                        #if pawn is not going to the bottom/change piece scenario
                        if y != 6:
                            self.kill(otherLoc, board.chessboard)
                            return 1

                        else:
                            #give user option for what piece to swap to
                            self.kill(otherLoc, board.chessboard)
                            board.chessboard[otherLoc[1]][otherLoc[0]] = self.swap()
                            return 1

                #diagonal move
                if otherLoc[0] == x-1 or otherLoc[0] == x+1:
                    if otherPiece != "":
                        if y != 6:
                            self.kill(otherLoc, board.chessboard)
                            return 1
                        else:
                            self.kill(otherLoc, board.chessboard)
                            board.chessboard[otherLoc[1]][otherLoc[0]] = self.swap()
                            return 1



            #piece is moving 2 down from its start position
            elif otherLoc[1]-y == 2 and y == 1 and otherLoc[0] == x:
                if otherPiece == "":
                    self.kill(otherLoc, board.chessboard)
                    return 1

        #choice is black move
        if self.side == "black" and board.turn.lower() == "black":
            if otherLoc[1]-y == -1:
                #piece is moving 1 up, take whatever is there
                if otherLoc[0] == x:
                    if otherPiece == "":
                        if y != 1:
                            #if pawn is not going to the top/change piece scenario
                            self.kill(otherLoc, board.chessboard)
                            return 1

                        else:
                            #give user option for what piece to swap to
                            self.kill(otherLoc, board.chessboard)
                            board.chessboard[otherLoc[1]][otherLoc[0]] = self.swap()
                            return 1


                #diagonal move
                if otherLoc[0] == x-1 or otherLoc[0] == x+1:
                    if otherPiece != "":
                        if y != 1:
                            self.kill(otherLoc, board.chessboard)
                            return 1

                        else:
                            self.kill(otherLoc, board.chessboard)
                            board.chessboard[otherLoc[1]][otherLoc[0]] = self.swap()
                            return 1

            #piece is moving 2 down from its start position
            elif otherLoc[1]-y == -2 and y == 6 and otherLoc[0] == x:
                if otherPiece == "":
                    self.kill(otherLoc, board.chessboard)
                    return 1

        return -1

    def swap(self):
        while True:
            choice = input("What piece should the pawn become? --> ").lower()
            if choice == "rook":
                return chessRook("rook", self.side, self.pos)
            elif choice == "knight":
                return chessKnight("knight", self.side, self.pos)
            elif choice == "bishop":
                return chessBishop("bishop", self.side, self.pos)
            elif choice == "queen":
                return chessQueen("queen", self.side, self.pos)
            elif choice == "pawn":
                return self
            else:
                print("Not an allowed choice.")
                continue

class chessRook(chessPiece):
    def move(self, otherLoc, board):
        """
        Rooks move horizontal or vertical
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]

        #check for matching sides
        if self.side == board.turn.lower():

            #check if direction of movement is parallel
            if otherLoc[0] - x == 0 or otherLoc[1] - y == 0:

                #check if pieces exist between location
                if self.checkPieces(otherLoc, board.chessboard):
                    self.kill(otherLoc, board.chessboard)
                    return 1
        return -1

class chessKnight(chessPiece):
    def move(self, otherLoc, board):
        """
        Knights move in L-shape, can hop over pieces and therefore no path check
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]

        #check for matching sides
        if self.side == board.turn.lower():

            #check if movement is an L-shape
            x_diff = abs(x-otherLoc[0])
            y_diff = abs(y-otherLoc[1])
            if (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):

                #valid move, kill the piece
                self.kill(otherLoc, board.chessboard)
                return 1

        return -1

class chessBishop(chessPiece):
    def move(self, otherLoc, board):
        """
        Bishops move diagonal, must path check
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]

        #check for matching sides
        if self.side == board.turn.lower():

            #check if movement is diagonal
            x_diff = abs(x-otherLoc[0])
            y_diff = abs(y-otherLoc[1])
            if x_diff == y_diff:

                #valid move, check path and kill if successful
                if self.checkPieces(otherLoc, board.chessboard):
                    self.kill(otherLoc, board.chessboard)
                    return 1

        return -1

class chessKing(chessPiece):
    def move(self, otherLoc, board):
        """
        King moves to 1 space away.
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]

        #check for matching sides
        if self.side == board.turn.lower():

            #check if movement is 1 away
            x_diff = abs(x-otherLoc[0])
            y_diff = abs(y-otherLoc[1])
            if (x_diff == 0 or x_diff == 1) and (y_diff == 0 or y_diff == 1):

                #valid move, kill piece
                self.kill(otherLoc, board.chessboard)
                return 1

        return -1

class chessQueen(chessPiece):
    def move(self, otherLoc, board):
        """
        Queen inherits bishop or rook movement skills
        Return true for a successful move, false if not
        """
        x,y = self.pos
        otherPiece = board.chessboard[otherLoc[1]][otherLoc[0]]

        #check for matching sides
        if self.side == board.turn.lower():

            x_diff = abs(x-otherLoc[0])
            y_diff = abs(y-otherLoc[1])

            #check if rook
            if x_diff == 0 or y_diff == 0:
                self.piece = "rook"

                #check if pieces exist between location, kill if successful
                if self.checkPieces(otherLoc, board.chessboard):
                    self.kill(otherLoc, board.chessboard)
                    self.piece = "queen"
                    return 1

            #check if bishop
            elif x_diff == y_diff:
                self.piece = "bishop"

                #check if pieces exist between location, kill if successful
                if self.checkPieces(otherLoc, board.chessboard):
                    self.kill(otherLoc, board.chessboard)
                    self.piece = "queen"
                    return 1

        return -1
