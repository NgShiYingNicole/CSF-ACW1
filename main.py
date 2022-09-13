from tkinter import *
from tkinter import ttk, filedialog, messagebox


def select_file():
    filetypes = (
        ('Image files', ('*.png', '*.bmp')),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    messagebox.showinfo(
        title='Selected File',
        message=filename
    )


root = Tk()
root.title('CSF-AWC1')
root.geometry('640x400')
menubar = Menu(root)  # creates the menubar
root.config(menu=menubar)
file_menu = Menu(menubar)  # creates a menu
file_menu.add_command(label='Open', command=select_file)  # add open file command to menubar
file_menu.add_command(label='Exit', command=root.destroy)  # add exit command to menubar
menubar.add_cascade(label='File', menu=file_menu)  # add menubar to menu
frame = ttk.Frame(root, padding=10)
frame.grid()
root.mainloop()
