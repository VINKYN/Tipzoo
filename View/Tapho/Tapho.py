from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

from Base.treeview_haut import Treeview_haut
from Base.Menu import Menu
from Tapho.TaphoBase import frameBase
from Tapho.TaphoDetails import frameDetail

class Tapho(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')

        self.pack(expand=True, fill='both')

        self.Frame1 = Frame(self)
        self.Frame1.pack(side=TOP, fill='both')
        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')

        self.Frame2 = Frame(self, bg='pink')
        self.Frame2.pack(fill=BOTH, expand=True)

        self.Notebook = ttk.Notebook(self.Frame2)

        self.frameBase = frameBase(self.Notebook)
        self.frameBase.pack(fill='both', expand=True)  # Réglez expand et fill ici
        self.frameDetail = frameDetail(self.Notebook)
        self.frameDetail.pack(fill='both', expand=True)  # Réglez expand et fill ici

        self.Notebook.add(self.frameBase, text="BASE (naked eye)")
        self.Notebook.add(self.frameDetail, text="DETAILS (microscopic)")

        self.Notebook.pack(expand=True, fill='both')  # Réglez expand et fill ici

        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')
        self.Menu = Menu(self.Frame3)
        self.Menu.pack()
