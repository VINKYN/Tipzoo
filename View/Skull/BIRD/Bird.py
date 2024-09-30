from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class BirdInterface(Frame):
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

        self.Notebook = ttk.Notebook(self.Frame4)
        self.Notebook.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

    
        ListeTab =['Skull (& tracheal rings)','Vertebras, synsacrum, etc','Rib, girdles, etc','Long bones','Phalanges']

        

        self.FrameSK = Frame(self.Notebook)
        self.FrameVS = Frame(self.Notebook)
        self.FrameRG = Frame(self.Notebook)
        self.FrameLB = Frame(self.Notebook)
        self.FrameP = Frame(self.Notebook)
        
       
        ListePage =[self.FrameSK,self.FrameVS,self.FrameRG,self.FrameLB,self.FrameP]

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()

        self.VarPorA = StringVar()
        self.VarPorM = StringVar()

        A , M = self.controller.portionBird()

        self.VarPorA.set(A)
        self.VarPorM.set(M)


        self.VarPotionP = StringVar()
        self.VarPotionS = StringVar()
        self.VarPotionD = StringVar()
        self.VarPotionE = StringVar()

        p ,s ,d ,e = self.controller.portion()

        self.VarPotionP.set(p)
        self.VarPotionS.set(s)
        self.VarPotionD.set(d)
        self.VarPotionE.set(e)

        self.tc = self.controller.tapho_category()

        self.VarVer = StringVar()
        

        self.VarAnatD = StringVar()
        self.VarAnatD.set(self.controller.getAnat_Detail())

        self.VarSAnat = StringVar()
        

        self.VarRAnat = StringVar()
        print(self.controller.get_anat())
        

        if self.controller.get_anat() !=None:
            if len(self.controller.get_anat())< 1:
                self.VarVer.set(None)
                self.VarSAnat.set(None)
                self.VarRAnat.set(None)
            else :
                self.VarVer.set(self.controller.get_anat())
                self.VarSAnat.set(self.controller.get_anat())
                self.VarRAnat.set(self.controller.get_anat())
        else:
            self.VarVer.set(None)
            self.VarSAnat.set(None)
            self.VarRAnat.set(None)
            


        

        self.VarSS = StringVar()
        self.VarD1 = StringVar()
        self.VarD2 = StringVar()
        self.VarA1 = StringVar()
        self.VarA2 = StringVar()

        S,D1,D2,A1,A2= self.controller.portionMandible()

        self.VarSS.set(S)
        self.VarD1.set(D1)
        self.VarD2.set(D2)
        self.VarA1.set(A1)
        self.VarA2.set(A2)


        self.VarF = StringVar()
        self.VarC1 = StringVar()
        self.VarC2 = StringVar()
        self.VarFA1 = StringVar()
        self.VarFA2 = StringVar()

        F,C1,C2,FA1,FA2= self.controller.portionFurcula()

        self.VarF.set(F)
        self.VarC1.set(C1)
        self.VarC2.set(C2)
        self.VarFA1.set(FA1)
        self.VarFA2.set(FA2)


        self.VarSterR = StringVar()
        self.VarSterKE = StringVar()
        self.VarSterKS = StringVar()
        self.VarSterP = StringVar()

        R,KE,KS,P= self.controller.portionSternum()

        self.VarSterR.set(R)
        self.VarSterKE.set(KE)
        self.VarSterKS.set(KS)
        self.VarSterP.set(P)

        self.VarCoxAce = StringVar()
        self.VarCoxThick = StringVar()
        self.VarCoxThin = StringVar()

        Ace,Thin,Thick= self.controller.portionCoxal()

        self.VarCoxAce.set(Ace)
        self.VarCoxThick.set(Thin)
        self.VarCoxThin.set(Thick)


        


        for tab, page in zip(ListeTab, ListePage):
            self.Notebook.add(page, text=tab)
            self.FrameDroite = Frame(page,bg=color_button)
            self.FrameDroite.pack(side=LEFT, fill='both', expand=True)
            self.FrameHaut = Frame(self.FrameDroite,bg=color_bleu,relief="solid",bd=1)
            self.FrameHaut.pack(side=TOP,fill="x",padx=10,pady=10)

            self.Bande = Bande(self.FrameHaut,self.controller,self.VarSpong,self.VarFrag,self.VarAgeCort)
            self.Bande.pack()

            self.FrameMid = Frame(self.FrameDroite,bg='white',relief="solid",bd=1)
            self.FrameMid.pack(fill='both',padx=10,expand=True)

            self.FrameMidhaut = Frame(self.FrameMid,bg='white')
            self.FrameMidhaut.pack(expand=True,fill="both")


            self.FrameBas = Frame(self.FrameDroite,bg=color_button)
            self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)


            if tab != "Vertebras, synsacrum, etc":

                self.Side = Side(self.FrameBas,self.controller,self.VarSide)
                self.Side.pack(side=LEFT)

            if tab == "Skull (& tracheal rings)":

                self.FrameSAnat = Frame(self.FrameMidhaut)
                self.FrameSAnat.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.RadioCra = Radiobutton(self.FrameSAnat, text='Cranium', value='CRA',variable=self.VarSAnat,font=font_ecriture,
                                        command=lambda:self.toggle_Man())
                
                self.RadioCra.pack(padx=5,anchor='w')
                
                self.RadioMan = Radiobutton(self.FrameSAnat, text='Mandible', value='MAN',variable=self.VarSAnat,font=font_ecriture,
                                        command=lambda:self.toggle_Man())
                self.RadioMan.pack(padx=5,anchor='w')
                
                self.RadioQua = Radiobutton(self.FrameSAnat, text='Quadrate', value='QUA',variable=self.VarSAnat,font=font_ecriture,
                                        command=lambda:self.toggle_Man())
                self.RadioQua.pack(padx=5,anchor='w')
                
                self.RadioRNG = Radiobutton(self.FrameSAnat, text='Tracheal ring', value='RNG',variable=self.VarSAnat,font=font_ecriture,
                                        command=lambda:self.toggle_Man())
                self.RadioRNG.pack(padx=5,anchor='w')


                self.FramePAnat = Frame(self.FrameMidhaut)
                self.FramePAnat.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPyn = Label(self.FramePAnat,text='Mandible portion',font=font_ecriture)
                self.LabelPyn.pack()

                self.RadioS = Checkbutton(self.FramePAnat, text="Symphyse",font=font_ecriture,
                                    variable=self.VarSS,onvalue='S',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarSS.get(),'S'))
                
                self.RadioS.pack(padx=5,anchor='w')
                
                self.RadioD1 =  Checkbutton(self.FramePAnat, text="First dental",font=font_ecriture,
                                    variable=self.VarD1,onvalue='D1',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarD1.get(),'D1'))
                self.RadioD1.pack(padx=5,anchor='w')
                
                self.RadioD2 =  Checkbutton(self.FramePAnat, text="Second dental",font=font_ecriture,
                                    variable=self.VarD2,onvalue='D2',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarD2.get(),'D2'))
                self.RadioD2.pack(padx=5,anchor='w')
                
                self.RadioA1 = Checkbutton(self.FramePAnat, text="First articular",font=font_ecriture,
                                    variable=self.VarA1,onvalue='A1',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarA1.get(),'A1'))
                self.RadioA1.pack(padx=5,anchor='w')

                self.RadioA2 = Checkbutton(self.FramePAnat, text="Second articular",font=font_ecriture,
                                    variable=self.VarA2,onvalue='A2',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarA2.get(),'A2'))
                self.RadioA2.pack(padx=5,anchor='w')


                self.listePor =[self.RadioS,self.RadioD1,self.RadioD2,self.RadioA1,self.RadioA2]

                self.toggle_Man()
                





            if tab == "Vertebras, synsacrum, etc":

                

                listVer =['ATL','AXI','CER','THO','NOT','SYN','CAU','VRT']
                listVert =['Atlas','Axis','Other cervical','Thoracic','Notarium (dorsal)','Synsacrum','Caudal']

                self.FrameVer = Frame(self.FrameMidhaut)
                self.FrameVer.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelVer = Label(self.FrameVer,text='Vertebras :',font=font_ecriture)
                self.LabelVer.pack()

                self.FrameV =Frame(self.FrameVer)
                self.FrameV.pack(anchor="w")

                self.comboVer = ttk.Combobox(self.FrameV,values=listVert,font=font_ecriture,
                                                textvariable=self.VarVer,state='readonly')
                self.comboVer.pack(side=LEFT,padx=20,pady=10)

                self.comboVer.bind("<<ComboboxSelected>>",lambda event:self.controller.update_fish(listVer[self.comboVer.current()]))

                popdown = self.comboVer.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboVer)
                self.comboVer.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboVer['font'])



                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelSyn = Label(self.FramePortion,text='Synsacrum & dorsal portions',font=font_ecriture)
                self.LabelSyn.pack()


                self.CheckA = Checkbutton(self.FramePortion, text="Anterior",font=font_ecriture,
                                    variable=self.VarPorA,onvalue='A',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPorA.get(),'A'))
                self.CheckA.pack(padx=5,anchor='w')

                self.CheckM = Checkbutton(self.FramePortion, text="Middle",font=font_ecriture,
                                    variable=self.VarPorM,onvalue='M',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPorM.get(),'M'))
                self.CheckM.pack(padx=5,anchor='w')

                self.CheckP = Checkbutton(self.FramePortion, text="Posterior",font=font_ecriture,
                                    variable=self.VarPotionP,onvalue='P',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPotionP.get(),'P'))
                self.CheckP.pack(padx=5,anchor='w')


            if tab=="Rib, girdles, etc":

                listRib = ['Rib', 'Sternum', 'Coracoid', 'Scapula', 'Furcula', 'Coxal', 'Patella']               
                listRibVal =['RIB', 'STE', 'COR', 'SCA', 'FUR', 'COX', 'PAT']

                self.FrameRib = Frame(self.FrameMidhaut)
                self.FrameRib.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                for i in range(len(listRib)):
                    self.FrameAna =Frame(self.FrameRib)
                    self.FrameAna.pack(anchor="w")

                    self.Radio = Radiobutton(self.FrameAna, text=listRib[i], value=listRibVal[i],variable=self.VarRAnat,font=font_ecriture,
                                        command=lambda:self.toggle_Rib())
                    self.Radio.pack(side=LEFT, padx=5)

                self.FrameFur = Frame(self.FrameMidhaut)
                self.FrameFur.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelFur = Label(self.FrameFur,text='Furcula portion',font=font_ecriture)
                self.LabelFur.pack()


                self.CheckF = Checkbutton(self.FrameFur, text="Furcular region",font=font_ecriture,
                                    variable=self.VarF,onvalue='F',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarF.get(),'F'))
                self.CheckF.pack(padx=5,anchor='w')

                self.CheckC1 = Checkbutton(self.FrameFur, text="First clavicle",font=font_ecriture,
                                    variable=self.VarC1,onvalue='C1',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarC1.get(),'C1'))
                self.CheckC1.pack(padx=5,anchor='w')

                self.CheckC2 = Checkbutton(self.FrameFur, text="Second clavicle",font=font_ecriture,
                                    variable=self.VarC2,onvalue='C2',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarC2.get(),'C2'))
                self.CheckC2.pack(padx=5,anchor='w')

                self.CheckA1 = Checkbutton(self.FrameFur, text="First articular",font=font_ecriture,
                                    variable=self.VarFA1,onvalue='A1',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarFA1.get(),'A1'))
                self.CheckA1.pack(padx=5,anchor='w')

                self.CheckA2 = Checkbutton(self.FrameFur, text="Second articular",font=font_ecriture,
                                    variable=self.VarFA2,onvalue='A2',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarFA2.get(),'A2'))
                self.CheckA2.pack(padx=5,anchor='w')


                self.listeFur =[self.CheckA2,self.CheckA1,self.CheckC2,self.CheckC1,self.CheckF]



                self.FrameSter = Frame(self.FrameMidhaut)
                self.FrameSter.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelSter = Label(self.FrameSter,text='Sternum portion',font=font_ecriture)
                self.LabelSter.pack()

                self.CheckR = Checkbutton(self.FrameSter, text="Region with grooves for coracoid",font=font_ecriture,
                                    variable=self.VarSterR,onvalue='R',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarSterR.get(),'R'))
                self.CheckR.pack(padx=5,anchor='w')

                self.CheckKE = Checkbutton(self.FrameSter, text="Keel edge (bord du bréchet)",font=font_ecriture,
                                    variable=self.VarSterKE,onvalue='KE',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarSterKE.get(),'KE'))
                self.CheckKE.pack(padx=5,anchor='w')

                self.CheckKS = Checkbutton(self.FrameSter, text="Keel surface (lame du bréchet)",font=font_ecriture,
                                    variable=self.VarSterKS,onvalue='KS',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarSterKS.get(),'KS'))
                self.CheckKS.pack(padx=5,anchor='w')

                self.CheckP = Checkbutton(self.FrameSter, text="Postero-lateral process",font=font_ecriture,
                                    variable=self.VarSterP,onvalue='P',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarSterP.get(),'P'))
                self.CheckP.pack(padx=5,anchor='w')

                self.listeSter =[self.CheckP,self.CheckKS,self.CheckKE,self.CheckR]


                self.FrameCoxal = Frame(self.FrameMidhaut)
                self.FrameCoxal.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelCox = Label(self.FrameCoxal,text='Coxal portion',font=font_ecriture)
                self.LabelCox.pack()

                self.CheckCoxAce = Checkbutton(self.FrameCoxal, text="Acetabulum",font=font_ecriture,
                                    variable=self.VarCoxAce,onvalue='ACE',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarCoxAce.get(),'ACE'))
                self.CheckCoxAce.pack(padx=5,anchor='w')

                self.CheckCoxThic = Checkbutton(self.FrameCoxal, text="Thick regions",font=font_ecriture,
                                    variable=self.VarCoxThick,onvalue='THICK',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarCoxThick.get(),'THICK'))
                self.CheckCoxThic.pack(padx=5,anchor='w')

                self.CheckCoxThin = Checkbutton(self.FrameCoxal, text="Thin regions",font=font_ecriture,
                                    variable=self.VarCoxThin,onvalue='THIN',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarCoxThin.get(),'THIN'))
                self.CheckCoxThin.pack(padx=5,anchor='w')


                self.listeCox =[self.CheckCoxAce,self.CheckCoxThin,self.CheckCoxThic]

                self.toggle_Rib()


                







                
                
            if tab =="Long bones":

                listAnat = ["Humerus","Femur","Radius","Ulna","Tibia","Fibulla","Metatarsal 1","Carpometacarpus","Tarsometatarsus","Tibiotarsus"]               
                listValAnat =["HUM", "FEM", "RAD", "ULN", "TIB", "FIB", "MT", "CMC", "TMT", "TBT"]

                self.FrameAnat = Frame(self.FrameMidhaut)
                self.FrameAnat.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                for i in range(len(listAnat)):
                    self.FrameAna =Frame(self.FrameAnat)
                    self.FrameAna.pack(anchor="w")

                    self.Radio = Radiobutton(self.FrameAna, text=listAnat[i], value=listValAnat[i],variable=self.VarVer,font=font_ecriture,
                                        command=lambda:self.controller.update_skel(self.VarVer.get(),'Skel_Anat'))
                    self.Radio.pack(side=LEFT, padx=5)

                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                self.LabelPortion.pack()

                

                self.FrameP =Frame(self.FramePortion)
                self.FrameP.pack(anchor="w")

                self.CheckP = Checkbutton(self.FrameP, text="P",font=font_ecriture,
                                    variable=self.VarPotionP,onvalue='P',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPotionP.get(),'P'))
                self.CheckP.pack(side=LEFT, padx=5)

                self.LabelP = Label(self.FrameP,text='Prox. extr.',font=font_ecriture)
                self.LabelP.pack(side=LEFT,padx=(0,5))

                self.FrameS =Frame(self.FramePortion)
                self.FrameS.pack(anchor="w")

                self.CheckS = Checkbutton(self.FrameS, text="S",font=font_ecriture,
                                    variable=self.VarPotionS,onvalue='S',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPotionS.get(),'S'))
                self.CheckS.pack(side=LEFT, padx=5)

                self.LabelS = Label(self.FrameS,text='Shaft',font=font_ecriture)
                self.LabelS.pack(side=LEFT,padx=(0,5))


                self.FrameD =Frame(self.FramePortion)
                self.FrameD.pack(anchor="w")

                self.CheckD = Checkbutton(self.FrameD, text="D",font=font_ecriture,
                                    variable=self.VarPotionD,onvalue="D",offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPotionD.get(),'D'))
                self.CheckD.pack(side=LEFT, padx=5)

                self.LabelD = Label(self.FrameD,text='Distal extr.',font=font_ecriture)
                self.LabelD.pack(side=LEFT,padx=(0,5))


                self.FrameE =Frame(self.FramePortion)
                self.FrameE.pack(anchor="w")

                self.CheckE = Checkbutton(self.FrameE, text="E",font=font_ecriture,
                                    variable=self.VarPotionE,onvalue='E',offvalue='',
                                    command=lambda:self.controller.updatePortion(self.VarPotionE.get(),'E'))
                self.CheckE.pack(side=LEFT, padx=5)

                self.LabelE = Label(self.FrameE,text='Ext. indet.',font=font_ecriture)
                self.LabelE.pack(side=LEFT,padx=(0,5))




                self.VarSeg = StringVar()
                self.VarSeg.set(self.controller.getSegment())
                self.FrameSH = Frame(self.FrameMidhaut)
                self.FrameSH.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.LabelPortion = Label(self.FrameSH,text='Proportion of the shaft',font=font_ecriture)
                self.LabelPortion.pack()

                self.FrameS1 =Frame(self.FrameSH)
                self.FrameS1.pack(anchor="w")

                self.Radio1 = Radiobutton(self.FrameS1, text="SH1", value="SH1",variable=self.VarSeg,font=font_ecriture,
                                        command=lambda:self.controller.update_skel(self.VarSeg.get(),'Skel_Segment'))
                self.Radio1.pack(side=LEFT, padx=5)

                self.LabelS1 = Label(self.FrameS1,text='<1/3 of the shaft',font=font_ecriture)
                self.LabelS1.pack(side=LEFT,padx=(0,5))

                self.FrameS2 =Frame(self.FrameSH)
                self.FrameS2.pack(anchor="w")

                self.Radio2 = Radiobutton(self.FrameS2, text="SH2", value="SH2",variable=self.VarSeg,font=font_ecriture,
                                        command=lambda:self.controller.update_skel(self.VarSeg.get(),'Skel_Segment'))
                
                self.Radio2.pack(side=LEFT, padx=5)

                self.LabelS2 = Label(self.FrameS2,text='1/3 to 2/3 of the shaft',font=font_ecriture)
                self.LabelS2.pack(side=LEFT,padx=(0,5))


                self.FrameS3 =Frame(self.FrameSH)
                self.FrameS3.pack(anchor="w")

                self.Radio3 = Radiobutton(self.FrameS3, text="SH3", value="SH3",variable=self.VarSeg,font=font_ecriture,
                                        command=lambda:self.controller.update_skel(self.VarSeg.get(),'Skel_Segment'))
                self.Radio3.pack(side=LEFT, padx=5)

                self.LabelS3 = Label(self.FrameS3,text='>2/3 of the shaft',font=font_ecriture)
                self.LabelS3.pack(side=LEFT,padx=(0,5))


        if tab =="Phalanges":

            listePha = ["PHL_11", "PHL_12", "PHL_21", "PHL_22", "PHL_23", "PHL_31", "PHL_32", "PHL_33", "PHL_34", "PHL_41", "PHL_42", "PHL_43", "PHL_44", "PHL_45", "PHL_PEN", "PHL_CLAW"]
            listePha2 =["PHW_2","PHW_31","PHW_31","PHW_4","PHA"]

            listePhaLabel = ["Limb, first digit, first phalange", "Limb, first digit, second phalange", "Limb, second digit, first phalange", "Limb, second digit, second phalange", "Limb, second digit, third phalange",
                            "Limb, third digit, first phalange", "Limb, third digit, second phalange", "Limb, third digit, third phalange", "Limb, third digit, fourth phalange", "Limb, fourth digit, first phalange",
                            "Limb, fourth digit, second phalange", "Limb, fourth digit, third phalange", "Limb, fourth digit, fourth phalange", "Limb, fourth digit, fifth phalange", "Limb, unidentified digit, penultimate phalange",
                            "Limb, unidentified digit, last phalange"]
            
            listePhaLabel2 =  ["Wing, second digit", "Wing, third digit, first phalange", "Wing, third digit, second phalange", "Wing, fourth digit", "Unidentified phalange"]


            self.FrameAnatD = Frame(self.FrameMidhaut)
            self.FrameAnatD.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')


            for i in range(len(listePha[:8])):
                self.FrameAnaD =Frame(self.FrameAnatD)
                self.FrameAnaD.pack(anchor="w")

                self.Radio = Radiobutton(self.FrameAnaD, text=listePha[:8][i], value=listePha[:8][i],variable=self.VarAnatD,font=font_ecriture,
                                    command=lambda:self.controller.update_skel(self.VarAnatD.get(),'Skel_Anat'))
                self.Radio.pack(side=LEFT, padx=5)

                self.Label = Label(self.FrameAnaD,text=listePhaLabel[:8][i])
                self.Label.pack(side=LEFT)

            self.FrameAnatD1 = Frame(self.FrameMidhaut)
            self.FrameAnatD1.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

            for i in range(len(listePha[8:])):
                self.FrameAnaD1 =Frame(self.FrameAnatD1)
                self.FrameAnaD1.pack(anchor="w")

                self.Radio = Radiobutton(self.FrameAnaD1, text=listePha[8:][i], value=listePha[8:][i],variable=self.VarAnatD,font=font_ecriture,
                                    command=lambda:self.controller.update_skel(self.VarAnatD.get(),'Skel_Anat'))
                self.Radio.pack(side=LEFT, padx=5)

                self.Label = Label(self.FrameAnaD1,text=listePhaLabel[8:][i])
                self.Label.pack(side=LEFT)


            self.FrameAnatD2 = Frame(self.FrameMidhaut)
            self.FrameAnatD2.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

            for j in range(len(listePha2)):
                self.FrameAnaD2 =Frame(self.FrameAnatD2)
                self.FrameAnaD2.pack(anchor="w")

                self.Radio = Radiobutton(self.FrameAnaD2, text=listePha2[j], value=listePha2[j],variable=self.VarAnatD,font=font_ecriture,
                                    command=lambda:self.controller.update_skel(self.VarAnatD.get(),'Skel_Anat'))
                self.Radio.pack(side=LEFT, padx=5)

                self.Label = Label(self.FrameAnaD2,text=listePhaLabel2[j])
                self.Label.pack(side=LEFT)
                

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


        self.Notebook.select(self.controller.getOnglet('Bird'))

        self.Notebook.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.Notebook.index("current"),'Bird'))
            
        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()


    def toggle_Man(self):
        if self.VarSAnat.get() == 'MAN':
            state = 'normal' 
        else: 
            state ='disabled'
            self.controller.set_portion()
            self.VarSS.set(None)
            self.VarA1.set(None)
            self.VarA2.set(None)
            self.VarD1.set(None)
            self.VarD2.set(None)

        for i in self.listePor:
             i.config(state=state)

        self.controller.update_skel(self.VarSAnat.get(),'Skel_Anat')

    def toggle_Rib(self):

        if self.VarRAnat.get() != 'COX' and self.VarRAnat.get() != 'FUR' and self.VarRAnat.get() != 'STE' :
            for i in self.listeCox:
                    i.config(state='disabled')
            for j in self.listeFur:
                    j.config(state='disabled')
            for k in self.listeSter:
                    k.config(state='disabled')
            self.controller.set_portion()

            self.VarF.set(None)
            self.VarC1.set(None)
            self.VarC2.set(None)
            self.VarFA1.set(None)
            self.VarFA2.set(None)

            self.VarCoxAce.set(None)
            self.VarCoxThick.set(None)
            self.VarCoxThin.set(None)

            self.VarSterR.set(None)
            self.VarSterKE.set(None)
            self.VarSterKS.set(None)
            self.VarSterP.set(None)
        else:
            if self.VarRAnat.get() == 'COX':
                self.controller.set_portion()
                state1 = 'normal' 
                state2 ='disabled'
                for i in self.listeCox:
                    i.config(state=state1)
                for j in self.listeFur:
                    j.config(state=state2)
                for k in self.listeSter:
                    k.config(state=state2)

                self.VarF.set(None)
                self.VarC1.set(None)
                self.VarC2.set(None)
                self.VarFA1.set(None)
                self.VarFA2.set(None)

                self.VarSterR.set(None)
                self.VarSterKE.set(None)
                self.VarSterKS.set(None)
                self.VarSterP.set(None)

            elif self.VarRAnat.get() == 'FUR':
                self.controller.set_portion()
                state2 ='disabled'
                state1 = 'normal' 
                for i in self.listeFur:
                    i.config(state=state1)
                for j in self.listeCox:
                    j.config(state=state2)
                for k in self.listeSter:
                    k.config(state=state2)

                self.VarCoxAce.set(None)
                self.VarCoxThick.set(None)
                self.VarCoxThin.set(None)

                self.VarSterR.set(None)
                self.VarSterKE.set(None)
                self.VarSterKS.set(None)
                self.VarSterP.set(None)
            elif self.VarRAnat.get() == 'STE':
                self.controller.set_portion()
                state2 ='disabled'
                state1 = 'normal' 
                for i in self.listeSter:
                    i.config(state=state1)
                for j in self.listeCox:
                    j.config(state=state2)
                for k in self.listeFur:
                    k.config(state=state2)

                self.VarF.set(None)
                self.VarC1.set(None)
                self.VarC2.set(None)
                self.VarFA1.set(None)
                self.VarFA2.set(None)

                self.VarCoxAce.set(None)
                self.VarCoxThick.set(None)
                self.VarCoxThin.set(None)

        self.controller.update_skel(self.VarRAnat.get(),'Skel_Anat')
