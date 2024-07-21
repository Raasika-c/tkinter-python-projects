from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
root.title('ROCK PAPER SCISSORS GAME')
root.geometry('350x300')
root.configure(bg='#2b2d42')

pt = 0 

def con():
    global pt  
    try:
        com = str(random.choice(choices)).lower()
        pl = str(user_choice.get()).lower()
        if pl == com:
           mes = 'Tie'
        elif (pl == 'rock' and com == 'scissors') or (pl == 'scissors' and com == 'paper') or (pl == 'paper' and com == 'rock'):
           mes = 'You won!!'
           pt += 1
        else:
           mes = 'You lost!'
    
        mb.showinfo("Result", f"Your choice: {pl}\nComputer's choice: {com}\n\n{mes}")
    except Exception as e:
        mb.showerror("Error", f"An error occurred: {e}")


def qt():
    mb.showinfo('Points', f'Total points: {pt}')
    root.quit()

l = Label(root, text='ENTER CHOICE', font='arial 20 bold', fg='#edf2f4', bg='#2b2d42')
#l.grid(row=0, column=1, columnspan=2)
l.pack()

user_choice = StringVar()
user_choice.set("")  

but = Button(root, text='CONFIRM', command=con, bg='#8d99ae', fg='white', activebackground='white', activeforeground='black', font='arial')
#but.grid(row=7, column=1)
but2 = Button(root, text='QUIT', command=qt, bg='#8d99ae', fg='white', activebackground='white', activeforeground='black', font='arial')
#but2.grid(row=8, column=1)

choices = ['rock', 'paper', 'scissors']
l2=Label(root,bg='#2b2d42').pack()
for c in choices:
    r = Radiobutton(root, text=c.upper(), variable=user_choice, value=c, font='arial 15', bg='#2b2d42',fg='white')#,activeforeground='#edf2f4')
    r.pack()
    # r.grid(row=R, column=1)  
    #R += 1
l3=Label(root,bg='#2b2d42').pack()
but.pack()
but2.pack()


mainloop()
