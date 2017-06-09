from players.player import Human
from players.color import Color
from board.board import Board
from board.coordinate import Coordinate

from pieces.piece import King, Pawn


def main():
    white = Human(Color.WHITE)
    black = Human(Color.BLACK)
    board = Board(white, black)

    print(board)

    # king = King(Coordinate.e1, Color.WHITE)
    # king.get_possible_moves()
    # print(king.get_possible_moves)

    pawn = Pawn(Coordinate.b2, Color.WHITE)
    pawn.get_possible_moves()
    print(pawn.get_possible_moves)

    print(board.board[Coordinate.a2].is_on_board)


if __name__ == "__main__":
    main()
