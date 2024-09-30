from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class NIDInterface(Frame):
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


        self.FrameNID = Frame(self.Frame4)
        self.FrameNID.pack(expand=True,fill=BOTH)

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()

        self.tc = self.controller.tapho_category()


        self.FrameDroite = Frame(self.FrameNID,bg=color_button)
        self.FrameDroite.pack(side=LEFT, fill='both', expand=True)
        self.FrameHaut = Frame(self.FrameDroite,bg=color_bleu,relief="solid",bd=1)
        self.FrameHaut.pack(side=TOP,fill="x",padx=10,pady=10)

        self.Bande = Bande(self.FrameHaut,self.controller,self.VarSpong,self.VarFrag,self.VarAgeCort)
        self.Bande.pack()

        self.FrameMid = Frame(self.FrameDroite,bg='white',relief="solid",bd=1)
        self.FrameMid.pack(fill='both',padx=10,expand=True)

        self.FrameMidhaut = Frame(self.FrameMid,bg='white')
        self.FrameMidhaut.pack(expand=True,fill="both")



        self.FrameLeftNID = Frame(self.FrameMidhaut,bg='white')
        self.FrameLeftNID.pack(expand=True,fill=BOTH)

        listeNid = ['NID','SVERT','MAM1','MAM12', 'MAM2','MAM23','MAM3','MAM34','MAM45','MAM4', 'MAM5']

        self.VarSpecies = StringVar()

        if self.controller.getspe():
            self.VarSpecies.set(self.controller.getspe()[0][0])
        else :
            self.VarSpecies.set(None)

        self.FrameSp = Frame(self.FrameLeftNID,bg='white')
        self.FrameSp.pack()

        self.FrameSpe1 = Frame(self.FrameSp,bg='white')
        self.FrameSpe1.pack(side=LEFT)

        self.FrameSpe2 = Frame(self.FrameSp,bg='white')
        self.FrameSpe2.pack(side=LEFT)

        for nid in listeNid[:5]:
                    self.FrameNID = Frame(self.FrameSpe1,bg='white')
                    self.FrameNID.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioNID = Radiobutton(self.FrameNID, text=nid, value=nid,
                                                variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                command=lambda:self.toggle_button(self.VarSpecies.get()))
                    self.RadioNID.pack(side=LEFT)

        for nid in listeNid[5:]:
                    self.FrameNID = Frame(self.FrameSpe2,bg='white')
                    self.FrameNID.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioNID = Radiobutton(self.FrameNID, text=nid, value=nid,
                                                variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                command=lambda:self.toggle_button(self.VarSpecies.get()))
                    self.RadioNID.pack(side=LEFT)
        
        self.FrameButton = Frame(self.FrameLeftNID,bg='white')
        self.FrameButton.pack(expand=TRUE)


        self.ButtonTap =Button(self.FrameButton,text='> Go directly to tapho \r(above tapho. threshold)',bg=color_police,
                                fg=color_button,font=font_button,bd=0,height=4, width=35)
        self.ButtonTap.pack(expand=True,pady=20)


        self.ButtonNew =Button(self.FrameButton,text='> Create new record \r(below tapho. threshold)',bg=color_police,
                                fg=color_button,font=font_button,bd=0,height=4, width=35,
                            )
        self.ButtonNew.pack(expand=True)


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



    def toggle_button(self,val):
        if self.controller.getSpe() or self.tc =='Yes':
                state1 ='disabled'
                state2 ='normal'
        elif self.controller.getSpe() or self.tc =='No':
                state1 = 'normal'
                state2 = 'disabled'
        else :
            state1 = 'disabled'
            state2 = 'disabled'
                

        self.ButtonTap.config(state=state1)
        self.ButtonNew.config(state=state2)

        self.controller.updateTaxon(val)

                
