# This Program is used to calculate the stats of players
# in the game MLB 9 Innings

# import modules
import math


# funcitons
def giFunction(distributionTotal, baseStat, baseTotal):
    return (baseStat - 40) / (baseTotal - 200) * distributionTotal


# function testing
# print(giFunction(200.0,41.0,0.0))

# introduction
print("Welcome to the MLB 9 Innings 21 GI Distribution Calculator")

# collecting data
baseStats = []
baseStats.append(float(input("Enter the base contact or location:\n")))
baseStats.append(float(input("Enter the base power or velocity:\n")))
baseStats.append(float(input("Enter the base eye or stamina:\n")))
baseStats.append(float(input("Enter the base speed or fastball:\n")))
baseStats.append(float(input("Enter the base field or breaking ball:\n")))
distributionTotal = float(
    input(
        "Please enter the total distribution you would like to calcualte for (60-90):\n"
    ))

# calculation
total = 0.0
for x in range(5):
    total = total + baseStats[x]

# distribution
distribution = []
for x in range(5):
    distribution.append(giFunction(distributionTotal, baseStats[x], total))

# round (flooring)
floorGi = []
for x in range(5):
    floorGi.append(math.floor(distribution[x]))

# determine left over GI
# total floored gi
floorTotal = 0
for x in range(5):
    floorTotal = floorTotal + floorGi[x]
# finding the difference
giDif = distributionTotal - floorTotal

# determine extra distribution order
tempFloorGi = list(floorGi)
indexOrder = []
for x in range(5):
    maxTemp = tempFloorGi[0]
    tempIndex = 0
    for x in range(len(tempFloorGi)):
        if maxTemp < tempFloorGi[x]:
            maxTemp = tempFloorGi[x]
            tempIndex = x
    indexOrder.append(tempIndex)
    tempFloorGi[tempIndex] = 0

# add extra distribution points
count = 0
while giDif > 0:
    floorGi[indexOrder[count]] = floorGi[indexOrder[count]] + 1
    count = count + 1
    giDif = giDif - 1
finalGi = floorGi

# Calculate final stat line
finalStat = []
for x in range(5):
    finalStat.append(int(baseStats[x]) + finalGi[x])

# print output
print("The GI distribution is:")
print(finalGi)

print("Final stat line is: ")
print(finalStat)
