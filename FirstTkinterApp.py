import tkinter as tk
def on_button():
    #label= tk.Label(root,text='Button Clicked and Name is ')
    #label.config(text='Button Clicked')
    print('value is :',text.get() + text1.get())
    #label.pack(pady=20)
    
root = tk.Tk()
root.title('Sample Tkinter App')

label = tk.Label(root,text='Enter Name')
label.pack(pady=20)

x=20

text=tk.Entry(root)
text.pack(pady=10)
text1=tk.Entry(root)
text1.pack(pady=10)

button=tk.Button(root,text='Click Me',command=on_button)
button.pack(pady=20)

root.mainloop()