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
        print("selfcoordvalue", self.coordinate.value)
        possible_moves.remove(self.coordinate)
        print(possible_moves)
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

    # Pawn unique starting move
    def is_starting_position(starting_coordinate):
        valid_start_coordinate = [(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)]
        if (starting_coordinate.value in valid_start_coordinate):
            # pass in coords from coord.Coord or numerical values work? diff?
            return True  # 16 checks for valid pawn starting positions

    def get_possible_moves(self):
        possible_moves = []
        starting_move = tuple(map(sum, zip(self.coordinate.value, (0, 2))))
        print("starting move", starting_move)
        # if pos is valid start pos, possible_moves.append starting_move
        if (self.is_on_board(starting_move) and
                self.is_starting_position(starting_move)):
            possible_moves.append(Coordinate(starting_move))
        # possible_moves.remove(self.coordinate)

        for x in range(-1, 2):
            for y in range(0, 2):
                possible_move = tuple(
                    map(sum, zip(self.coordinate.value, (x, y))))
                if (self.is_on_board(possible_move)):
                    possible_moves.append(Coordinate(possible_move))
        print("selfcoordvaluepawn", self.coordinate.value)
        possible_moves.remove(self.coordinate)
        print(possible_moves)
        return possible_moves

    def __str__(self):
        if self.color == Color.WHITE:
            return u'\u2659'
        elif self.color == Color.BLACK:
            return u'\u265F'
