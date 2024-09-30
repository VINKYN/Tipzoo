from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Mollusca(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')
        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['1']
        
        liste1 = ['PAT', 'MED', 'CLM', 'BUC', 'WLKSP', 'MOLSP']


        liste1Lab = ['Patella vulgata', 'Mytjlus edulis', 'Mya species', 'Buccinum undatum', 'Buccinum sp.', 'Mollusca']

        
        liste1C =  ['common limpet', 'common/blue mussel', 'indeterminate clam species', 'common/waved whelk', 
                    'indeterminate whelk species', 'indeterminate mollusk species']


        # Première partie des catégories
        self.Frame1 = Frame(self, bg='#D9D9D9')
        self.Frame1.pack(expand=True, fill=BOTH)

        for i in listeCat:
            self.FrameCat = Frame(self.Frame1, bd=1, relief=SOLID, bg='white')
            self.FrameCat.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

            if (i == '1'):
                for id,un in enumerate(liste1):
                    self.Frame11 = Frame(self.FrameCat,bg='white')
                    self.Frame11.pack(anchor='w',fill='y',expand=True)
                    self.Radio1 = Radiobutton(self.Frame11, text=un, value=un,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = un :self.controller.updateTaxon(val))
                    self.Radio1.pack(side=LEFT)

                    self.Label1 = Label(self.Frame11, text=liste1Lab[id], font=("Roboto 12"), 
                                            bg="white",fg='#45464b')
                    self.Label1.pack(side=LEFT)

                    self.Label1C = Label(self.Frame11, text=liste1C[id], font=("Roboto 12"), 
                                           bg="white",fg='black')
                    self.Label1C.pack(side=LEFT,padx=10)

           