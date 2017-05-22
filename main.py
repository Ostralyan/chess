from pieces.pawn import Pawn
from board.coordinate import Coordinate


def main():
    pawn = Pawn(Coordinate.a1)
    pawn.move(Coordinate.a1)


if __name__ == "__main__":
    main()
