from abc import ABC, abstractmethod
from pieces.piece import Pawn, Rook, Knight, Bishop, King, Queen
from board.coordinate import Coordinate


class Player(ABC):
    def __init__(self, color):
        self.color = color
        self.available_pieces = [
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Pawn(Coordinate.a1, color),
                Rook(Coordinate.a1, color),
                Rook(Coordinate.a1, color),
                Knight(Coordinate.a1, color),
                Knight(Coordinate.a1, color),
                Bishop(Coordinate.a1, color),
                Bishop(Coordinate.a1, color),
                King(Coordinate.a1, color),
                Queen(Coordinate.a1, color)
        ]

        print(King(Coordinate.a1, color))

        super(Player, self).__init__()

    @abstractmethod
    def move(self, piece, coordinate):
        pass


class Human(Player):
    def move(self, piece, coordinate):
        pass


class Computer(Player):
    pass
