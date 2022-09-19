from tkinter import *
from tkinter import ttk, filedialog, messagebox


def select_file(sv: StringVar):
    filetypes = (
        ('Image files', ('*.png', '*.bmp')),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    try:
        sv.set(filename)
    except:
        messagebox.showinfo('Error', message='Invalid file selection')


root = Tk()
root.title('CSF-AWC1')
root.geometry('800x600')
# Variable declarations
selected_cover_file_stringvar = StringVar(root)
selected_payload_file_stringvar = StringVar(root)
function_selected = StringVar(root)

# Frame creation
frame = ttk.Frame(root, padding=10)
frame.grid()

# Labels
cover_file_selection_label = Label(root, text='Cover file selected: ')
cover_selected_file_label = Label(root, textvariable=selected_cover_file_stringvar)
payload_file_selection_label = Label(root, text='Payload file selected: ')
payload_selected_file_label = Label(root, textvariable=selected_payload_file_stringvar)
function_selection = Label(root, text='Select function: ')
function_selection_dropdown = OptionMenu(root, function_selected, 'Encrypt', 'Decrypt')

# Buttons
select_cover_file_button = Button(root, text='Choose cover file:',
                                  command=lambda: select_file(selected_cover_file_stringvar))
select_payload_file_button = Button(root, text='Choose cover file:',
                                    command=lambda: select_file(selected_payload_file_stringvar))
try_start_function_button = Button(root, text='Begin!',
                                   command='')

# Grid alignment
cover_file_selection_label.grid(row=0, column=0, sticky=W, pady=2, padx=2)
cover_selected_file_label.grid(row=0, column=1, sticky=W, pady=2, padx=2)
select_cover_file_button.grid(row=0, column=2, sticky=E, pady=2, padx=2)
payload_file_selection_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)
payload_selected_file_label.grid(row=1, column=1, sticky=W, pady=2, padx=2)
select_payload_file_button.grid(row=1, column=2, sticky=E, pady=2, padx=2)
function_selection.grid(row=2, column=0, sticky=W, pady=2, padx=2)
function_selection_dropdown.grid(row=2, column=2, sticky=E, pady=2, padx=2)
try_start_function_button.grid(row=3, column=2, sticky=E, pady=2, padx=2)
# Main loop
root.mainloop()
