from players.player import Human
from players.color import Color


def main():
    human = Human(Color.BLACK)
    print(human.available_pieces)


if __name__ == "__main__":
    main()
