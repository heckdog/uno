# another quality program

# LATEST CHANGES:
# (12/13) reverses fixed but wont work in multiplayer. wildcards perfect.
#  skips and draw 2/4 don't work yet but the effect ID is there.
# TODO: see if you can fix above.
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

    bots = [[],[]]
    bot_names = bots[0]
    bot_decks = bots[1]
    # Setting Bot Decks
    for p in range(player_count):
        cards = []  # start with empty hand
        for i in range(7):
            card = deck.pop(0)
            cards.append(card)  # add card to hand
        # bots["Bot {}".format(p+1)] = cards  # adds new cards for bot
        bot_names.append("Bot {}".format(p+1))
        bot_decks.append(cards)

    # Setting User Deck
    cards = []
    for i in range(7):
        card = deck.pop(0)
        cards.append(card)  # add card to hand
    # cards.append("WILDCARD")
    # cards.append("RED REVERSE")  #TODO: remove lines adding reverse and wild
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
    card_choice = None
    wild = False
    wild_color = None
    valid = False
    reverse = False
    skip = False

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
        check = True
        while check:
            card_choice = input("Which card will you deploy? (type 'draw' to get a new card) \n>>>").strip().upper()
            if card_choice in player.hand or card_choice == "DRAW":
                check = False
            else:
                print("That's not a real card! Try again, or draw a card.")

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
                    skip = True
                    for i in range(4):
                        if deck:
                            bots[0][0].append(deck.pop(0))
                        else:
                            reshuffle(discard, deck)
                            bots[0][0].append(deck.pop(0))
                    # TODO: make the next player draw cards from deck.pop(0)
            # Other Cards
            else:
                split = card_choice.find(" ")
                card_color = card_choice[:split]
                card_number = card_choice[split + 1:]

                if card_number == "SKIP" and (card_color == current_color or card_number == current_number):
                    print("Skipped next player.")
                    skip = True
                    valid = True
                # TODO: the below isnt working.
                elif card_number == "REVERSE" and (card_color == current_color or card_number == current_number):
                    print("The order is reversed!")
                    if reverse:
                        reverse = False
                    else:
                        reverse = True
                    valid = True
                elif card_number == "DRAW 2" and (card_color == current_color or card_number == current_number):
                    print("The next player draws 2 cards!")
                    for i in range(2):
                        if deck:
                            bots[0][0].append(deck[-1])
                        else:
                            reshuffle(discard, deck)
                            bots[0][0].append(deck[-1])
                    skip = True
                    valid = True
                elif card_color == current_color:
                    print("Valid!")
                    valid = True
                elif card_number == current_number:
                    print("Valid!")
                    valid = True
                elif card_choice == "DRAW":
                    pass  # this is to avoid the below
                else:
                    print("{} don't work. gonna need a different card bub.".format(card_choice))
                    # TODO: make this draw a card.

        if valid:
            valid = False
            c_spot = player.hand.index(card_choice)
            used_card = player.hand.pop(c_spot)
            discard.append(used_card)

        if len(player.hand) == 0:
            active = False
            print("You win! Congratulations!")
            print(discard) # prints out entire game
            break
        elif len(player.hand) == 1:
            print("Uno!")

        # TODO: put this in the bot loop
        if reverse:
            bot_names = list(reversed(bot_names))
            bot_decks = list(reversed(bot_decks))
            reverse = False

        for bot in range(len(bot_names)):

            current_card = discard[-1]
            if wild:
                current_card = "WILDCARD"
            bot_cards = bot_decks[bot]
            bot_name = bot_names[bot]
            print("\nThe Card is {}".format(current_card))

            # Below is for drawing cards. Dont touch.
            pos = -1
            if range(len(bot_names))[-1] != bot:
                pos = 0
            # ok you can mess with things again

            if not skip:
                print("{}, what do you do?".format(bot_name))
                sleep(2)
                if len(bot_cards) > 0:
                    if len(bot_cards) == 1:
                        print("{} says: 'Uno!'".format(bot))

                    if wild:
                        bot_card, status, wild_color = use_card(current_card, bot_cards, discard, wild_color)
                        wild = False
                    else:
                        bot_card, status, wild_color = use_card(current_card, bot_cards, discard)
                    if bot_card is not None:
                        print("{} used {}.".format(bot_name, bot_card))
                        if status == "reverse":
                            reverse = True
                        elif status == "skip":
                            skip = True
                        elif status.find("wild") != -1:
                            wild = True
                        # ghetto solution
                        elif status == "draw 2":
                            # TODO: make this work for players.
                            for i in range(2):
                                if deck:
                                    bot_decks[bot+1].append(deck[pos])
                                else:
                                    reshuffle(discard, deck)
                                    bot_decks[bot+1].append(deck[pos])
                        # ahaha i doubt this will work
                        if status == "wild draw 4":
                            for i in range(4):
                                if deck:
                                    bots[0][bot+1].append(deck[pos])
                                else:
                                    reshuffle(discard, deck)
                                    bots[0][bot+1].append(deck[pos])


                        if len(bot_cards) == 0:  # if the bot has no cards left it wins
                            print("{} has won the game!".format(bot))
                            break
                    else:  # if nothing happens, draw a card
                        print("{} drew a card.".format(bot_name))
                        bots[bot].append(deck.pop(0))
                elif len(bot_cards) == 0:  # This shouldn't happen but if it does heres a solution
                    print("{} has won the game... but this text should never show up!".format(bot))
                    active = False
                    break
            else: # when skip != False
                skip = False
                print("{} was skipped!".format(bot_name))
            sleep(1)


