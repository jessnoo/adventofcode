# part one - find the file size of the largest files
# $ cd / - go to root
# $ cd .. go up one directory
# $ cd {letter} go into that directory
# ls - list contents of current folder
# ###### lsdfjadsf.asdf - file info
# dir {letters} is a directory in the current directory
# not the answer ... 1311800

infile = 'in.txt'
#infile = 'inex.txt'

currentDir = ""
fileStuffs = {}

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for line in lines:
        line = line.replace("\n", "")

        if "$" in line:
            # navigating the directories
            commands = line.split(" ")
            print commands

            if commands[1] == "ls":
                print ""
            elif commands[2] == "/":
                # at the root
                currentDir = "root"
            elif commands[2] == "..":
                # move up a level
                if currentDir != "root":
                    dirParts = currentDir.split("-")
                    le = len(dirParts[-1]) + 1
                    currentDir = currentDir[:-le]
            elif commands[1] == "cd":
                # move down a level
                currentDir += "-" + commands[2]
                print "move down to ... {}".format(currentDir)

            # check if the current directory is in the list of possible directories - if it's not, then add it
            print currentDir
            if currentDir not in fileStuffs:
                fileStuffs[currentDir] = []

        elif line[0:3] == "dir":
            # there's a directory in the current directory
            print " "
        else:
            # got a file
            fileParts = line.split(" ")
            fileSize = int(fileParts[0])

            dirFiles = fileStuffs.get(currentDir)
            dirFiles.append(fileSize)
            fileStuffs.update({currentDir: dirFiles})

            # if that file isn't at the root, then it needs to be added to all the directories above it also ...
            tempDir = currentDir
            while True:
                if tempDir != "root":
                    dirParts = tempDir.split("-")
                    le = len(dirParts[-1]) + 1
                    tempDir = tempDir[:-le]

                    if tempDir in fileStuffs:
                        dirFiles = fileStuffs.get(tempDir)
                        dirFiles.append(fileSize)
                        fileStuffs.update({tempDir: dirFiles})
                    else:
                        fileStuffs[tempDir] = [fileSize]

                else:
                    break

# part one - find the total size of folders that are at most 100000

# part two ...
# total disk size ... 70000000
# need unused space of at least ... 30000000
# find one directory that create enough free space

allFilesSizes = fileStuffs.get("root")
allFilesSize = 0
for i in range(len(allFilesSizes)):
    allFilesSize += allFilesSizes[i]

print "All files on disk: {}".format(allFilesSizes)
currentFreeSpace = 70000000 - allFilesSize
spaceNeeds = 30000000 - currentFreeSpace
print "need to find smallest folder that's at least bigger than: {}".format(spaceNeeds)

totalSize = 0
currentPartTwo = allFilesSizes
fileLists = fileStuffs.values()
for fileList in fileLists:
    thisSize = 0

    for i in range(len(fileList)):
        thisSize += fileList[i]

    if thisSize < 100001:
        totalSize += thisSize
    if thisSize > spaceNeeds and thisSize < currentPartTwo:
        currentPartTwo = thisSize


print "done"
print fileStuffs
print "part one answer: {}".format(totalSize)
print "part two answer: {}".format(currentPartTwo)


