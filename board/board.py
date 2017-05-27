class Board():
    def __init__(self, white_player, black_player):
        self.board = {}
        for piece in white_player.available_pieces:
            self.board[piece.coordinate] = piece 
        for piece in black_player.available_pieces:
            self.board[piece.coordinate] = piece 
        print(self.board, "\n")
