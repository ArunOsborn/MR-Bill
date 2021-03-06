#-------------------------------------------------------------------------------
# Name:        MR Bill
# Purpose:	   To calculate how much many each person should pay
#
# Author:      Arun Osborn
#
# Created:     20/09/2021
# Copyright:   (c) AOs Productions 2021 - 2022
# Version:	   1.0.0
#-------------------------------------------------------------------------------
import re
import json
import requests

class Bill():

    def __init__(self,text=None,path=None):

        if text != None:
            self.rawBill = self.openString(text)
        elif path != None:
            self.rawBill = self.openText(path)
        else:
            print("Please enter a string or a path to a text file")
        self.processBill()

    def processBill(self):

        self.people = {}
        self.billList = []
        self.aliases = {}
        self.items = []
        self.totalCost = 0
        for line in self.rawBill:
            if len(line) > 1:
                if line[-1:] == "\n": # Removes new line characters
                    line = line[:-1]
                item = re.split(" *(?:,|=) *",line)

                # Removes comments
                for x in range(len(item)):
                    if "#" in item[x]:
                        item[x] = item[x][:item[x].index("#")]
                try:
                    itemCost = eval(item[0])
                    self.totalCost += itemCost  # Eval used so calculations can be done directly on the input
                    self.billList.append(item)  # Processed bill (unused so far)
                    expandedItem = [item[0]]  # Makes new item where aliases are changed to the individual people
                    for x in range(1,len(item)):
                        if item[x] in self.aliases:  # If alias found, it must be split into separate people
                            for person in self.aliases[item[1]]:
                                expandedItem.append(person)
                        else:
                            expandedItem.append(item[x])
                    item = expandedItem
                    self.items.append({"cost":item[0],"people":item[1:]})
                    for x in range(1, len(item)):
                        if item[x] not in self.people:  # If person has been noted down before
                            self.people[item[x]] = {"total": 0, "items": []}
                        self.people[item[x]]["total"] += itemCost / (len(item) - 1)  # Adds money
                        self.people[item[x]]["items"].append(len(self.items))  # Adds the last item in the list for reference
                except NameError:  # Value assumed to be an alias indicator
                    self.aliases[item[0]] = item[1:]  # Adds dictionary about the alias to the list of aliases
                except SyntaxError as e:
                    print(str(e) + "on line containing \""+line+"\"")
                    if line != "\n":
                        return None

    def getTotalsPrintout(self):
        def moneyFormat(amount):
            result = "??{:,.2f}".format(amount)
            return result
        printout= ""
        printout+="--------------------\n"
        for person in self.people:
            printout += person+"'s Total: "+moneyFormat(self.people[person]["total"]) + "\n"

        printout+="--------------------\n"
        printout += "Grand Total: " +moneyFormat(self.totalCost) + "\n"
        printout+="--------------------"
        return printout

    def getBillAsText(self):
        formattedBlock = ""
        for line in self.billList:
            formattedLine = line[0]
            for x in range(1,len(line)):
                formattedLine += "," + line[x]
            formattedBlock += formattedLine + "\n"
        return formattedBlock

    def openText(self,path):
        """Takes the path of the .txt file and returns the contents of the file as rawBill for processing"""
        print(path)
        if path.startswith("https"):
            file = requests.get(path).content
            print(type(file))
            print(file.decode())
            return self.openString(file.decode())
        else:
            with open(path) as file:
                rawBill = file.readlines()
        return rawBill

    def openString(self,string):
        """Takes string input of bill and returns rawBill for processing"""
        rawBill = string.split("\n")
        return rawBill

if __name__ == '__main__':
    # Displays bill.txt by default
    bill = Bill(path="bill.txt")
    print(bill.getTotalsPrintout())

    # Console
    command = ""
    while command!="exit":
        command = input("Command: ").lower()

        if "help" in command:
            print("Type \"Exit\" to quit the program")
            print("Type \"Totals\" to display the total again")
            print("Type \"Load\" to load the data from the bill.txt file")
            print("Type \"Input\" to load the inputted data after the command")
            print("Type \"Save\" to save the data as a json file. (This system currently can't read this format)")

        elif "total" in command:
            print(bill.getTotalsPrintout())

        elif command.startswith("load"):
            if command == "load":
                path = "bill.txt"
            else:
                path = command[len("load "):]
                if len(path)<4 or path[-4] != ".txt":
                    path += ".txt"
            bill = Bill(path=path)
            print(f"{path} was loaded\n"
                  "Type \"Totals\" to display the total again")

        elif command.startswith("input"):
            text = command[len("input "):]
            bill = Bill(text=text)
            print(f"{text} was loaded\n"
                  "Type \"Totals\" to display the total again")

        elif command == "list":
            print(bill.getBillAsText())

        elif command == "people":
            print(bill.people)

        elif command == "items":
            print(bill.items)

        elif command.startswith("save"):
            if command == "save":
                path = "bill-auto.json"
            else:
                path = command[len("save "):]
                if len(path)<5 or path[-5] != ".json":
                    path += ".json"

            save = {"people":bill.people,"items":bill.items}
            with open(path, "w", encoding='utf-8') as file:
                json.dump(save, file, indent=4)
            print(f"File saved as {path}")
