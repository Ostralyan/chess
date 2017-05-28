from abc import ABC, abstractmethod
from players.color import Color
from board.coordinate import Coordinate


class Piece(ABC):
    def __init__(self, coordinate, color):
        self.coordinate = coordinate
        self.color = color
        super(Piece, self).__init__()

    @abstractmethod
    def is_move_valid(self, new_coordinate):
        pass

    @abstractmethod
    def get_possible_moves(self):
        pass

    def move(self, new_coordinate):
        if self.is_move_valid():
            self.coordinate = new_coordinate
            print('I have moved')

    @staticmethod
    def is_on_board(possible_move):
        return (possible_move[0] > 0 and possible_move[0] < 9) and \
                (possible_move[1] > 0 and possible_move[1] < 9)


class King(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_possible_moves(self):
        possible_moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                possible_move = tuple(
                        map(sum, zip(self.coordinate.value, (x, y))))
                if (self.is_on_board(possible_move)):
                    possible_moves.append(Coordinate(possible_move))
        possible_moves.remove(self.coordinate)
        return possible_moves

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2654'
        elif self.color == Color.BLACK:
            return u'\u265A'


class Queen(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_possible_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2655'
        elif self.color == Color.BLACK:
            return u'\u265B'


class Rook(Piece):
    def is_move_valid(self):
        return True

    def get_possible_moves(self):
        return True

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2656'
        elif self.color == Color.BLACK:
            return u'\u265C'


class Knight(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_possible_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2658'
        elif self.color == Color.BLACK:
            return u'\u265E'


class Bishop(Piece):
    def is_move_valid():
        raise NotImplementedError

    def get_possible_moves():
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2657'
        elif self.color == Color.BLACK:
            return u'\u265D'


class Pawn(Piece):
    def is_move_valid(self):
        return True

    def get_possible_moves(self):
        raise NotImplementedError

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2659'
        elif self.color == Color.BLACK:
            return u'\u265F'


