from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class SpeciesHaut(Frame):
    def __init__(self, master=None,variable=None,controller=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#F2E2CE')
        self.pack(expand=True, fill='both')

        self.controller = controller
        self.VarSpecies = variable

        self.VarObs = StringVar()
        varObs = self.controller.getObs()

        

            
        self.VarObs.set(varObs)

        self.VarCheck = StringVar()
        self.VarImprove = StringVar()

        check, improve = self.controller.checkimprove()

        self.VarCheck.set(check)
        self.VarImprove.set(improve)

        self.FrameHaut = Frame(self,bg='white',bd=1,relief="solid")
        self.FrameHaut.pack(pady=10)

        self.LabelSpe = Label(self.FrameHaut,text='Species',font=("Roboto 12"),bg='white')
        self.LabelSpe.pack(side=LEFT,padx=(10,0))

        self.EntrySpe = Entry(self.FrameHaut ,font=("Roboto 12"),width=15,textvariable=self.VarSpecies)
        self.EntrySpe.pack(side=LEFT,padx=(0,10))
        """
        if varObs == None:
            self.EntrySpe.delete(0,END)
        else :
            self.VarObs.set(varObs)"""

        self.VarSpecies.trace_add("write",lambda *args: self.controller.updateTaxon(self.VarSpecies.get()))

        self.CheckTo = Checkbutton(self.FrameHaut , text="To Check",font=("Roboto 12"),bg='white',
                                   variable=self.VarCheck,onvalue='To Check',offvalue='',
                                   command=lambda:self.controller.updateCheckImprove(self.VarCheck.get(),'To Check'))
        self.CheckTo.pack(side=LEFT,padx=10)

        self.CheckImp = Checkbutton(self.FrameHaut , text="To Improve",font=("Roboto 12"),bg='white',
                                    variable=self.VarImprove,onvalue='To Improve',offvalue='',
                                    command=lambda:self.controller.updateCheckImprove(self.VarImprove.get(),'To Improve'))
        self.CheckImp.pack(side=LEFT,padx=10)

        self.LabelCom = Label(self.FrameHaut,text='Taxonomic observations',font=("Roboto 12"),bg='white')
        self.LabelCom.pack(side=LEFT,padx=10)

        self.EntryCom = Entry(self.FrameHaut ,font=("Roboto 12"),textvariable=self.VarObs)
        self.EntryCom.pack(side=LEFT,padx=(0,10),pady=10)

        if varObs == None:
            self.EntryCom.delete(0,END)
        else :
            self.VarObs.set(varObs)

        self.VarObs.trace_add("write",lambda *args: self.controller.updateObs(self.VarObs.get()))
        