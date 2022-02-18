from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Mini notepad")
root.minsize(650, 650)
root.maxsize(650, 650)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
exit_image = ImageTk.PhotoImage(Image.open('exit.jpg'))
save_image = ImageTk.PhotoImage(Image.open('save.png'))

label_fileName = Label(root, text = "File Name: ")
label_fileName.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_fileName = Entry(root)
input_fileName.place(relx = 0.46, rely = 0.03, anchor = CENTER)

textarea_text = Text(root, height = 28, width = 70)
textarea_text.place(relx = 0.5, rely = 0.5, anchor = CENTER)

name = ""

def OpenFile():
    global name
    textarea_text.delete(1.0, END)
    input_fileName.delete(0, END)
    popup_file = filedialog.askopenfilename(title = 'Open Text Files', filetypes = (("Text Files", '*.txt'),))
    print(popup_file)
    name = os.path.basename(popup_file)
    formattedName = name.split('.') [0]
    input_fileName.insert(END, formattedName)
    root.title(formattedName)
    popup_file = open(name, 'r')
    para = popup_file.read()
    textarea_text.insert(END, para)
    popup_file.close()
    
def SaveFile():
    fileName = input_fileName.get()
    file = open(fileName+'.txt', 'w')
    data = textarea_text.get(1.0, END)
    file.write(data)
    input_fileName.delete(0, END)
    textarea_text.delete(1.0, END)
    messagebox.showinfo("Success", "Your file was saved.")
    
def CloseFile():
    root.destroy()
    
button_open = Button(root, image = open_image, text = "Open file", command = OpenFile)
button_open.place(relx = 0.03, rely = 0.03, anchor = CENTER)

button_save = Button(root, image = save_image, text = "Save file", command = SaveFile)
button_save.place(relx = 0.09, rely = 0.03, anchor = CENTER)

button_destroy = Button(root, image = exit_image, text = "Exit Application", command = CloseFile)
button_destroy.place(relx = 0.15, rely = 0.03, anchor = CENTER)

root.mainloop()