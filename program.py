# another quality program
import random

cards = ["1 RED"]


def main():
    print_header()
    deck = get_deck()
    for card in deck:
        print(card)


def print_header():
    print("------------------------------")
    print(" /$$   /$$ /$$   /$$  /$$$$$$ ")
    print("| $$  | $$| $$$ | $$ /$$__  $$")
    print("| $$  | $$| $$$$| $$| $$  \ $$")
    print("| $$  | $$| $$ $$ $$| $$  | $$")
    print("| $$  | $$| $$  $$$$| $$  | $$")
    print("| $$  | $$| $$\  $$$| $$  | $$")
    print("|  $$$$$$/| $$ \  $$|  $$$$$$/")
    print(" \______/ |__/  \__/ \______/ ")
    print("------------------------------")


def get_deck():
    deck = []
    # The below just creates the deck.
    for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
        # Cards 0-9
        for i in range(10):
            deck.append(str(i) + " " + color)
        # Another set of 1-9
        for i in range(1, 10):
            deck.append(str(i) + " " + color)
        # Action Cards
        deck.append("REVERSE " + color)
        deck.append("REVERSE " + color)
        deck.append("SKIP " + color)
        deck.append("SKIP " + color)
        deck.append("DRAW 2 " + color)
        deck.append("DRAW 2 " + color)

    # Wild Cards
    for i in range(4):
        deck.append("WILDCARD")
        deck.append("WILD +4")

    random.shuffle(deck)
    return deck

    # for card in deck:
    # print(card)


if __name__ == "__main__":
    main()