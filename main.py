from tkinter import *

import tkinter.simpledialog

import tkinter.messagebox

root = Tk()
w = Label(root, text="my program")
w.pack()

tkinter.messagebox.showinfo("hi", "hi and welcome")
name = tkinter.simpledialog.askstring("name", "what is your name?")
yd = tkinter.simpledialog.askstring("feels", "how to you feel? (good not good)")
if yd in "good":
    output1 = "nice to hear", name
    tkinter.messagebox.showinfo("done", output1)
elif yd in "not good":
    output2 = "sorry to hear", name
    tkinter.messagebox.showinfo("done", output2)
    output4 = "does something can help you? (yes or no)"
    hy = tkinter.simpledialog.askstring("help?", output4)
    if hy in "yes":
        wis = tkinter.simpledialog.askstring("what it is?", "what it is?")
        output5 = "amm you can look it on google something like: how to", wis, "or something like that"
        tkinter.messagebox.showinfo("amm", output5)
    elif hy in "no":
        output6 = "its ok i recommend to play some games talk to your friends or something like that its help me!"
        tkinter.messagebox.showinfo("sorry", output6)
else:
    output3 = "I did not understand that"
    tkinter.messagebox.showinfo("rest the app", output3)
root.mainloop()