# part one rules
# first letter is elf -- A : rock, B : paper, C : Scissors
# second letter is me -- X : rock, Y : paper, Z : Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# score is     my shape (1 for Rock, 2 for Paper, and 3 for Scissors)
#              + outcome (0 if you lost, 3 if the round was a draw, and 6 if you won)

shapeScore = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcomeScore = {
    "rock paper": 6,
    "rock scissors": 0,
    "scissors rock": 6,
    "scissors paper": 0,
    "paper rock": 0,
    "paper scissors": 6
}

shapeLU = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

myScore = 0
numMatches = 0

with open('day2input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

    for index, line in enumerate(lines):
        match = line.split(" ")
        print match
        numMatches += 1
        elf = shapeLU[match[0]]
        me = shapeLU[match[1].replace('\n', '')]

        if elf == me:
            myScore += shapeScore[me] + 3

        else:
            myScore += outcomeScore[elf + " " + me] + shapeScore[me]

print myScore
print numMatches

### part two
# X - lose, Y - draw, Z - win
print("PART TWO")
myScore = 0
numMatches = 0
outcomeLU = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
winShape = {
    "rock": "paper",
    "scissors": "rock",
    "paper": "scissors"
}
loseShape = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

with open('day2input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

    for index, line in enumerate(lines):
        match = line.split(" ")
        # print match
        numMatches += 1
        elf = shapeLU[match[0]]
        outcome = outcomeLU[match[1].replace('\n', '')]

        if outcome == 3:
            myScore += shapeScore[elf] + outcome

        elif outcome == 0:
            # i lost
            myScore += outcome + shapeScore[loseShape[elf]]

        else:
            # i won
            myScore += outcome + shapeScore[winShape[elf]]

print myScore
print numMatches