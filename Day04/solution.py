import fileinput
import re

INPUT_FILE = "input.in"
OUTPUT_FILE = "output.refout"
WINNING_RX = "(?<=: )(.*)(?= \|)"
HAND_RX = "(?<=\| )(.*)"

def getMatches(card):
    # TODO: move matching here
    return 0

def getPoints(card):
    winningCards = [i for i in re.findall(WINNING_RX, card)[0].split(" ") if i != ""]
    handCards = [i for i in re.findall(HAND_RX, card)[0].split(" ") if i != ""]
    matches = len([i for i in handCards if i in winningCards])
    if matches <= 1:
        return matches
    return 2 ** (matches - 1)

def getTotalCards(card, multiplier):
    return 0

def solve(input):
    points = 0
    cards = 0
    lines = fileinput.input(files=input)
    for line in lines:
        points += getPoints(line)

    return str(points), str(cards)

if __name__ == '__main__':
    f = open(OUTPUT_FILE, "w")
    solutions = solve(INPUT_FILE)
    f.write(solutions[0] + "\n" + solutions[1])