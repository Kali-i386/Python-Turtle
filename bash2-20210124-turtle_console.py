#!/usr/bin/python
"""bash2.py--use turtle to draw"""

from turtle import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
size = 1
root.title("Console")
setup(600,600)
pensize(size)
pencolor(0,0,0)

def tfd():
    fd(float(OPTION.get()))
def L():
    left(float(OPTION.get()))
def R():
    right(float(OPTION.get()))
def Res():
    reset()
def SETWide():
    print("wide:%d" %(wide.get()))
    pensize(int(wide.get()))
def UNDO():
    undo()
def BOMB():
    print("""
                                    ,se%n.    ,  .
                                 ,se*'  `*'.,$
                               ;s*'  .  `s,,$$.
                           ,. ,$'   .  . `$F^?$*'
       ,.ssSS$$$SSss,.  .sS$$s;*        ,*"$s$$,  .
    ,sS$$$$$$$$$$$$$$$s$$$$$$$$,   .   . . $'.`*.  . 
  ,sS$?M$$$$$$$$$$$$$$$$$$$$$^'            '  .
 ,$V;;tY$$$$$$$$$$$$$$$$$$$F'
,$Y;;tYV$$$$$$$$$$$$$$$$$$$$,
$Y;;tYH$$$$$$$$$$$$$$$$$$$$$$
$;;iYV$$$$$$$$$$$$$$$$$$$$$$$
$=;IYYV$$$$$$$$$$$$$$$$$$$$$$
`Y;;VV$$$$$$$$$$$$$$$$$$$$$$'
 `$YV$$$$$$$$$$$$$$$$$$$$$$'
  `*$$$$$$$$$$$$$$$$$$$$$*'
    `*S$$$$$$$$$$$$$$$$S*'
       `"**SS$$$$SS**"'
""")
def colorchoose():
	pass



LABEL = tk.Label(root,
              text="Console-Turtle",
              bitmap="info",
              relief="groove",
              compound="left",
              cursor="circle",
              bg="#FFA500")
LABEL2 = tk.Label(text="Option")
OPTION = tk.Entry(root)
OPTION.grid(row=1,column=1)
op = OPTION.get()
print(type(op))

btn1 = tk.Button(text="Forward",cursor="top_side",command=tfd)
btn2 = tk.Button(text="Left   ",cursor="left_side",command=L)
btn3 = tk.Button(text="Right  ",cursor="right_side",command=R)
btn5 = tk.Button(text="Undo   ",command=UNDO)
btn6 = tk.Button(text="Surprise!",command=BOMB)
btn7 = tk.Button(text="Choose Color",commmand=colorchoose)

btn4 = tk.Button(text="Reset  ",command=Res)
wide = tk.Scale(root,
                activebackground="#00FF00",
                cursor="hand1",
                from_=1,
                to=10,
                label="Pensize",
                relief="raised",
                orient=tk.HORIZONTAL)
setwidenew = tk.Button(root,text="Set Wide",command=SETWide,relief="raised")
sep = ttk.Separator(root,orient=tk.HORIZONTAL)

LABEL.grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)
LABEL2.grid(row=1,column=0)
btn1.grid(row=2,column=0)
btn2.grid(row=3,column=0)
btn3.grid(row=3,column=1)
btn4.grid(row=2,column=1)
btn5.grid(row=6,column=0)
sep.grid(row=4,column=0,columnspan=2,sticky=tk.W+tk.E)
wide.grid(row=5,column=0)
btn6.grid(row=6,column=1)
setwidenew.grid(row=5,column=1)

root.mainloop()
