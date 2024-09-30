from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Domestic(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')

        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['NID by size class', '1', '2', '3']
        
        liste1 = ['SUI', 'SUD', 'BOST', 'EQUID', 'CAB', 'EQUA']

        liste1Lab = ['Sus sp.', 'Sus domesticus', 'Bos taurus', 'Equus sp.', 'Horse','Donkey']

        liste2 = ['CAPRI', 'CAPRA', 'CAPRH', 'OVIA']

        liste2Lab = ['Caprinae', 'Capra sp.', 'Capra hircus', 'Ovis aries']

        liste3 = ['CANI', 'CANF', 'FEL', 'FELIC', 'SCARN', 'LCARN']

        liste3Lab = ['Canis sp.', 'Canis familiaris', 'Felis sp.', 'Felis catus', 'Small carnivore', 'Large carnivore']


        listeNid = ['MAMI', 'MAM2', 'MAM12', 'MAM3', 'MAM23', 'MAM4', 'MAM34', 'MAM5', 'MAM45']
        
        # Première partie des catégories
        self.Frame1 = Frame(self, bg='#D9D9D9')
        self.Frame1.pack(expand=True, fill=BOTH)

        for i in listeCat:
            self.FrameCat = Frame(self.Frame1, bd=1, relief=SOLID, bg='white')
            self.FrameCat.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

            if (i == '1'):
                for id,un in enumerate(liste1):
                    self.Frame11 = Frame(self.FrameCat,bg='white')
                    self.Frame11.pack(anchor='w')
                    self.Radio1 = Radiobutton(self.Frame11, text=un, value=un,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = un :self.controller.updateTaxon(val))
                    self.Radio1.pack(side=LEFT)

                    self.Label1 = Label(self.Frame11, text=liste1Lab[id], font=("Roboto 12"), 
                                            bg="white",fg='#45464b')
                    self.Label1.pack(side=LEFT)

            if (i == '2'):
                for id,de in enumerate(liste2):
                    self.Frame2 = Frame(self.FrameCat,bg='white')
                    self.Frame2.pack(anchor='w')
                    self.Radio2 = Radiobutton(self.Frame2, text=de, value=de,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = de :self.controller.updateTaxon(val))
                    self.Radio2.pack(side=LEFT)

                    self.Label2 = Label(self.Frame2, text=liste2Lab[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.Label2.pack(side=LEFT)


            if (i == '3'):
                for id,tro in enumerate(liste3):
                    self.Frame3 = Frame(self.FrameCat,bg='white')
                    self.Frame3.pack(anchor='w')
                    self.Radio3 = Radiobutton(self.Frame3, text=tro, value=tro,
                                                  variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                  command=lambda val = tro :self.controller.updateTaxon(val))
                    self.Radio3.pack(side=LEFT)

                    self.Label3 = Label(self.Frame3, text=liste3Lab[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.Label3.pack()
 
            if (i == 'NID by size class'):
                for nid in listeNid:
                    self.FrameNID = Frame(self.FrameCat)
                    self.FrameNID.pack(anchor='w')
                    self.RadioNID = Radiobutton(self.FrameNID, text=nid, value=nid,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = nid :self.controller.updateTaxon(val))
                    self.RadioNID.pack()
