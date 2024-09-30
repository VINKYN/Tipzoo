from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk



class SpeciesBas(Frame,Variable):
    def __init__(self, master=None,variable=None,controller = None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#F2E2CE')
        self.pack(expand=True, fill='both')

        self.controller = controller
        self.VarSpecies = variable

        self.FrameBas = Frame(self,bg='white',bd=1,relief="solid")
        self.FrameBas.pack(pady=10)

        self.RadioNID = Radiobutton(self.FrameBas , text="NID",variable= self.VarSpecies,bg='white',
                                    value='NID',font=("Roboto 12"),
                                     command=lambda val = 'NID' :self.controller.updateTaxon(val))
        self.RadioNID.pack(side=LEFT,padx=10)

        #self.RadioAutre = Radiobutton(self.FrameBas , text="Autre....",bg='white',
         #                             variable=self.VarSpecies,value='Other',font=("Roboto 12"))
        #self.RadioAutre.pack(side=LEFT,padx=10)
        
        self.ButtonTapho = Button(self.FrameBas,text="Go to Tapho",bg='#1b1b1b',
                                fg='#F2E2CE',font="Helvetica  13 bold" ,bd=0,)
        self.ButtonTapho.pack(padx=40,pady=10),