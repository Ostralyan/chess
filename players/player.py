from abc import ABC, abstractmethod
from pieces.piece import Pawn, Rook, Knight, Bishop, King, Queen
from .color import Color
from board.coordinate import Coordinate


class Player(ABC):
    def __init__(self, color):
        self.color = color
        if color == Color.WHITE:
            self.available_pieces = [
                Pawn(Coordinate.a7, color),
                Pawn(Coordinate.b7, color),
                Pawn(Coordinate.c7, color),
                Pawn(Coordinate.d7, color),
                Pawn(Coordinate.e7, color),
                Pawn(Coordinate.f7, color),
                Pawn(Coordinate.g7, color),
                Pawn(Coordinate.h7, color),
                Rook(Coordinate.a7, color),
                Rook(Coordinate.h7, color),
                Knight(Coordinate.b8, color),
                Knight(Coordinate.g8, color),
                Bishop(Coordinate.c8, color),
                Bishop(Coordinate.f8, color),
                King(Coordinate.e8, color),
                Queen(Coordinate.d8, color)
            ]
        elif color == Color.BLACK:
            self.available_pieces = [
                Pawn(Coordinate.a2, color),
                Pawn(Coordinate.b2, color),
                Pawn(Coordinate.c2, color),
                Pawn(Coordinate.d2, color),
                Pawn(Coordinate.e2, color),
                Pawn(Coordinate.f2, color),
                Pawn(Coordinate.g2, color),
                Pawn(Coordinate.h2, color),
                Rook(Coordinate.a2, color),
                Rook(Coordinate.h2, color),
                Knight(Coordinate.b1, color),
                Knight(Coordinate.g1, color),
                Bishop(Coordinate.c1, color),
                Bishop(Coordinate.f1, color),
                King(Coordinate.e1, color),
                Queen(Coordinate.d1, color)
            ]

        super(Player, self).__init__()

    @abstractmethod
    def move(self, piece, coordinate):
        pass


class Human(Player):
    def move(self, piece, coordinate):
        pass


class Computer(Player):
    pass
