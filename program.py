# another quality program
import random
from time import sleep



def main():
    print_header()

    active = True

    while active:
        print("\nWelcome to Uno! Type your choice!")
        choice = input("[PLAY] [QUIT]\n>>>").strip().lower()
        # Play
        if choice == "play":
            game()
            # After the game
            choice = input("\nWould you like to play again? (y/n)\n>>>").strip().lower()
            if choice == "no" or choice == "n":
                print("Goodbye!")
                active = False
            elif choice == "yes" or choice == "y":
                print("")
        elif choice == "quit":
            print("Goodbye!")
            active = False
        else:
            print("'{}' not recognized. Please try again.".format(choice))


def game():
    deck = get_deck()

    player_count = input("How many players? (2-5) ")
    try:
        if int(player_count) <= 5 >= 2:  # the <= 5 >= 2 works as a double check.
            player_count = int(player_count)
            print("Valid!")
        else:
            print("Invalid, you get 2.")
            player_count = 2
    except TypeError:
        print("Invalid. Setting Players to 2")
        player_count = 2
    # TODO: give each player (for player_count) 7 cards from deck
    # Setting Bot Decks
    for p in range(player_count):
        cards = []  # start with empty hand
        for i in range(7):
            card = deck.pop(0)
            cards.append(card)  # add card to hand
        bot = Bot(cards, p+2)  # initialize with cards as deck, player+1 as number

    # Setting User Deck
    cards = []
    for i in range(7):
        card = deck.pop(0)
        cards.append(card)  # add card to hand
    player = Player(cards)  # initialize with cards as deck, player+1 as number

    discard = []
    discard.append(deck.pop(0))

    # game
    active = True
    while active:
        print("The current card is {}".format(discard[-1]))  # discard[-1] is the last added card.
        sleep(1)
        print("You have {} cards. They are:".format(len(player.hand)))
        for card in player.hand:
            print(card)
        card_choice = input("Which card will you deploy? (type in caps like shown above) \n>>>").strip()

        # CARD CHECK
        # Wildcard
        if card_choice[:4] == "WILD":
            print("Wild Card! What is the new Color?")
            print("note: this dont do anything yet")
            # TODO: set the color
            if card_choice == "WILD +4":
                print("The Next player draws 4 cards!")
                # TODO: make the next player draw cards from deck.pop(0)
        else:
            split = card_choice.find(" ")
            card_color = card_choice[:split]
            # TODO: compare to discard color (and check for wild color)


def print_header():
    print("--------------------------------------")
    print(" ■■   ■■    ■■    ■■     ■■■■■■■")
    print(" ■■   ■■    ■■■   ■■    ■■    ■■")
    print(" ■■   ■■    ■■■■  ■■    ■■    ■■")
    print(" ■■   ■■    ■■ ■■ ■■    ■■    ■■")
    print(" ■■   ■■    ■■  ■■■■    ■■    ■■")
    print(" ■■   ■■    ■■    ■■■    ■■    ■■")
    print(" ■■■■■■    ■■     ■■     ■■■■■■■")
    print("---------------------------------------")


def get_deck():
    deck = []
    # The below just creates the deck.
    for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
        # Cards 0-9
        for i in range(10):
            deck.append(color + " " + str(i))
        # Another set of 1-9
        for i in range(1, 10):
            deck.append(color + " " + str(i))
        # Action Cards
        deck.append(color + " REVERSE")
        deck.append(color + " REVERSE")
        deck.append(color + " SKIP")
        deck.append(color + " SKIP")
        deck.append(color + " DRAW 2")
        deck.append(color + " DRAW 2")

    # Wild Cards
    for i in range(4):
        deck.append("WILDCARD")
        deck.append("WILD +4")

    random.shuffle(deck)
    return deck

    # for card in deck:
    # print(card)


class Player:
    def __init__(self, hand):
        self.hand = hand
        self.number = 1


class Bot:
    def __init__(self, hand, number):
        self.hand = hand
        self.number = number


if __name__ == "__main__":
    main()
