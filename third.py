from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry


GUI = Tk()
GUI.title('Expense and Income Recorder')
GUI.geometry('700x500')

GUI.state('zoomed')

Tab = Notebook(GUI)

F1 = Frame(Tab,width=500 , height=500)
F2 = Frame(Tab,width=500 , height=500)

Tab.add(F1, text='Expense')
Tab.add(F2, text='Income')


Tab.pack(fill=BOTH , expand=1)

#Tab 1 Expense
#---------------Row0--------------
LDate = ttk.Label(F1, text='Date',font=(None,18))
LDate.grid(row=0 , column=0 , padx=5 , pady=5)
#use date picker
EDate = DateEntry(F1, width=18 , background='blue',foregroud='white')
EDate.grid(row=0 ,column=1 , padx=5 , pady=5)

#---------------Row1--------------
LTitle = ttk.Label(F1, text='Title' , font=(None,18))
LTitle.grid(row=1 , column=0 , padx=5 , pady=5)
Title = StringVar()
ETitle = ttk.Entry(F1 , textvariable=Title,font=(None,18))
ETitle.grid(row=1 , column=1 , padx=5 , pady=5 )



#---------------Row2--------------
LExpense = ttk.Label(F1, text='Expense' , font=(None,18))
LExpense.grid(row=2 , column=0 , padx=5 , pady=5)




GUI.mainloop()

