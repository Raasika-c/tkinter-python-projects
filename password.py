from tkinter import*
import random
from tkinter import messagebox as mb
from tkinter.ttk import Combobox

root=Tk() 
root.title('password generator')
root.geometry('450x200')
root.configure(bg='#2b2d42')


alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=[1,2,3,4,5,6,7,8,9,0]
spl=['!','@','#','$','%','&','*']
def con():
    p=''
    try:
        n=int(enter.get())
    except ValueError:
        mb.showerror("Invalid Input", "Length must be an integer")
        return
   
    enter.delete(0,END)
    c = combo.get().lower()
    combo.set('')
   
    if c=='easy':
        for i in range(n):
            p+=random.choice(alpha)
    elif c=='moderate':
        for i in range(n):
            nu=alpha+num
            p+=str(random.choice(nu))
    elif c=='hard':
        for i in range(n):
            sp=alpha+num+spl
            p+=str(random.choice(sp))
    
    else:
        mb.showerror("Invalid Complexity", "Complexity must be 'easy', 'moderate', or 'hard'")
        return

    mb.showinfo("Generated Password", p)



l=Label(root,text='length',font='arial 20 bold',fg='#edf2f4',bg='#2b2d42')

l.grid(row=0,column=0)
enter=Entry(root,width=45)
enter.grid(row=0,column=1,columnspan=2,pady=10)

l1=Label(root,text='complextity',font='arial 20 bold',fg='#edf2f4',bg='#2b2d42')
l1.grid(row=1,column=0)

combo = Combobox(root, values=['easy', 'moderate', 'hard'], state='readonly', width=43)
combo.grid(row=1, column=1, columnspan=2, pady=10)
combo.set('')

but=Button(root,text='CONFIRM',command=con,bg='#8d99ae',fg='white',activebackground='white',activeforeground='black',font='arial').grid(row=2,column=1)
#bdel=Button(root,text='DELETE',command=dele,bg='#03045e',fg='white',activebackground='white',activeforeground='black',font='arial')

#badd.grid(row=6,column=3)
#bdel.grid(row=2,column=3)




mainloop()