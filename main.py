from players.player import Human
from players.color import Color
from board.board import Board
from board.coordinate import Coordinate

from pieces.piece import King


def main():
    white = Human(Color.WHITE)
    black = Human(Color.BLACK)
    board = Board(white, black)

    print(board)

    print(board.board[Coordinate.d8].is_on_board)
    print(board.board[Coordinate.e8].is_on_board)




if __name__ == "__main__":
    main()
