from tkinter import *
from tkinter import ttk, filedialog, messagebox

import mp3_steg
import utility


def select_file(sv: StringVar):

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',)

    try:
        sv.set(filename)
    except:
        messagebox.showinfo('Error', message='Invalid file selection')


def check_free_bits(file: StringVar, mode: StringVar):
    """Function takes in the file name and mode both in StringVar
    format and returns number of available bit positions"""
    if mode.get() == 'MP3':
        bits = mp3_steg.get_available_bits(utility.read_file_into_hex_list(file.get()))
        messagebox.showinfo('Available storage at different settings',
                            f'If bit 0 is used only: {bits/8} bytes\n'
                            f'If bit 0 and 1: {bits*2/8} bytes\n'
                            f'if bit 0-2: {bits*3/8} bytes\n'
                            f'if bit 0-3: {bits*4/8} bytes\n'
                            f'if bit 0-4: {bits*5/8} bytes\n'
                            f'if bit 0-5: {bits*6/8} bytes\n'
                            f'if bit 0-6: {bits*7/8} bytes\n')


root = Tk()
root.title('CSF-AWC1')
root.geometry('800x600')

# Variable declarations
selected_cover_file_stringvar = StringVar(root)
selected_payload_file_stringvar = StringVar(root)
function_selected = StringVar(root)
mode_selected = StringVar(root)
num_bits = StringVar(root)

# Frame creation
frame = ttk.Frame(root, padding=10)
frame.grid()

# Labels
cover_file_selection_label = Label(root, text='Cover file selected: ')
cover_selected_file_label = Label(root, textvariable=selected_cover_file_stringvar)
payload_file_selection_label = Label(root, text='Payload file selected: ')
payload_selected_file_label = Label(root, textvariable=selected_payload_file_stringvar)
function_selection = Label(root, text='Select function: ')
mode_selection = Label(root, text='Select mode: ')
num_bits_label = Label(root, text='Select number of bits to use (0-7): ')

# Dropdowns
function_selection_dropdown = OptionMenu(root, function_selected, 'Encrypt', 'Decrypt')
mode_selection_dropdown = OptionMenu(root, mode_selected, 'PNG', 'MP3')

# Buttons
select_cover_file_button = Button(root, text='Choose cover file:',
                                  command=lambda: select_file(selected_cover_file_stringvar))
select_payload_file_button = Button(root, text='Choose payload file:',
                                    command=lambda: select_file(selected_payload_file_stringvar))
try_start_function_button = Button(root, text='Begin!',
                                   command='')
get_num_bits_button = Button(root, text='Get number of bits available',
                             command=lambda: check_free_bits(selected_cover_file_stringvar, mode_selected))

# Spinbox
num_bits_selection = Spinbox(root, from_=0, to=7, textvariable=num_bits)

# Grid alignment
cover_file_selection_label.grid(row=0, column=0, sticky=W, pady=2, padx=2)
cover_selected_file_label.grid(row=0, column=1, sticky=W, pady=2, padx=2)
select_cover_file_button.grid(row=0, column=2, sticky=E, pady=2, padx=2)
payload_file_selection_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)
payload_selected_file_label.grid(row=1, column=1, sticky=W, pady=2, padx=2)
select_payload_file_button.grid(row=1, column=2, sticky=E, pady=2, padx=2)
function_selection.grid(row=2, column=0, sticky=W, pady=2, padx=2)
function_selection_dropdown.grid(row=2, column=2, sticky=E, pady=2, padx=2)
mode_selection.grid(row=3, column=0, sticky=W, pady=2, padx=2)
mode_selection_dropdown.grid(row=3, column=2, sticky=E, pady=2, padx=2)
num_bits_label.grid(row=4, column=0, sticky=E, pady=2, padx=2)
num_bits_selection.grid(row=4, column=2, sticky=E, pady=2, padx=2)
try_start_function_button.grid(row=5, column=2, sticky=E, pady=2, padx=2)
get_num_bits_button.grid(row=6, column=2, sticky=E, pady=2, padx=2)
# Main loop
root.mainloop()
