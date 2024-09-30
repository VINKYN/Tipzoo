from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class Menu(Frame):
    def __init__(self, master=None,controller=None):
        super().__init__(master)

        self.master = master
        self.controller=controller
        self.configure(bg='white')
        self.pack( fill='x')

        


        self.Frame1 = Frame(self,bg='#b9e2f9')
        self.Frame1.pack(fill='both',expand=True,ipady=10)

        self.ButtonHome = Button(self.Frame1, text="Home", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),
                                command=self.controller.show_home_page)
        self.ButtonHome.pack(side=LEFT, padx=20)

        self.ButtonBase = Button(self.Frame1, text="Go to Base", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),state='disabled',
                                command=self.controller.show_base_page)
        self.ButtonBase.pack(side=LEFT, padx=20)

        self.ButtonSkel = Button(self.Frame1, text="Go to Skel", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),state='disabled',
                                command=self.controller.show_skel_page)
        self.ButtonSkel.pack(side=LEFT, padx=20)

        self.ButtonSpe = Button(self.Frame1, text="Go to Species", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),state='disabled',
                                command=self.controller.show_spe_page)
        self.ButtonSpe.pack(side=LEFT, padx=20)

        self.ButtonTapho = Button(self.Frame1, text="Go to Tapho", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),state='disabled')
        self.ButtonTapho.pack(side=LEFT, padx=20)

        self.ButtonCut = Button(self.Frame1, text="Go to Cut", width=10, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Helvetica", 12),state='disabled')
        self.ButtonCut.pack(side=LEFT, padx=20)


        b , sk , s = self.controller.get_menu()


        if b :
            self.ButtonBase.config(state='normal')
        if s :
            self.ButtonSpe.config(state='normal')
        if sk :
            self.ButtonSkel.config(state='normal')


