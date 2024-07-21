from tkinter import *

root = Tk()
root.title('CALCULATOR')
#root.geometry('400x600')


entry = Entry(root, font='arial',width=24)
entry.grid(row=0, column=0, columnspan=4, padx=0, pady=1)

def onclick(val):
    now=entry.get()
    entry.delete(0,END)
    entry.insert (0, now+val)

def rem():
   entry.delete(0,END)    

def dele():
    entry.delete(len(entry.get())-1)

def calc():
 try:
    r=eval(entry.get())
    entry.delete(0,END)
    entry.insert (0,str(r))
 except Exception as e:
    entry.delete(0,END)
    entry.insert (0,str('Error'))
    
button_properties = {
    'bg': '#293241',
    'fg': 'white',
    'activebackground': 'white',
    'activeforeground': 'black',
    'font': 'arial',
    'height': 2
}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('+', 4, 3),('D',4,2),('.',4,0)
]


for (text, row, column) in buttons:
    Button(root, text=text,width=5, command=lambda t=text :onclick(t),**button_properties).grid(row=row, column=column, padx=0, pady=1)
Button(root, text='C', command=rem,width=11, **button_properties).grid(row=5, column=0, padx=0, pady=1,columnspan=2)
Button(root, text='=', command=calc,width=11, **button_properties).grid(row=5, column=2, padx=0, pady=1,columnspan=2)
Button(root, text='D', command=dele,width=5, **button_properties).grid(row=4, column=2, padx=0, pady=1)


root.mainloop()
