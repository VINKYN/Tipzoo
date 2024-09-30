from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Fish(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')
        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['1', '2']
        
        liste1 = ['COD', 'LIN', 'HAD', 'GAD', 'SAL', 'TRT', 'CHR']


        liste1Lab = ['Gadus morhua', 'Molva molva', 'Melanogrammus aeglefinus', 'Gadidae', 'Salmo salar', 'Salmo trutta', 'Salvelinus alpinus']

        
        liste1C = ['Atlantic puffin', 'manx shearwater', 'little auk/dovekie', 'Indeterminate alcidae species',
                    'American golden plover', 'herring gull', 'common gull/mew gull', 
                    'indeterminate gull species', 'razorbill', 'northern fulmar', 
                    'black guillemot', 'guillemot/common murre']


        liste2 = ['SMD', 'HAL', 'ANA', 'BRO', 'POL', 'PLE', 'FISH']

        liste2Lab = ['Salmonidae', 'Hippoglossus hippoglossus', 'Anarhichas lupus', 'Brosme brosme', 'Pollachius virens', 'Pleuronectiformes', 'Fish']

        liste2C = ['salmon family', 'Atlantic halibut', 'Atlantic wolf fish', 'cusk/tusk/torsk', 'pollock/saithe', 'flatfishes', 'indeterminate fish species']


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

            if (i == '2'):
                for id,de in enumerate(liste2):
                    self.Frame2 = Frame(self.FrameCat,bg='white')
                    self.Frame2.pack(anchor='w',fill='y',expand=True)
                    self.Radio2 = Radiobutton(self.Frame2, text=de, value=de,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = de :self.controller.updateTaxon(val))
                    self.Radio2.pack(side=LEFT)

                    self.Label2 = Label(self.Frame2, text=liste2Lab[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.Label2.pack(side=LEFT)

                    self.Label2C = Label(self.Frame2, text=liste2C[id], font=("Roboto 12"), 
                                           bg="white",fg='black')
                    self.Label2C.pack(side=LEFT,padx=10)


