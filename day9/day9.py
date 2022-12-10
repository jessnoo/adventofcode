# why did i get myself into this obsession
# part one correct answer - 6464
# part two - 7424, 6522 is too high
infile = 'in.txt'
#infile = 'inex.txt'

tailPositions = ["0,0"]
knots = []
numberKnots = 10


def moveknot(movedir, hx, hy, tx, ty, movehead):

    # basically -- the logic for just one move - manage step counts, etc outside of this ...
    # get new head position
    if movehead:
        if movedir == "R":
            hx += 1
        elif movedir == "L":
            hx -= 1
        elif movedir == "U":
            hy += 1
        else:
            hy -= 1

    # scenarios
    # same column
    if tx == hx:
        if abs(hy - ty) > 1:
            if hy > ty:
                ty += 1
            elif ty > hy:
                ty -= 1
    # same row
    elif ty == hy:
        if abs(hx - tx) > 1:
            if hx > tx:
                tx += 1
            elif tx > hx:
                tx -= 1

    # diff column and row
    else:
        # need to move tail one step in both directions
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            if hx > tx:
                tx += 1
            elif tx > hx:
                tx -= 1

            if hy > ty:
                ty += 1
            elif ty > hy:
                ty -= 1

    print "     new positions .. {}, {}  {}, {}".format(hx, hy, tx, ty)
    return hx, hy, tx, ty


# set up knot array ...
for i in range(numberKnots):
    knots.append([0, 0])

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    # ok so basically -- we start at 0, 0 and then move around the board based on the inputs.
    # i think the size of the board is not known or maybe it is but i don't know if it matters yet
    # need to keep track of ...
    #     head position
    #     tail position
    #     unique tail positions - just need count but keep the list
    # the head moves and the tail follows ...
    # have to go one step at a time ...asdfkjawerjal;sdkmasd
    for line in lines:
        direction, amount = line.replace("\n", "").split(" ")
        print "GO: {} {}".format(direction, amount)
        print knots
        takeStep = True

        trackTail = False
        step = 1
        while takeStep:
            # move the knots
            moveHead = True
            for i in range(numberKnots - 1):

                thisTail = i + 1
                print ("step: {}  ----  lead knot: {}  ----  in positions {}, {}   {}, {}".format(step, i, knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1]))
                curHX = knots[i][0]
                curHY = knots[i][1]
                curTX = knots[thisTail][0]
                curTY = knots[thisTail][1]
                newHX, newHY, newTX, newTY = moveknot(direction, curHX, curHY, curTX, curTY, moveHead)
                knots[i][0] = newHX
                knots[i][1] = newHY
                knots[thisTail][0] = newTX
                knots[thisTail][1] = newTY

                if i == 0:
                    moveHead = False

                if thisTail == numberKnots - 1:
                    tailPosition = "{},{}".format(knots[thisTail][0], knots[thisTail][1])
                    print "track tail {}".format(tailPosition)
                    if tailPosition not in tailPositions:
                        tailPositions.append(tailPosition)

            step += 1

            if step > int(amount):
                takeStep = False
        print knots

print "done"
#print tailPositions
print len(tailPositions)
