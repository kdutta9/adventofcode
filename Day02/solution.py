import fileinput
import re
from functools import reduce

INPUT_FILE = "input.in"
OUTPUT_FILE = "output.refout"
BAG = {"red": 12, "green": 13, "blue": 14}
ID_RX = "(?<=Game )(.*)(?=:)"
GAMES_RX = "(?<=: )(.*)"

def getValue(game):
    id = int(re.findall(ID_RX, game)[0])
    pulls = re.findall(GAMES_RX, game)[0].split("; ")
    maxColors = {"red": 0, "green": 0, "blue": 0}
    for pull in pulls:
        hand = {"red": 0, "green": 0, "blue": 0}
        groups = re.findall("(\d+) (red|green|blue)", pull)
        for group in groups:
            hand[group[1]] += int(group[0])
        for key in hand.keys():
            if hand[key] > BAG[key]:
                id = 0
            if hand[key] > maxColors[key]:
                maxColors[key] = hand[key]

    return id, reduce(lambda x, y: x*y, maxColors.values())

def solve(input):
    total = 0
    powers = 0

    for line in fileinput.input(files=input):
        total += getValue(line)[0]
        powers += getValue(line)[1]

    return str(total), str(powers)


if __name__ == '__main__':
    f = open(OUTPUT_FILE, "w")
    solutions = solve(INPUT_FILE)
    f.write(solutions[0] + "\n" + solutions[1])