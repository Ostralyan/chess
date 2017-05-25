from abc import ABC, abstractmethod
from players.color import Color


class Piece(ABC):
    def __init__(self, coordinate, color):
        self.coordinate = coordinate
        self.color = color
        super(Piece, self).__init__()

    @abstractmethod
    def is_move_valid(self, new_coordinate):
        pass

    @abstractmethod
    def get_valid_moves(self):
        pass

    def move(self, new_coordinate):
        if self.is_move_valid():
            self.coordinate = new_coordinate
            print('I have moved')


class King(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_valid_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2654'
        elif self.color == Color.BLACK:
            return u'\u265A'


class Queen(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_valid_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2655'
        elif self.color == Color.BLACK:
            return u'\u265B'


class Rook(Piece):
    def is_move_valid(self):
        return True

    def get_valid_moves(self):
        return True

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2656'
        elif self.color == Color.BLACK:
            return u'\u265C'


class Knight(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_valid_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2658'
        elif self.color == Color.BLACK:
            return u'\u265E'


class Bishop(Piece):
    def is_move_valid():
        raise NotImplementedError

    def get_valid_moves():
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2657'
        elif self.color == Color.BLACK:
            return u'\u265D'


class Pawn(Piece):
    def is_move_valid(self):
        return True

    def get_valid_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2659'
        elif self.color == Color.BLACK:
            return u'\u265F'


