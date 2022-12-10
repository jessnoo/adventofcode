# read input
# keep a record of the number of the elf with the most calories and report both

currentElfCalories = 0
currentElf = 1
maxCalories = 0
maxElf = 0
elfDictionary = {}
allCalories = []


with open('day1/input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

    for index, line in enumerate(lines):
        #print(line)
        if line.strip() == "":
            #print('new elf')
            if maxCalories < currentElfCalories:
                maxCalories = currentElfCalories
                maxElf = currentElf
            allCalories.append(currentElfCalories)
            currentElf += 1
            currentElfCalories = 0
            elfDictionary.update({currentElf: currentElfCalories})

        else:
            # print(type(line))
            calories = int(line)
            # print(type(calories))
            currentElfCalories = currentElfCalories + int(calories)

allCalories.sort(reverse=True)
topThreeCalories = allCalories[0] + allCalories[1] + allCalories[2]
print(len(allCalories))
print(allCalories)
print(topThreeCalories)

# print("Elf {} with {} calories").format(maxElf, maxCalories)
# print("last elf {} with {} calories").format(currentElf, currentElfCalories)
