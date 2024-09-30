from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class Side(Frame):
    def __init__(self, master=None, controller=None, var1=None):
        super().__init__(master)
        
        color_bleu = '#b9e2f9'
        font_button = ("Helvetica 13 ")
        self.master = master
        self.configure(bg=color_bleu,bd=1,relief=SOLID)
        self.pack()
        self.controller = controller

        self.VarSide = var1

        self.VarSide.set(self.controller.getSide())

        self.FrameSide = Frame(self, bg=color_bleu)
        self.FrameSide.pack(pady=10, fill='x', expand=True)

        self.LabelSide = Label(self.FrameSide, text='Side :', font=font_button, bg=color_bleu)
        self.LabelSide.pack(side=LEFT, padx=10)

        self.RadioLF = Radiobutton(self.FrameSide, text="LEFT", variable=self.VarSide,
                                    value='Left', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarSide.get(), 'Skel_Side'))
        self.RadioLF.pack(side=LEFT, padx=(0,10))

        self.RadioRG = Radiobutton(self.FrameSide, text="RIGHT", variable=self.VarSide,
                                    value='Right', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarSide.get(), 'Skel_Side'))
        self.RadioRG.pack(side=LEFT, padx=10)

        self.RadioQ = Radiobutton(self.FrameSide, text="?", variable=self.VarSide,
                                    value='?', font=font_button, bg=color_bleu,
                                    command=lambda: self.controller.update_skel(self.VarSide.get(), 'Skel_Side'))
        self.RadioQ.pack(side=LEFT, padx=10)
