from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Species.SpeciesBas import SpeciesBas
from View.Species.SpeciesHaut  import SpeciesHaut

from View.Species.pages.European import European
from View.Species.pages.Mollusca import Mollusca
from View.Species.pages.AfricanCar import AfricanCar
from View.Species.pages.AfricanHerb import AfricanHerb
from View.Species.pages.Artic import Artic
from View.Species.pages.Birds import Birds
from View.Species.pages.Domestic import Domestic
from View.Species.pages.Fish import Fish



class Species(Frame,):
    def __init__(self, master=None,controller=None,bulk=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')
        self.pack(expand=True, fill='both')

        self.controller = controller

        
        self.bulk = bulk

        font_button = ("Helvetica  13 bold" )

        font_ecriture =("Helvetica  16" )

        color_button = '#F2E2CE'

        color_bleu ='#b9e2f9'

        color_police ='#1b1b1b'

        style = ttk.Style()
        # Configuration de la couleur de fond normale des onglets
        style.configure('TNotebook.Tab', padding=[20, 10])


        """self.Frame1 = Frame(self)
        self.Frame1.pack(side=TOP, fill='both')
        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')"""


        self.Frame2 = Frame(self, bg='pink')
        self.Frame2.pack(fill=BOTH, expand=True)


        self.VarSpecies = StringVar()
        self.VarSpecies.set(self.controller.getspe())

        self.FrameHaut = Frame(self.Frame2)
        self.FrameHaut.pack(side=TOP, fill='both')
        self.SpeciesHaut = SpeciesHaut(self.FrameHaut,self.VarSpecies,self.controller)
        self.SpeciesHaut.pack(side=LEFT)

       

        self.Notebook = ttk.Notebook(self.Frame2)
        style = ttk.Style()

        

        self.European = European(self.Notebook,self.VarSpecies,self.controller)
        self.Domestic = Domestic(self.Notebook,self.VarSpecies,self.controller)
        self.AfricanCar = AfricanCar(self.Notebook,self.VarSpecies,self.controller)
        self.AfricanHerb = AfricanHerb(self.Notebook,self.VarSpecies,self.controller)
        self.Artic = Artic(self.Notebook,self.VarSpecies,self.controller)
        self.Birds = Birds(self.Notebook,self.VarSpecies,self.controller)
        self.Fish = Fish(self.Notebook,self.VarSpecies,self.controller)
        self.Mollusca = Mollusca(self.Notebook,self.VarSpecies,self.controller)

        ListeTab =["European wild macrofauna","Domestic taxa","African carnivores",
                   "African herbivores","Arctic mammals","Birds","Fish","Mollusca"]
        ListePage =[self.European,self.Domestic,self.AfricanCar,self.AfricanHerb,self.Artic
                    ,self.Birds,self.Fish,self.Mollusca]
        
        for tab, page in zip(ListeTab, ListePage):
            self.Notebook.add(page, text=tab)

        self.Notebook.pack(expand=True, fill='both')




    

        self.FrameBas = Frame(self.Frame2)
        self.FrameBas.pack(side=BOTTOM, fill='both')
        self.SpeciesBas = SpeciesBas(self.FrameBas,self.VarSpecies,self.controller)
        self.SpeciesBas.pack(side=LEFT)
        


        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')
        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()
