from tkinter import *
import tkinter
import random


spel = 0
sst = ['schaar', 'steen', 'papier']
jan = sst.pop(0)


def stenig(spel, jan, top):
    spel = 'steen'
    wiewint(spel, jan, top)

def scharig(spel, jan, top):
    spel = 'schaar'
    wiewint(spel, jan, top)

def papierig(spel, jan, top):
    spel = 'papier'
    wiewint(spel, jan, top)

def prop():
    global jan
    sst = ['schaar', 'steen', 'papier']
    random.shuffle(sst)
    jan = sst.pop(0)

def wiewint(spel, jan, top):
    prop()
    if spel == jan:
        top.z += 1
    elif jan == "schaar":
        if spel == "steen":
            top.y += 1
        else:
            top.x += 1
    elif jan == "papier":
        if spel == "schaar":
            top.y += 1
        else:
            top.x += 1
    elif jan == "steen":
        if spel == "papier":
            top.y += 1
        else:
            top.x += 1
    free(spel, jan, top)
    score(top)

def score (top):
    W = tkinter.Label(top, fg="black", text="Uw score bedraagt: {0}\nDe computer heeft: {1}\nAantal keren gelijkspel:{2}".format(
        str(top.y), str(top.x), str(top.z)))

    W.pack()
    W.place(x=0, y=230)


def free (spel, jan, top):
    W = tkinter.Label(top, fg="black", text="     U koos: {0}\nDe computer: {1}".format(
        str(spel), str(jan)))

    W.pack()
    W.place(x=170, y=230)

def reset (top):
    top.x = 0
    top.y = 0
    top.z = 0
    spel = "                     "
    jan = "                      "
    free(spel, jan, top)
    score(top)


def applic(top):
    W = tkinter.Label(top, fg="green", text="Welkom, ik nodig u uit om een potje schaar, steen papier te spelen.")
    W.place(x=0, y=0)

    W = tkinter.Label(top, fg="red", text="Kies een van de opties terwijl ik mijn optie kies.")
    W.place(x=0, y=20)

    W = tkinter.Label(top, fg="blue", text="Uw score verschijnt onderaan, als u wilt stoppen druk op 'The End'.")
    W.place(x=0, y=40)


def pof(top):
    A = tkinter.Button(top, text="Schaar", command=lambda: scharig(spel, jan, top))

    A.pack()
    A.place(y=60, bordermode=OUTSIDE, height=100, width=100)

    B = tkinter.Button(top, text="Steen", command=lambda: stenig(spel, jan, top))

    B.pack()
    B.place(y=60, x=100, bordermode=OUTSIDE, height=100, width=100)

    C = tkinter.Button(top, text="Papier", command=lambda: papierig(spel, jan, top))

    C.pack()
    C.place(x=200, y=60, bordermode=OUTSIDE, height=100, width=100)


    Z = tkinter.Button(top, text="The End", command=top.quit, activeforeground="red")

    Z.pack()
    Z.place(x=100, y=160, bordermode=OUTSIDE, height=50, width=100)

    Z = tkinter.Button(top, text="Reset", command=lambda: reset(top), activeforeground="red")

    Z.pack()
    Z.place(x=0, y=160, bordermode=OUTSIDE, height=50, width=100)


def apl():
    top = tkinter.Tk()
    top.title("Schaar steen papier")
    top.geometry("400x300+200+200")
    top.x = 0
    top.y = 0
    top.z = 0
    applic(top)
    pof(top)
    top.mainloop()

apl()
