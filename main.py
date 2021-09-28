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
shared = {}
totalCost = 0

shared = {"shared":{"total": 0,"items": []}} # Sets the default indicator for shared items between everyone mentioned
for line in rawBill:
    if line[-1:] == "\n": # Removes new line characters
        line = line[:-1]
    item = line.split(",")
    if len(item) == 1: # Item of length one is read as a shared indicator to be used in future
        shared = {item[0]: shared[list(shared.keys())[0]]} # Renames shared user indicator
    else:
        totalCost += float(item[0])
        billList.append(item) # Processed bill (unused so far)
        for x in range(1,len(item)):
            #print(list(shared.keys())[0])
            if item[x] == list(shared.keys())[0]:
                shared[list(shared.keys())[0]]["total"] += float(item[0]) / (len(item) - 1)  # Adds money
                shared[list(shared.keys())[0]]["items"].append(item)  # Adds item for reference
            else:
                if item[x] not in people: # If person has been noted down before
                    people[item[x]] = {"total": 0,"items": []}
                people[item[x]]["total"] += float(item[0])/(len(item)-1) # Adds money
                people[item[x]]["items"].append(item) # Adds item for reference

for person in people:
    print(float(shared[list(shared.keys())[0]]["total"]) / (len(people)))
    people[item[x]]["total"] += float(shared[list(shared.keys())[0]]["total"]) / (len(people))  # Adds money
    people[item[x]]["items"].append(shared[list(shared.keys())[0]]["items"])  # Adds item for reference
    print(person+"'s Total:"+"£"+str(round(people[person]["total"],2)))
print(shared)

print("--------------------")
print("Grand Total:" + str(totalCost))