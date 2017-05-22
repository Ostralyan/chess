from pieces.piece import Piece


class Queen(Piece):
    def is_move_valid(self):
        raise NotImplementedError

    def get_valid_moves(self):
        raise NotImplementedError
