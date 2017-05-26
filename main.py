from players.player import Human
from players.color import Color
from board.board import Board

def main():
    white = Human(Color.WHITE)
    black = Human(Color.BLACK)

    Board(white, black)

if __name__ == "__main__":
    main()
    
