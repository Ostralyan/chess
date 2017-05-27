from .coordinate import Coordinate


class Board():
    def __init__(self, white_player, black_player):
        self.board = {}
        for piece in white_player.available_pieces + \
                black_player.available_pieces:
            self.board[piece.coordinate] = piece

    def __str__(self):
        result = ""
        for i, coord in enumerate(Coordinate):
            piece = self.board.get(coord, None)
            if i % 8 == 0:
                result += "\n"
            if piece is not None:
                result += str(piece) + " "
            else:
                result += "_ "
        return result
