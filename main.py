#-------------------------------------------------------------------------------
# Name:        MR Bill
# Purpose:	   To calculate how much many each person should pay
#
# Author:      Arun Osborn
#
# Created:     20/09/2021
# Copyright:   (c) AOs Productions 2021 - 2022
# Version:	   0.4.0
#-------------------------------------------------------------------------------
import re

people = {}
billList = []
totalCost = 0

def loadBill():
    global people
    global totalCost
    global billList
    with open("bill.txt") as file:
        rawBill = file.readlines()

    people = {}
    billList = []
    aliases = {}
    totalCost = 0
    for line in rawBill:
        if line != "\n":
            if line[-1:] == "\n": # Removes new line characters
                line = line[:-1]
            item = re.split(" *(?:,|=) *",line)

            # Removes comments
            for x in range(len(item)):
                if "#" in item[x]:
                    item[x] = item[x][:item[x].index("#")]
            try:
                itemCost = eval(item[0])
                totalCost += itemCost  # Eval used so calculations can be done directly on the input
                billList.append(item)  # Processed bill (unused so far)
                expandedItem = [item[0]]  # Makes new item where aliases are changed to the individual people
                for x in range(1,len(item)):
                    if item[x] in aliases:  # If alias found, it must be split into separate people
                        for person in aliases[item[1]]:
                            expandedItem.append(person)
                    else:
                        expandedItem.append(item[x])
                item = expandedItem
                for x in range(1, len(item)):
                    if item[x] not in people:  # If person has been noted down before
                        people[item[x]] = {"total": 0, "items": []}
                    people[item[x]]["total"] += itemCost / (len(item) - 1)  # Adds money
                    people[item[x]]["items"].append(item)  # Adds item for reference
            except NameError:  # Value assumed to be an alias indicator
                aliases[item[0]] = item[1:]  # Adds dictionary about the alias to the list of aliases
            except SyntaxError as e:
                print(str(e) + "on line containing \""+line+"\"")

def displayTotals():
    for person in people:
        print(person+"'s Total: "+"£"+str(round(people[person]["total"],2)))

    print("--------------------")
    print("Grand Total: " +"£"+str(round(totalCost,4)))

def displayBill():
    for line in billList:
        formattedLine = line[0]
        for x in range(1,len(line)):
            formattedLine += "," + line[x]
        print(formattedLine)

loadBill()
displayTotals()
command = ""
while command!="exit":
    command = input("Command: ").lower()
    if "help" in command:
        print("Type \"Exit\" to quit the program")
        print("Type \"Totals\" to display the total again")
        print("Type \"Load\" to load the data from the bill.txt file")
    elif "total" in command:
        displayTotals()
    elif command == "load":
        loadBill()
        print("bill.txt was reloaded\n"
              "Type \"Totals\" to display the total again")
    elif command == "list":
        displayBill()
