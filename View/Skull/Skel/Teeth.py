from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class TeethInterface(Frame):
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

        self.img_on = PhotoImage(file="View\img\check.png")  
        self.img_off = PhotoImage(file="View\img\stop-fill.png")

        self.custom_font = ('Helvetica', 13)       
        # Appliquer la police Roboto en taille 12
        self.pack(expand=True, fill='both')

        """self.Frame1 = Frame(self,bg="red")
        self.Frame1.pack(side=TOP, fill='both')

        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')"""

        self.VarSpong = IntVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()
        self.VarSide.set(self.controller.getSide())

        self.VarFM = StringVar()
        self.VarFM.set(self.controller.get_anat())

        self.VarAgef = StringVar()
        self.VarAgej = StringVar()
        self.VarAgeu = StringVar()

        af ,aj ,au = self.controller.SkelAgeFus()
        
        self.VarAgef.set(af)
        self.VarAgej.set(aj)
        self.VarAgeu.set(au)


        self.VarPotionMAX = StringVar()
        self.VarPotionNAS = StringVar()
        self.VarPotionFRO = StringVar()
        self.VarPotionORB = StringVar()
        self.VarPotionTEM = StringVar()
        self.VarPotionPAR = StringVar()
        self.VarPotionOCC = StringVar()

        Max,Nas,Fro,Orb,Tem,Par,Occ = self.controller.portionCra()

        self.VarPotionMAX.set(Max)
        self.VarPotionNAS.set(Nas)
        self.VarPotionFRO.set(Fro)
        self.VarPotionORB.set(Orb)
        self.VarPotionTEM.set(Tem)
        self.VarPotionPAR.set(Par)
        self.VarPotionOCC.set(Occ)

        self.VarPotionCOND = StringVar()
        self.VarPotionCORO = StringVar()
        self.VarPotionRAM = StringVar()
        self.VarPotionALV = StringVar()
        self.VarPotionBODman = StringVar()
        self.VarPotionSYM = StringVar()

        Cond, Coro, Ram, Alv, Bodman, Sym = self.controller.portionMan()
        self.VarPotionCOND.set(Cond)
        self.VarPotionCORO.set(Coro)
        self.VarPotionRAM.set(Ram)
        self.VarPotionALV.set(Alv)
        self.VarPotionBODman.set(Bodman)
        self.VarPotionSYM.set(Sym)


        self.listebut = []

        self.VarCrab1 = StringVar()
        self.VarCrab1.set(self.controller.getNDe(35))

        self.VarCrab2 = StringVar()
        self.VarCrab2.set(self.controller.getNDe(36))


        self.VarCheck38 = IntVar()
        self.VarCheck38.set(self.controller.getNDe(38))

        self.VarCheck37 = IntVar()
        self.VarCheck37.set(self.controller.getNDe(37))

        self.VarCheck39 = IntVar()
        self.VarCheck39.set(self.controller.getNDe(39))


        self.tc = self.controller.tapho_category()

        self.Frame2 = Frame(self,bg="pink")
        self.Frame2.pack(fill=BOTH, expand=False)

        self.Frame4 = Frame(self,bg='red')
        self.Frame4.pack(expand=True,fill=BOTH)

        self.Notebook = ttk.Notebook(self.Frame4)
        self.Notebook.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])
    
        ListeTab =[ 'Cranium with teeth','Mandible with teeth','CRA or MAN (NID) with teeth','Isolated tooth','Cranium','Mandible','Antler','Horncore','CRA or MAN (NID) without teeth']

        self.FrameCRAT = Frame(self.Notebook)
        self.FrameMANT= Frame(self.Notebook)
        self.FrameNIDT = Frame(self.Notebook)
        self.FrameISO= Frame(self.Notebook)
        self.FrameCRA = Frame(self.Notebook)
        self.FrameMAN = Frame(self.Notebook)
        self.FrameANT = Frame(self.Notebook)
        self.FrameHCO = Frame(self.Notebook)
        self.FrameNID = Frame(self.Notebook)
       
        ListePage =[self.FrameCRAT,self.FrameMANT,self.FrameNIDT,self.FrameISO,self.FrameCRA,self.FrameMAN,self.FrameANT,self.FrameHCO,self.FrameNID]

        for tab, page in zip(ListeTab, ListePage):
            self.Notebook.add(page, text=tab)

            self.FrameDroite = Frame(page,bg=color_button)
            self.FrameDroite.pack(side=LEFT, fill='both', expand=True)
            self.FrameHaut = Frame(self.FrameDroite,bg=color_bleu,relief="solid",bd=1)
            self.FrameHaut.pack(side=TOP,fill="x",padx=10,pady=10)

            #self.Bande = Bande(self.FrameHaut,self.controller,self.VarSpong,self.VarFrag,self.VarAgeCort)
            #self.Bande.pack()

            self.FrameMid = Frame(self.FrameDroite,bg='white',relief="solid",bd=1)
            self.FrameMid.pack(fill='both',padx=10,expand=True)

            self.FrameMidhaut = Frame(self.FrameMid,bg='white')
            self.FrameMidhaut.pack(expand=True,fill="both")


            if tab =="Cranium with teeth" or tab == 'Mandible with teeth' or tab == 'CRA or MAN (NID) with teeth' or tab =='Isolated tooth':
                
                self.FrameTab = Frame(self.FrameMidhaut,bg='white')
                self.FrameTab.pack(side=BOTTOM)

                self.FrameTableau = Frame(self.FrameTab)
                self.FrameTableau.pack(side=LEFT)

                colonnes = ('id','Position','Side','Type','Dentition', 'Class', 'Number','Portion','Occ')

                style = ttk.Style(self.FrameTableau)
                style.configure('Treeview', rowheight=20,foreground =color_police) 

                style.configure('Treeview.Heading', rowheight=20) 

            
                self.tableau = ttk.Treeview(self.FrameTableau,columns=colonnes , show='headings')
                self.tableau.heading('id', text='id')
                self.tableau.heading('Position', text='Position')
                self.tableau.heading('Side', text='Side')
                self.tableau.heading('Type', text='Type')
                self.tableau.heading('Dentition', text='Dentition')
                self.tableau.heading('Class', text='Class')
                self.tableau.heading('Number', text='Number')
                self.tableau.heading('Portion', text='Portion')
                self.tableau.heading('Occ', text='Occ')

                for col in colonnes:
                    self.tableau.column(col, width=int((self.winfo_screenwidth())/(len(colonnes)+1)))
                    self.tableau.config(displaycolumns=('Position','Side','Type','Dentition', 'Class', 'Number','Portion','Occ'))

                Valteeth = self.controller.get_Teeth()

                for colonnes in Valteeth:
                        self.tableau.insert('', END, values=colonnes)

                self.tableau.pack(side=LEFT,fill=X)
                self.tableau.config(height=5)

                self.FrameEdit = Frame(self.FrameTab,bg='white')
                self.FrameEdit.pack(side=LEFT,padx=10,expand=True,fill=BOTH)

                self.create_edit_button(self.FrameEdit, self.tableau)

                self.create_delete_button(self.FrameEdit, self.tableau)

            

                self.FrameButton = Frame(self.FrameMidhaut,bg='#c0edfe')
                self.FrameButton.pack(fill='both',side="right",expand=True)

                
                self.ButtonTap =Button(self.FrameButton,text='Add a teeth',bg=color_police,
                                        fg=color_button,font=font_button,bd=0,height=4, width=35,
                                        command=self.controller.show_new_teeth_create)
                self.ButtonTap.pack(expand=True,pady=20)

                self.listebut.append(self.ButtonTap)

                

        
            if tab == "Cranium with teeth" or tab =="Cranium":

                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                self.LabelPortion.pack()
                 

                self.CheckMAX = Checkbutton(self.FramePortion, text="Maxillary",font=font_ecriture,
                                        variable=self.VarPotionMAX,onvalue='MAX',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionMAX.get(),'MAX'))
                self.CheckMAX.pack(padx=5,anchor='w')

                self.CheckNAS = Checkbutton(self.FramePortion, text="Nasal",font=font_ecriture,
                                        variable=self.VarPotionNAS,onvalue='NAS',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionNAS.get(),'NAS'))
                self.CheckNAS.pack(padx=5,anchor='w')

                self.CheckFRO = Checkbutton(self.FramePortion, text="Frontal",font=font_ecriture,
                                        variable=self.VarPotionFRO,onvalue='FRO',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionFRO.get(),'FRO'))
                self.CheckFRO.pack(padx=5,anchor='w')

                self.CheckORB = Checkbutton(self.FramePortion, text="Orbit",font=font_ecriture,
                                        variable=self.VarPotionORB,onvalue='ORB',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionORB.get(),'ORB'))
                self.CheckORB.pack(padx=5,anchor='w')

                self.CheckTEM = Checkbutton(self.FramePortion, text="Temporal / petrous",font=font_ecriture,
                                        variable=self.VarPotionTEM,onvalue='TEM',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionTEM.get(),'TEM'))
                self.CheckTEM.pack(padx=5,anchor='w')

                self.CheckPAR = Checkbutton(self.FramePortion, text="Parietal",font=font_ecriture,
                                        variable=self.VarPotionPAR,onvalue='PAR',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionPAR.get(),'PAR'))
                self.CheckPAR.pack(padx=5,anchor='w')

                self.CheckOCC = Checkbutton(self.FramePortion, text="Occipital",font=font_ecriture,
                                        variable=self.VarPotionOCC,onvalue='OCC',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionOCC.get(),'OCC'))
                self.CheckOCC.pack(padx=5,anchor='w')

                ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

                self.NotebookCRA = ttk.Notebook(self.FrameMidhaut)
                self.NotebookCRA.pack(fill='both',side="left",expand=True)
                style = ttk.Style()
                style.configure('TNotebook.Tab', padding=[20, 10])

                self.FrameBovidCRA = Frame(self.NotebookCRA,bg='white')
                self.FrameEquidCRA = Frame(self.NotebookCRA,bg='white')
                self.FrameSuiformCRA = Frame(self.NotebookCRA,bg='white')
                self.FrameUrsidCRA = Frame(self.NotebookCRA,bg='white')
                self.FrameOtherCRA = Frame(self.NotebookCRA,bg='white')

                ListePageCRA =[self.FrameBovidCRA,self.FrameEquidCRA,self.FrameSuiformCRA,self.FrameUrsidCRA,self.FrameOtherCRA]
                
                for tabCRA, pageCRA in zip(ListeTab, ListePageCRA):
                    self.NotebookCRA.add(pageCRA, text=tabCRA)

                
                    self.FrameCRAB1 = Frame(pageCRA)
                    self.FrameCRAB1.pack(side=LEFT,expand=True)

                    self.LabelCrab1 =Label(self.FrameCRAB1,text='UD4 or worn UM3 \r >50% mesial lobe')

                    self.LabelCrab1.pack()
                    self.radioCrab330 = Radiobutton(self.FrameCRAB1, text="0",value="0", variable=self.VarCrab1,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(35,self.VarCrab1.get()))
                    
                    self.radioCrab330.pack()

                    self.radioCrab331 = Radiobutton(self.FrameCRAB1, text="1",value="1", variable=self.VarCrab1,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(35,self.VarCrab1.get()))
                    
                    self.radioCrab331.pack()

                    self.radioCrab332 = Radiobutton(self.FrameCRAB1, text="2",value="2", variable=self.VarCrab1,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(35,self.VarCrab1.get()))
                    
                    self.radioCrab332.pack()


                    self.FrameCRAB2 = Frame(pageCRA)
                    self.FrameCRAB2.pack(side=LEFT,expand=True)

                    self.LabelCrab2 =Label(self.FrameCRAB2,text='petrosal >50%')

                    self.LabelCrab2.pack()
                    self.radioCrab3302 = Radiobutton(self.FrameCRAB2, text="0",value="0", variable=self.VarCrab2,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(36,self.VarCrab2.get()))
                    
                    self.radioCrab3302.pack()

                    self.radioCrab3312 = Radiobutton(self.FrameCRAB2, text="1",value="1", variable=self.VarCrab2,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(36,self.VarCrab2.get()))
                    
                    self.radioCrab3312.pack()

                    self.radioCrab3322 = Radiobutton(self.FrameCRAB2, text="2",value="2", variable=self.VarCrab2,font=font_ecriture,
                                                    command=lambda:self.controller.landmark(36,self.VarCrab2.get()))
                    
                    self.radioCrab3322.pack()


                

            if tab == "Mandible with teeth":
                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                self.LabelPortion.pack()

                self.CheckCOND = Checkbutton(self.FramePortion, text="Condyle",font=font_ecriture,
                                        variable=self.VarPotionCOND,onvalue='COND',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionCOND.get(),'COND'))
                self.CheckCOND.pack(padx=5,anchor='w')

                self.CheckCORO = Checkbutton(self.FramePortion, text="Coronoid process",font=font_ecriture,
                                        variable=self.VarPotionCORO,onvalue='CORO',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionCORO.get(),'CORO'))
                self.CheckCORO.pack(padx=5,anchor='w')

                self.CheckRAM = Checkbutton(self.FramePortion, text="Ramus (branch)",font=font_ecriture,
                                        variable=self.VarPotionRAM,onvalue='RAM',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionRAM.get(),'RAM'))
                self.CheckRAM.pack(padx=5,anchor='w')

                self.CheckALV = Checkbutton(self.FramePortion, text="Alveolar process",font=font_ecriture,
                                        variable=self.VarPotionALV,onvalue='ALV',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionALV.get(),'ALV'))
                self.CheckALV.pack(padx=5,anchor='w')

                self.CheckBODman = Checkbutton(self.FramePortion, text="Body (horizontal)",font=font_ecriture,
                                        variable=self.VarPotionBODman,onvalue='BODman',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBODman.get(),'BODman'))
                self.CheckBODman.pack(padx=5,anchor='w')

                self.CheckSYM = Checkbutton(self.FramePortion, text="Symphisis",font=font_ecriture,
                                        variable=self.VarPotionSYM,onvalue='SYM',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionSYM.get(),'SYM'))
                self.CheckSYM.pack(padx=5,anchor='w')

                ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

                self.NotebookMANT = ttk.Notebook(self.FrameMidhaut)
                self.NotebookMANT.pack(fill='both',side="right",expand=True)
                style = ttk.Style()
                style.configure('TNotebook.Tab', padding=[20, 10])

                self.FrameBovidMANT = Frame(self.NotebookMANT,bg='white')
                self.FrameEquidMANT = Frame(self.NotebookMANT,bg='white')
                self.FrameSuiformMANT = Frame(self.NotebookMANT,bg='white')
                self.FrameUrsidMANT = Frame(self.NotebookMANT,bg='white')
                self.FrameOtherMANT = Frame(self.NotebookMANT,bg='white')

                ListePageMANT =[self.FrameBovidMANT,self.FrameEquidMANT,self.FrameSuiformMANT,self.FrameUrsidMANT,self.FrameOtherMANT]
                
                for tabMANT, pageMANT in zip(ListeTab, ListePageMANT):
                    self.NotebookMANT.add(pageMANT, text=tabMANT)



                self.VarCheck38 = IntVar()
                self.VarCheck38.set(self.controller.getNDe(38))

                self.VarCheck37 = IntVar()
                self.VarCheck37.set(self.controller.getNDe(37))

                self.VarCheck39 = IntVar()
                self.VarCheck39.set(self.controller.getNDe(39))

                self.canvaManB = Canvas(self.FrameBovidMANT,bg='white')
                self.canvaManB.pack(expand=True,fill=BOTH)

                self.image_fondManB = PhotoImage(file="View/Skull/Skel/mandibule_img/b.png")
                self.image_fondManB = self.image_fondManB.subsample(2)
                self.canvaManB.create_image(0, 0, anchor="nw", image=self.image_fondManB)

                self.CheckManB = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManB.create_window(40,85, anchor="nw", window= self.CheckManB)

                self.CheckManB2 = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManB.create_window(210,85, anchor="nw", window= self.CheckManB2)

                self.CheckManB3 = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManB.create_window(290,35, anchor="nw", window= self.CheckManB3)



                self.canvaManE = Canvas(self.FrameEquidMANT,bg='white')
                self.canvaManE.pack(expand=True,fill=BOTH)

                self.image_fondManE = PhotoImage(file="View/Skull/Skel/mandibule_img/e.png")
                self.image_fondManE = self.image_fondManE.subsample(4)
                self.canvaManE.create_image(0, 0, anchor="nw", image=self.image_fondManE)

                self.CheckManE = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManE.create_window(45,130, anchor="nw", window= self.CheckManE)

                self.CheckManE2 = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManE.create_window(205,105, anchor="nw", window= self.CheckManE2)

                self.CheckManE3 = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManE.create_window(290,35, anchor="nw", window= self.CheckManE3)


                self.canvaManS = Canvas(self.FrameSuiformMANT,bg='white')
                self.canvaManS.pack(expand=True,fill=BOTH)

                self.image_fondManS = PhotoImage(file="View/Skull/Skel/mandibule_img/s.png")
                self.image_fondManS = self.image_fondManS.subsample(2)
                self.canvaManS.create_image(0, 0, anchor="nw", image=self.image_fondManS)

                self.CheckManS = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManS.create_window(65,115, anchor="nw", window= self.CheckManS)

                self.CheckManS2 = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManS.create_window(210,60, anchor="nw", window= self.CheckManS2)

                self.CheckManS3 = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManS.create_window(310,30, anchor="nw", window= self.CheckManS3)


                self.canvaManU = Canvas(self.FrameUrsidMANT,bg='white')
                self.canvaManU.pack(expand=True,fill=BOTH)

                self.image_fondManU = PhotoImage(file="View/Skull/Skel/mandibule_img/u.png")
                self.image_fondManU = self.image_fondManU.subsample(3)
                self.canvaManU.create_image(0, 0, anchor="nw", image=self.image_fondManU)

                self.CheckManU = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManU.create_window(85,175, anchor="nw", window= self.CheckManU)

                self.CheckManU2 = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManU.create_window(60,100, anchor="nw", window= self.CheckManU2)

                self.CheckManU3 = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManU.create_window(315,75, anchor="nw", window= self.CheckManU3)



                self.canvaManO = Canvas(self.FrameOtherMANT,bg='white')
                self.canvaManO.pack(expand=True,fill=BOTH)

                self.image_fondManO = PhotoImage(file="View/Skull/Skel/mandibule_img/o.png")
                self.image_fondManO = self.image_fondManO.subsample(2)
                self.canvaManO.create_image(0, 0, anchor="nw", image=self.image_fondManO)

                self.CheckManO = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManO.create_window(60,125, anchor="nw", window= self.CheckManO)

                self.CheckManO2 = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManO.create_window(115,80, anchor="nw", window= self.CheckManO2)

                self.CheckManO3 = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManO.create_window(200,60, anchor="nw", window= self.CheckManO3)


            if tab == "Mandible":

                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                self.LabelPortion.pack()

                self.CheckCOND = Checkbutton(self.FramePortion, text="Condyle",font=font_ecriture,
                                        variable=self.VarPotionCOND,onvalue='COND',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionCOND.get(),'COND'))
                self.CheckCOND.pack(padx=5,anchor='w')

                self.CheckCORO = Checkbutton(self.FramePortion, text="Coronoid process",font=font_ecriture,
                                        variable=self.VarPotionCORO,onvalue='CORO',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionCORO.get(),'CORO'))
                self.CheckCORO.pack(padx=5,anchor='w')

                self.CheckRAM = Checkbutton(self.FramePortion, text="Ramus (branch)",font=font_ecriture,
                                        variable=self.VarPotionRAM,onvalue='RAM',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionRAM.get(),'RAM'))
                self.CheckRAM.pack(padx=5,anchor='w')

                self.CheckALV = Checkbutton(self.FramePortion, text="Alveolar process",font=font_ecriture,
                                        variable=self.VarPotionALV,onvalue='ALV',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionALV.get(),'ALV'))
                self.CheckALV.pack(padx=5,anchor='w')

                self.CheckBODman = Checkbutton(self.FramePortion, text="Body (horizontal)",font=font_ecriture,
                                        variable=self.VarPotionBODman,onvalue='BODman',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBODman.get(),'BODman'))
                self.CheckBODman.pack(padx=5,anchor='w')

                self.CheckSYM = Checkbutton(self.FramePortion, text="Symphisis",font=font_ecriture,
                                        variable=self.VarPotionSYM,onvalue='SYM',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionSYM.get(),'SYM'))
                self.CheckSYM.pack(padx=5,anchor='w')

                ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

                self.NotebookMAN = ttk.Notebook(self.FrameMidhaut)
                self.NotebookMAN.pack(fill='both',side="right",expand=True)
                style = ttk.Style()
                style.configure('TNotebook.Tab', padding=[20, 10])

                self.FrameBovidMAN = Frame(self.NotebookMAN,bg='white')
                self.FrameEquidMAN = Frame(self.NotebookMAN,bg='white')
                self.FrameSuiformMAN = Frame(self.NotebookMAN,bg='white')
                self.FrameUrsidMAN = Frame(self.NotebookMAN,bg='white')
                self.FrameOtherMAN = Frame(self.NotebookMAN,bg='white')

                ListePageMAN =[self.FrameBovidMAN,self.FrameEquidMAN,self.FrameSuiformMAN,self.FrameUrsidMAN,self.FrameOtherMAN]
                
                for tabMAN, pageMAN in zip(ListeTab, ListePageMAN):
                    self.NotebookMAN.add(pageMAN, text=tabMAN)

                self.VarCheck38 = IntVar()
                self.VarCheck38.set(self.controller.getNDe(38))

                self.VarCheck37 = IntVar()
                self.VarCheck37.set(self.controller.getNDe(37))

                self.VarCheck39 = IntVar()
                self.VarCheck39.set(self.controller.getNDe(39))

                self.canvaManB = Canvas(self.FrameBovidMAN,bg='white')
                self.canvaManB.pack(expand=True,fill=BOTH)

                self.image_fondManB = PhotoImage(file="View/Skull/Skel/mandibule_img/b.png")
                self.image_fondManB = self.image_fondManB.subsample(2)
                self.canvaManB.create_image(0, 0, anchor="nw", image=self.image_fondManB)

                self.CheckManB = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManB.create_window(40,85, anchor="nw", window= self.CheckManB)

                self.CheckManB2 = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManB.create_window(210,85, anchor="nw", window= self.CheckManB2)

                self.CheckManB3 = Checkbutton(self.canvaManB,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManB.create_window(290,35, anchor="nw", window= self.CheckManB3)



                self.canvaManE = Canvas(self.FrameEquidMAN,bg='white')
                self.canvaManE.pack(expand=True,fill=BOTH)

                self.image_fondManE = PhotoImage(file="View/Skull/Skel/mandibule_img/e.png")
                self.image_fondManE = self.image_fondManE.subsample(4)
                self.canvaManE.create_image(0, 0, anchor="nw", image=self.image_fondManE)

                self.CheckManE = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManE.create_window(45,130, anchor="nw", window= self.CheckManE)

                self.CheckManE2 = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManE.create_window(205,105, anchor="nw", window= self.CheckManE2)

                self.CheckManE3 = Checkbutton(self.canvaManE,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManE.create_window(290,35, anchor="nw", window= self.CheckManE3)


                self.canvaManS = Canvas(self.FrameSuiformMAN,bg='white')
                self.canvaManS.pack(expand=True,fill=BOTH)

                self.image_fondManS = PhotoImage(file="View/Skull/Skel/mandibule_img/s.png")
                self.image_fondManS = self.image_fondManS.subsample(2)
                self.canvaManS.create_image(0, 0, anchor="nw", image=self.image_fondManS)

                self.CheckManS = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManS.create_window(65,115, anchor="nw", window= self.CheckManS)

                self.CheckManS2 = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManS.create_window(210,60, anchor="nw", window= self.CheckManS2)

                self.CheckManS3 = Checkbutton(self.canvaManS,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManS.create_window(310,30, anchor="nw", window= self.CheckManS3)


                self.canvaManU = Canvas(self.FrameUrsidMAN,bg='white')
                self.canvaManU.pack(expand=True,fill=BOTH)

                self.image_fondManU = PhotoImage(file="View/Skull/Skel/mandibule_img/u.png")
                self.image_fondManU = self.image_fondManU.subsample(3)
                self.canvaManU.create_image(0, 0, anchor="nw", image=self.image_fondManU)

                self.CheckManU = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManU.create_window(85,175, anchor="nw", window= self.CheckManU)

                self.CheckManU2 = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManU.create_window(60,100, anchor="nw", window= self.CheckManU2)

                self.CheckManU3 = Checkbutton(self.canvaManU,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManU.create_window(315,75, anchor="nw", window= self.CheckManU3)



                self.canvaManO = Canvas(self.FrameOtherMAN,bg='white')
                self.canvaManO.pack(expand=True,fill=BOTH)

                self.image_fondManO = PhotoImage(file="View/Skull/Skel/mandibule_img/o.png")
                self.image_fondManO = self.image_fondManO.subsample(2)
                self.canvaManO.create_image(0, 0, anchor="nw", image=self.image_fondManO)

                self.CheckManO = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck38,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(38,self.VarCheck38.get()))
                self.canvaManO.create_window(60,125, anchor="nw", window= self.CheckManO)

                self.CheckManO2 = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck37,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(37,self.VarCheck37.get()))
                self.canvaManO.create_window(115,80, anchor="nw", window= self.CheckManO2)

                self.CheckManO3 = Checkbutton(self.canvaManO,bd=0,fg='red',bg='yellow',
                            onvalue=1,offvalue=0,variable=self.VarCheck39,
                            image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                            command=lambda:self.controller.landmark(39,self.VarCheck39.get()))
                self.canvaManO.create_window(200,60, anchor="nw", window= self.CheckManO3)




            if tab == 'Antler':

                self.VarAnatD = StringVar()
                self.VarAnatD.set(self.controller.getAnat_Detail())

                self.FrameAnatD = Frame(self.FrameMidhaut)
                self.FrameAnatD.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelAnatD = Label(self.FrameAnatD,text='Antler Type',font=font_ecriture)
                self.LabelAnatD.pack()


                self.Radio1 = Radiobutton(self.FrameAnatD, text="Shed",value="Shed", variable=self.VarAnatD,font=font_ecriture)
                self.Radio1.pack(padx=5,anchor='w')

                self.Radio2 = Radiobutton(self.FrameAnatD, text="Shed",value="Shed", variable=self.VarAnatD,font=font_ecriture)
                self.Radio2.pack(padx=5,anchor='w')

                self.Radio3 = Radiobutton(self.FrameAnatD, text="NID",value="NID", variable=self.VarAnatD,font=font_ecriture)
                self.Radio3.pack(padx=5,anchor='w')

            if tab != "Isolated tooth":

                self.VarSpong.set(self.controller.getSPong())

                self.CheckSpon = Checkbutton(self.FrameHaut, text="Spongy portion?", font=font_ecriture,
                                            variable=self.VarSpong, onvalue=1, offvalue=0, bg=color_bleu,
                                            command=lambda: self.controller.update_skel(self.VarSpong.get(), 'Skel_Spongy'))
                self.CheckSpon.pack(side=LEFT, padx=10)

                self.LabelAge = Label(self.FrameHaut, text='Age Cort :', font=font_ecriture, bg=color_bleu)
                self.LabelAge.pack(side=LEFT, padx=10)

                self.VarAgeCort.set(self.controller.getAge())

                self.RadioF = Radiobutton(self.FrameHaut, text="F", variable=self.VarAgeCort,
                                            value='F', font=font_ecriture, bg=color_bleu,
                                            command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
                self.RadioF.pack(side=LEFT, padx=(0,10))

                self.RadioJ = Radiobutton(self.FrameHaut, text="J", variable=self.VarAgeCort,
                                            value='J', font=font_ecriture, bg=color_bleu,
                                            command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
                self.RadioJ.pack(side=LEFT, padx=10)

                self.RadioA = Radiobutton(self.FrameHaut, text="A", variable=self.VarAgeCort,
                                            value='A', font=font_ecriture, bg=color_bleu,
                                            command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
                self.RadioA.pack(side=LEFT, padx=10)

                self.RadioQ = Radiobutton(self.FrameHaut, text="?", variable=self.VarAgeCort,
                                            value='?', font=font_ecriture, bg=color_bleu,
                                            command=lambda: self.controller.update_skel(self.VarAgeCort.get(), 'Skel_AgeCort'))
                self.RadioQ.pack(side=LEFT, padx=10)



                self.LabelSide = Label(self.FrameHaut, text='Side :', font=font_ecriture, bg=color_bleu)
                self.LabelSide.pack(side=LEFT, padx=10)

                self.RadioLF = Radiobutton(self.FrameHaut, text="LEFT", variable=self.VarSide,
                                            value='Left', font=font_ecriture, bg=color_bleu,
                                            command=lambda:self.toggle_side())
                self.RadioLF.pack(side=LEFT, padx=(0,10))

                self.RadioLR = Radiobutton(self.FrameHaut, text="LEFT+RIGHT", variable=self.VarSide,
                                            value='Left+Right', font=font_ecriture, bg=color_bleu,
                                            command=lambda:self.toggle_side())
                self.RadioLR.pack(side=LEFT, padx=10)

                self.RadioRG = Radiobutton(self.FrameHaut, text="RIGHT", variable=self.VarSide,
                                            value='Right', font=font_ecriture, bg=color_bleu,
                                            command=lambda:self.toggle_side())
                self.RadioRG.pack(side=LEFT, padx=10)

                self.RadioQ = Radiobutton(self.FrameHaut, text="?", variable=self.VarSide,
                                            value='?', font=font_ecriture, bg=color_bleu,
                                            command=lambda:self.toggle_side())
                self.RadioQ.pack(side=LEFT, padx=10)


                self.LabelAge = Label(self.FrameHaut,text='AgeFus',font=font_ecriture, bg=color_bleu)
                self.LabelAge.pack(side=LEFT,padx=10)

                self.CheckAgef = Checkbutton(self.FrameHaut, text="fus",font=font_ecriture, bg=color_bleu,
                                    variable=self.VarAgef,onvalue='fus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgef.get(),'fus'))
                self.CheckAgef.pack(padx=5,anchor='w',side=LEFT)

                self.CheckAgej = Checkbutton(self.FrameHaut, text="justfus",font=font_ecriture, bg=color_bleu,
                                    variable=self.VarAgej,onvalue='justfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgej.get(),'justfus'))
                self.CheckAgej.pack(padx=5,anchor='w',side=LEFT)

                self.CheckAgeu = Checkbutton(self.FrameHaut, text="unfus",font=font_ecriture, bg=color_bleu,
                                    variable=self.VarAgeu,onvalue='unfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeu.get(),'unfus'))
                self.CheckAgeu.pack(padx=5,anchor='w',side=LEFT)
            


            self.FrameBas = Frame(self.FrameDroite,bg=color_button)
            self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)

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
            
        self.Notebook.select(self.controller.getOnglet('Skull'))

        self.Notebook.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.Notebook.index("current"),'Skull'))

        

    
        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()

        self.toggle_side()


    def toggle_side(self):
        if self.VarSide.get() not in ('', 'None'):
            for i in self.listebut:
                i.config(state='normal')
            self.controller.update_skel(self.VarSide.get(), 'Skel_Side')
        else :
            for j in self.listebut:
                j.config(state='disabled')


    def create_edit_button(self, parent, treeview):
        color_button = '#F2E2CE'
        color_police = '#1b1b1b'
        font_button = ("Helvetica 13 bold")

        button = Button(parent, text='Edit', width=7, height=2, bg=color_button, fg=color_police, bd=0, font=font_button,
                        command=lambda: self.controller.show_new_teeth(treeview))
        button.pack(pady=5)

    def create_delete_button(self, parent, treeview):
        color_button = '#F2E2CE'
        color_police = '#1b1b1b'
        font_button = ("Helvetica 13 bold")

        button = Button(parent, text='Delete', width=7, height=2, bg=color_button, fg=color_police, bd=0, font=font_button,
                        command=lambda: self.controller.delete_teeth(treeview))
        button.pack(pady=5)

            

        
           