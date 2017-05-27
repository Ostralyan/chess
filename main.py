from players.player import Human
from players.color import Color
from board.board import Board
from board.coordinate import Coordinate


def main():
    white = Human(Color.WHITE)
    black = Human(Color.BLACK)
    board = Board(white, black)

    print(board)


if __name__ == "__main__":
    main()
