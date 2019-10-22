"""
Name: Hunter Anderson
Version: 1.0.0
Description: Simple game of chess played through the command-line interface
"""

import chess_game

def getUserInput(board, move):
    """
    Return -1 for quit, 0 for failed input, and entry if pass
    """
    if move.lower() == "quit":
        return -1

    entry = move.replace(" ", "").split(',')
    if not board.validLocation(entry[0]) or not board.validLocation(entry[1]):
        print("Invalid input")
        return 0

    start = board.convertLocation(entry[0])
    start = board.chessboard[start[1]][start[0]]
    if start == "":
        print("Invalid input")
        return 0
    elif entry[0] == entry[1]:
        print("invalid input")
        return 0

    return entry



def main():
    board = chess_game.ChessBoard()

    #white gets to go first
    turn = ["White", "Black"]
    turn_bit = 0
    board.turn = turn[turn_bit]
    move = ""
    board.printChessBoard()

    while True:
        move = input(turn[turn_bit] + " move(ex: A1, B1) --> ")
        entry = getUserInput(board, move)

        if entry == -1:
            break
        elif entry == 0:
            continue
        else:
            start = board.convertLocation(entry[0])
            start = board.chessboard[start[1]][start[0]]
            end = board.convertLocation(entry[1])

            #if move cannot be made, retry
            if start.move(end, board) != 1:
                print("Move cannot be made")
                continue

            turn_bit ^= 1
            board.turn = turn[turn_bit]
            board.printChessBoard()

    print("\nGoodbye!\n")
    return

if __name__ == "__main__":
    main()
