from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=Tk()

window.wm_title("Entry management System")

labelfont = ('times', 18, 'bold')

l1=Label(window,text="Name")
l1.config(font=labelfont)
l1.config(height=2,width=20)
l1.grid(row=3,column=9)      

l2=Label(window,text="Phone")
l2.config(font=labelfont)
l2.config(height=2,width=20)
l2.grid(row=6,column=9)      

l3=Label(window,text="CheckIn")
l3.config(font=labelfont)
l3.config(height=2,width=20)
l3.grid(row=9,column=9)      

l4=Label(window,text="CheckOut")
l4.config(font=labelfont)
l4.config(height=2,width=20)
l4.grid(row=12,column=9)      

title_text=StringVar()
e1=Entry(window,textvariable=title_text,width=30,bd=4)
e1.grid(row=3,column=11)

author_text=StringVar()
e2=Entry(window,textvariable=author_text,width=30,bd=4)
e2.grid(row=6,column=11)

year_text=StringVar()
e3=Entry(window,textvariable=year_text,width=30,bd=4)
e3.grid(row=9,column=11)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text,width=30,bd=4)
e4.grid(row=12,column=11)

list1=Listbox(window, height=12,width=100)
list1.grid(row=30,column=120,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=30,column=122,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=20,command=view_command)
b1.grid(row=23,column=28)

b2=Button(window,text="Search entry", width=20,command=search_command)
b2.grid(row=25,column=28)

b3=Button(window,text="Add entry", width=20,command=add_command)
b3.grid(row=27,column=28)

b4=Button(window,text="Update selected", width=20,command=update_command)
b4.grid(row=29,column=28)

b5=Button(window,text="Delete selected", width=20,command=delete_command)
b5.grid(row=31,column=28)

b6=Button(window,text="Close", width=20,command=window.destroy)
b6.grid(row=33,column=28)

window.mainloop()
