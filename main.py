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

    king = King(Coordinate.e4, Color.WHITE)
    king.get_possible_moves()


if __name__ == "__main__":
    main()
