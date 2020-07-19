import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, filedialog, messagebox, font
import os

main_application = tk.Tk()
main_application.title('iNotepad')
main_application.geometry('1200x800')
main_application.wm_iconbitmap('icon.ico')


###################################### main menu ############################################################
# def func():
   # print('testing...')


main_menu = tk.Menu(main_application)
# icon file
new_icon = tk.PhotoImage(file='icons2\\new.png')
open_icon = tk.PhotoImage(file='icons2\\open.png')
save_icon = tk.PhotoImage(file='icons2\\save.png')
save_as_icon = tk.PhotoImage(file='icons2\\save_as.png')
exit_icon = tk.PhotoImage(file='icons2\\exit.png')

file = tk.Menu(main_menu, tearoff=0)

copy_icon = tk.PhotoImage(file='icons2\\copy.png')
paste_icon = tk.PhotoImage(file='icons2\\paste.png')
cut_icon = tk.PhotoImage(file='icons2\\cut.png')
clear_all_icon = tk.PhotoImage(file='icons2\\clear_all.png')
find_icon = tk.PhotoImage(file='icons2\\find.png')

edit = tk.Menu(main_menu, tearoff=0)

tool_bar_icon = tk.PhotoImage(file='icons2\\tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2\\status_bar.png')

view = tk.Menu(main_menu, tearoff=0)

light_default_icon = tk.PhotoImage(file='icons2\\light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2\\light_plus.png')
dark_icon = tk.PhotoImage(file='icons2\\dark.png')
red_icon = tk.PhotoImage(file='icons2\\red.png')
monokai_icon = tk.PhotoImage(file='icons2\\monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2\\night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=0)
color_choice = tk.StringVar()
color_icon = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#474747', '#ffe0bd'),
    'Night Blue': ('#ededed', '#003366')
}

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

# ------------------------------------End main menu------------------------------------------------------------

##################################### toolbar ################################################################
# tool bar
tool_bar = tk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)
# font box
font_colony = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_colony
font_box.current(font_colony.index('Arial'))
font_box.grid(row=0, column=0, padx=5)
# size box
size_cur = tk.IntVar()
size_box = ttk.Combobox(tool_bar, width=6, textvariable=size_cur, state='readonly')
size_box['values'] = tuple(range(8, 80, 2))
size_box.current(4)
size_box.grid(row=0, column=1, padx=5)
# bold button
bold_icon = tk.PhotoImage(file='icons2\\bold.png')
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)
# italic button
italic_icon = tk.PhotoImage(file='icons2\\italic.png')
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)
# underline button
underline_icon = tk.PhotoImage(file='icons2\\underline.png')
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)
# font color button
font_color_icon = tk.PhotoImage(file='icons2\\font_color.png')
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)
# align left button
align_left_icon = tk.PhotoImage(file='icons2\\align_left.png')
align_left_button = ttk.Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=6, padx=5)
# align centre button
align_center_icon = tk.PhotoImage(file='icons2\\align_center.png')
align_center_button = ttk.Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=7, padx=5)
# align right button
align_right_icon = tk.PhotoImage(file='icons2\\align_right.png')
align_right_button = ttk.Button(tool_bar, image=align_right_icon)
align_right_button.grid(row=0, column=8, padx=5)
# ------------------------------------ End toolbar -------------------------------------------------------------

##################################### text editor #############################################################
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
text_editor.focus_set()
scroll_bar = ttk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
# change font and size function
current_font_family = 'Arial'
current_font_size = 12


def font_change(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def size_change(event=None):
    global current_font_size
    current_font_size = size_cur.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", font_change)
size_box.bind("<<ComboboxSelected>>", size_change)


# button fuctionality
# bold button
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_button.configure(command=change_bold)


# italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))


italic_button.configure(command=change_italic)


# underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] != 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_button.configure(command=change_underline)


# font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_button.configure(command=change_font_color)


# align functionality
# left align functionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_button.configure(command=align_left)


# centre align functionality
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_button.configure(command=align_center)


# right align functionality
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_button.configure(command=align_right)

text_editor.configure(font=('Arial', 12))
# ------------------------------------ End text editor ---------------------------------------------------------

##################################### status bar #############################################################
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    if text_editor.edit_modified():
        global text_changed
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        chars = len(text_editor.get(1.0, 'end-1c')) - (text_editor.get(1.0, 'end-1c').count(' '))
        status_bar.config(text=f'Words:{words}, Characters:{chars}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)
# ------------------------------------ End status bar ---------------------------------------------------------

# ################################### Main menu fuctionality ##################################################
url = ''


# new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


# new command
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


# open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                     filetypes=(('TEXT FILE', '*.txt'), ('ALL FILE', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    else:
        return
    file_name = os.path.basename(url)
    main_application.title(file_name)


file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)
file.add_separator()


# save functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('TEXT FILE', '*.txt'), ('ALL FILE', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)


# save as functionality
def save_as_file(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('TEXT FILE', '*.txt'), ('ALL FILE', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Shift+S',
                 command=save_as_file)
file.add_separator()


# exit functionality
def exit_func():
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save this file?')
            if mbox is True:
                if url:
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('TEXT FILE', '*.txt'), ('ALL FILE', '*.*')))
                    content2 = text_editor.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Alt+F4', command=exit_func)


# # edit functionality
# ######### find functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_delete('match', 1.0, tk.END)
        matches = 0
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0, 0)

    find_frame = ttk.LabelFrame(find_dialog, text='Find/Replace')
    find_frame.pack(pady=20)

    find_label = ttk.Label(find_frame, text='Find: ')
    replace_label = ttk.Label(find_frame, text='Replace: ')

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    find_label.grid(row=0, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)

    replace_label.grid(row=1, column=0, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=1, padx=4, pady=4)
    replace_button.grid(row=2, column=2, padx=4, pady=4)

    find_dialog.mainloop()


edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT,
                 accelerator='Ctrl+C', command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT,
                 accelerator='Ctrl+V', command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT,
                 accelerator='Ctrl+X', command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT,
                 accelerator='Ctrl+Alt+X', command=lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

# view functionality
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, onvalue=1, offvalue=0, variable=show_toolbar,
                     compound=tk.LEFT, accelerator='Ctrl+R', command=hide_toolbar)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, onvalue=1, offvalue=0, variable=show_statusbar,
                     compound=tk.LEFT, accelerator='Ctrl+?', command=hide_statusbar)

def change_theme():
    chosen_color = color_choice.get()
    color_tuple = color_dict.get(chosen_color)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon[count], variable=color_choice, compound=tk.LEFT, command=change_theme)
    count += 1

# shortcut functionality
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


# -----------------------------------End Main menu fuctionality--------------------------------
main_application.config(menu=main_menu)
main_application.mainloop()
