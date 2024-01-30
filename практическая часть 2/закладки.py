from tkinter import *
import os

def add_note():
    note = text.get(1.0, END)
    listbox.insert(END, note)

def edit_note():
    selected = listbox.curselection()
    if selected:
        note = text.get(1.0, END)
        listbox.delete(selected[0])
        listbox.insert(selected[0], note)

def delete_note():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

def select_note(event):
    selected = listbox.curselection()
    if selected:
        note = listbox.get(selected[0])
        text.delete(1.0, END)
        text.insert(END, note)

def save_notes():
    notes = list(listbox.get(0, END))
    with open('notes.txt', 'w') as file:
        for note in notes:
            file.write(note + '\n')

def load_notes():
    if os.path.exists('notes.txt'):
        with open('notes.txt', 'r') as file:
            notes = file.readlines()
            for note in notes:
                listbox.insert(END, note.strip())

root = Tk()
root.title('Бер')

frame1 = Frame(root)
frame1.pack(side=LEFT, padx=10, pady=10)

frame2 = Frame(root)
frame2.pack(side=LEFT, padx=10, pady=10)

add_button = Button(frame1, text='Добавить', command=add_note)
add_button.pack()

edit_button = Button(frame1, text='Редактировать', command=edit_note)
edit_button.pack()

delete_button = Button(frame1, text='Удалить', command=delete_note)
delete_button.pack()

save_button = Button(frame1, text='Сохранить', command=save_notes)
save_button.pack()

load_button = Button(frame1, text='Загрузить', command=load_notes)
load_button.pack()

listbox = Listbox(frame1, height=10)
listbox.pack()
listbox.bind('<<ListboxSelect>>', select_note)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

text = Text(frame2, height=10, width=30)
text.pack()

root.mainloop()
