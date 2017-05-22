from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, coordinate):
        self.coordinate = coordinate
        super(Piece, self).__init__()

    @abstractmethod
    def get_position(self):
        pass
