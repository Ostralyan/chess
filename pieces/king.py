from pieces.piece import Piece


class King(Piece):
    def is_move_valid(self):
        return True

    def get_valid_moves(self):
        return True
