from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-do-list',
                           font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            for item in delete_:
                self.main_text.delete(item)

        def edit():
            selected_task_index = self.main_text.curselection()

            if not selected_task_index:
                return  # No task selected for editing

            selected_task_text = self.main_text.get(selected_task_index)

            edit_window = Toplevel(self.root)
            edit_window.title('Edit Task')

            edit_text = Text(edit_window, bd=5, height=2, width=30, font='ariel, 10 bold')
            edit_text.insert(END, selected_task_text)
            edit_text.pack()

            def save_edit():
                edited_task_text = edit_text.get("1.0", END)
                self.main_text.delete(selected_task_index)
                self.main_text.insert(selected_task_index, edited_task_text)
                edit_window.destroy()

            save_button = Button(edit_window, text="Save", font='sarif, 20 bold italic',
                                 width=10, bd=5, bg='orange', fg='black', command=save_edit)
            save_button.pack()

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                             width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                              width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)

        self.edit_button = Button(self.root, text="Edit", font='sarif, 20 bold italic',
                                  width=10, bd=5, bg='orange', fg='black', command=edit)
        self.edit_button.place(x=30, y=230)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
