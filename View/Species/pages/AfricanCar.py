from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class AfricanCar(Frame):
    def __init__(self, master=None, variable=None,controller = None):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')
        self.pack(expand=True, fill='both')

        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['Scarn', 'Lcarn']
        
        listeScarn =['VULPI', 'CANI', 'PROT', 'FEL', 'CARC', 'SCARN']

        listeScarnLab =  ['Vulpes sp.', 'Canis sp.', 'Proteles sp.', 'Felis sp.', 'Caracal sp.', 'Small carnivore']


        listeLcarn = ['LCARN','LYC', 'PLEO', 'PPAR', 'ACIN', 'MEGAN', 'DINO', 'PARAH', 'CROC', 'HYEN', 'CHASM']


        listeLCARLabel = ['Large Carnivore','Lycaon sp.', 'Panthera leo', 'Panthera pardus', 'Acinonyx sp.', 'Megantereon sp.', 'Dinofelis sp.', 'Parahyaena brunnea', 'Crocuta crocuta', 'Hyaena hyaena', 'Chasmaporthetes sp.']

        
        # Première partie des catégories
        self.Frame1 = Frame(self, bg='#D9D9D9')
        self.Frame1.pack(expand=True, fill=BOTH)

        for i in listeCat:
            self.FrameCat = Frame(self.Frame1, bd=1, relief=SOLID, bg='white')
            self.FrameCat.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

            self.LabelCat2 = Label(self.FrameCat, text=i, font=("Roboto 12"), bg="white")
            self.LabelCat2.pack(anchor='w', pady=5)


            if (i == 'Scarn'):
                for id,un in enumerate(listeScarn):
                    self.Frame11 = Frame(self.FrameCat,bg='white')
                    self.Frame11.pack(anchor='w',fill='y',expand=True)
                    self.Radio1 = Radiobutton(self.Frame11, text=un, value=un,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = un :self.controller.updateTaxon(val))
                    self.Radio1.pack(side=LEFT)

                    self.Label1 = Label(self.Frame11, text=listeScarnLab[id], font=("Roboto 12"), 
                                            bg="white",fg='#45464b')
                    self.Label1.pack(side=LEFT)

            if (i == 'Lcarn'):
                for id,de in enumerate(listeLcarn):
                    self.Frame2 = Frame(self.FrameCat,bg='white')
                    self.Frame2.pack(anchor='w',fill='y',expand=True)
                    self.Radio2 = Radiobutton(self.Frame2, text=de, value=de,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = de :self.controller.updateTaxon(val))
                    self.Radio2.pack(side=LEFT)

                    self.Label2 = Label(self.Frame2, text=listeLCARLabel[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.Label2.pack(side=LEFT)
                    
                self.LabelCredit = Label(self.FrameCat,text="code list by R Hanon",
                                         bg="white",fg='#45464b',font=("Roboto 10"))
                self.LabelCredit.pack(anchor='w',pady=(0,5))
