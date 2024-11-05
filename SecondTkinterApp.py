import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input=entry.get()
    messagebox.showinfo('Information: ',f'You Entered: {user_input}')
    
root = tk.Tk()
root.title('Simple App')
    
label=tk.Label(root,text='Enter Something:')
label.pack(pady=10)
    
entry=tk.Entry(root,width=20)
entry.pack(pady=10)
    
    
button=tk.Button(root,text='Submit',command=on_button_click)
button.pack(pady=10)
root.mainloop()