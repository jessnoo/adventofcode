# part one - find the number of visible trees ...
# incorrect answers ... too high - 9469, 3334, 2942
infile = 'in.txt'
#infile = 'inex.txt'

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    width = len(lines[0].replace("\n", ""))
    height = len(lines)
    board = {"testing": "winging it"}
    print "height {} width {}".format(height, width)
    for x in range(width):
        for y in range(height):
            board[(x, y)] = ""

    curRow = 0
    for line in lines:
        for curCol in range(width):
            board.update({(curCol, curRow): line[curCol]})
        curRow += 1

    print "built map"
    # print board

# ok so for all the trees on the inside find the number of trees that aren't visible.
# a tree isn't visible if the horizontal and vertical trees from it are all larger
# it's not necessary to evaluate the first and last row and the first and last column
# board is (column, row) or (width, height)
invisibleTrees = 0
visibleTree = 0
maxScenicScore = 0

for x in range(width-1):
    if x > 0:
        for y in range(height-1):
            if y > 0:
                currentHeight = board.get((x, y))
                print "evaluate {}, {}: {}".format(x, y, currentHeight)

                # assume that the tree visible...
                leftVisible = True
                rightVisible = True
                upVisible = True
                downVisible = True

                leftVizTrees = 0
                rightVizTrees = 0
                upVizTrees = 0
                downVizTrees = 0

                # check horizontal left...
                #print "horizontal left"
                nextX = x
                while True:
                    nextX = nextX - 1
                    if board.get((nextX, y)):
                        thisHeight = board.get((nextX, y))
                        leftVizTrees += 1
                        #print "   {}, {}, {}".format(nextX, y, thisHeight)
                        if thisHeight >= currentHeight:
                            # at this point - any tree taller means this side is invisible
                            leftVisible = False
                            # print "   {}, {}, {}".format(nextX, y, thisHeight)
                            # print "      found a taller tree in this direction"
                            break
                    else:
                        # nothing else to check
                        break
                # check horizontal right...
                # print "horizontal right"
                nextX = x
                while True:
                    nextX = nextX + 1
                    if board.get((nextX, y)):
                        thisHeight = board.get((nextX, y))
                        rightVizTrees += 1
                        # print "   {}, {}, {}".format(nextX, y, thisHeight)
                        if thisHeight >= currentHeight:
                            # tree is invisible from this side can move on
                            rightVisible = False
                            # print "   {}, {}, {}".format(nextX, y, thisHeight)
                            # print "      found a taller tree in this direction"
                            break
                    else:
                        # nothing else to check
                        break
                # check vertical up ...
                #print "vertical up"
                nextY = y
                while True:
                    nextY = nextY + 1
                    if board.get((x, nextY)):
                        thisHeight = board.get((x, nextY))
                        upVizTrees += 1
                        #print "   {}, {}, {}".format(x, nextY, thisHeight)
                        if thisHeight >= currentHeight:
                            # tree is invisible from this direction can move on
                            upVisible = False
                            # print "   {}, {}, {}".format(x, nextY, thisHeight)
                            # print "      found a taller tree in this direction"
                            break
                    else:
                        # nothing else to check
                        break
                # check vertical down
                #print "vertical down"
                nextDoor = True
                nextY = y
                while True:
                    nextY = nextY - 1
                    if board.get((x, nextY)):
                        downVizTrees += 1
                        thisHeight = board.get((x, nextY))
                        #print "   {}, {}, {}".format(x, nextY, thisHeight)
                        if thisHeight >= currentHeight:
                            # tree is invisible can move on
                            downVisible = False
                            # print "   {}, {}, {}".format(x, nextY, thisHeight)
                            # print "      found a taller tree in this direction"
                            break
                    else:
                        # nothing else to check
                        break

                if not rightVisible and not leftVisible and not upVisible and not downVisible:
                    print "INVISIBLE TREE"
                    invisibleTrees += 1

                scenicScore = leftVizTrees * rightVizTrees * upVizTrees * downVizTrees
                if scenicScore > maxScenicScore:
                    maxScenicScore = scenicScore

# print invisibleTrees
allTrees = height*width
visibleTrees = allTrees - invisibleTrees
print "formula ... {} = {} - {}".format(visibleTrees, allTrees, invisibleTrees)
print "visible trees: {}".format(visibleTrees)
print "max scenic score: {}".format(maxScenicScore)

print "done"