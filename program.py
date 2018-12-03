# another quality program

cards = ["1 RED"]


def main():
    print_header()


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


deck = []
# The below just creates the deck.
for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
    # Cards 0-9
    for i in range(10):
        deck.append(str(i) + " " + color)
    # Another set of 1-9
    for i in range(1,10):
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

for card in deck:
    print(card)




if __name__ == "__main__":
    main()