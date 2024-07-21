from tkinter import *
from tkinter import ttk

t_status={}

root = Tk()
root.title('TO DO LIST')
root.geometry('400x500')
l=Label(root,text='tasks',font='arial 20 bold',fg='#edf2f4',bg='#0077b6')
root.configure(bg='#0077b6')
l.grid(row=0,column=0,columnspan=2)
#l.pack()

def add():
    v=enter.get()
    status = stat.get()
    list.insert(END,f'{v} => {status}')
    enter.delete(0,END)

def dele():
    list.delete(list.curselection())

def track():
    s= list.curselection()
    task =list.get(s).split(' => ')[0]
    status = stat.get()
    t_status[task] = status
    list.delete(s)     
    list.insert(s, f'{task} => {status}')    
    

badd=Button(root,text='ADD',command=add,bg='#03045e',fg='white',activebackground='white',activeforeground='black',font='arial')
bdel=Button(root,text='DELETE',command=dele,bg='#03045e',fg='white',activebackground='white',activeforeground='black',font='arial')
bex=Button(root,text='EXIT',command=root.quit,bg='#03045e',fg='white',activebackground='white',activeforeground='black',font='arial')
btr=Button(root,text='UPDATE',command=track,bg='#03045e',fg='white',activebackground='white',activeforeground='black',font='arial')


fr=Frame(root)
fr.grid(row=1,column=0,rowspan=5)
scr=Scrollbar(fr,orient=VERTICAL)
list=Listbox(fr,width=40,height=20,yscrollcommand=scr.set)
list.pack(side=LEFT)
scr.configure(command=list.yview)
scr.pack(side=RIGHT,fill=Y)

enter=Entry(root,width=45)
enter.grid(row=6,column=0,columnspan=2,pady=10)

badd.grid(row=6,column=3)
bdel.grid(row=2,column=3)
btr.grid(row=3,column=3)
bex.grid(row=4,column=3)


stat = ttk.Combobox(root, values=["Not Started", "In Progress", "Completed"])
stat.grid(row=5, column=0, columnspan=2, pady=10)
stat.set("Not Started")

mainloop()