# HEY: THIS LOOKS TERRIBLE IN EDITOR SOMETIMES BUT IT WORKS IN TERMINAL. DO NOT MESS WITH print_header().
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


# "reshuffle" probably will break and be sad for anyone in a long game :(
def reshuffle(discard, deck):
    for card in discard:
        if discard.index(card) != discard.index(discard[-1]):
            card = discard.pop(card)
            deck.append(card)


# TODO: make Player not be a class, but with the bots list, then rename bots to players.
# TODO: make sure player is only accessable by player.
class Player:
    def __init__(self, hand):
        self.hand = hand
        self.number = 1  # abosolutely redundant code.


def use_card(current_card, hand, pile, wild_color=None):
    # set up for card check
    split = current_card.find(" ")
    current_color = current_card[:split]
    current_number = current_card[split + 1:]
    status = "default"
    if wild_color:
        current_color = wild_color

    # card check
    for card in hand:
        split = card.find(" ")
        card_color = card[:split]
        card_number = card[split + 1:]

        if card == "WILDCARD" or card == "WILD +4":
            for color in ["BLUE", "RED", "GREEN", "YELLOW"]:
                if color in hand:  # TODO: make an "ai" for this? count cards before choosing? right now its just based on first card seen
                    card_color = color
                    wild_color = card_color
                else:
                    card_color = random.choice(["BLUE", "RED", "GREEN", "YELLOW"])  # rare occurance but still
                    wild_color = card_color
            print("Wildcard! New color is {}".format(card_color))
            if card == "WILD +4":
                print("The next player will ALSO draw 4 cards! Rekt!")
                status == "wild draw 4"
            return "WILDCARD", "wild", wild_color

        # the following just tell the event handler what happens in this function
        elif card_number == "SKIP" and (card_color == current_color or card_number == current_number):
            print("Skipped next player.")
            status = "skip"
            break
        elif card_number == "REVERSE" and (card_color == current_color or card_number == current_number):
            print("The order is reversed!")
            status = "reverse"
            break
        elif card_number == "DRAW 2" and (card_color == current_color or card_number == current_number):
            print("The next player draws 2 cards!")
            print("note, this dont do anything yet")
            status = "draw 2"
            break
        elif card_color == current_color:
            break
        elif card_number == current_number:
            break
        elif card == hand[-1]:
            return None, status, None

    wild_color = None
    pile.append(hand.pop(hand.index(card)))
    return card, status, wild_color


if __name__ == "__main__":
    main()
