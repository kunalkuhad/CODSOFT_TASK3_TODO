from tkinter import *
import tkinter.messagebox

def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Toplevel()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.focus_set()  
    root1.grab_set()   
    root1.wait_window()  

def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        index = marked[0]
        temp_marked = listbox_task.get(index)
        if not temp_marked.endswith(" ✔"):
            temp_marked += " ✔"
        listbox_task.delete(index)
        listbox_task.insert(index, temp_marked)

window = Tk()
window.title("kunal's To-Do List")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
