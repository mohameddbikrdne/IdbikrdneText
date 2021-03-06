from tkinter import *
from tkinter import filedialog

def new_file():
    text.delete(0.0,END)
def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data= file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data)
def save_file():
    filename = "Idbikrdne.text"
    data=text.get(0.0,END)
    file1=open(filename,'w')
    file1.write(data)
def save_as():
    file1=filedialog.asksaveasfile(mode='w')
    data=text.get(0.0,END)
    file1.write(data)

gui=Tk()
gui.title("IdbikrdneText")
gui.iconbitmap(r"icon.ico")
gui.geometry("600x500")
text=Text(gui)
text.pack()
mynenu=Menu()
list1=Menu()
list1.add_command(label='New File',command=new_file)
list1.add_command(label='Open File',command=open_file)
list1.add_command(label='Save',command=save_file)
list1.add_command(label='Save as',command=save_as)
list1.add_command(label='Exit',command=gui.quit)
mynenu.add_cascade(label='File', menu=list1)
gui.config(menu = mynenu)
gui.mainloop()
