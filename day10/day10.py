# awlkejfalwekfaef
# ok so ---
# noop -- one cycle, nothing exciting happens
# addx # -- two cycles -- first cycle nothing - second cycle - then add the value to the register
# register starts at --
# signal strength = register * cycle
# keep track of cycles and signal strengths ...

# part two ...
# register is actually a three character 'sprite', center character is at register
# cycle relates to a pixel
# if the sprite is at the current cycle pixel, it draws, if not, it doesn't
# also - there are 6 rows of 40 pixels that the cycles related to...
# pixel positions - 0 - 39 -- each row + 40

infile = 'in.txt'
#infile = 'inex.txt'

signals = {}
pixels = {}
sprite = 1
cycle = 0
row = 1
pixelLoc = 0


def cyclestuff(addr):
    global cycle
    global sprite
    global signals
    global pixels
    global row
    global pixelLoc

    cycle += 1
    signals[cycle] = sprite * cycle

    #print cycle, sprite

    # figure out pixels...
    # basically - if the sprite is w/in + or - 1 of the cycle -- current cycle get's a #, otherwise .
    # but there's a row thing ...
    if sprite > (pixelLoc - 2) and sprite < (pixelLoc + 2):
        pixels[cycle] = "#"
    else:
        pixels[cycle] = "."

    pixelLoc += 1
    if pixelLoc == 40:
        row += 1
        pixelLoc = 0

    sprite += addr


with open(infile, 'r') as inputFile:
    lines = inputFile.readlines()

    for line in lines:
        instructions = line.replace("\n", "").split(" ")

        if instructions[0] == "noop":
            cyclestuff(0)

        else:
            cyclestuff(0)
            cyclestuff(int(instructions[1]))

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?

sumStrengths = signals.get(20) + signals.get(60) + signals.get(100) + signals.get(140) + signals.get(180) + signals.get(220)

print sumStrengths
print ""

# print the pixels ...
#print pixels

for row in range(6):
    pixelList = ""
    for pixel in range(40):
        cycle = pixel + 1 + (40 * row)
        pixelList += pixels.get(cycle)
    print pixelList


print "done"




