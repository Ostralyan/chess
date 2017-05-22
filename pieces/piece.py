from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, coordinate):
        self.coordinate = coordinate
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
