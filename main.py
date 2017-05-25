from players.player import Human
from players.color import Color


def main():
    human = Human(Color.BLACK)

    for piece in human.available_pieces:
        print(piece)


if __name__ == "__main__":
    main()
