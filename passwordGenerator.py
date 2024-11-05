from tkinter import *
import random, string
import pyperclip
root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('PYTHON PROJECT - PASSWORD GENERATOR')
Label(root,text="PASSWORD GENERATOR",font='arial 15 bold').pack()
Label(root,text='Python',font='arial 15 bold').pack(side=BOTTOM)

pass_label=Label(root,text='PASSWORD LENGTH',font='arial 15 bold').pack()
pass_len=IntVar()
length=Spinbox(root,from_=4,to_=32,textvariable=pass_len,width=15).pack()
pass_str=StringVar()


def generator():
    password=[]
    if pass_len.get() >= 4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        
        for _ in range(pass_len.get() - 4):
            password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation))
            
        random.shuffle(password)
    else:
        for _ in range(pass_len.get()):
            password(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation))
            
    pass_str.set(''.join(password))
    
def copyPassword():
    pyperclip.copy(pass_str.get())
    
Button(root,text='GENERATE PASSWORD',command=generator).pack(pady=5)
Entry(root,textvariable=pass_str).pack()
Button(root,text='Copy to Clipboard',command=copyPassword).pack(pady=5) 
root.mainloop()       
