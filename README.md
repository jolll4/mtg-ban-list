
## How to check for conflicts

Store your list of banned cards as banlist.txt.

Copy-paste your deck into deck.txt

Run bancheck.py

The output will give all mentions of the names listed in banlist.txt by outputting the name of the banned card and the detected card in the checked deck.

## banlist.txt

The file should contain just the names of the cards, one for each row of the file.

To divide the banlist into segments use # as the first symbol of a line. These lines will be interpreted as a header and printed out for the user.

## deck.txt

From f.ex. deckstats.net or in cockatrice format (.cod-file)
