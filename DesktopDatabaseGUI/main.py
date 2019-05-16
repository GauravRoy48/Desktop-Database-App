##################################################################################
# Creator     : Gaurav Roy
# Date        : 16 May 2019
# File        : main.py
#
# Description : The program creates a GUI using Tkinter to access and manage the
#               database of a bookstore. The backend uses Sqlite3 .
##################################################################################

from tkinter import *
import backend

# Function to clear the 4 entry windows
def clear_entries():
    te.delete(0, END)
    ae.delete(0, END)
    ye.delete(0, END)
    ie.delete(0, END)
    
# Function to fetch the details of the selected (clicked) element from the list output.
def get_selected_row(event):
    try:
        global selected_tuple
        index = op.curselection()[0]
        selected_tuple = op.get(index)
        te.delete(0, END)
        te.insert(END, selected_tuple[1])
        ae.delete(0, END)
        ae.insert(END, selected_tuple[2])
        ye.delete(0, END)
        ye.insert(END, selected_tuple[3])
        ie.delete(0, END)
        ie.insert(END, selected_tuple[4])
    except IndexError:
        pass

# Function to invoke the view() command of backend.
def view_command():
    op.delete(0, END)
    for row in backend.view():
        op.insert(END, row)

# Function to invoke the search() command of backend.
def search_command():
    op.delete(0, END)
    for row in backend.search(te_value.get(), ae_value.get(), ye_value.get(), ie_value.get()):
        op.insert(END, row)

# Function to invoke the insert() command of backend.
def add_command():
    backend.insert(te_value.get(), ae_value.get(), ye_value.get(), ie_value.get())
    op.delete(0, END)
    view_command()
    clear_entries()

# Function to invoke the delete() command of backend.
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    clear_entries()
    
# Function to invoke the update() command of backend.
def update_command():
    backend.update(selected_tuple[0], te_value.get(), ae_value.get(), ye_value.get(), ie_value.get())
    view_command()


window = Tk()

window.title("BookStore")

# Title related elements
tl=Label(window,text="Title", width=12) # Label
tl.grid(row=0,column=0)

te_value = StringVar()
te = Entry(window, textvariable=te_value) # Entry
te.grid(row=0, column=1)

# Author related elements
al=Label(window,text="Author", width=12) # Label
al.grid(row=0,column=2)

ae_value = StringVar()
ae = Entry(window, textvariable=ae_value) # Entry
ae.grid(row=0, column=3)

# Year related elements
yl=Label(window,text="Year", width=12) # Label
yl.grid(row=1,column=0)

ye_value = StringVar()
ye = Entry(window, textvariable=ye_value) # Entry
ye.grid(row=1, column=1)

# ISBN related elements
il=Label(window,text="ISBN", width=12) # Label
il.grid(row=1,column=2)

ie_value = StringVar()
ie = Entry(window, textvariable=ie_value) # Entry
ie.grid(row=1, column=3)

# Database Interaction related elements
op = Listbox(window, height=6, width=35) # Listbox
op.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window) # Scrollbar
sb.grid(row=2, column=2, rowspan=6)

op.configure(yscrollcommand=sb.set) # Binding Listbox and Scrollbar
sb.configure(command=op.yview)
op.bind('<<ListboxSelect>>', get_selected_row)

vab = Button(window, text='View All', width=16, command = view_command) # Button
vab.grid(row=2, column=3, rowspan=1)

seb = Button(window, text='Search Entry', width=16, command = search_command) # Button
seb.grid(row=3, column=3, rowspan=1)

aeb = Button(window, text='Add Entry', width=16, command = add_command) # Button
aeb.grid(row=4, column=3, rowspan=1)

usb = Button(window, text='Update Seleted', width=16, command = update_command) # Button
usb.grid(row=5, column=3, rowspan=1)

dsb = Button(window, text='Delete Selected', width=16, command = delete_command) # Button
dsb.grid(row=6, column=3, rowspan=1)

cl = Button(window, text='Close', width=16, command = window.destroy) # Button
cl.grid(row=7, column=3, rowspan=1)

window.mainloop()