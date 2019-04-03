# Python Uno
It's a simple uno card game in Python. ~~It's nothing special. Heck, as of writing this its nothing more than a virtual deck shuffler.~~ Now its a card shuffler with cards that do things and if ur thing supports ANSI you also have colorful cards.

### LATEST UPDATES
older updates can be found in the [wiki](https://github.com/Heckin-Doggo/uno/wiki/Update-Log)

## update 8 (1/11)
* added colors to title and debug.
* added options menu. supports color and debug toggle. doesn't truly save, however. thats a whole lotta work for nothing
* added colors to the cards for readability
* removed `wild` variable, which caused at least 3 issues.
* data dump added. call it by saying `data dump` in the car selection screen
* `colorize(text, color)` added

## update 9 (1/11) 
ok so firstly, today was a good day like god damn i killed 5 bugs today AND added features like thats badass
anyways:
* added colorama to hopefully fix any issues with windows coloring
* added colorama failsafe because i haven't added it to venv yet.
* fixed that random crashing bug when starting a game. i forgot a `(0)` after `deck.pop`

## update 10 (1/17)
* fixed player limits. no more playing against yourself
* fixed bot names showing up as "0 drew a card" on certain occasions

## update 11 (4/3)
* updated README.md just to announce that this game is a lost cause. it functions alright but i dont give enough of a crap about it to continue with it. if i make any other change to python uno it will be in a new repo and completely redone.
