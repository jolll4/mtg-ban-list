
def open_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().lower() for line in lines]
    return lines

def check_bans():
    bans = open_file('banlist.txt')
    deck = open_file('deck.txt')
    for i in bans:
        if "#" != i[0]:
            for j in deck:
                if i in j:
                    print("Cardname", i, "detected in", j)
        else:
            print(i)
    print("Check complete")
    return 0

def main():
    check_bans()

main()