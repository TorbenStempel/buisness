from tkinter import *
import time
import tkinter as tk
import os
import sys
root = Tk()
root.title('')

frameCnt = 12
frames = [PhotoImage(file='./banned-and-you-are-banned.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

root.bind('<Control-Shift-Key>', exit)
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(25, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)

def exit(event=None):
    sys.exit()

root.mainloop()