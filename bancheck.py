import os
import sys

def read_file_to_list(filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, filename)) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def check_bans():
    bans = read_file_to_list('banlist.txt')
    deck = read_file_to_list('deck.txt')

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'comparison.txt'), 'w') as outputfile:
        for i in bans:
            if "#" != i[0]:
                for j in deck:
                    if i.lower() in j.lower():
                        print("Banned card \"%s\" detected as \"%s\"" % (i, j), file=outputfile)
            else:
                print(i, file=outputfile)
    print("Check complete")
    return 0

def main():
    check_bans()

main()