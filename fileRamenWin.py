# File Ramen-er

from tkinter import *
import os
from pathlib import Path
import random
from random import randint


win = Tk()
win.title("File Ramen")
win.resizable(0, 0)


def JPGrenamer():
    names = ["blah", "stonks", "marker", "volgin", "raiden", "a", "b", "c", "v", "n", "m", "ocelot", "meow", "peko", "pekora", "gugulu", "potion", "seller", "knight", "traveler", "d", "e", "f", "g", "h", "i", "j", "k", "l", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
    wordbank.delete("1.0", "end")
    wordbank.insert(END, names)
    #value = randint(0,100)
    cn = entry1.get("0.0", END)
    fol = entry2.get("0.0", END)
    #wb = entry3.get("0.0", END)
    # str(value)
    for count, filename in enumerate(os.listdir('C:\\Users\\' + cn.strip('\n') + "\\Desktop\\" + fol.strip("\n") + "\\")):
        dst = random.choice(names) + random.choice(names) + str(count) + ".jpg"
        src = 'C:\\Users\\' + cn.strip('\n') + "\\Desktop\\" + fol.strip("\n") + "\\" + filename
        dst = 'C:\\Users\\' + cn.strip('\n') + "\\Desktop\\" + fol.strip('\n') + "\\" + dst

        os.rename(src, dst)

def PNGrenamer():
    names = ["blah", "stonks", "marker", "volgin", "raiden", "a", "b", "c", "v", "n", "m", "ocelot", "meow", "peko", "pekora", "gugulu", "potion", "seller", "knight", "traveler", "d", "e", "f", "g", "h", "i", "j", "k", "l", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
    wordbank.delete("1.0", "end")
    wordbank.insert(END, names)
    #value = randint(0,100)
    cn = entry1.get("0.0", END)
    fol = entry2.get("0.0", END)
    #wb = entry3.get("0.0", END)
    # str(value)
    for count, filename in enumerate(os.listdir('C:\\Users\\' + cn.strip('\n') + "\\Desktop\\" + fol.strip("\n") + "\\")):
        dst = random.choice(names) + random.choice(names) + str(count) + ".png"
        src = 'C:\\Users\\' + cn.strip('\n') + '\\Desktop\\' + fol.strip('\n') + '\\' + filename
        dst = 'C:\\Users\\' + cn.strip('\n') + '\\Desktop\\' + fol.strip('\n') + '\\' + dst

        os.rename(src, dst)


l1 = Label(win, text = "Place the desired folder on your desktop and make sure the files are all JPG or PNG\n This WILL rename everything in the folder to either [x].JPG or [x].PNG\nThis warning exists for any potential messups when changing file extensions")
l1.grid(row = 1, column = 1, padx = 150, pady = 30, sticky = W)

l5 = Label(win, text = "Your Computer Name:")
entry1 = Text(win, width = 25, height = 1, wrap = WORD)
l5.grid(row = 2, column = 1, padx = 20, sticky = W)
entry1.grid(row = 2, column = 1, columnspan = 2, pady = (10,10))

l7 = Label(win, text = "Folder name on your Desktop:")
entry2 = Text(win, width = 25, height = 1, wrap = WORD)
l7.grid(row = 3, column = 1, padx = 20, sticky = W)
entry2.grid(row = 3, column = 1, columnspan = 2, pady = (10,10))

#l7 = Label(win, text = "Enter word to add to word bank:")
#entry3 = Text(win, width = 25, height = 1, wrap = WORD)
#l7.grid(row = 4, column = 1, padx = 20, sticky = W)
#entry3.grid(row = 4, column = 1, columnspan = 2, pady = (10,10))

button = Button(win, text = "JPG ONLY Rename", width = 20)
button.grid(row = 5, column = 1, columnspan = 2, sticky = W, padx = 50, pady = 5)
button.configure(command = JPGrenamer)

button = Button(win, text = "PNG ONLY Rename", width = 20)
button.grid(row = 5, column = 1, columnspan = 2, padx = 200, pady = 5)
button.configure(command = PNGrenamer)

l7 = Label(win, text = "")
l7.grid(row = 6, column = 1, padx = 20, sticky = W)

l7 = Label(win, text = "Current word bank being applied:")
wordbank = Text(win, width = 100, height = 10, wrap = WORD)
l7.grid(row = 7, column = 1, padx = 20, sticky = W)
wordbank.grid(row = 8, column = 1, columnspan = 2, pady = (10,10))


win.mainloop()