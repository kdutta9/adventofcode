import fileinput
import re

INPUT_FILE = "input.in"
OUTPUT_FILE = "output.refout"
DIGITS = {
    "one": 1, "two": 2, "three": 3, 
    "four": 4, "five": 5, "six": 6, 
    "seven": 7, "eight": 8, "nine": 9
    }

def getValue(line, rx):
    num1, num2 = re.findall(rx, line)[0], re.findall(rx, line)[-1]
    return (int(DIGITS.get(num1, num1)) * 10) + int(DIGITS.get(num2, num2))

def getTotal(input):
    total1 = 0
    total2 = 0

    for line in fileinput.input(files=input):
        total1 += getValue(line, "\d")
        total2 += getValue(line, "(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

    return str(total1), str(total2)


if __name__ == '__main__':
    f = open(OUTPUT_FILE, "w")
    f.write(getTotal(INPUT_FILE)[0] + "\n" + getTotal(INPUT_FILE)[1])