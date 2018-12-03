# another quality program
import random


def main():
    print_header()
    deck = get_deck()
    # for card in deck:
    #     print(card)
    player_count = input("How many players? (2-5) ")
    try:
        if int(player_count) <= 5 and int(player_count) >= 2:
            print("Valid!")
        else:
            print("Invalid, you get 2.")
            player_count = 2
    except TypeError:
        print("Invalid. Setting Players to 2")
        player_count = 2
    # TODO: give each player (for player_count) 7 cards from deck


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