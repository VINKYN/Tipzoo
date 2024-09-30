from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from View.Home import HomeInterface

class AllValueInterface(Frame):
    def __init__(self, master=None, controller=None,label =None):
        super().__init__(master)

        self.master = master
        self.controller = controller  # Assigning the controller
        self.configure(bg='white')
        self.pack(expand=True, fill='both')
        self.label = label

        color_button = '#F2E2CE'
        font_button = ("Helvetica  13 bold" )

        self.Frame1 = Frame(self, bg='#b9e2f9')
        self.Frame1.pack(fill='x', side=TOP,ipady=20)  # Ajout de padx et pady pour l'espacement

        self.ButtonMenu = Button(self.Frame1, text="Home", width=15, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=font_button,
                                command=self.controller.show_home_page)
        self.ButtonMenu.pack(side=LEFT, padx=20)  # Ajout de padx pour l'espacement à gauche

        if label == "Spatial":
            self.ButtonDelete = Button(self.Frame1, text="Delete", width=15, height=2, background=color_button,
                                relief='solid', bd=1, activebackground='white', font=font_button,
                                command=self.controller.delete)
            self.ButtonDelete.pack(side=LEFT, padx=20)

        self.FrameTab = Frame(self,bg='white')
        self.FrameTab.pack(expand=True,fill=BOTH)

        style = ttk.Style(self.FrameTab)
        style.configure('Treeview', rowheight=40) 

        style.configure('Treeview.Heading', rowheight=40) 
        
        colonnes = self.controller.get_column(self.label)

        self.treeview = ttk.Treeview(self.FrameTab,columns=colonnes , show='headings',
                                selectmode='browse')
        
        for i in colonnes:
            self.treeview.heading(i, text=i)
            self.treeview.column(i, width=int(self.winfo_screenwidth()/(len(colonnes))))
    
        valTree = self.controller.getAll(self.label)

        self.treeview.tag_configure('1', background='white')
        self.treeview.tag_configure('2', background='#F7F7F7')
        tag = 1
        for colonnes in valTree:
            if tag == 1 :
                self.treeview.insert('', END, values=colonnes, tags = (tag))
                tag += 1
            else :
                self.treeview.insert('', END, values=colonnes, tags = (tag))
                tag = 1

        self.Scrolbar = ttk.Scrollbar(self.FrameTab)
        self.Scrolbar.configure(command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.Scrolbar.set)
        self.Scrolbar.pack(side=RIGHT, fill='y')

        self.treeview.pack(expand=True, fill='both',side=LEFT)


