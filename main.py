# TKinter project **Notepad**

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

class Notepad:
    root = Tk()
    root.title("My Notepad - Untitled")
    root.geometry("1400x700")
    Textarea = Text(root, font=("arial", 15))
    menubar = Menu(root,font=("consolas"))
    Filemenu = Menu(menubar, tearoff=0)
    Editmenu = Menu(menubar, tearoff=0)
    Helpmenu = Menu(menubar, tearoff=0)

    Scrollbar = Scrollbar(Textarea)
    file = None

    def __init__(self):
        # make text area resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.Textarea.grid(sticky=N+S+E+W)

        # file menu
        self.Filemenu.add_command(label="New File", command=self.newFile)
        self.Filemenu.add_command(label="Save", command=self.saveFile)
        self.Filemenu.add_command(label="Open file...", command=self.openFile)
        self.Filemenu.add_separator()
        self.Filemenu.add_command(label="Exit", activebackground="red", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.Filemenu)

        # edit menu
        self.Editmenu.add_command(label="Select all", accelerator="(Ctrl+A)", command=lambda: self.Textarea.tag_add('sel', 1.0, 'end'))
        self.Editmenu.add_command(label="Cut", accelerator="(Ctrl+X)", command=lambda: self.root.focus_get().event_generate("<<Cut>>"))
        self.Editmenu.add_command(label="Copy", accelerator="(Ctrl+A)", command=lambda: self.root.focus_get().event_generate("<<Copy>>"))
        self.Editmenu.add_command(label="Paste", accelerator="(Ctrl+V)", command=lambda: self.root.focus_get().event_generate("<<Paste>>"))
        self.menubar.add_cascade(label="Edit", menu=self.Editmenu)

        # help menu
        self.Helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.Helpmenu)

        self.root.config(menu=self.menubar)
        self.Scrollbar.pack(side='right', fill=Y)

        self.Scrollbar.config(command=self.Textarea.yview)
        self.Textarea.config(yscrollcommand=self.Scrollbar.set)
        self.root.bind("<Control-s>", lambda e: self.saveFile())
        self.root.bind("<Control-n>", lambda d: self.newFile())
        self.root.bind("<Control-o>", lambda r: self.openFile())
    
    def quit(self):
        self.root.destroy()

    def about(self):
        showinfo("About", "Just some text for no reason")

    def Run(self):
        self.root.mainloop()
    
    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All files", "*.*"),
                                               ("text document", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title("My Notepad - "+os.path.basename(self.file))
            self.Textarea.delete(1.0, END)
            file = open(self.file, 'r')
            self.Textarea.insert(1.0, file.read())
            file.close()
    
    def newFile(self):
        self.root.title("My Notepad - Untitled")
        self.file = None
        self.Textarea.delete(1.0, END)

    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt",
                                          defaultextension=".txt",
                                          filetypes=[("All files", "*.*"),
                                                     ("text document", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, 'w')
                file.write(self.Textarea.get(1.0, END))
                file.close()

                self.root.title("My Notepad - "+os.path.basename(self.file))
        else:
            file = open(self.file, 'w')
            file.write(self.Textarea.get(1.0, END))
            file.close()


notepad = Notepad()
notepad.Run()