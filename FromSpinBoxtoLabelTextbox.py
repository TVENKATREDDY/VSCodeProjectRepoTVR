from tkinter import *
import random,string

root=Tk()
Label(root,text="Enter Text Here").pack()
test=IntVar()
Spinbox(root,from_=4,to_=10,textvariable=test).pack()
#label1.pack()
#spn.pack()
def func():
    Entry(root,textvariable=test.get()).pack()

Button(root,text='Click Here',command=func).pack()
#ent.pack()

root.mainloop()

