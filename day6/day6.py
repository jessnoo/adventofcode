# part one - look for the first instance of 4 unique characters

infile = 'in.txt'
#infile = 'inex.txt'

with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for line in lines:
        line = line.replace("/n", "")
        marker = 0
        startofMessage = 0
        print ""
        print "new line ... "
        for i in range(len(line)):
            #if the current plus next 3 are all unique - marker starts at the next index...
            7print "{} {}".format(i, line[i:(i+3)])
            curSet = set(line[i:(i+4)])
            if len(curSet) == 4:
                print "we found the marker! {}".format((i + 4))
                marker = (i + 4)

            curSet = set(line[i:(i + 14)])
            if len(curSet) == 14:
                print "we found the start of message {}".format((i + 14))
                startofMessage = i + 14

                break


