from pieces.pawn import Pawn
from coordinate import Coordinate


def main():
    pawn = Pawn(Coordinate.A1)
    pawn.move(Coordinate.A1)


if __name__ == "__main__":
    main()
