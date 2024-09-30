from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Birds(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')

        self.controller = controller
        self.VarSpecies = variable

        listeCat = ['1', '2', '3']
        
        liste1 = ['FRA', 'MANX', 'ALE', 'PLA', 'HER', 'LAC', 'LAS', 'ALT', 'FUL', 'CEP', 'URA']

        liste1Lab = ['Fratercula arctica','Puffinus puffinus','Alle','Alcidae','Pluvialis dominica','Larus argentatus','Larus canus',
                     'Larus sp','Alca torda','Fulmarus glacialis','Cepphus grylle']
        
        liste1C = ['Atlantic puffin', 'manx shearwater', 'little auk/dovekie', 'Indeterminate alcidae species',
                    'American golden plover', 'herring gull', 'common gull/mew gull', 
                    'indeterminate gull species', 'razorbill', 'northern fulmar', 
                    'black guillemot', 'guillemot/common murre']


        liste2 = ['URIA', 'SUB', 'SOM', 'PHC', 'PHSP', 'SOL', 'LAM', 'LAG', 'ANSP', 'RAV', 'AVES']

        liste2Lab = ['Uria sp.', 'Morus bassanus', 'Somaterla molljssltna', 'Phalacrocorax carbo', 'Phalacrocorax sp.', 'Bubo scandiacus', 'Lagopus muta', 'Lagopus sp.', 'Anser sp.', 'Corvus corax', 'Bird']

        liste2C = ['guillemot/murre species', 'northern gannet', 'common eider', 
                   'great cormorant', 'cormorant/shag species', 'snowy owl', 'rock ptarmigan',
                     'Indeterminate lagopus species', 'goose', 'common raven', 'indeterminate bird species']


        liste3 = ['LYT', 'TEU', 'TUM', 'PLU', 'PHE', 'PIC', 'COR', 'PAS', 'CRV', 'PYR']

        liste3Lab = ['Lyrurus tetrlx', 'Tetrao urogallus', 'Turdus merula', 'Pluvialis sp.', 'Phasianidae', 'Pica pica', 'Corvidae', 'Passeriforms', 'Corvus corone', 'Pyrrhocorax graculus']


        liste3C =['Black grouse', 'Western capercaillie', 'Common Blackbird', 'Indeterminate plover',
                   'Phasianidae', 'Eurasian Magpie', 'Corvids', 'Passerine', 'Carrion crow', 'Alpine Chough']

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


            if (i == '3'):
                for id,tro in enumerate(liste3):
                    self.Frame3 = Frame(self.FrameCat,bg='white')
                    self.Frame3.pack(anchor='w',fill='y',expand=True)
                    self.Radio3 = Radiobutton(self.Frame3, text=tro, value=tro,
                                                  variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                  command=lambda val = tro :self.controller.updateTaxon(val))
                    self.Radio3.pack(side=LEFT)

                    self.Label3 = Label(self.Frame3, text=liste3Lab[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.Label3.pack(side=LEFT)

                    self.Label3C = Label(self.Frame3, text=liste3C[id], font=("Roboto 12"), 
                                           bg="white",fg='black')
                    self.Label3C.pack(side=LEFT,padx=10)

