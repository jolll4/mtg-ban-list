
## How to check for conflicts

Store your list of banned cards as banlist.txt.

Copy-paste your deck into deck.txt

Run bancheck.py

The output (comparison.txt) will give all mentions of the names listed in banlist.txt by outputting the name of the banned card and the detected card in the checked deck. It is possible to get false matches from banned cards that have short names, such as "Opt" being detected in "Ornithopter".

## banlist.txt

The file should contain only the names of the cards, one for each row of the file.

To divide the banlist into segments use # as the first symbol of a line. These lines will be interpreted as a header and printed out for the user.

## deck.txt

From f.ex. deckstats.net. Put each card on their own row as the flagged entry will be given as the entire row regardless of all additional content written.
