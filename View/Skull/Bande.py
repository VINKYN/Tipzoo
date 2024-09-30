from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class Bande(Frame, Variable):
    def __init__(self, master=None, controller=None, var1=None, var2=None, var3=None):
        super().__init__(master)
        
        color_bleu = '#b9e2f9'
        font_button = ("Helvetica 13 ")
        
        self.master = master
        self.configure(bg=color_bleu)
        self.pack(fill='x')
        self.controller = controller

        self.VarSpong = var1
        self.VarFrag = var2
        self.VarAgeCort = var3

        self.FrameBas = Frame(self, bg=color_bleu)
        self.FrameBas.pack(pady=10, fill='x', expand=True)

        self.VarFrag.set(self.controller.getFrag())

        self.RadioCo = Radiobutton(self.FrameBas, text="CO", variable=self.VarFrag,
                                    value='CO', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarFrag.get(), 'Skel_Frag'))
        self.RadioCo.pack(side=LEFT, padx=10)

        self.RadioACo = Radiobutton(self.FrameBas, text="ACO", variable=self.VarFrag,
                                    value='ACO', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarFrag.get(), 'Skel_Frag'))
        self.RadioACo.pack(side=LEFT, padx=10)

        self.RadioFR = Radiobutton(self.FrameBas, text="FR", variable=self.VarFrag,
                                    value='FR', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarFrag.get(), 'Skel_Frag'))
        self.RadioFR.pack(side=LEFT, padx=10)

        self.VarSpong.set(self.controller.getSPong())

        self.CheckSpon = Checkbutton(self.FrameBas, text="Spongy portion?", font=font_button,
                                    variable=self.VarSpong, onvalue=1, offvalue=0, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarSpong.get(), 'Skel_Spongy'))
        self.CheckSpon.pack(side=LEFT, padx=10)

        self.LabelAge = Label(self.FrameBas, text='Age Cort :', font=font_button, bg=color_bleu)
        self.LabelAge.pack(side=LEFT, padx=10)

        self.VarAgeCort.set(self.controller.getAge())

        self.RadioF = Radiobutton(self.FrameBas, text="F", variable=self.VarAgeCort,
                                    value='F', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
        self.RadioF.pack(side=LEFT, padx=(0,10))

        self.RadioJ = Radiobutton(self.FrameBas, text="J", variable=self.VarAgeCort,
                                    value='J', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
        self.RadioJ.pack(side=LEFT, padx=10)

        self.RadioA = Radiobutton(self.FrameBas, text="A", variable=self.VarAgeCort,
                                    value='A', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
        self.RadioA.pack(side=LEFT, padx=10)

        self.RadioQ = Radiobutton(self.FrameBas, text="?", variable=self.VarAgeCort,
                                    value='?', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
        self.RadioQ.pack(side=LEFT, padx=10)
