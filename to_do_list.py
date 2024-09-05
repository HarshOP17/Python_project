from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get().strip()
    if task_string:
        tasks.append((task_string, False)) 
        update_listbox()
        task_field.delete(0, 'end')
    else:
        messagebox.showinfo('Error', 'Task field is empty.')

def mark_as_complete():
    try:
        index = task_listbox.curselection()[0]
        selected_task = tasks[index]
        tasks[index] = (selected_task[0], True) 
        update_listbox()
    except IndexError:
        messagebox.showinfo('Error', 'No task selected.')

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except IndexError:
        messagebox.showinfo('Error', 'No task selected.')

def update_listbox():
    task_listbox.delete(0, 'end')
    for task, completed in tasks:
        if completed:
            task_listbox.insert('end', task)
            task_listbox.itemconfig('end', {'fg': 'green'})
        else:
            task_listbox.insert('end', task)
if __name__ == "_main_":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("550x350+550+275")
    guiWindow.resizable(0, 0)

    tasks = []

    frame = Frame(guiWindow)
    frame.pack(fill="both", expand=True)

    Label(frame, text="TO-DO LIST\nEnter Task Title:").grid(row=0, column=0, padx=20, pady=10)
    task_field = Entry(frame, width=40)
    task_field.grid(row=0, column=1, padx=10, pady=10)

    Button(frame, text="Add", width=10, command=add_task).grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text="Remove", width=10, command=remove_task).grid(row=1, column=2, padx=10, pady=10)
    Button(frame, text="Mark as Complete", width=15, command=mark_as_complete).grid(row=1, column=1, padx=10, pady=10)
    
    task_listbox = Listbox(frame, width=70, height=9)
    task_listbox.grid(row=3, column=0, columnspan=3, padx=20, pady=10)
  
    guiWindow.mainloop()