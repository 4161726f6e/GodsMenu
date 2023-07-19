import tkinter as tk
import random, csv

def randProtein():
    protein = []
    for x in range(8):
        protein.append(random.randint(1,4))
    return protein

def sanityCheck(item, menu, file):
    if item < 5:
        if len(menu) < 8:
            from tkinter import messagebox
            messagebox.showerror("Oops!", "Ran out of choices! Need at least 8 choices for each protein. Please edit " + str(file))
            exit(1)

def readMenu(file, item):
    menu = []
    with open(file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            menu.append(row)

    sanityCheck(item, menu, file)

    return menu

def pickItem(item):
    if item == 1:
        options = readMenu("beef.csv", item)
    elif item == 2:
        options = readMenu("pork.csv", item)
    elif item == 3:
        options = readMenu("chicken.csv", item)
    elif item == 4:
        options = readMenu("seafood.csv", item)
    elif item == 5:
        options = readMenu("carbs.csv", item)
    elif item == 6:
        options = readMenu("veggies.csv", item)
    elif item == 7:
        options = readMenu("breakfast.csv", item)

    return random.choice(options)
    
def pickCarbs(choices):
    carbs = []
    for x in range(len(choices)):
        choice = pickItem(5)
        carbs.append(choice)

    # flatten the list
    carbs = [item for sublist in carbs for item in sublist]

    return carbs

def pickVeg(choices):
    veg = []
    for x in range(len(choices)):
        choice = pickItem(6)
        veg.append(choice)

    # flatten the list
    veg = [item for sublist in veg for item in sublist]

    return veg

def pick2Veg(choices):
    veg = []
    for x in range(len(choices)):
        choice1 = pickItem(6)
        x = [" and "]
        choice2 = pickItem(6)
        while choice2 == choice1:
            choice2 = pickItem(6)
        myveg = choice1 + x + choice2
        this = ""
        for y in myveg:
            this += '' + y
        veg.append(this)

    return veg

def pickMeats(choices):
    meats = []
    
    choice = ""
    catcher = []
    for x in range(len(choices)):
        choice = pickItem(choices[x])
        while choice in meats:
            choice = pickItem(choices[x])
            if choice not in catcher:
                catcher.append(choice)
        meats.append(choice)

    # flatten the list
    meats = [item for sublist in meats for item in sublist]

    return meats

def pickBreakfast():
    breakfast = []

    choice = ""
    catcher = []
    for x in range(2):
        choice = pickItem(7)
        while choice in breakfast:
            choice = pickItem(7)
            if choice not in catcher:
                catcher.append(choice)
        breakfast.append(choice)

    # flatten the list
    breakfast = [item for sublist in breakfast for item in sublist]

    return breakfast

def get_meats():
    if var3.get() == 1 and var4.get() == 1 and var5.get() == 1 and var6.get() == 1:
        x = [1,1,2,2,3,3,4,4]
    elif var3.get() == 1 and var4.get() == 1 and var5.get() == 1:
        x = [1,1,1,2,2,2,3,3]
    elif var3.get() == 1 and var4.get() == 1 and var6.get() == 1:
        x = [1,1,1,2,2,2,4,4]
    elif var3.get() == 1 and var5.get() == 1 and var6.get() == 1:
        x = [1,1,1,3,3,3,4,4]
    elif var4.get() == 1 and var5.get() == 1 and var6.get() == 1:
        x = [2,2,2,3,3,3,4,4]
    elif var3.get() == 1 and var4.get() == 1:
        x = [1,1,1,1,2,2,2,2]
    elif var3.get() == 1 and var5.get() == 1:
        x = [1,1,1,1,3,3,3,3]
    elif var3.get() == 1 and var6.get() == 1:
        x = [1,1,1,1,4,4,4,4]
    elif var4.get() == 1 and var5.get() == 1:
        x = [2,2,2,2,3,3,3,3]
    elif var4.get() == 1 and var6.get() == 1:
        x = [2,2,2,2,4,4,4,4]
    elif var5.get() == 1 and var6.get() == 1:
        x = [3,3,3,3,4,4,4,4]
    elif var4.get() == 1:
        x = [2,2,2,2,2,2,2,2]
    elif var4.get() == 1:
        x = [2,2,2,2,2,2,2,2]
    elif var3.get() == 1:
        x = [1,1,1,1,1,1,1,1]
    elif var4.get() == 1:
        x = [2,2,2,2,2,2,2,2]
    elif var5.get() == 1:
        x = [3,3,3,3,3,3,3,3]
    elif var6.get() == 1:
        x = [4,4,4,4,4,4,4,4]
    else:
        x = randProtein()
    
    meats = []
    meats = pickMeats(x)
    return meats

def getText():
    meats = get_meats()
    if var1.get() == 1 and var2.get() == 1:
        carbs = pickCarbs(meats)
        veg = pick2Veg(meats)
        count = 0
        text = []
        for x in meats:
            text.append("Dinner " + str((count + 1)) + ": " + meats[count] + ", with " + carbs[count] + ", " + veg[count] + "\n")
            count += 1
    elif var1.get() == 1:
        carbs = pickCarbs(meats)
        veg = pickVeg(meats)
        count = 0
        text = []
        for x in meats:
            text.append("Dinner " + str((count + 1)) + ": " + meats[count] + ", with " + carbs[count] + ", " + veg[count] + "\n")
            count += 1
    elif var2.get() == 1:
        veg = pick2Veg(meats)
        count = 0
        text = []
        for x in meats:
            text.append("Dinner " + str((count + 1)) + ": " + meats[count] + ", with " + veg[count] + "\n")
            count += 1
    else:
        veg = pickVeg(meats)
        count = 0
        text = []
        for x in meats:
            text.append("Dinner " + str((count + 1)) + ": " + meats[count] + ", with " + veg[count] + "\n")
            count += 1

    # Always print 2 breakfasts for the weekend
    breakfast = pickBreakfast()
    text.append("\nBreakfast 1: " + breakfast[0] + "\n")
    text.append("Breakfast 2: " + breakfast[1] + "\n")

    mytext = ''.join(text)
    return mytext

def getIntro():
    lyrics = ["ne sonnim", "eoseo osibsio", "i gageneun cham menyuga goleugido swibjyo", "mwol sikyeodo ogam-eul manjoghaji haji",\
              "jinagadeon nageune, bidulgikkaji", "kkachikkaji kkamagwideulkkaji", "Cooking a sauce ibmasdaelo teol-eo", \
                "I just wanna taste it, make it hot", "Taste so good ban-eung-eun modu jjeol-eo", "DU DU DU DU DU DU"]
    return random.choice(lyrics)

window = tk.Tk()
window.title('God\'s Menu')
window.geometry('700x350')

gmenu = r"""
     ______          ___          __  ___                
    / ____/___  ____/ ( )_____   /  |/  /__  ____  __  __
   / / __/ __ \/ __  /|// ___/  / /|_/ / _ \/ __ \/ / / /
  / /_/ / /_/ / /_/ /  (__  )  / /  / /  __/ / / / /_/ / 
  \____/\____/\__,_/  /____/  /_/  /_/\___/_/ /_/\__,_/  """

g = tk.Label(window, bg='black', width=20, font='Courier', text=gmenu)
g.pack(fill="both", expand="1")
 
l = tk.Label(window, bg='black', width=20, text=getIntro())
l.pack(fill="both", expand="1")

def print_selection():
    l.config(text=getText(), justify="left")

protein = []
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Carbs',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack(side=tk.RIGHT)
c2 = tk.Checkbutton(window, text='2 Veg',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack(side=tk.RIGHT)

var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
c3 = tk.Checkbutton(window, text='Beef',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack(side=tk.LEFT)
c4 = tk.Checkbutton(window, text='Chicken',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack(side=tk.LEFT)
c5 = tk.Checkbutton(window, text='Pork',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.pack(side=tk.LEFT)
c6 = tk.Checkbutton(window, text='Seafood',variable=var6, onvalue=1, offvalue=0, command=print_selection)
c6.pack(side=tk.LEFT)

window.mainloop()