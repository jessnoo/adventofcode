# read line
# split in half
# find common item
# score it - add it to total


import string
from itertools import islice

infile = 'day3input.txt'
#infile = 'day3examplein.txt'
prioritySum = 0

# PART ONE

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for index, line in enumerate(lines):
        compartmentOne, compartmentTwo = line[:len(line) / 2], line[len(line) / 2:]

        oneSet = set(compartmentOne)
        twoSet = set(compartmentTwo)

        if oneSet & twoSet:
            commonSet = oneSet & twoSet

            commonItem = next(iter(commonSet))
            itemValue = "abcdefghijklmnopqrstuvwxyz".index(commonItem.lower()) + 1

            if commonItem.isupper():
                prioritySum += itemValue + 26
            else:
                prioritySum += itemValue
        else:
            print("no common elements")

print prioritySum

# PART TWO
# look at groups of three elves...
groupPriority = 0

with open(infile, 'r') as inputFile:
    while True:
        firstElf = inputFile.readline()
        if not firstElf: break
        secondElf = inputFile.readline()
        thirdElf = inputFile.readline()

        firstSet = set(firstElf.replace('\n', ''))
        secondSet = set(secondElf.replace('\n', ''))
        thirdSet = set(thirdElf.replace('\n', ''))

        if firstSet & secondSet & thirdSet:
            commonSet = firstSet & secondSet & thirdSet
            commonItem = next(iter(commonSet))
            print(commonItem)

            itemValue = "abcdefghijklmnopqrstuvwxyz".index(commonItem.lower()) + 1

            if commonItem.isupper():
                groupPriority += itemValue + 26
            else:
                groupPriority += itemValue

print groupPriority
