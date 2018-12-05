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
    except:
        print("Invalid. Setting Players to 2")
        player_count = 2
    # TODO: give each player (for player_count) 7 cards from deck

    bots = {}
    # Setting Bot Decks
    for p in range(player_count):
        cards = []  # start with empty hand
        for i in range(7):
            card = deck.pop(0)
            cards.append(card)  # add card to hand
        bots["Bot {}".format(p+1)] = cards  # adds new cards for bot

    # Setting User Deck
    cards = []
    for i in range(7):
        card = deck.pop(0)
        cards.append(card)  # add card to hand
    player = Player(cards)  # initialize with cards as deck, player+1 as number

    discard = []
    discard.append(deck.pop(0))
    # Anti Wildcard for the start card.
    check = True
    while check:
        if "WILDCARD" == discard[-1] or "WILD +4" == discard[-1]:
            discard.append(deck.pop)
        else:
            check = False

    # game variables initialized
    active = True
    wild = False
    wild_color = None
    valid = False
    reverse = False
    # game
    while active:
        print("\nThe current card is {}".format(discard[-1]))  # discard[-1] is the last added card.
        split = discard[-1].find(" ")
        current_color = discard[-1][:split]  # grabs color
        current_number = discard[-1][split + 1:]  # grabs number
        sleep(1)

        if wild:
            wild = False
            current_color = wild_color
            print("The Wild Card's color is {}".format(current_color))

        print("You have {} cards. They are:".format(len(player.hand)))
        for card in player.hand:
            print(card)
        card_choice = input("Which card will you deploy? (type 'draw' to get a new card) \n>>>").strip().upper()

        # CARD CHECK
        if card_choice == "DRAW":
            if deck:
                new_card = deck.pop(0)
                player.hand.append(new_card)  # grab top card from deck
                print("Drew a {}.".format(new_card))

            else:
                print("No more cards! Shuffling...")
                deck = discard[:-2]  # all but top card
                random.shuffle(deck)

        elif card_choice in player.hand:  # duh, gotta see if the card actually exists

            # Wildcard
            if card_choice == "WILDCARD" or card_choice == "WILD +4":
                print("Wild Card! What is the new Color?")
                # TODO: set the color
                wild = True
                check = True
                valid = True
                while check:
                    wild_color = input("[BLUE][YELLOW][RED][GREEN]\n>>>").lower().strip()

                    # set wild color
                    if wild_color == "blue" or wild_color == "red" or wild_color == "green" or wild_color == "yellow":
                        wild_color = wild_color.upper()
                        check = False
                    else:
                        print("That's not a color! Try again.")

                if card_choice == "WILD +4":
                    print("The Next player draws 4 cards!")
                    # TODO: make the next player draw cards from deck.pop(0)
            # Other Cards
            else:
                split = card_choice.find(" ")
                card_color = card_choice[:split]
                card_number = card_choice[split + 1:]

                if card_color == current_color:
                    print("Valid!")
                    valid = True
                elif card_number == current_number:
                    print("Valid!")
                    valid = True
                elif card_number == "SKIP" and (card_color == current_color or card_number == current_number):
                    print("Skipped next player.")
                    print("note: this dont do anything yet.")
                    valid = True
                elif card_number == "REVERSE" and (card_color == current_color or card_number == current_number):
                    print("The order is reversed!")
                    if reverse:
                        reverse = False
                    else:
                        reverse = True
                    valid = True
                elif card_number == "DRAW 2" and (card_color == current_color or card_number == current_number):
                    print("The next player draws 2 cards!")
                    print("note, this dont do anything yet")
                    valid = True
                elif card_choice == "DRAW":
                    pass  # this is to avoid the below
                else:
                    print("{} doesn't seem like a real card, bub".format(card_choice))

        if valid:
            valid = False
            c_spot = player.hand.index(card_choice)
            used_card = player.hand.pop(c_spot)
            discard.append(used_card)

        if len(player.hand) == 0:
            active = False
            print("You win! Congratulations!")
            break
        elif len(player.hand) == 1:
            print("Uno!")

        if not reverse:
            for bot in bots:
                current_card = discard[-1]
                bot_cards = bots[bot]
                print("\nThe Card is {}".format(current_card))
                print("{}, what do you do?".format(bot))
                sleep(2)

                if len(bot_cards) > 0:
                    if len(bot_cards) == 1:
                        print("{} says: 'Uno!'".format(bot))

                    bot_card = use_card(current_card, bot_cards, discard)
                    # TODO: check to see if the bot used a special card. make function called "card_check"
                    if bot_card is not None:
                        print("{} used {}.".format(bot, bot_card))
                        if len(bot) == 0:
                            print("{} has won the game!".format(bot))
                            break
                    else:
                        print("{} drew a card.".format(bot))
                        bots[bot].append(deck.pop(0))
                elif len(bot_cards) == 0:
                    print("{} has won the game!".format(bot))
                    active = False
                    break
                sleep(1)
        # TODO: make it a function or something to not have the same code twice after this else
        else:
            for bot in reversed(bots):
                current_card = discard[-1]
                bot_cards = bots[bot]
                print("\nThe Card is {}".format(current_card))
                print("{}, what do you do?".format(bot))
                sleep(1.5)

                if len(bot_cards) > 0:
                    if len(bot_cards) == 1:
                        print("{} says: 'Uno!'".format(bot))

                    bot_card = use_card(current_card, bot_cards, discard)
                    # TODO: check to see if the bot used a special card. make function called "card_check"
                    if bot_card is not None:
                        print("{} used {}.".format(bot, bot_card))
                        if len(bot_cards) == 0:
                            print("{} has won the game!".format(bot))
                            active = False
                            break
                    else:
                        print("{} drew a card.".format(bot))
                        bots[bot].append(deck.pop(0))
                elif len(bot_cards) == 0:
                    print("{} has won the game!".format(bot))
                    break
                sleep(1)




def print_header():
    print("----------------------------------")
    print(" ■■   ■■    ■■    ■■    ■■■■■■■■")
    print(" ■■   ■■    ■■■   ■■    ■■    ■■")
    print(" ■■   ■■    ■■■■  ■■    ■■    ■■")
    print(" ■■   ■■    ■■ ■■ ■■    ■■    ■■")
    print(" ■■   ■■    ■■  ■■■■    ■■    ■■")
    print(" ■■   ■■    ■■    ■■    ■■    ■■")
    print(" ■■■■■■■    ■■    ■■    ■■■■■■■■")
    print("----------------------------------")


# Deck Generation + Shuffling
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


def use_card(current_card, hand, pile):
    split = current_card.find(" ")
    current_color = current_card[:split]
    current_number = current_card[split + 1:]

    for card in hand:
        split = card.find(" ")
        card_color = card[:split]
        card_number = card[split + 1:]

        if card_number == "SKIP" and (card_color == current_color or card_number == current_number):
            print("Skipped next player.")
            print("note: this dont do anything yet.")
            break
        elif card_number == "REVERSE" and (card_color == current_color or card_number == current_number):
            print("The order is reversed!")
            break
        elif card_number == "DRAW 2" and (card_color == current_color or card_number == current_number):
            print("The next player draws 2 cards!")
            print("note, this dont do anything yet")
            break
        elif card_color == current_color:
            break
        elif card_number == current_number:
            break
        elif card == hand[-1]:
            return None

    pile.append(hand.pop(hand.index(card)))
    return card


if __name__ == "__main__":
    main()