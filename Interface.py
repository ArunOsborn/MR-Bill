# The interface plugin for MR Bill
import tkinter as t

def launch(people):
    #updateData(people)

    width = "1200"
    height = "660"

    window = t.Tk()
    window.title("MR Bill GUI")
    window.geometry(width + "x" + height)
    window.config(bg="#123456")
    window.grid_anchor(t.N)

    # Container for output
    mainFrame = t.Frame(window, bg="BROWN", width=200, cursor="dotbox")
    mainFrame.pack(fill=t.BOTH, expand=1)

    inputScreen = t.Canvas(mainFrame, bg="#a5424a", width=200)
    inputScreen.pack(side=t.LEFT, fill=t.BOTH, expand=1)

    outputScreen = t.Canvas(mainFrame, bg="#35424a", width=200)
    outputScreen.pack(side=t.RIGHT, fill=t.BOTH, expand=1)


    window.mainloop()

def updateData(people):
    pass

if __name__ == '__main__':
    people = {'a': {'total': 1.0833333333333333, 'items': [['1', 'a', 'l', 'c'], ['1.5', 'c', 'a']]}, 'l': {'total': 6.5633333333333335, 'items': [['1', 'a', 'l', 'c'], ['2.7', 'l', 'c'], ['2', '7', 'l'], ['1.59', 'l'], ['2.29', 'l']]}, 'c': {'total': 5.3133333333333335, 'items': [['1', 'a', 'l', 'c'], ['2.7', 'l', 'c'], ['1.29', 'c'], ['1.59', 'c'], ['1.5', 'c', 'a']]}, '7': {'total': 1.0, 'items': [['2', '7', 'l']]}}

    launch(people)

