# Python Uno
It's a simple uno card game in Python. It's nothing special. Heck, as of writing this its nothing more than a virtual deck shuffler.

### LATEST UPDATES
older updates can be found in the [wiki](https://github.com/Heckin-Doggo/uno/wiki/Update-Log)

## update 5 (1/3)
* fixed card draw issue partially
* documented many new bugs

## update 6 (1/4)
* fixed many bugs from the day before
* drawing cards (WILD +4 and DRAW 2) work now, even on players
* got rid of bad code that broke a lot of things. dunno why it was even in there to begin with.

## update 7 (1/7)
* fixed wildcard spam for real this time

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
