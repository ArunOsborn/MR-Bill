#-------------------------------------------------------------------------------
# Name:        MR Bill
# Purpose:	   To calculate how much many each person should pay
#
# Author:      Arun Osborn
#
# Created:     20/09/2021
# Copyright:   (c) AOs Productions 2021 - 2021
# Version:	   0.1.1
#-------------------------------------------------------------------------------
with open("bill.txt") as file:
    rawBill = file.readlines()

billList = []
people = {}
totalCost = 0
for line in rawBill:
    if line[-1:] == "\n": # Removes new line characters
        line = line[:-1]
    item = line.split(",")
    totalCost += float(item[0])
    billList.append(item) # Processed bill (unused so far)
    for x in range(1,len(item)):
        if item[x] not in people: # If person has been noted down before
            people[item[x]] = {"total": 0,"items": []}
        people[item[x]]["total"] += float(item[0])/(len(item)-1) # Adds money
        people[item[x]]["items"].append(item) # Adds item for reference

for person in people:
    print(person+"'s Total:"+"£"+str(round(people[person]["total"],2)))

print("--------------------")
print("Grand Total:" + str(totalCost))