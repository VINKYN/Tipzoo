from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class NMBInterface(Frame):
    def __init__(self, master=None, controller=None,bulk=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.configure(bg='white')

        self.bulk = bulk

        font_button = ("Helvetica  13 bold" )

        font_ecriture =("Helvetica  10" )

        color_button = '#F2E2CE'

        color_bleu ='#b9e2f9'

        color_police ='#1b1b1b'

        self.custom_font = ('Helvetica', 13)       
        # Appliquer la police Roboto en taille 12
        self.pack(expand=True, fill='both')

        """self.Frame1 = Frame(self,bg="red")
        self.Frame1.pack(side=TOP, fill='both')

        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')"""

        self.Frame2 = Frame(self,bg="pink")
        self.Frame2.pack(fill=BOTH, expand=False)

        self.Frame4 = Frame(self,bg='red')
        self.Frame4.pack(expand=True,fill=BOTH)


        self.FrameNMB = Frame(self.Frame4)
        self.FrameNMB.pack(expand=True,fill=BOTH)

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()

        self.VarFM = StringVar()
        self.VarFM.set(self.controller.get_anat())

        self.tc = self.controller.tapho_category()

        self.FrameDroite = Frame(self.FrameNMB,bg=color_button)
        self.FrameDroite.pack(side=LEFT, fill='both', expand=True)
        self.FrameHaut = Frame(self.FrameDroite,bg=color_bleu,relief="solid",bd=1)
        self.FrameHaut.pack(side=TOP,fill="x",padx=10,pady=10)

        self.Bande = Bande(self.FrameHaut,self.controller,self.VarSpong,self.VarFrag,self.VarAgeCort)
        self.Bande.pack()

        

        self.FrameMid = Frame(self.FrameDroite,bg='white',relief="solid",bd=1)
        self.FrameMid.pack(fill='both',padx=10,expand=True)

        self.FrameMidhaut = Frame(self.FrameMid,bg='white')
        self.FrameMidhaut.pack(expand=True,fill="both")

        self.FrameMol = Frame(self.FrameMidhaut)
        self.FrameMol.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

        self.LabelMol = Label(self.FrameMol,text='Mollusca',font=font_ecriture)
        self.LabelMol.pack()

        self.FrameM =Frame(self.FrameMol)
        self.FrameM.pack(anchor="w")

        self.CheckM1 = Radiobutton(self.FrameM, text="UMB",font=font_ecriture,
                            variable= self.VarFM,value='UMB',
                            command=lambda:self.controller.update_fish( self.VarFM.get()))
        self.CheckM1.pack(side=LEFT, padx=20)

        self.LabelP = Label(self.FrameM,text='Umbo(univalves, e.g. limpet centers)',font=font_ecriture)
        self.LabelP.pack(side=LEFT,padx=(0,20))

        self.FrameM2 =Frame(self.FrameMol)
        self.FrameM2.pack(anchor="w")

        self.CheckM2 = Radiobutton(self.FrameM2, text="VLV",font=font_ecriture,
                            variable= self.VarFM,value='VLV',
                            command=lambda:self.controller.update_fish(self.VarFM.get()))
        self.CheckM2.pack(side=LEFT, padx=20)

        self.LabelM2 = Label(self.FrameM2,text='Valve(bivalves, e.g., mussels)',font=font_ecriture)
        self.LabelM2.pack(side=LEFT,padx=(0,20))
        
        listFish = ["Ethmoid", "Supraoccipital", "Prefrontal", "Exoccipital", "Vomer",
                    "Mesopterygoid", "Mesethmoid", "Metapterygoid", "Alisphenoid", "Hyomandibular",
                    "Parasphenoid", "Symplectic", "Parietal", "Interhyal", "Sphenotic",
                    "Epihyal", "Pterrotic", "Ceratohyal", "Epiotic", "Hypohyal",
                    "Opisthotic", "Basihyal", "Prootic", "Pharyngeal plate", "Otolith",
                    "Epibranchial", "Investing bones", "Ceratobranchial", "Nasal", "Hypobranchial",
                    "Frontal", "Basibranchial", "Supratemporal", "Basibranchial plate", "Supraorbital",
                    "Urohyal", "Lachrymal", "Pharyngobranchial", "Suborbital", "Postemporal",
                    "Dentary", "Supracleithrum", "Angular", "Cleithrum", "Retroangular",
                    "Postcleithrum", "Supraopercle", "Quadrate", "Preopercle", "Mesocoracoid",
                    "Supramaxilla", "Radials", "Opercle", "Basipterygium", "Subopercle",
                    "Interhaemal spine", "Interopercle", "Precaudal vertebra", "Branchiostegal ray", "Penultimate vertebra",
                    "Palatine", "Ultimate vertebra", "Ectopterygoid", "Hypural", "Epural",
                    "Expanded neural spine", "Expanded haemal spine", "Basioccipital", "Caudal bone plate", "Uroneural"
                ]
        

        
        self.FrameFish = Frame(self.FrameMidhaut)
        self.FrameFish.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

        self.LabelFish = Label(self.FrameFish,text='Fish Bones :',font=font_ecriture)
        self.LabelFish.pack()

        self.FrameF =Frame(self.FrameFish)
        self.FrameF.pack(anchor="w")

        self.comboFish = ttk.Combobox(self.FrameF,values=listFish,font=font_ecriture,
                                        textvariable=self.VarFM,state='readonly')
        self.comboFish.pack(side=LEFT,padx=20,pady=10)

        self.comboFish.bind("<<ComboboxSelected>>",lambda event:self.controller.update_fish(self.VarFM.get()))

        popdown = self.comboFish.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboFish)
        self.comboFish.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboFish['font'])

        self.FrameBas = Frame(self.FrameDroite,bg=color_button)
        self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)


        self.Side = Side(self.FrameBas,self.controller,self.VarSide)
        self.Side.pack(side=LEFT)


        self.FrameBouton = Frame(self.FrameBas,background=color_button)
        self.FrameBouton.pack(side=LEFT)

        if self.bulk.get_bulk_species():

            self.ButtonTa = Button(self.FrameBouton, text="> Go to Tapho",bd=0,font=font_button,bg=color_police,fg='white')
            self.ButtonTa.pack(padx=20,side=LEFT)
        else :
            self.ButtonSpe = Button(self.FrameBouton, text="> Go to Species",bd=0,font=font_button,bg=color_police,fg='white',
                                    command=self.controller.show_Species_page)
            self.ButtonSpe.pack(padx=20,side=LEFT)



        if self.bulk.get_bulk_species() or self.tc == 'Yes':

            self.ButtonBa = Button(self.FrameBouton, text="> Create \rNew Record",bd=0,font=font_button,bg=color_police,fg='white',
                                    command=self.controller.show_new_Base_create)
            self.ButtonBa.pack(padx=20,side=LEFT)

    
        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()
