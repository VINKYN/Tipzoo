from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class FNBInterface(Frame):
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

        """ self.Frame1 = Frame(self,bg="red")
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

    
        ListeTab =[ '','FBN NID','Vertebra','Rib','Sternum','Scapula','Coxal','Hyoid']

        self.FrameRien = Frame(self.Notebook)
        self.FrameNID = Frame(self.Notebook)
        self.FrameVertebra = Frame(self.Notebook)
        self.FrameRib = Frame(self.Notebook)
        self.FrameSternum = Frame(self.Notebook)
        self.FrameScapula = Frame(self.Notebook)
        self.FrameCoxal = Frame(self.Notebook)
        self.FrameHyoid = Frame(self.Notebook)

       
        ListePage =[self.FrameRien,self.FrameNID,self.FrameVertebra,self.FrameRib,self.FrameSternum,self.FrameScapula,self.FrameCoxal,self.FrameHyoid]

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()

        self.VarPotionBOD = StringVar()
        self.VarPotionBODe = StringVar()
        self.VarPotionDISC = StringVar()
        self.VarPotionDISCe = StringVar()
        self.VarPotionTRP = StringVar()
        self.VarPotionARP = StringVar()
        self.VarPotionSPIvrt = StringVar()

        bod, bode, disc, disce, trp, arp, spivrt = self.controller.portion2()

        self.VarPotionBOD.set(bod)
        self.VarPotionBODe.set(bode)
        self.VarPotionDISC.set(disc)
        self.VarPotionDISCe.set(disce)
        self.VarPotionTRP.set(trp)
        self.VarPotionARP.set(arp)
        self.VarPotionSPIvrt.set(spivrt)


        self.VarPotionD = StringVar()
        self.VarPotionP = StringVar()
        self.VarPotionC = StringVar()

        P, D, C = self.controller.portion3()

        self.VarPotionD.set(D)
        self.VarPotionP.set(P)
        self.VarPotionC.set(C)


        self.VarPotionG = StringVar()
        self.VarPotionBODs = StringVar()
        self.VarPotionSP = StringVar()

        G, Bs, Sp = self.controller.portion4()

        self.VarPotionG.set(G)
        self.VarPotionBODs.set(Bs)
        self.VarPotionSP.set(Sp)



        self.VarPotionPub = StringVar()
        self.VarPotionIsc = StringVar()
        self.VarPotionIli = StringVar()
        self.VarPotionAce = StringVar()

        pub, isc, ili , ace = self.controller.portion5()

        self.VarPotionPub.set(pub)
        self.VarPotionIsc.set(isc)
        self.VarPotionIli.set(ili)
        self.VarPotionAce.set(ace)

        self.tc = self.controller.tapho_category()

        

        for tab, page in zip(ListeTab, ListePage):
            self.Notebook.add(page, text=tab)
            if tab != "":
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


                if tab == "FBN NID": 
                    self.FrameLeftNID = Frame(self.FrameMidhaut,bg='white')
                    self.FrameLeftNID.pack(expand=True,fill=BOTH)

                    listeNid = ['NID','SVERT','MAM1','MAM12', 'MAM2','MAM23','MAM3','MAM34','MAM45','MAM4', 'MAM5']

                    self.VarSpecies = StringVar()

                    print(self.controller.getspe())
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


                if tab != "FBN NID" and tab != "Vertebra" and tab!= "Sternum":

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

                if tab == "Vertebra":
                     
                    self.FramePortion = Frame(self.FrameMidhaut)
                    self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                    self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                    self.LabelPortion.pack()


                    self.CheckBOD = Checkbutton(self.FramePortion, text="Body",font=font_ecriture,
                                        variable=self.VarPotionBOD,onvalue='BOD',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBOD.get(),'BOD'))
                    self.CheckBOD.pack(padx=5,anchor='w')

                    self.CheckBODe = Checkbutton(self.FramePortion, text="Body unfused",font=font_ecriture,
                                        variable=self.VarPotionBODe,onvalue='BODe',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBODe.get(),'BODe'))
                    self.CheckBODe.pack(padx=5,anchor='w')

                    self.CheckDisc = Checkbutton(self.FramePortion, text="Disc fused",font=font_ecriture,
                                        variable=self.VarPotionDISC,onvalue='DISC',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionDISC.get(),'DISC'))
                    self.CheckDisc.pack(padx=5,anchor='w')

                    self.CheckDisce = Checkbutton(self.FramePortion, text="Disc unfused",font=font_ecriture,
                                        variable=self.VarPotionDISCe,onvalue='DISCe',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionDISCe.get(),'DISCe'))
                    self.CheckDisce.pack(padx=5,anchor='w')

                    self.CheckTRP = Checkbutton(self.FramePortion, text="Transverse proc",font=font_ecriture,
                                        variable=self.VarPotionTRP,onvalue='TRP',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionTRP.get(),'TRP'))
                    self.CheckTRP.pack(padx=5,anchor='w')

                    self.CheckARP = Checkbutton(self.FramePortion, text="Articular proc",font=font_ecriture,
                                        variable=self.VarPotionARP,onvalue='ARP',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionARP.get(),'ARP'))
                    self.CheckARP.pack(padx=5,anchor='w')

                    self.CheckARP = Checkbutton(self.FramePortion, text="Spinous proc",font=font_ecriture,
                                        variable=self.VarPotionSPIvrt,onvalue='SPIvrt',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionSPIvrt.get(),'SPIvrt'))
                    self.CheckARP.pack(padx=5,anchor='w')


                    listeDetail =['Vertebra indet','Atlas','Axis','Other cervical','Thoracic','Lumblar','Sacrum','Caudal']

                    self.NotebookD = ttk.Notebook(self.FrameMidhaut)
                    self.NotebookD.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameVertebraInd = Frame(self.NotebookD,bg='white')
                    self.FrameAtlas = Frame(self.NotebookD,bg='white')
                    self.FrameAxis = Frame(self.NotebookD,bg='white')
                    self.FrameOther = Frame(self.NotebookD,bg='white')
                    self.FrameThoracic = Frame(self.NotebookD,bg='white')
                    self.FrameLumblar = Frame(self.NotebookD,bg='white')
                    self.FrameSacrum = Frame(self.NotebookD,bg='white')
                    self.FrameCaudal = Frame(self.NotebookD,bg='white')

                    ListePageD =[self.FrameVertebraInd,self.FrameAtlas,self.FrameAxis,self.FrameOther,self.FrameThoracic,self.FrameLumblar,self.FrameSacrum,self.FrameCaudal]
                    
                    for tabD, pageD in zip(listeDetail, ListePageD):
                        self.NotebookD.add(pageD, text=tabD)
                    
                    ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

                    self.NotebookVA = ttk.Notebook(self.FrameAtlas)
                    self.NotebookVA.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVA = Frame(self.NotebookVA,bg='white')
                    self.FrameEquidVA = Frame(self.NotebookVA,bg='white')
                    self.FrameSuiformVA = Frame(self.NotebookVA,bg='white')
                    self.FrameUrsidVA = Frame(self.NotebookVA,bg='white')
                    self.FrameOtherVA = Frame(self.NotebookVA,bg='white')

                    ListePageVA =[self.FrameBovidVA,self.FrameEquidVA,self.FrameSuiformVA,self.FrameUrsidVA,self.FrameOtherVA]
                    
                    for tabVA, pageVA in zip(ListeTab, ListePageVA):
                        self.NotebookVA.add(pageVA, text=tabVA)


                    #atlas

                    self.VarCheckVA47 = IntVar()
                    self.VarCheckVA47.set(self.controller.getNDe(47))

                    self.VarCheckVA48 = IntVar()
                    self.VarCheckVA48.set(self.controller.getNDe(48))

                    self.canvaVAB = Canvas(self.FrameBovidVA,bg='white')
                    self.canvaVAB.pack(expand=True,fill=BOTH)

                    self.image_fondVAB = PhotoImage(file="View/Skull/FBN/vertebta_img/atlas/b.png")
                    self.canvaVAB.create_image(0, 0, anchor="nw", image=self.image_fondVAB)

                    self.CheckVA47 = Checkbutton(self.canvaVAB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVA47,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(47,self.VarCheckVA47.get()))
                    self.canvaVAB.create_window(160,85, anchor="nw", window= self.CheckVA47)

                    

                    self.CheckVA48 = Checkbutton(self.canvaVAB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVA48,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(48,self.VarCheckVA48.get()))
                    self.canvaVAB.create_window(580,115, anchor="nw", window= self.CheckVA48)




                    self.canvaVAE = Canvas(self.FrameEquidVA,bg='white')
                    self.canvaVAE.pack(expand=True,fill=BOTH)

                    self.image_fondVAE = PhotoImage(file="View/Skull/FBN/vertebta_img/atlas/e.png")
                    self.image_fondVAE = self.image_fondVAE.subsample(3)
                    self.canvaVAE.create_image(0, 0, anchor="nw", image=self.image_fondVAE)

                    self.CheckVAE47 = Checkbutton(self.canvaVAE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVA47,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(47,self.VarCheckVA47.get()))
                    self.canvaVAE.create_window(160,105, anchor="nw", window= self.CheckVAE47)

                    

                    self.CheckVAE48 = Checkbutton(self.canvaVAE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVA48,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(48,self.VarCheckVA48.get()))
                    self.canvaVAE.create_window(480,145, anchor="nw", window= self.CheckVAE48)



                    self.canvaVAS = Canvas(self.FrameSuiformVA,bg='white')
                    self.canvaVAS.pack(expand=True,fill=BOTH)

                    self.image_fondVAS = PhotoImage(file="View/Skull/FBN/vertebta_img/atlas/s.png")
                    self.canvaVAS.create_image(0, 0, anchor="nw", image=self.image_fondVAS)

                    self.CheckVAS47 = Checkbutton(self.canvaVAS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVA47,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(47,self.VarCheckVA47.get()))
                    self.canvaVAS.create_window(170,145, anchor="nw", window= self.CheckVAS47)

                    

                    self.CheckVAS48 = Checkbutton(self.canvaVAS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVA48,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(48,self.VarCheckVA48.get()))
                    self.canvaVAS.create_window(650,165, anchor="nw", window= self.CheckVAS48)



                    self.canvaVAU = Canvas(self.FrameUrsidVA,bg='white')
                    self.canvaVAU.pack(expand=True,fill=BOTH)

                    self.image_fondVAU = PhotoImage(file="View/Skull/FBN/vertebta_img/atlas/u.png")
                    self.image_fondVAU = self.image_fondVAU.subsample(2)
                    self.canvaVAU.create_image(0, 0, anchor="nw", image=self.image_fondVAU)

                    self.CheckVAU47 = Checkbutton(self.canvaVAU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVA47,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(47,self.VarCheckVA47.get()))
                    self.canvaVAU.create_window(170,85, anchor="nw", window= self.CheckVAU47)

                    

                    self.CheckVAU48 = Checkbutton(self.canvaVAU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVA48,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(48,self.VarCheckVA48.get()))
                    self.canvaVAU.create_window(575,125, anchor="nw", window= self.CheckVAU48)



                    self.canvaVAO = Canvas(self.FrameOtherVA,bg='white')
                    self.canvaVAO.pack(expand=True,fill=BOTH)

                    self.image_fondVAO = PhotoImage(file="View/Skull/FBN/vertebta_img/atlas/o.png")
                    self.canvaVAO.create_image(0, 0, anchor="nw", image=self.image_fondVAO)

                    self.CheckVAO47 = Checkbutton(self.canvaVAO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVA47,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(47,self.VarCheckVA47.get()))
                    self.canvaVAO.create_window(195,115, anchor="nw", window= self.CheckVAO47)

                    

                    self.CheckVAO48 = Checkbutton(self.canvaVAO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVA48,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(48,self.VarCheckVA48.get()))
                    self.canvaVAO.create_window(675,165, anchor="nw", window= self.CheckVAO48)





                    self.NotebookVAx = ttk.Notebook(self.FrameAxis)
                    self.NotebookVAx.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVAx = Frame(self.NotebookVAx,bg='white')
                    self.FrameEquidVAx = Frame(self.NotebookVAx,bg='white')
                    self.FrameSuiformVAx = Frame(self.NotebookVAx,bg='white')
                    self.FrameUrsidVAx = Frame(self.NotebookVAx,bg='white')
                    self.FrameOtherVAx = Frame(self.NotebookVAx,bg='white')

                    ListePageVAx =[self.FrameBovidVAx,self.FrameEquidVAx,self.FrameSuiformVAx,self.FrameUrsidVAx,self.FrameOtherVAx]
                    
                    for tabVAx, pageVAx in zip(ListeTab, ListePageVAx):
                        self.NotebookVAx.add(pageVAx, text=tabVAx)



                    self.VarCheckVAx49 = IntVar()
                    self.VarCheckVAx49.set(self.controller.getNDe(49))

                    self.VarCheckVAx50 = IntVar()
                    self.VarCheckVAx50.set(self.controller.getNDe(50))

                    self.canvaVAxB = Canvas(self.FrameBovidVAx,bg='white')
                    self.canvaVAxB.pack(expand=True,fill=BOTH)

                    self.image_fondVAxB = PhotoImage(file="View/Skull/FBN/vertebta_img/axis/b.png")
                    self.canvaVAxB.create_image(0, 0, anchor="nw", image=self.image_fondVAxB)

                    self.CheckVAx49 = Checkbutton(self.canvaVAxB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVAx49,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(49,self.VarCheckVAx49.get()))
                    self.canvaVAxB.create_window(140,135, anchor="nw", window= self.CheckVAx49)

                    

                    self.CheckVAx50 = Checkbutton(self.canvaVAxB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVAx50,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(50,self.VarCheckVAx50.get()))
                    self.canvaVAxB.create_window(220,85, anchor="nw", window= self.CheckVAx50)




                    self.canvaVAxE = Canvas(self.FrameEquidVAx,bg='white')
                    self.canvaVAxE.pack(expand=True,fill=BOTH)

                    self.image_fondVAxE = PhotoImage(file="View/Skull/FBN/vertebta_img/axis/e.png")
                    self.image_fondVAxE = self.image_fondVAxE.subsample(3)
                    self.canvaVAxE.create_image(0, 0, anchor="nw", image=self.image_fondVAxE)

                    self.CheckVAxE49 = Checkbutton(self.canvaVAxE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVAx49,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(49,self.VarCheckVAx49.get()))
                    self.canvaVAxE.create_window(75,255, anchor="nw", window= self.CheckVAxE49)

                    

                    self.CheckVAxE50 = Checkbutton(self.canvaVAxE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVAx50,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(50,self.VarCheckVAx50.get()))
                    self.canvaVAxE.create_window(185,195, anchor="nw", window= self.CheckVAxE50)



                    self.canvaVAxS = Canvas(self.FrameSuiformVAx,bg='white')
                    
                    self.canvaVAxS.pack(expand=True,fill=BOTH)

                    self.image_fondVAxS = PhotoImage(file="View/Skull/FBN/vertebta_img/axis/s.png")
                    self.image_fondVAxS = self.image_fondVAxS.subsample(2)
                    self.canvaVAxS.create_image(0, 0, anchor="nw", image=self.image_fondVAxS)

                    self.CheckVAxS49 = Checkbutton(self.canvaVAxS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVAx49,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(49,self.VarCheckVAx49.get()))
                    self.canvaVAxS.create_window(15,175, anchor="nw", window= self.CheckVAxS49)

                    

                    self.CheckVAxS50= Checkbutton(self.canvaVAxS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVAx50,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(50,self.VarCheckVAx50.get()))
                    self.canvaVAxS.create_window(130,155, anchor="nw", window= self.CheckVAxS50)



                    self.canvaVAxU = Canvas(self.FrameUrsidVAx,bg='white')
                    self.canvaVAxU.pack(expand=True,fill=BOTH)

                    self.image_fondVAxU = PhotoImage(file="View/Skull/FBN/vertebta_img/axis/u.png")
                    self.image_fondVAxU = self.image_fondVAxU.subsample(2)
                    self.canvaVAxU.create_image(0, 0, anchor="nw", image=self.image_fondVAxU)

                    self.CheckVAxU49= Checkbutton(self.canvaVAxU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVAx49,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(49,self.VarCheckVAx49.get()))
                    self.canvaVAxU.create_window(20,135, anchor="nw", window= self.CheckVAxU49)

                    

                    self.CheckVAxU50 = Checkbutton(self.canvaVAxU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVAx50,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(50,self.VarCheckVAx50.get()))
                    self.canvaVAxU.create_window(130,135, anchor="nw", window= self.CheckVAxU50)



                    self.canvaVAxO = Canvas(self.FrameOtherVAx,bg='white')
                    self.canvaVAxO.pack(expand=True,fill=BOTH)

                    self.image_fondVAxO = PhotoImage(file="View/Skull/FBN/vertebta_img/axis/o.png")
                    self.image_fondVAxO = self.image_fondVAxO.subsample(2)
                    self.canvaVAxO.create_image(0, 0, anchor="nw", image=self.image_fondVAxO)

                    self.CheckVAxO49 = Checkbutton(self.canvaVAxO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVAx49,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(49,self.VarCheckVAx49.get()))
                    self.canvaVAxO.create_window(5,125, anchor="nw", window= self.CheckVAxO49)

                    

                    self.CheckVAOx50 = Checkbutton(self.canvaVAxO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVAx50,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(50,self.VarCheckVAx50.get()))
                    self.canvaVAxO.create_window(75,165, anchor="nw", window= self.CheckVAOx50)




                    self.NotebookVO = ttk.Notebook(self.FrameOther)
                    self.NotebookVO.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVO = Frame(self.NotebookVO,bg='white')
                    self.FrameEquidVO = Frame(self.NotebookVO,bg='white')
                    self.FrameSuiformVO = Frame(self.NotebookVO,bg='white')
                    self.FrameUrsidVO = Frame(self.NotebookVO,bg='white')
                    self.FrameOtherVO = Frame(self.NotebookVO,bg='white')

                    ListePageVO =[self.FrameBovidVO,self.FrameEquidVO,self.FrameSuiformVO,self.FrameUrsidVO,self.FrameOtherVO]
                    
                    for tabVO, pageVO in zip(ListeTab, ListePageVO):
                        self.NotebookVO.add(pageVO, text=tabVO)

                    self.VarCheckVO51 = IntVar()
                    self.VarCheckVO51.set(self.controller.getNDe(51))

                    self.VarCheckVO52 = IntVar()
                    self.VarCheckVO52.set(self.controller.getNDe(52))

                    self.canvaVOB = Canvas(self.FrameBovidVO,bg='white')
                    self.canvaVOB.pack(expand=True,fill=BOTH)

                    self.image_fondVOB = PhotoImage(file="View/Skull/FBN/vertebta_img/cervical/b.png")
                    self.canvaVOB.create_image(0, 0, anchor="nw", image=self.image_fondVOB)

                    self.CheckVO51 = Checkbutton(self.canvaVOB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVO51,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(51,self.VarCheckVO51.get()))
                    self.canvaVOB.create_window(90,85, anchor="nw", window= self.CheckVO51)

                    

                    self.CheckVO52 = Checkbutton(self.canvaVOB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVO52,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(52,self.VarCheckVO52.get()))
                    self.canvaVOB.create_window(150,100, anchor="nw", window= self.CheckVO52)




                    self.canvaVOE = Canvas(self.FrameEquidVO,bg='white')
                    self.canvaVOE.pack(expand=True,fill=BOTH)

                    self.image_fondVOE = PhotoImage(file="View/Skull/FBN/vertebta_img/cervical/e.png")
                    self.image_fondVOE = self.image_fondVOE.subsample(3)
                    self.canvaVOE.create_image(0, 0, anchor="nw", image=self.image_fondVOE)

                    self.CheckVOE51 = Checkbutton(self.canvaVOE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVO51,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(51,self.VarCheckVO51.get()))
                    self.canvaVOE.create_window(80,70, anchor="nw", window= self.CheckVOE51)

                    

                    self.CheckVOE52 = Checkbutton(self.canvaVOE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVO52,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(52,self.VarCheckVO52.get()))
                    self.canvaVOE.create_window(130,75, anchor="nw", window= self.CheckVOE52)



                    self.canvaVOS = Canvas(self.FrameSuiformVO,bg='white')
                    self.canvaVOS.pack(expand=True,fill=BOTH)

                    self.image_fondVOS = PhotoImage(file="View/Skull/FBN/vertebta_img/cervical/s.png")
                    self.image_fondVOS = self.image_fondVOS.subsample(2)
                    self.canvaVOS.create_image(0, 0, anchor="nw", image=self.image_fondVOS)

                    self.CheckVOS51 = Checkbutton(self.canvaVOS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVO51,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(51,self.VarCheckVO51.get()))
                    self.canvaVOS.create_window(50,75, anchor="nw", window= self.CheckVOS51)

                    

                    self.CheckVOS52 = Checkbutton(self.canvaVOS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVO52,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(52,self.VarCheckVO52.get()))
                    self.canvaVOS.create_window(80,85, anchor="nw", window= self.CheckVOS52)




                    self.canvaVOU = Canvas(self.FrameUrsidVO,bg='white')
                    self.canvaVOU.pack(expand=True,fill=BOTH)

                    self.image_fondVOU = PhotoImage(file="View/Skull/FBN/vertebta_img/cervical/u.png")
                    self.image_fondVOU = self.image_fondVOU.subsample(2)
                    self.canvaVOU.create_image(0, 0, anchor="nw", image=self.image_fondVOU)

                    self.CheckVOU51 = Checkbutton(self.canvaVOU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVO51,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(51,self.VarCheckVO51.get()))
                    self.canvaVOU.create_window(110,115, anchor="nw", window= self.CheckVOU51)

                    

                    self.CheckVOU52 = Checkbutton(self.canvaVOU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVO52,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(52,self.VarCheckVO52.get()))
                    self.canvaVOU.create_window(200,85, anchor="nw", window= self.CheckVOU52)



                    self.canvaVOO = Canvas(self.FrameOtherVO,bg='white')
                    self.canvaVOO.pack(expand=True,fill=BOTH)

                    self.image_fondVOO = PhotoImage(file="View/Skull/FBN/vertebta_img/cervical/o.png")
                    self.image_fondVOO = self.image_fondVOO.subsample(2)
                    self.canvaVOO.create_image(0, 0, anchor="nw", image=self.image_fondVOO)

                    self.CheckVOO51 = Checkbutton(self.canvaVOO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVO51,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(51,self.VarCheckVO51.get()))
                    self.canvaVOO.create_window(55,55, anchor="nw", window= self.CheckVOO51)

                    

                    self.CheckVOO52 = Checkbutton(self.canvaVOO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVO52,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(52,self.VarCheckVO52.get()))
                    self.canvaVOO.create_window(115,35, anchor="nw", window= self.CheckVOO52)



                    self.NotebookVT = ttk.Notebook(self.FrameThoracic)
                    self.NotebookVT.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVT = Frame(self.NotebookVT,bg='white')
                    self.FrameEquidVT = Frame(self.NotebookVT,bg='white')
                    self.FrameSuiformVT = Frame(self.NotebookVT,bg='white')
                    self.FrameUrsidVT = Frame(self.NotebookVT,bg='white')
                    self.FrameOtherVT = Frame(self.NotebookVT,bg='white')

                    ListePageVT =[self.FrameBovidVT,self.FrameEquidVT,self.FrameSuiformVT,self.FrameUrsidVT,self.FrameOtherVT]
                    
                    for tabVT, pageVT in zip(ListeTab, ListePageVT):
                        self.NotebookVT.add(pageVT, text=tabVT)

                    self.VarCheckVT53 = IntVar()
                    self.VarCheckVT53.set(self.controller.getNDe(53))

                    self.VarCheckVT54 = IntVar()
                    self.VarCheckVT54.set(self.controller.getNDe(54))

                    self.canvaVT = Canvas(self.FrameBovidVT,bg='white')
                    self.canvaVT.pack(expand=True,fill=BOTH)

                    self.image_fondVT = PhotoImage(file="View/Skull/FBN/vertebta_img/thoracic/b.png")
                    self.image_fondVT = self.image_fondVT.subsample(2)
                    self.canvaVT.create_image(0, 0, anchor="nw", image=self.image_fondVT)

                    self.CheckVT51 = Checkbutton(self.canvaVT,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVT53,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(53,self.VarCheckVT53.get()))
                    self.canvaVT.create_window(65,110, anchor="nw", window= self.CheckVT51)

                    self.CheckVT52 = Checkbutton(self.canvaVT,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVT54,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(54,self.VarCheckVT54.get()))
                    self.canvaVT.create_window(55,165, anchor="nw", window= self.CheckVT52)


                    self.canvaVTE = Canvas(self.FrameEquidVT,bg='white')
                    self.canvaVTE.pack(expand=True,fill=BOTH)

                    self.image_fondVTE = PhotoImage(file="View/Skull/FBN/vertebta_img/thoracic/e.png")
                    self.image_fondVTE = self.image_fondVTE.subsample(4)
                    self.canvaVTE.create_image(0, 0, anchor="nw", image=self.image_fondVTE)

                    self.CheckVTE51 = Checkbutton(self.canvaVTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVT53,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(53,self.VarCheckVT53.get()))
                    self.canvaVTE.create_window(85,115, anchor="nw", window= self.CheckVTE51)

                    self.CheckVTE52 = Checkbutton(self.canvaVTE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVT54,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(54,self.VarCheckVT54.get()))
                    self.canvaVTE.create_window(70,185, anchor="nw", window= self.CheckVTE52)


                    self.canvaVTS = Canvas(self.FrameSuiformVT,bg='white')
                    self.canvaVTS.pack(expand=True,fill=BOTH)

                    self.image_fondVTS = PhotoImage(file="View/Skull/FBN/vertebta_img/thoracic/s.png")
                    self.image_fondVTS = self.image_fondVTS.subsample(2)
                    self.canvaVTS.create_image(0, 0, anchor="nw", image=self.image_fondVTS)

                    self.CheckVTS51 = Checkbutton(self.canvaVTS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVT53,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(53,self.VarCheckVT53.get()))
                    self.canvaVTS.create_window(85,75, anchor="nw", window= self.CheckVTS51)

                    self.CheckVTS52 = Checkbutton(self.canvaVTS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVT54,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(54,self.VarCheckVT54.get()))
                    self.canvaVTS.create_window(70,135, anchor="nw", window= self.CheckVTS52)



                    self.canvaVTU = Canvas(self.FrameUrsidVT,bg='white')
                    self.canvaVTU.pack(expand=True,fill=BOTH)

                    self.image_fondVTU = PhotoImage(file="View/Skull/FBN/vertebta_img/thoracic/u.png")
                    self.image_fondVTU = self.image_fondVTU.subsample(3)
                    self.canvaVTU.create_image(0, 0, anchor="nw", image=self.image_fondVTU)

                    self.CheckVTU51 = Checkbutton(self.canvaVTU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVT53,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(53,self.VarCheckVT53.get()))
                    self.canvaVTU.create_window(85,105, anchor="nw", window= self.CheckVTU51)

                    self.CheckVTU52 = Checkbutton(self.canvaVTU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVT54,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(54,self.VarCheckVT54.get()))
                    self.canvaVTU.create_window(90,170, anchor="nw", window= self.CheckVTU52)

                    self.canvaVTO = Canvas(self.FrameOtherVT,bg='white')
                    self.canvaVTO.pack(expand=True,fill=BOTH)

                    self.image_fondVTO = PhotoImage(file="View/Skull/FBN/vertebta_img/thoracic/o.png")
                    self.image_fondVTO = self.image_fondVTO.subsample(2)
                    self.canvaVTO.create_image(0, 0, anchor="nw", image=self.image_fondVTO)

                    self.CheckVTO51 = Checkbutton(self.canvaVTO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVT53,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(53,self.VarCheckVT53.get()))
                    self.canvaVTO.create_window(80,50, anchor="nw", window= self.CheckVTO51)

                    

                    self.CheckVTO52 = Checkbutton(self.canvaVTO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVT54,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(54,self.VarCheckVT54.get()))
                    self.canvaVTO.create_window(60,110, anchor="nw", window= self.CheckVTO52)



                    self.NotebookVL = ttk.Notebook(self.FrameLumblar)
                    self.NotebookVL.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVL = Frame(self.NotebookVL,bg='white')
                    self.FrameEquidVL = Frame(self.NotebookVL,bg='white')
                    self.FrameSuiformVL = Frame(self.NotebookVL,bg='white')
                    self.FrameUrsidVL = Frame(self.NotebookVL,bg='white')
                    self.FrameOtherVL = Frame(self.NotebookVL,bg='white')

                    ListePageVL =[self.FrameBovidVL,self.FrameEquidVL,self.FrameSuiformVL,self.FrameUrsidVL,self.FrameOtherVL]
                    
                    for tabVL, pageVL in zip(ListeTab, ListePageVL):
                        self.NotebookVL.add(pageVL, text=tabVL)

                    self.VarCheckVL55 = IntVar()
                    self.VarCheckVL55.set(self.controller.getNDe(55))

                    self.VarCheckVL56 = IntVar()
                    self.VarCheckVL56.set(self.controller.getNDe(56))


                    self.canvaVL = Canvas(self.FrameBovidVL,bg='white')
                    self.canvaVL.pack(expand=True,fill=BOTH)

                    self.image_fondVL = PhotoImage(file="View/Skull/FBN/vertebta_img/lumblar/b.png")
                    #self.image_fondVL = self.image_fondVL.subsample(2)
                    self.canvaVL.create_image(0, 0, anchor="nw", image=self.image_fondVL)



                    self.CheckVL55 = Checkbutton(self.canvaVL,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVL55,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(55,self.VarCheckVL55.get()))
                    self.canvaVL.create_window(230,60, anchor="nw", window= self.CheckVL55)

                    self.CheckVL56 = Checkbutton(self.canvaVL,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVL56,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(56,self.VarCheckVL56.get()))
                    self.canvaVL.create_window(245,110, anchor="nw", window= self.CheckVL56)



                    self.canvaVLE = Canvas(self.FrameEquidVL,bg='white')
                    self.canvaVLE.pack(expand=True,fill=BOTH)

                    self.image_fondVLE = PhotoImage(file="View/Skull/FBN/vertebta_img/lumblar/e.png")
                    self.image_fondVLE = self.image_fondVLE.subsample(2)
                    self.canvaVLE.create_image(0, 0, anchor="nw", image=self.image_fondVLE)



                    self.CheckVLE55 = Checkbutton(self.canvaVLE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVL55,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(55,self.VarCheckVL55.get()))
                    self.canvaVLE.create_window(240,75, anchor="nw", window= self.CheckVLE55)

                    self.CheckVLE56 = Checkbutton(self.canvaVLE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVL56,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(56,self.VarCheckVL56.get()))
                    self.canvaVLE.create_window(225,160, anchor="nw", window= self.CheckVLE56)



                    self.canvaVLS = Canvas(self.FrameSuiformVL,bg='white')
                    self.canvaVLS.pack(expand=True,fill=BOTH)

                    self.image_fondVLS = PhotoImage(file="View/Skull/FBN/vertebta_img/lumblar/s.png")
                    #self.image_fondVLS = self.image_fondVLS.subsample(2)
                    self.canvaVLS.create_image(0, 0, anchor="nw", image=self.image_fondVLS)



                    self.CheckVLS55 = Checkbutton(self.canvaVLS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVL55,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(55,self.VarCheckVL55.get()))
                    self.canvaVLS.create_window(255,85, anchor="nw", window= self.CheckVLS55)

                    self.CheckVLS56 = Checkbutton(self.canvaVLS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVL56,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(56,self.VarCheckVL56.get()))
                    self.canvaVLS.create_window(270,150, anchor="nw", window= self.CheckVLS56)




                    self.canvaVLU = Canvas(self.FrameUrsidVL,bg='white')
                    self.canvaVLU.pack(expand=True,fill=BOTH)

                    self.image_fondVLU = PhotoImage(file="View/Skull/FBN/vertebta_img/lumblar/u.png")
                    self.image_fondVLU = self.image_fondVLU.subsample(2)
                    self.canvaVLU.create_image(0, 0, anchor="nw", image=self.image_fondVLU)



                    self.CheckVLU55 = Checkbutton(self.canvaVLU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVL55,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(55,self.VarCheckVL55.get()))
                    self.canvaVLU.create_window(130,55, anchor="nw", window= self.CheckVLU55)

                    self.CheckVLU56 = Checkbutton(self.canvaVLU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVL56,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(56,self.VarCheckVL56.get()))
                    self.canvaVLU.create_window(225,90, anchor="nw", window= self.CheckVLU56)





                    self.canvaVLO = Canvas(self.FrameOtherVL,bg='white')
                    self.canvaVLO.pack(expand=True,fill=BOTH)

                    self.image_fondVLO = PhotoImage(file="View/Skull/FBN/vertebta_img/lumblar/o.png")
                    self.image_fondVLO = self.image_fondVLO.subsample(2)
                    self.canvaVLO.create_image(0, 0, anchor="nw", image=self.image_fondVLO)



                    self.CheckVLO55 = Checkbutton(self.canvaVLO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVL55,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(55,self.VarCheckVL55.get()))
                    self.canvaVLO.create_window(105,20, anchor="nw", window= self.CheckVLO55)

                    self.CheckVLO56 = Checkbutton(self.canvaVLO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVL56,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(56,self.VarCheckVL56.get()))
                    self.canvaVLO.create_window(90,90, anchor="nw", window= self.CheckVLO56)



                    self.NotebookVS = ttk.Notebook(self.FrameSacrum)
                    self.NotebookVS.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidVS = Frame(self.NotebookVS,bg='white')
                    self.FrameEquidVS = Frame(self.NotebookVS,bg='white')
                    self.FrameSuiformVS = Frame(self.NotebookVS,bg='white')
                    self.FrameUrsidVS = Frame(self.NotebookVS,bg='white')
                    self.FrameOtherVS = Frame(self.NotebookVS,bg='white')

                    ListePageVS =[self.FrameBovidVS,self.FrameEquidVS,self.FrameSuiformVS,self.FrameUrsidVS,self.FrameOtherVS]
                    
                    for tabVS, pageVS in zip(ListeTab, ListePageVS):
                        self.NotebookVS.add(pageVS, text=tabVS)

                    self.VarCheckVS57 = IntVar()
                    self.VarCheckVS57.set(self.controller.getNDe(57))

                    self.VarCheckVS58 = IntVar()
                    self.VarCheckVS58.set(self.controller.getNDe(58))


                    self.canvaVS = Canvas(self.FrameBovidVS,bg='white')
                    self.canvaVS.pack(expand=True,fill=BOTH)

                    self.image_fondVS = PhotoImage(file="View/Skull/FBN/vertebta_img/sacrum/b.png")
                    #self.image_fondVL = self.image_fondVL.subsample(2)
                    self.canvaVS.create_image(0, 0, anchor="nw", image=self.image_fondVS)



                    self.CheckVS57 = Checkbutton(self.canvaVS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVS57,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(57,self.VarCheckVS57.get()))
                    self.canvaVS.create_window(210,110, anchor="nw", window= self.CheckVS57)

                    self.CheckVS58 = Checkbutton(self.canvaVS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVS58,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(58,self.VarCheckVS58.get()))
                    self.canvaVS.create_window(410,160, anchor="nw", window= self.CheckVS58)


                    self.canvaVSE = Canvas(self.FrameEquidVS,bg='white')
                    self.canvaVSE.pack(expand=True,fill=BOTH)

                    self.image_fondVSE = PhotoImage(file="View/Skull/FBN/vertebta_img/sacrum/e.png")
                    self.image_fondVSE = self.image_fondVSE.subsample(4)
                    self.canvaVSE.create_image(0, 0, anchor="nw", image=self.image_fondVSE)



                    self.CheckVSE57 = Checkbutton(self.canvaVSE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVS57,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(57,self.VarCheckVS57.get()))
                    self.canvaVSE.create_window(140,125, anchor="nw", window= self.CheckVSE57)

                    self.CheckVSE58 = Checkbutton(self.canvaVSE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVS58,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(58,self.VarCheckVS58.get()))
                    self.canvaVSE.create_window(265,115, anchor="nw", window= self.CheckVSE58)



                    self.canvaVSS = Canvas(self.FrameSuiformVS,bg='white')
                    self.canvaVSS.pack(expand=True,fill=BOTH)

                    self.image_fondVSS = PhotoImage(file="View/Skull/FBN/vertebta_img/sacrum/s.png")
                    self.image_fondVSS = self.image_fondVSS.subsample(2)
                    self.canvaVSS.create_image(0, 0, anchor="nw", image=self.image_fondVSS)



                    self.CheckVSS57 = Checkbutton(self.canvaVSS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVS57,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(57,self.VarCheckVS57.get()))
                    self.canvaVSS.create_window(110,85, anchor="nw", window= self.CheckVSS57)

                    self.CheckVSS58 = Checkbutton(self.canvaVSS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVS58,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(58,self.VarCheckVS58.get()))
                    self.canvaVSS.create_window(230,90, anchor="nw", window= self.CheckVSS58)


                    self.canvaVSU = Canvas(self.FrameUrsidVS,bg='white')
                    self.canvaVSU.pack(expand=True,fill=BOTH)

                    self.image_fondVSU = PhotoImage(file="View/Skull/FBN/vertebta_img/sacrum/u.png")
                    self.image_fondVSU = self.image_fondVSU.subsample(2)
                    self.canvaVSU.create_image(0, 0, anchor="nw", image=self.image_fondVSU)



                    self.CheckVSU57 = Checkbutton(self.canvaVSU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVS57,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(57,self.VarCheckVS57.get()))
                    self.canvaVSU.create_window(180,170, anchor="nw", window= self.CheckVSU57)

                    self.CheckVSU58 = Checkbutton(self.canvaVSU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVS58,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(58,self.VarCheckVS58.get()))
                    self.canvaVSU.create_window(500,120, anchor="nw", window= self.CheckVSU58)


                    self.canvaVSO = Canvas(self.FrameOtherVS,bg='white')
                    
                    self.canvaVSO.pack(expand=True,fill=BOTH)

                    self.image_fondVSO = PhotoImage(file="View/Skull/FBN/vertebta_img/sacrum/o.png")
                    self.image_fondVSO = self.image_fondVSO.subsample(2)
                    self.canvaVSO.create_image(0, 0, anchor="nw", image=self.image_fondVSO)



                    self.CheckVSO57 = Checkbutton(self.canvaVSO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckVS57,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(57,self.VarCheckVS57.get()))
                    self.canvaVSO.create_window(125,95, anchor="nw", window= self.CheckVSO57)

                    self.CheckVSO58 = Checkbutton(self.canvaVSO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckVS58,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(58,self.VarCheckVS58.get()))
                    self.canvaVSO.create_window(230,145, anchor="nw", window= self.CheckVSO58)


                    self.FrameCaudalCheck = Frame(self.FrameCaudal,bg='white')
                    self.FrameCaudalCheck.pack(expand=True)

                    self.VarCheckV59 = IntVar()
                    self.VarCheckV59.set(self.controller.getNDe(59))

                    self.Label59 = Label(self.FrameCaudalCheck,text="Caudal NDE :",bg='white')
                    self.Label59.pack(side=LEFT)

                    self.CheckV59 = Checkbutton(self.FrameCaudalCheck,bd=0,fg='red',bg='yellow',text=">50%",
                                            onvalue=1,offvalue=0,variable=self.VarCheckV59,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(59,self.VarCheckV59.get()))
                    self.CheckV59.pack(side=LEFT)




                                                                                                            


                if tab == "Rib":

                    self.FramePortion = Frame(self.FrameMidhaut)
                    self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                    self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                    self.LabelPortion.pack()


                    self.CheckP = Checkbutton(self.FramePortion, text="Head",font=font_ecriture,
                                        variable=self.VarPotionP,onvalue='P',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionP.get(),'P'))
                    self.CheckP.pack(padx=5,anchor='w')

                    self.CheckBOD = Checkbutton(self.FramePortion, text="Body",font=font_ecriture,
                                        variable=self.VarPotionBOD,onvalue='BOD',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBOD.get(),'BOD'))
                    self.CheckBOD.pack(padx=5,anchor='w')

                    self.CheckD = Checkbutton(self.FramePortion, text="Distal end",font=font_ecriture,
                                        variable=self.VarPotionD,onvalue='D',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionD.get(),'D'))
                    self.CheckD.pack(padx=5,anchor='w')

                    self.CheckCost = Checkbutton(self.FramePortion, text="Costal cartilage",font=font_ecriture,
                                        variable=self.VarPotionC,onvalue='COST',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionC.get(),'COST'))
                    self.CheckCost.pack(padx=5,anchor='w')


                    self.NotebookR = ttk.Notebook(self.FrameRib)
                    self.NotebookR.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidR = Frame(self.NotebookR,bg='white')
                    self.FrameEquidR = Frame(self.NotebookR,bg='white')
                    self.FrameSuiformR = Frame(self.NotebookR,bg='white')
                    self.FrameUrsidR = Frame(self.NotebookR,bg='white')
                    self.FrameOtherR = Frame(self.NotebookR,bg='white')

                    ListePageR =[self.FrameBovidR,self.FrameEquidR,self.FrameSuiformR,self.FrameUrsidR,self.FrameOtherR]

                    self.VarCir = StringVar()
                    self.VarCir.set(self.controller.getCirc())

                    self.VarCheck111= StringVar()
                    self.VarCheck111.set(self.controller.getNDe(111))

                    self.listeentry =[]
                    
                    for tabR, pageR in zip(ListeTab, ListePageR):
                        self.NotebookR.add(pageR, text=tabR)

                        self.FrameSHC = Frame(pageR)
                        self.FrameSHC.pack()

                        self.LabelSHC = Label(self.FrameSHC,text="SCH")
                        self.LabelSHC.pack()

                        

                        self.RadioM50 = Radiobutton(self.FrameSHC, text=">50%",value=">50%", variable=self.VarCir,font=font_ecriture,
                                                    command=lambda:self.toggle_shc())
                
                        self.RadioM50.pack(padx=5,anchor='w',side=LEFT)

                        self.RadioP50 = Radiobutton(self.FrameSHC, text="<50%", value="<50%",variable=self.VarCir,font=font_ecriture,
                                                    command=lambda:self.toggle_shc())
                        self.RadioP50.pack(padx=5,anchor='w',side=LEFT)

                        self.RadioCo = Radiobutton(self.FrameSHC, text="CO", value="CO",variable=self.VarCir,font=font_ecriture,
                                                   command=lambda:self.toggle_shc())
                        self.RadioCo.pack(padx=5,anchor='w',side=LEFT)


                        self.FrameSlen = Frame(pageR,bg='white')
                        self.FrameSlen.pack()

                        self.LabelSlen = Label(self.FrameSlen,text='Lenght (mm) \r(only for fragments with SHC >50%)',bg='white')
                        self.LabelSlen.pack(side=LEFT)

                        self.EntrySlen = NumpadEntry(self.FrameSlen,width=8,bg='white',bd=1 ,relief='solid',
                                                    textvariable=self.VarCheck111)
                        self.EntrySlen.pack(side=LEFT)

                        self.listeentry.append(self.EntrySlen)

                        self.toggle_shc()

                        self.VarCheck111.trace_add("write", lambda *args:self.controller.landmark(111,self.VarCheck111.get()))

                    self.VarCheckR60 = IntVar()
                    self.VarCheckR60.set(self.controller.getNDe(60))

                    self.VarCheckR61 = IntVar()
                    self.VarCheckR61.set(self.controller.getNDe(61))

                    self.canvaRB = Canvas(self.FrameBovidR,bg='white')
                    self.canvaRB.pack(expand=True,fill=BOTH)

                    self.image_fondRB = PhotoImage(file="View/Skull/FBN/rib_img/o.png")
                    self.image_fondRB = self.image_fondRB.subsample(2)
                    self.canvaRB.create_image(0, 0, anchor="nw", image=self.image_fondRB)



                    self.CheckR60 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR60,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(60,self.VarCheckR60.get()))
                    self.canvaRB.create_window(55,35, anchor="nw", window= self.CheckR60)

                    self.CheckR61 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckR61,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(61,self.VarCheckR61.get()))
                    self.canvaRB.create_window(295,60, anchor="nw", window= self.CheckR61)



                    self.canvaRE = Canvas(self.FrameEquidR,bg='white')
                    self.canvaRE.pack(expand=True,fill=BOTH)

                    self.image_fondRE = PhotoImage(file="View/Skull/FBN/rib_img/e.png")
                    self.image_fondRE = self.image_fondRE.subsample(2)
                    self.canvaRE.create_image(0, 0, anchor="nw", image=self.image_fondRE)

                    self.CheckRE60 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR60,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(60,self.VarCheckR60.get()))
                    self.canvaRE.create_window(60,20, anchor="nw", window= self.CheckRE60)

                    self.CheckRE61 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckR61,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(61,self.VarCheckR61.get()))
                    self.canvaRE.create_window(290,35, anchor="nw", window= self.CheckRE61)




                    self.canvaRS = Canvas(self.FrameSuiformR,bg='white')
                    self.canvaRS.pack(expand=True,fill=BOTH)

                    self.image_fondRS = PhotoImage(file="View/Skull/FBN/rib_img/s.png")
                    self.image_fondRS = self.image_fondRS.subsample(2)
                    self.canvaRS.create_image(0, 0, anchor="nw", image=self.image_fondRS)

                    self.CheckRS60 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR60,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(60,self.VarCheckR60.get()))
                    self.canvaRS.create_window(60,20, anchor="nw", window= self.CheckRS60)

                    self.CheckRS61 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckR61,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(61,self.VarCheckR61.get()))
                    self.canvaRS.create_window(290,35, anchor="nw", window= self.CheckRS61)


                    self.canvaRU = Canvas(self.FrameUrsidR,bg='white')
                    self.canvaRU.pack(expand=True,fill=BOTH)

                    self.image_fondRU = PhotoImage(file="View/Skull/FBN/rib_img/u.png")
                    self.image_fondRU = self.image_fondRU.subsample(2)
                    self.canvaRU.create_image(0, 0, anchor="nw", image=self.image_fondRU)

                    self.CheckRU60 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR60,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(60,self.VarCheckR60.get()))
                    self.canvaRU.create_window(70,45, anchor="nw", window= self.CheckRU60)

                    self.CheckRU61 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckR61,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(61,self.VarCheckR61.get()))
                    self.canvaRU.create_window(405,95, anchor="nw", window= self.CheckRU61)


                    self.canvaRO = Canvas(self.FrameOtherR,bg='white')
                    self.canvaRO.pack(expand=True,fill=BOTH)

                    self.image_fondRO = PhotoImage(file="View/Skull/FBN/rib_img/o.png")
                    self.image_fondRO = self.image_fondRO.subsample(2)
                    self.canvaRO.create_image(0, 0, anchor="nw", image=self.image_fondRO)

                    self.CheckRO60 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR60,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(60,self.VarCheckR60.get()))
                    self.canvaRO.create_window(55,35, anchor="nw", window= self.CheckRO60)

                    self.CheckRO61 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheckR61,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(61,self.VarCheckR61.get()))
                    self.canvaRO.create_window(295,60, anchor="nw", window= self.CheckRO61)


                if tab =="Sternum":

                    self.FrameSternumCheck = Frame(self.FrameMidhaut,bg='white')
                    self.FrameSternumCheck.pack(expand=True)

                    self.VarCheck62 = IntVar()
                    self.VarCheck62.set(self.controller.getNDe(62))

                    self.Label62 = Label(self.FrameSternumCheck,text="Sternebrae NDE : ",bg='white')
                    self.Label62.pack(side=LEFT)

                    self.Check62 = Checkbutton(self.FrameSternumCheck,bd=0,fg='red',bg='yellow',text=">50%",
                                            onvalue=1,offvalue=0,variable=self.VarCheck62,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(62,self.VarCheck62.get()))
                    self.Check62.pack(side=LEFT)


                if tab == "Scapula":

                    self.FramePortion = Frame(self.FrameMidhaut)
                    self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                    self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                    self.LabelPortion.pack()


                    self.CheckG = Checkbutton(self.FramePortion, text="Glenoid Cavity",font=font_ecriture,
                                        variable=self.VarPotionG,onvalue='GLEscp',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionG.get(),'GLEscp'))
                    self.CheckG.pack(padx=5,anchor='w')

                    self.CheckBODs = Checkbutton(self.FramePortion, text="Body/Blade",font=font_ecriture,
                                        variable=self.VarPotionBODs,onvalue='BODscp',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionBODs.get(),'BODscp'))
                    self.CheckBODs.pack(padx=5,anchor='w')

                    self.CheckSp = Checkbutton(self.FramePortion, text="Spine",font=font_ecriture,
                                        variable=self.VarPotionSP,onvalue='SPIscp',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionSP.get(),'SPIscp'))
                    self.CheckSp.pack(padx=5,anchor='w')


                    self.NotebookSc = ttk.Notebook(self.FrameMidhaut)
                    self.NotebookSc.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidSc = Frame(self.NotebookSc,bg='white')
                    self.FrameEquidSc = Frame(self.NotebookSc,bg='white')
                    self.FrameSuiformSc = Frame(self.NotebookSc,bg='white')
                    self.FrameUrsidSc = Frame(self.NotebookSc,bg='white')
                    self.FrameOtherSc = Frame(self.NotebookSc,bg='white')

                    ListePageSc =[self.FrameBovidSc,self.FrameEquidSc,self.FrameSuiformSc,self.FrameUrsidSc,self.FrameOtherSc]

                    for tabSc, pageSc in zip(ListeTab, ListePageSc):
                        self.NotebookSc.add(pageSc, text=tabSc)

                    self.VarCheck63= StringVar()
                    self.VarCheck63.set(self.controller.getNDe(63))

                    self.VarCheck64= StringVar()
                    self.VarCheck64.set(self.controller.getNDe(64))

                    self.VarCheck65= StringVar()
                    self.VarCheck65.set(self.controller.getNDe(65))


                    self.canvaSB = Canvas(self.FrameBovidSc,bg='white')
                    self.canvaSB.pack(expand=True,fill=BOTH)


                    self.image_fondSB = PhotoImage(file="View/Skull/FBN/scapula_img/b.png")
                    #self.image_fondSB = self.image_fondSB.subsample(2)
                    self.canvaSB.create_image(0, 0, anchor="nw", image=self.image_fondSB)



                    self.CheckS63 = Checkbutton(self.canvaSB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck63,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(63,self.VarCheck63.get()))
                    self.canvaSB.create_window(185,125, anchor="nw", window= self.CheckS63)

                    self.CheckS64 = Checkbutton(self.canvaSB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck64,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(64,self.VarCheck64.get()))
                    self.canvaSB.create_window(300,50, anchor="nw", window= self.CheckS64)

                    self.CheckS65 = Checkbutton(self.canvaSB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck65,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(65,self.VarCheck65.get()))
                    self.canvaSB.create_window(370,150, anchor="nw", window= self.CheckS65)




                    self.canvaSEB = Canvas(self.FrameEquidSc,bg='white')
                    self.canvaSEB.pack(expand=True,fill=BOTH)


                    self.image_fondSE = PhotoImage(file="View/Skull/FBN/scapula_img/e.png")
                    self.image_fondSE = self.image_fondSE.subsample(2)
                    self.canvaSEB.create_image(0, 0, anchor="nw", image=self.image_fondSE)



                    self.CheckSE63 = Checkbutton(self.canvaSEB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck63,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(63,self.VarCheck63.get()))
                    self.canvaSEB.create_window(235,125, anchor="nw", window= self.CheckSE63)

                    self.CheckSE64 = Checkbutton(self.canvaSEB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck64,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(64,self.VarCheck64.get()))
                    self.canvaSEB.create_window(595,90, anchor="nw", window= self.CheckSE64)

                    self.CheckSE65 = Checkbutton(self.canvaSEB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck65,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(65,self.VarCheck65.get()))
                    self.canvaSEB.create_window(470,150, anchor="nw", window= self.CheckSE65)



                    self.canvaSS = Canvas(self.FrameSuiformSc,bg='white')
                    self.canvaSS.pack(expand=True,fill=BOTH)


                    self.image_fondSS = PhotoImage(file="View/Skull/FBN/scapula_img/s.png")
                    #self.image_fondSS = self.image_fondSS.subsample(2)
                    self.canvaSS.create_image(0, 0, anchor="nw", image=self.image_fondSS)



                    self.CheckSS63 = Checkbutton(self.canvaSS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck63,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(63,self.VarCheck63.get()))
                    self.canvaSS.create_window(240,125, anchor="nw", window= self.CheckSS63)

                    self.CheckSS64 = Checkbutton(self.canvaSS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck64,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(64,self.VarCheck64.get()))
                    self.canvaSS.create_window(605,80, anchor="nw", window= self.CheckSS64)

                    self.CheckSS65 = Checkbutton(self.canvaSS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck65,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(65,self.VarCheck65.get()))
                    self.canvaSS.create_window(440,150, anchor="nw", window= self.CheckSS65)




                    self.canvaSU = Canvas(self.FrameUrsidSc,bg='white')
                    self.canvaSU.pack(expand=True,fill=BOTH)


                    self.image_fondSU = PhotoImage(file="View/Skull/FBN/scapula_img/u.png")
                    self.image_fondSU = self.image_fondSU.subsample(2)
                    self.canvaSU.create_image(0, 0, anchor="nw", image=self.image_fondSU)



                    self.CheckSU63 = Checkbutton(self.canvaSU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck63,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(63,self.VarCheck63.get()))
                    self.canvaSU.create_window(230,125, anchor="nw", window= self.CheckSU63)

                    self.CheckSU64 = Checkbutton(self.canvaSU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck64,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(64,self.VarCheck64.get()))
                    self.canvaSU.create_window(360,100, anchor="nw", window= self.CheckSU64)

                    self.CheckSU65 = Checkbutton(self.canvaSU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck65,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(65,self.VarCheck65.get()))
                    self.canvaSU.create_window(380,170, anchor="nw", window= self.CheckSU65)



                    self.canvaSO = Canvas(self.FrameOtherSc,bg='white')
                    self.canvaSO.pack(expand=True,fill=BOTH)

                    self.image_fondSO = PhotoImage(file="View/Skull/FBN/scapula_img/o.png")
                    #self.image_fondSO = self.image_fondSO.subsample(2)
                    self.canvaSO.create_image(0, 0, anchor="nw", image=self.image_fondSO)



                    self.CheckSO63 = Checkbutton(self.canvaSO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck63,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(63,self.VarCheck63.get()))
                    self.canvaSO.create_window(290,125, anchor="nw", window= self.CheckSO63)

                    self.CheckSO64 = Checkbutton(self.canvaSO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck64,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(64,self.VarCheck64.get()))
                    self.canvaSO.create_window(420,105, anchor="nw", window= self.CheckSO64)

                    self.CheckSO65 = Checkbutton(self.canvaSO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck65,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(65,self.VarCheck65.get()))
                    self.canvaSO.create_window(475,150, anchor="nw", window= self.CheckSO65)


                if tab == "Coxal":

                    self.FramePortion = Frame(self.FrameMidhaut)
                    self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                    self.LabelPortion = Label(self.FramePortion,text='Portion',font=font_ecriture)
                    self.LabelPortion.pack()

                    self.Frameportion2 = Frame(self.FramePortion)
                    self.Frameportion2.pack(side=LEFT,anchor='nw')


                    self.CheckIli = Checkbutton(self.Frameportion2, text="Ilium",font=font_ecriture,fg='#caa857',
                                        variable=self.VarPotionIli,onvalue='ILI',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionIli.get(),'ILI'))
                    self.CheckIli.pack(padx=5,anchor='w')

                    self.CheckIsc = Checkbutton(self.Frameportion2, text="Ischium",font=font_ecriture,fg='#71b1ba',
                                        variable=self.VarPotionIsc,onvalue='ISC',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionIsc.get(),'ISC'))
                    self.CheckIsc.pack(padx=5,anchor='w')

                    self.CheckPub = Checkbutton(self.Frameportion2, text="Pubis",font=font_ecriture,fg='#d2634c',
                                        variable=self.VarPotionPub,onvalue='PUB',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionPub.get(),'PUB'))
                    self.CheckPub.pack(padx=5,anchor='w')

                    self.CheckAce = Checkbutton(self.Frameportion2, text="Acetabulum",font=font_ecriture,fg='black',
                                        variable=self.VarPotionAce,onvalue='ACE',offvalue='',
                                        command=lambda:self.controller.updatePortion(self.VarPotionAce.get(),'ACE'))
                    self.CheckAce.pack(padx=5,anchor='w')

                    self.FrameImg = Frame(self.FramePortion)
                    self.FrameImg.pack(side=LEFT,anchor='nw')

                    self.canvaCox = Canvas(self.FrameImg,width=120)
                    self.canvaCox.pack(side=RIGHT,expand=True)

                    self.image_coxal = PhotoImage(file="View\Skull\FBN\coxal_img\coxal.png")
                    self.image_coxal = self.image_coxal.subsample(3)
                    self.canvaCox.create_image(0, 0, anchor="nw", image=self.image_coxal)



                    self.NotebookC = ttk.Notebook(self.FrameMidhaut)
                    self.NotebookC.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidC = Frame(self.NotebookC,bg='white')
                    self.FrameEquidC = Frame(self.NotebookC,bg='white')
                    self.FrameSuiformC = Frame(self.NotebookC,bg='white')
                    self.FrameUrsidC = Frame(self.NotebookC,bg='white')
                    self.FrameOtherC = Frame(self.NotebookC,bg='white')

                    ListePageC =[self.FrameBovidC,self.FrameEquidC,self.FrameSuiformC,self.FrameUrsidC,self.FrameOtherC]

                    for tabC, pageC in zip(ListeTab, ListePageC):
                        self.NotebookC.add(pageC, text=tabC)

                    self.VarCheck78= StringVar()
                    self.VarCheck78.set(self.controller.getNDe(78))

                    self.VarCheck79= StringVar()
                    self.VarCheck79.set(self.controller.getNDe(79))

                    self.VarCheck80= StringVar()
                    self.VarCheck80.set(self.controller.getNDe(80))

                    self.canvaC = Canvas(self.FrameBovidC,bg='white')
                    self.canvaC.pack(expand=True,fill=BOTH)

                    self.image_fondC = PhotoImage(file="View/Skull/FBN/coxal_img/b.png")
                    #self.image_fondSO = self.image_fondSO.subsample(2)
                    self.canvaC.create_image(0, 0, anchor="nw", image=self.image_fondC)



                    self.CheckC78 = Checkbutton(self.canvaC,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck78,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(78,self.VarCheck78.get()))
                    self.canvaC.create_window(150,185, anchor="nw", window= self.CheckC78)

                    self.CheckC79 = Checkbutton(self.canvaC,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck79,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(79,self.VarCheck79.get()))
                    self.canvaC.create_window(610,215, anchor="nw", window= self.CheckC79)

                    self.CheckC80 = Checkbutton(self.canvaC,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck80,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(80,self.VarCheck80.get()))
                    self.canvaC.create_window(515,245, anchor="nw", window= self.CheckC80)



                    self.canvaCE = Canvas(self.FrameEquidC,bg='white')
                    self.canvaCE.pack(expand=True,fill=BOTH)
                    
                    self.image_fondCE = PhotoImage(file="View/Skull/FBN/coxal_img/e.png")
                    self.image_fondCE = self.image_fondCE.subsample(2)
                    self.canvaCE.create_image(0, 0, anchor="nw", image=self.image_fondCE)



                    self.CheckCE78 = Checkbutton(self.canvaCE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck78,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(78,self.VarCheck78.get()))
                    self.canvaCE.create_window(400,125, anchor="nw", window= self.CheckCE78)

                    self.CheckCE79 = Checkbutton(self.canvaCE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck79,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(79,self.VarCheck79.get()))
                    self.canvaCE.create_window(560,165, anchor="nw", window= self.CheckCE79)

                    self.CheckCE80 = Checkbutton(self.canvaCE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck80,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(80,self.VarCheck80.get()))
                    self.canvaCE.create_window(480,235, anchor="nw", window= self.CheckCE80)



                    self.canvaCS = Canvas(self.FrameSuiformC,bg='white')
                    self.canvaCS.pack(expand=True,fill=BOTH)
                    
                    self.image_fondCS = PhotoImage(file="View/Skull/FBN/coxal_img/s.png")
                    self.canvaCS.create_image(0, 0, anchor="nw", image=self.image_fondCS)



                    self.CheckCS78 = Checkbutton(self.canvaCS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck78,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(78,self.VarCheck78.get()))
                    self.canvaCS.create_window(135,125, anchor="nw", window= self.CheckCS78)

                    self.CheckCS79 = Checkbutton(self.canvaCS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck79,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(79,self.VarCheck79.get()))
                    self.canvaCS.create_window(665,145, anchor="nw", window= self.CheckCS79)

                    self.CheckCS80 = Checkbutton(self.canvaCS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck80,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(80,self.VarCheck80.get()))
                    self.canvaCS.create_window(600,210, anchor="nw", window= self.CheckCS80)



                    self.canvaCU = Canvas(self.FrameUrsidC,bg='white')
                    
                    self.canvaCU.pack(expand=True,fill=BOTH)
                    
                    self.image_fondCU = PhotoImage(file="View/Skull/FBN/coxal_img/u.png")
                    self.image_fondCU = self.image_fondCU.subsample(3)
                    self.canvaCU.create_image(0, 0, anchor="nw", image=self.image_fondCU)



                    self.CheckCU78 = Checkbutton(self.canvaCU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck78,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(78,self.VarCheck78.get()))
                    self.canvaCU.create_window(305,35, anchor="nw", window= self.CheckCU78)

                    self.CheckCU79 = Checkbutton(self.canvaCU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck79,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(79,self.VarCheck79.get()))
                    self.canvaCU.create_window(270,125, anchor="nw", window= self.CheckCU79)

                    self.CheckCU80 = Checkbutton(self.canvaCU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck80,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(80,self.VarCheck80.get()))
                    self.canvaCU.create_window(195,175, anchor="nw", window= self.CheckCU80)



                    self.canvaCO = Canvas(self.FrameOtherC,bg='white')
                    
                    self.canvaCO.pack(expand=True,fill=BOTH)
                    
                    self.image_fondCO = PhotoImage(file="View/Skull/FBN/coxal_img/o.png")
                    #self.image_fondCO = self.image_fondCO.subsample(2)
                    self.canvaCO.create_image(0, 0, anchor="nw", image=self.image_fondCO)



                    self.CheckCO78 = Checkbutton(self.canvaCO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck78,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(78,self.VarCheck78.get()))
                    self.canvaCO.create_window(120,140, anchor="nw", window= self.CheckCO78)

                    self.CheckCO79 = Checkbutton(self.canvaCO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck79,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(79,self.VarCheck79.get()))
                    self.canvaCO.create_window(660,200, anchor="nw", window= self.CheckCO79)

                    self.CheckCO80 = Checkbutton(self.canvaCO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck80,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(80,self.VarCheck80.get()))
                    self.canvaCO.create_window(575,270, anchor="nw", window= self.CheckCO80)


            if tab == "Hyoid":

                self.NotebookH = ttk.Notebook(self.FrameMidhaut)
                self.NotebookH.pack(fill='both',side="right",expand=True)
                style = ttk.Style()
                style.configure('TNotebook.Tab', padding=[20, 10])

                self.FrameBovidH = Frame(self.NotebookH,bg='white')
                self.FrameEquidH = Frame(self.NotebookH,bg='white')
                self.FrameSuiformH = Frame(self.NotebookH,bg='white')
                self.FrameUrsidH = Frame(self.NotebookH,bg='white')
                self.FrameOtherH = Frame(self.NotebookH,bg='white')

                ListePageH =[self.FrameBovidH,self.FrameEquidH,self.FrameSuiformH,self.FrameUrsidH,self.FrameOtherH]

                for tabH, pageH in zip(ListeTab, ListePageH):
                    self.NotebookH.add(pageH, text=tabH)


                self.VarCheck40= StringVar()
                self.VarCheck40.set(self.controller.getNDe(40))

                self.VarCheck42= StringVar()
                self.VarCheck42.set(self.controller.getNDe(42))

                self.VarCheck43= StringVar()
                self.VarCheck43.set(self.controller.getNDe(43))

                self.VarCheck44= StringVar()
                self.VarCheck44.set(self.controller.getNDe(44))

                self.VarCheck45= StringVar()
                self.VarCheck45.set(self.controller.getNDe(45))

                self.VarCheck46= StringVar()
                self.VarCheck46.set(self.controller.getNDe(46))


                self.canvaH = Canvas(self.FrameBovidH,bg='white')
                self.canvaH.pack(expand=True,fill=BOTH)
                
                self.image_fondH = PhotoImage(file="View/Skull/FBN/hyoid_img/b.png")
                #self.image_fondCO = self.image_fondCO.subsample(2)
                self.canvaH.create_image(0, 0, anchor="nw", image=self.image_fondH)

                self.CheckHE40 = Checkbutton(self.canvaH,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck40,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(40,self.VarCheck40.get()))
                self.canvaH.create_window(50,130, anchor="nw", window= self.CheckHE40)

                self.CheckHE42 = Checkbutton(self.canvaH,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck42,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(42,self.VarCheck42.get()))
                self.canvaH.create_window(150,60, anchor="nw", window= self.CheckHE42)

                self.CheckHE43 = Checkbutton(self.canvaH,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck43,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(43,self.VarCheck43.get()))
                self.canvaH.create_window(190,230, anchor="nw", window= self.CheckHE43)




                self.canvaHE = Canvas(self.FrameEquidH,bg='white')
                self.canvaHE.pack(expand=True,fill=BOTH)
                
                self.image_fondHE = PhotoImage(file="View/Skull/FBN/hyoid_img/e.png")
                #self.image_fondCO = self.image_fondCO.subsample(2)
                self.canvaHE.create_image(0, 0, anchor="nw", image=self.image_fondHE)

                self.CheckHE40 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck40,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(40,self.VarCheck40.get()))
                self.canvaHE.create_window(50,130, anchor="nw", window= self.CheckHE40)

                self.CheckHE42 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck42,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(42,self.VarCheck42.get()))
                self.canvaHE.create_window(150,60, anchor="nw", window= self.CheckHE42)

                self.CheckHE43 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck43,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(43,self.VarCheck43.get()))
                self.canvaHE.create_window(190,230, anchor="nw", window= self.CheckHE43)

                self.canvaHS = Canvas(self.FrameSuiformH,bg='white')
                self.canvaHS.pack(expand=True,fill=BOTH)
                
                self.image_fondHS = PhotoImage(file="View/Skull/FBN/hyoid_img/s.png")
                #self.image_fondCO = self.image_fondCO.subsample(2)
                self.canvaHS.create_image(0, 0, anchor="nw", image=self.image_fondHS)

                self.CheckHS40 = Checkbutton(self.canvaHS,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck40,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(40,self.VarCheck40.get()))
                self.canvaHS.create_window(130,80, anchor="nw", window= self.CheckHS40)



                self.canvaHU = Canvas(self.FrameUrsidH,bg='white')
                self.canvaHU.pack(expand=True,fill=BOTH)
                
                self.image_fondHU = PhotoImage(file="View/Skull/FBN/hyoid_img/u.png")
                self.image_fondHU = self.image_fondHU.subsample(3)
                self.canvaHU.create_image(0, 0, anchor="nw", image=self.image_fondHU)

                self.CheckHU40 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck40,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(40,self.VarCheck40.get()))
                self.canvaHU.create_window(40,50, anchor="nw", window= self.CheckHU40)

                self.CheckHU42 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck42,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(42,self.VarCheck42.get()))
                self.canvaHU.create_window(50,100, anchor="nw", window= self.CheckHU42)

                self.CheckHU45 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck45,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(45,self.VarCheck45.get()))
                self.canvaHU.create_window(5,160, anchor="nw", window= self.CheckHU45)


                self.CheckHU44 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck44,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(44,self.VarCheck44.get()))
                self.canvaHU.create_window(90,190, anchor="nw", window= self.CheckHU44)

                self.CheckHU46 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck46,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(46,self.VarCheck46.get()))
                self.canvaHU.create_window(50,230, anchor="nw", window= self.CheckHU46)

               

                self.canvaHO = Canvas(self.FrameOtherH,bg='white')
                self.canvaHO.pack(expand=True,fill=BOTH)
                
                self.image_fondHO = PhotoImage(file="View/Skull/FBN/hyoid_img/o.png")
                #self.image_fondCO = self.image_fondCO.subsample(2)
                self.canvaHO.create_image(0, 0, anchor="nw", image=self.image_fondHO)



                self.CheckHO40 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck40,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(40,self.VarCheck40.get()))
                self.canvaHO.create_window(65,120, anchor="nw", window= self.CheckHO40)

                self.CheckHO42 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                onvalue=1,offvalue=0,variable=self.VarCheck42,
                                image=self.img_off, selectimage=self.img_on,
                                compound='left', indicatoron=False,
                                command=lambda:self.controller.landmark(42,self.VarCheck42.get()))
                self.canvaHO.create_window(220,140, anchor="nw", window= self.CheckHO42)


        self.Notebook.select(self.controller.getOnglet('FBN'))

        self.Notebook.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.Notebook.index("current"),'FBN'))
            

        self.LabelExpl = Label(self.FrameRien,text='SELECT SKELETAL ELEMENT IN THE PANEL ABOVE\rOR FBN NID IF NOT IDENTIFIABLE\r\r(costal cartilage fragments are listed as RIB)'
                               ,bg='white',font=("Helvetica  20 bold" ))
        self.LabelExpl.pack(expand=True,fill=BOTH)

        #NID

       
        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()


        self.NotebookD.select(self.controller.get_Vertebra())

        self.NotebookD.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Vertebra(self.NotebookD.index("current")))

        



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


    def toggle_shc(self):
        if self.VarCir.get() == 'CO' or self.VarCir.get() =="<50%":
            state = 'normal' 
        else: 
            state ='disabled'
            self.controller.update_skel(self.VarCir.get(),'Skel_SHC')
            self.VarCheck111.set(0)

        for i in self.listeentry:
             i.config(state=state)
        self.controller.update_skel(self.VarCir.get(),'Skel_SHC')
