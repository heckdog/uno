# Python Uno
It's a simple uno card game in Python. It's nothing special. Heck, as of writing this its nothing more than a virtual deck shuffler.

## update 1 (12/4)
you can now win against yourself. there are no bots yet and REVERSE, DRAW 2, and SKIP cards do nothing yet. WILDCARDS, however, do work.

## update 2 (12/5)
You can now play against 2 to 5 bots. That's all the customizability right now. You can also play the game and they can now win against you. DRAW 2/4, and SKIP still dont do anything, WILDCARDS still work, but are broken for the bots, and REVERSE cards *should* work, but I think they are still broken on the bots. Reverse code also inst that great. The end.

## update 3 (12/6-12/12)


* use_card() now returns tuples allowing for bots to use abilities such as skip and reverse and draw 2/4, as well as wild
* ~~**BROKEN** using a reverse card crashes the game.~~


## update 4 (12/13)
* fixed reverses and wildcards.
* drawing cards and skip cards still dont do anything, but can be used like a number card.
* *bug: reverses only apply to bots. you always go after the last bot, no matter what.*
~~* *possible bug: bot names dont appear when drawing cards.*~~


## update 5 (1/3)
* fixed card draw issue partially
* documented many new bugs

## update 6 (1/4)
* fixed many bugs from the day before
* drawing cards (WILD +4 and DRAW 2) work now, even on players
* got rid of bad code that broke a lot of things. dunno why it was even in there to begin with.
