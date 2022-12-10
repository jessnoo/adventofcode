# part one - find pairs where one is contained by the other
# input looks like 1-3,4-5
# split - create set? find contains?
infile = 'in.txt'
#infile = 'inex.txt'
containedPairs = 0
overlappingPairs = 0

# PART ONE

def createSet(inSections):

    startSet = inSections.split("-")[0]
    endSet = inSections.split("-")[1]

    startNum = int(startSet)
    endNum = int(endSet)

    newSet = {startNum}

    while True:
        if startNum == endNum:
            break

        startNum += 1
        newSet.add(startNum)

    return newSet


with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for curPair in lines:

        elfOne = curPair.split(",")[0]
        elfTwo = curPair.split(",")[1]

        oneSet = createSet(elfOne)
        twoSet = createSet(elfTwo)

        if oneSet.issubset(twoSet):
            containedPairs += 1
        elif twoSet .issubset(oneSet):
            containedPairs += 1

        # PART TWO - test for any overlap in the pair
        overlap = oneSet.intersection(twoSet)
        if overlap:
            overlappingPairs += 1

print containedPairs
print overlappingPairs
