import tkinter as tk
from tkinter import *
import random,time
#Generate 5 random numbers between 10 and 30
master=Tk()
master.title('Ludo')
master.geometry('200x50')
Coin= [" Red  ","Blue  ","Green ","Yellow"]
Count=0

def Count1():
           global Count
           Label(master, text=Coin[Count]).grid(row=0,column=2)
           Count=Count+1
           if Count==4:
                Count=0
    
def Roll():
        Dice = random.sample(range(1,7), 1)
        Label(master, text="          ").grid(row=0,column=1)
        Count1()
        Label(master, text=Dice).grid(row=0,column=4)
        Label(master, text="                  ").grid(row=0,column=5)
        Button(master, text='Roll', command=Roll,bg="lightBlue").grid(row=0, column=6,ipadx=3,ipady=6)
        

Roll()
mainloop()
