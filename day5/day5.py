# vertical varying sized lists first
# blank line
# move statements

infile = 'in.txt'
#infile = 'inex.txt'

numStacks = 0
rows = []
moves = []

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for line in lines:
        line = line.replace("\n", "")

        if "[" in line:
            rows.append(line)

        elif "move" in line:
            moves.append(line)

        elif line.replace(" ", "").isdigit():
            numStacks = int(line.replace(" ", "")[-1])

# there's basically 4 characters per item in a stack
stacks = []
rowList = []
maxItemCount = 0
for row in rows:
    # so we're going to create a list of lists.... i think ...
    curRowList = []
    for i in range(numStacks):
        curRowList.append(row[(i+1)*4-3])
    rowList.append(curRowList)
    print curRowList
    maxItemCount += 1

print numStacks
print maxItemCount
# print rowList

for i in range(numStacks):
    # now loop through and get the items for each stack and put those in a list
    curStack = []

    for j in range(maxItemCount):
        if rowList[j][i] != " ":
            curStack.append(rowList[j][i])
    stacks.append(curStack)

# ok now move stuff around ...
# move 1 from 2 to 1
# number to move, from stack, to stack ... and they come off the left side

#print len(stacks)
#print stacks

# for move in moves:
#
#     moveParts = move.split(" ")
#     numToMove = int(moveParts[1])
#     fromStack = int(moveParts[3]) - 1
#     toStack = int(moveParts[5]) - 1
#
# #    print "{} from {} to {}".format(numToMove, fromStack, toStack)
#
#     for i in range(numToMove):
#         curItem = stacks[fromStack].pop(0)
#         stacks[toStack].insert(0, curItem)
#
# topList = ""
#
# for stack in stacks:
#     topList += stack[0]
#
# print topList

# part two - when stuff is moved it stays in order

for move in moves:

    moveParts = move.split(" ")
    numToMove = int(moveParts[1])
    fromStack = int(moveParts[3]) - 1
    toStack = int(moveParts[5]) - 1

    print "{} from {} to {}".format(numToMove, fromStack, toStack)
    print stacks[fromStack]
    print stacks[toStack]

    items = stacks[fromStack][:(numToMove)]
    print items
    stacks[toStack][:0] = items

    print stacks[toStack]
    print stacks[fromStack]

    for i in range(numToMove):
        print 'pop'
        curItem = stacks[fromStack].pop(0)


topList = ""

for stack in stacks:
    topList += stack[0]

print topList