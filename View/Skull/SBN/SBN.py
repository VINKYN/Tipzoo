from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class SBNInterface(Frame):
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

        self.tc = self.controller.tapho_category()

        self.img_on = PhotoImage(file="View\img\check.png")  
        self.img_off = PhotoImage(file="View\img\stop-fill.png")

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

    
        ListeTab =['','SBN NID','Carpals','Tarsals','Patella','Malleol','Sesamoids']


        self.FrameRien = Frame(self.Notebook)
        self.FrameNID = Frame(self.Notebook)
        self.FrameCarp = Frame(self.Notebook)
        self.FrameTars = Frame(self.Notebook)
        self.FramePatel = Frame(self.Notebook)
        self.FrameMal = Frame(self.Notebook)
        self.FrameSesa = Frame(self.Notebook)

        ListePage =[self.FrameRien,self.FrameNID,self.FrameCarp,self.FrameTars,self.FramePatel,self.FrameMal,self.FrameSesa]

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

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


                self.FrameBas = Frame(self.FrameDroite,bg=color_button)
                self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)

                self.FrameBouton = Frame(self.FrameBas,background=color_button)
                self.FrameBouton.pack(side=LEFT)

                ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

                if self.bulk.get_bulk_species():

                    self.ButtonTa = Button(self.FrameBouton, text="> Go to Tapho",bd=0,font=font_button,bg=color_police,fg='white')
                    self.ButtonTa.pack(padx=20,side=LEFT)
                else :
                    self.ButtonSpe = Button(self.FrameBouton, text="> Go to Species",bd=0,font=font_button,bg=color_police,fg='white',
                                            command=self.controller.show_Species_page)
                    self.ButtonSpe.pack(padx=20,side=LEFT)
    
    
            if tab == "SBN NID": 
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

            if tab =="Carpals":
                 
                self.Notebookmt = ttk.Notebook(self.FrameMidhaut)
                self.Notebookmt.pack(expand=True, fill='both')
                style = ttk.Style()
                style.configure('TNotebook.Tab', padding=[20, 10])

                self.FrameBovidMT = Frame(self.Notebookmt,bg='white')
                self.FrameEquidMT = Frame(self.Notebookmt,bg='white')
                self.FrameSuiformMT = Frame(self.Notebookmt,bg='white')
                self.FrameUrsidMT = Frame(self.Notebookmt,bg='white')
                self.FrameOtherMT = Frame(self.Notebookmt,bg='white')

                ListePageMT =[self.FrameBovidMT,self.FrameEquidMT,self.FrameSuiformMT,self.FrameUrsidMT,self.FrameOtherMT]
                
                for tabMT, pageMT in zip(ListeTab, ListePageMT):
                    self.Notebookmt.add(pageMT, text=tabMT)

                self.VarCheck66= StringVar()
                self.VarCheck66.set(self.controller.getNDe(66))

                self.VarCheck67= StringVar()
                self.VarCheck67.set(self.controller.getNDe(67))

                self.VarCheck68= StringVar()
                self.VarCheck68.set(self.controller.getNDe(68))

                self.VarCheck69= StringVar()
                self.VarCheck69.set(self.controller.getNDe(69))

                self.FrameB = Frame(self.FrameBovidMT)
                self.FrameB.pack(fill='y',expand=True,side=LEFT,anchor='w')

                self.FrameLab = Frame(self.FrameB,bg='white')
                self.FrameLab.pack(anchor='w')

                self.labelMEEO2 = Label(self.FrameLab,text='Proximal row:',bg='white')
                self.labelMEEO2.pack(side='left',padx=20)

                self.labelMEEO = Label(self.FrameLab,text='50%:',bg='white')
                self.labelMEEO.pack(side='left')

                self.FrameSc= Frame(self.FrameB,bg='white')
                self.FrameSc.pack(anchor='w',expand=True)

                self.ButtonSc = Button(self.FrameSc, text="Scaphoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('SCA'))
                self.ButtonSc.pack(padx=20,side='left')

                self.Check66 = Checkbutton(self.FrameSc,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck66,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(66,self.VarCheck66.get()))
                self.Check66.pack(side='left')

                self.canvaSc = Canvas(self.FrameSc,height=62)
                self.canvaSc.pack(side=LEFT)

                self.image_sc = PhotoImage(file="View\Skull\SBN\carpals_img\sc.png")
                self.image_sc = self.image_sc.subsample(5)
                print(self.image_sc.height())
                self.canvaSc.create_image(0, 0, anchor="nw", image=self.image_sc)

                self.FrameLu= Frame(self.FrameB,bg='white')
                self.FrameLu.pack(anchor='w',expand=True)

                self.ButtonLu = Button(self.FrameLu, text="Lunatum(semilunar)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('LUN'))
                self.ButtonLu.pack(padx=20,side='left')

                self.Check67 = Checkbutton(self.FrameLu,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck67,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(67,self.VarCheck67.get()))
                self.Check67.pack(side='left')

                self.canvaLu = Canvas(self.FrameLu,height=51)
                self.canvaLu.pack(side=LEFT)

                self.image_Lu = PhotoImage(file="View\Skull\SBN\carpals_img\lu.png")
                self.image_Lu = self.image_Lu.subsample(5)
                print(self.image_Lu.height())
                self.canvaLu.create_image(0, 0, anchor="nw", image=self.image_Lu)

                self.FramePy= Frame(self.FrameB,bg='white')
                self.FramePy.pack(anchor='w',expand=True)

                self.ButtonPy = Button(self.FramePy, text="Pyramidal(triquetral)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PYR'))
                self.ButtonPy.pack(padx=20,side='left')

                self.Check68 = Checkbutton(self.FramePy,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck68,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(68,self.VarCheck68.get()))
                self.Check68.pack(side='left')

                self.canvaPy = Canvas(self.FramePy,height=53)
                self.canvaPy.pack(side=LEFT)

                self.image_Py = PhotoImage(file="View\Skull\SBN\carpals_img\py.png")
                self.image_Py = self.image_Py.subsample(5)
                print(self.image_Py.height())
                self.canvaPy.create_image(0, 0, anchor="nw", image=self.image_Py)

                self.FramePi= Frame(self.FrameB,bg='white')
                self.FramePi.pack(anchor='w',expand=True)

                self.ButtonPi = Button(self.FramePi, text="pisiform",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PIS'))
                self.ButtonPi.pack(padx=20,side='left')

                self.Check69 = Checkbutton(self.FramePi,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck69,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(69,self.VarCheck69.get()))
                self.Check69.pack(side='left')

                self.canvaPi = Canvas(self.FramePi,height=39)
                self.canvaPi.pack(side=LEFT)

                self.image_Pi = PhotoImage(file="View\Skull\SBN\carpals_img\pi.png")
                self.image_Pi = self.image_Pi.subsample(5)
                print(self.image_Pi.height())
                self.canvaPi.create_image(0, 0, anchor="nw", image=self.image_Pi)


                self.VarCheck73= StringVar()
                self.VarCheck73.set(self.controller.getNDe(73))

                self.VarCheck77= StringVar()
                self.VarCheck77.set(self.controller.getNDe(77))

                self.FrameB2 = Frame(self.FrameBovidMT)
                self.FrameB2.pack(fill='y',expand=True,side=LEFT)

                self.FrameLab2 = Frame(self.FrameB2,bg='white')
                self.FrameLab2.pack(anchor='w')

                self.labelMEEO22 = Label(self.FrameLab2,text='Distal row:',bg='white')
                self.labelMEEO22.pack(side='left',padx=20)

                self.labelMEEO222 = Label(self.FrameLab2,text='50%:',bg='white')
                self.labelMEEO222.pack(side='left')


                self.FrameCap= Frame(self.FrameB2,bg='white')
                self.FrameCap.pack(anchor='w',expand=True)

                self.ButtonCap = Button(self.FrameCap, text="Capitato-trapezoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonCap.pack(padx=20,side='left')

                self.Check73 = Checkbutton(self.FrameCap,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck73,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(73,self.VarCheck73.get()))
                self.Check73.pack(side='left')

                self.canvaCap = Canvas(self.FrameCap,height=62)
                self.canvaCap.pack(side=LEFT)

                self.image_cap = PhotoImage(file="View\Skull\SBN\carpals_img\cap.png")
                self.image_cap = self.image_cap.subsample(5)
                print(self.image_cap.height())
                self.canvaCap.create_image(0, 0, anchor="nw", image=self.image_cap)


                self.FrameHam= Frame(self.FrameB2,bg='white')
                self.FrameHam.pack(anchor='w',expand=True)

                self.ButtonHam = Button(self.FrameHam, text="Hamatum\r(unciform)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('HAM'))
                self.ButtonHam.pack(padx=20,side='left')

                self.Check77 = Checkbutton(self.FrameHam,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck77,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(77,self.VarCheck77.get()))
                self.Check77.pack(side='left')

                self.canvaHam = Canvas(self.FrameHam,height=62)
                self.canvaHam.pack(side=LEFT)

                self.image_ham = PhotoImage(file="View\Skull\SBN\carpals_img\ham.png")
                self.image_ham = self.image_ham.subsample(5)
                print(self.image_ham.height())
                self.canvaHam.create_image(0, 0, anchor="nw", image=self.image_ham)



                self.FrameB = Frame(self.FrameEquidMT)
                self.FrameB.pack(fill='y',expand=True,side=LEFT,anchor='w')

                self.FrameLab = Frame(self.FrameB,bg='white')
                self.FrameLab.pack(anchor='w')

                self.labelMEEO2 = Label(self.FrameLab,text='Proximal row:',bg='white')
                self.labelMEEO2.pack(side='left',padx=20)

                self.labelMEEO = Label(self.FrameLab,text='50%:',bg='white')
                self.labelMEEO.pack(side='left')

                self.FrameSc= Frame(self.FrameB,bg='white')
                self.FrameSc.pack(anchor='w',expand=True)

                self.ButtonSc = Button(self.FrameSc, text="Scaphoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('SCA'))
                self.ButtonSc.pack(padx=20,side='left')

                self.Check66 = Checkbutton(self.FrameSc,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck66,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(66,self.VarCheck66.get()))
                self.Check66.pack(side='left')

                self.canvaSc2 = Canvas(self.FrameSc,height=62)
                self.canvaSc2.pack(side=LEFT)

                self.image_sc2 = PhotoImage(file="View\Skull\SBN\carpals_img\sc2.png")
                self.image_sc2 = self.image_sc2.subsample(5)
                print(self.image_sc2.height())
                self.canvaSc2.create_image(0, 0, anchor="nw", image=self.image_sc2)

                self.FrameLu= Frame(self.FrameB,bg='white')
                self.FrameLu.pack(anchor='w',expand=True)

                self.ButtonLu = Button(self.FrameLu, text="Lunatum(semilunar)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('LUN'))
                self.ButtonLu.pack(padx=20,side='left')

                self.Check67 = Checkbutton(self.FrameLu,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck67,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(67,self.VarCheck67.get()))
                self.Check67.pack(side='left')

                self.canvaLu2 = Canvas(self.FrameLu,height=51)
                self.canvaLu2.pack(side=LEFT)

                self.image_Lu2 = PhotoImage(file="View\Skull\SBN\carpals_img\lu2.png")
                self.image_Lu2 = self.image_Lu2.subsample(5)
                print(self.image_Lu2.height())
                self.canvaLu2.create_image(0, 0, anchor="nw", image=self.image_Lu2)

                self.FramePy= Frame(self.FrameB,bg='white')
                self.FramePy.pack(anchor='w',expand=True)

                self.ButtonPy = Button(self.FramePy, text="Pyramidal(triquetral)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PYR'))
                self.ButtonPy.pack(padx=20,side='left')

                self.Check68 = Checkbutton(self.FramePy,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck68,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(68,self.VarCheck68.get()))
                self.Check68.pack(side='left')

                self.canvaPy2 = Canvas(self.FramePy,height=53)
                self.canvaPy2.pack(side=LEFT)

                self.image_Py2 = PhotoImage(file="View\Skull\SBN\carpals_img\py2.png")
                self.image_Py2 = self.image_Py2.subsample(5)
                print(self.image_Py2.height())
                self.canvaPy2.create_image(0, 0, anchor="nw", image=self.image_Py2)

                self.FramePi= Frame(self.FrameB,bg='white')
                self.FramePi.pack(anchor='w',expand=True)

                self.ButtonPi = Button(self.FramePi, text="pisiform",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PIS'))
                self.ButtonPi.pack(padx=20,side='left')

                self.Check69 = Checkbutton(self.FramePi,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck69,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(69,self.VarCheck69.get()))
                self.Check69.pack(side='left')

                self.canvaPi2 = Canvas(self.FramePi,height=60)
                self.canvaPi2.pack(side=LEFT)

                self.image_Pi2 = PhotoImage(file="View\Skull\SBN\carpals_img\pi2.png")
                self.image_Pi2 = self.image_Pi2.subsample(5)
                print(self.image_Pi2.height())
                self.canvaPi2.create_image(0, 0, anchor="nw", image=self.image_Pi2)


                self.VarCheck74= StringVar()
                self.VarCheck74.set(self.controller.getNDe(74))

                self.VarCheck76= StringVar()
                self.VarCheck76.set(self.controller.getNDe(76))

                self.FrameB2 = Frame(self.FrameEquidMT)
                self.FrameB2.pack(fill='y',expand=True,side=LEFT)

                self.FrameLab2 = Frame(self.FrameB2,bg='white')
                self.FrameLab2.pack(anchor='w')

                self.labelMEEO22 = Label(self.FrameLab2,text='Distal row:',bg='white')
                self.labelMEEO22.pack(side='left',padx=20)

                self.labelMEEO222 = Label(self.FrameLab2,text='50%:',bg='white')
                self.labelMEEO222.pack(side='left')


                self.FrameTra= Frame(self.FrameB2,bg='white')
                self.FrameTra.pack(anchor='w',expand=True)

                self.ButtonTra = Button(self.FrameTra, text="Trapezoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra.pack(padx=20,side='left')

                self.Check76 = Checkbutton(self.FrameTra,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck76,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(76,self.VarCheck76.get()))
                self.Check76.pack(side='left')

                self.canvaTra = Canvas(self.FrameTra,height=62)
                self.canvaTra.pack(side=LEFT)

                self.image_tra = PhotoImage(file="View\Skull\SBN\carpals_img\etra.png")
                self.image_tra = self.image_tra.subsample(5)
                print(self.image_tra.height())
                self.canvaTra.create_image(0, 0, anchor="nw", image=self.image_tra)


                self.FrameCap= Frame(self.FrameB2,bg='white')
                self.FrameCap.pack(anchor='w',expand=True)

                self.ButtonCap = Button(self.FrameCap, text="Capitatum",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonCap.pack(padx=20,side='left')

                self.Check74 = Checkbutton(self.FrameCap,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck74,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(74,self.VarCheck74.get()))
                self.Check74.pack(side='left')

                self.canvaCap2 = Canvas(self.FrameCap,height=62)
                self.canvaCap2.pack(side=LEFT)

                self.image_cap2 = PhotoImage(file="View\Skull\SBN\carpals_img\cap2.png")
                self.image_cap2 = self.image_cap2.subsample(5)
                print(self.image_cap2.height())
                self.canvaCap2.create_image(0, 0, anchor="nw", image=self.image_cap2)


                self.FrameHam= Frame(self.FrameB2,bg='white')
                self.FrameHam.pack(anchor='w',expand=True)

                self.ButtonHam = Button(self.FrameHam, text="Hamatum\r(unciform)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('HAM'))
                self.ButtonHam.pack(padx=20,side='left')

                self.Check77 = Checkbutton(self.FrameHam,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck77,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(77,self.VarCheck77.get()))
                self.Check77.pack(side='left')

                self.canvaHam2 = Canvas(self.FrameHam,height=62)
                self.canvaHam2.pack(side=LEFT)

                self.image_ham2 = PhotoImage(file="View\Skull\SBN\carpals_img\ham2.png")
                self.image_ham2 = self.image_ham2.subsample(5)
                print(self.image_ham2.height())
                self.canvaHam2.create_image(0, 0, anchor="nw", image=self.image_ham2)





                self.FrameB = Frame(self.FrameSuiformMT)
                self.FrameB.pack(fill='y',expand=True,side=LEFT,anchor='w')

                self.FrameLab = Frame(self.FrameB,bg='white')
                self.FrameLab.pack(anchor='w')

                self.labelMEEO2 = Label(self.FrameLab,text='Proximal row:',bg='white')
                self.labelMEEO2.pack(side='left',padx=20)

                self.labelMEEO = Label(self.FrameLab,text='50%:',bg='white')
                self.labelMEEO.pack(side='left')

                self.FrameSc= Frame(self.FrameB,bg='white')
                self.FrameSc.pack(anchor='w',expand=True)

                self.ButtonSc = Button(self.FrameSc, text="Scaphoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('SCA'))
                self.ButtonSc.pack(padx=20,side='left')

                self.Check66 = Checkbutton(self.FrameSc,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck66,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(66,self.VarCheck66.get()))
                self.Check66.pack(side='left')

                self.FrameLu= Frame(self.FrameB,bg='white')
                self.FrameLu.pack(anchor='w',expand=True)

                self.ButtonLu = Button(self.FrameLu, text="Lunatum(semilunar)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('LUN'))
                self.ButtonLu.pack(padx=20,side='left')

                self.Check67 = Checkbutton(self.FrameLu,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck67,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(67,self.VarCheck67.get()))
                self.Check67.pack(side='left')

                self.FramePy= Frame(self.FrameB,bg='white')
                self.FramePy.pack(anchor='w',expand=True)

                self.ButtonPy = Button(self.FramePy, text="Pyramidal(triquetral)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PYR'))
                self.ButtonPy.pack(padx=20,side='left')

                self.Check68 = Checkbutton(self.FramePy,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck68,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(68,self.VarCheck68.get()))
                self.Check68.pack(side='left')


                self.FramePi= Frame(self.FrameB,bg='white')
                self.FramePi.pack(anchor='w',expand=True)

                self.ButtonPi = Button(self.FramePi, text="pisiform",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PIS'))
                self.ButtonPi.pack(padx=20,side='left')

                self.Check69 = Checkbutton(self.FramePi,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck69,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(69,self.VarCheck69.get()))
                self.Check69.pack(side='left')

                

                self.VarCheck75= StringVar()
                self.VarCheck75.set(self.controller.getNDe(75))

                self.FrameB2 = Frame(self.FrameSuiformMT)
                self.FrameB2.pack(fill='y',expand=True,side=LEFT)

                self.FrameLab2 = Frame(self.FrameB2,bg='white')
                self.FrameLab2.pack(anchor='w')

                self.labelMEEO22 = Label(self.FrameLab2,text='Distal row:',bg='white')
                self.labelMEEO22.pack(side='left',padx=20)

                self.labelMEEO222 = Label(self.FrameLab2,text='50%:',bg='white')
                self.labelMEEO222.pack(side='left')


                self.FrameTra2= Frame(self.FrameB2,bg='white')
                self.FrameTra2.pack(anchor='w',expand=True)

                self.ButtonTra2 = Button(self.FrameTra2, text="Trapeze\r(trapezium)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra2.pack(padx=20,side='left')

                self.Check75 = Checkbutton(self.FrameTra2,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck75,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(75,self.VarCheck75.get()))
                self.Check75.pack(side='left')


                self.FrameTra= Frame(self.FrameB2,bg='white')
                self.FrameTra.pack(anchor='w',expand=True)

                self.ButtonTra = Button(self.FrameTra, text="Trapezoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra.pack(padx=20,side='left')

                self.Check76 = Checkbutton(self.FrameTra,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck76,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(76,self.VarCheck76.get()))
                self.Check76.pack(side='left')


                self.FrameCap= Frame(self.FrameB2,bg='white')
                self.FrameCap.pack(anchor='w',expand=True)

                self.ButtonCap = Button(self.FrameCap, text="Capitatum",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonCap.pack(padx=20,side='left')

                self.Check74 = Checkbutton(self.FrameCap,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck74,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(74,self.VarCheck74.get()))
                self.Check74.pack(side='left')

                self.FrameHam= Frame(self.FrameB2,bg='white')
                self.FrameHam.pack(anchor='w',expand=True)

                self.ButtonHam = Button(self.FrameHam, text="Hamatum\r(unciform)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('HAM'))
                self.ButtonHam.pack(padx=20,side='left')

                self.Check77 = Checkbutton(self.FrameHam,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck77,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(77,self.VarCheck77.get()))
                self.Check77.pack(side='left')



                self.FrameB = Frame(self.FrameUrsidMT)
                self.FrameB.pack(fill='y',expand=True,side=LEFT,anchor='w')

                self.FrameLab = Frame(self.FrameB,bg='white')
                self.FrameLab.pack(anchor='w')

                self.labelMEEO2 = Label(self.FrameLab,text='Proximal row:',bg='white')
                self.labelMEEO2.pack(side='left',padx=20)

                self.labelMEEO = Label(self.FrameLab,text='50%:',bg='white')
                self.labelMEEO.pack(side='left')

                self.FrameSc= Frame(self.FrameB,bg='white')
                self.FrameSc.pack(anchor='w',expand=True)

                self.ButtonSc = Button(self.FrameSc, text="Scapho-lunate",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('SCA'))
                self.ButtonSc.pack(padx=20,side='left')

                self.Check66 = Checkbutton(self.FrameSc,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck66,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(66,self.VarCheck66.get()))
                self.Check66.pack(side='left')


                self.FramePy= Frame(self.FrameB,bg='white')
                self.FramePy.pack(anchor='w',expand=True)

                self.ButtonPy = Button(self.FramePy, text="Pyramidal(triquetral)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PYR'))
                self.ButtonPy.pack(padx=20,side='left')

                self.Check68 = Checkbutton(self.FramePy,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck68,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(68,self.VarCheck68.get()))
                self.Check68.pack(side='left')


                self.FramePi= Frame(self.FrameB,bg='white')
                self.FramePi.pack(anchor='w',expand=True)

                self.ButtonPi = Button(self.FramePi, text="pisiform",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PIS'))
                self.ButtonPi.pack(padx=20,side='left')

                self.Check69 = Checkbutton(self.FramePi,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck69,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(69,self.VarCheck69.get()))
                self.Check69.pack(side='left')

                self.FrameB2 = Frame(self.FrameUrsidMT)
                self.FrameB2.pack(fill='y',expand=True,side=LEFT)

                self.FrameLab2 = Frame(self.FrameB2,bg='white')
                self.FrameLab2.pack(anchor='w')

                self.labelMEEO22 = Label(self.FrameLab2,text='Distal row:',bg='white')
                self.labelMEEO22.pack(side='left',padx=20)

                self.labelMEEO222 = Label(self.FrameLab2,text='50%:',bg='white')
                self.labelMEEO222.pack(side='left')


                self.FrameTra2= Frame(self.FrameB2,bg='white')
                self.FrameTra2.pack(anchor='w',expand=True)

                self.ButtonTra2 = Button(self.FrameTra2, text="Trapeze\r(trapezium)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra2.pack(padx=20,side='left')

                self.Check75 = Checkbutton(self.FrameTra2,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck75,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(75,self.VarCheck75.get()))
                self.Check75.pack(side='left')


                self.FrameTra= Frame(self.FrameB2,bg='white')
                self.FrameTra.pack(anchor='w',expand=True)

                self.ButtonTra = Button(self.FrameTra, text="Trapezoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra.pack(padx=20,side='left')

                self.Check76 = Checkbutton(self.FrameTra,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck76,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(76,self.VarCheck76.get()))
                self.Check76.pack(side='left')


                self.FrameCap= Frame(self.FrameB2,bg='white')
                self.FrameCap.pack(anchor='w',expand=True)

                self.ButtonCap = Button(self.FrameCap, text="Capitatum",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonCap.pack(padx=20,side='left')

                self.Check74 = Checkbutton(self.FrameCap,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck74,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(74,self.VarCheck74.get()))
                self.Check74.pack(side='left')

                self.FrameHam= Frame(self.FrameB2,bg='white')
                self.FrameHam.pack(anchor='w',expand=True)

                self.ButtonHam = Button(self.FrameHam, text="Hamatum\r(unciform)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('HAM'))
                self.ButtonHam.pack(padx=20,side='left')

                self.Check77 = Checkbutton(self.FrameHam,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck77,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(77,self.VarCheck77.get()))
                self.Check77.pack(side='left')


                self.FrameB = Frame(self.FrameOtherMT)
                self.FrameB.pack(fill='y',expand=True,side=LEFT,anchor='w')

                self.FrameLab = Frame(self.FrameB,bg='white')
                self.FrameLab.pack(anchor='w')

                self.labelMEEO2 = Label(self.FrameLab,text='Proximal row:',bg='white')
                self.labelMEEO2.pack(side='left',padx=20)

                self.labelMEEO = Label(self.FrameLab,text='50%:',bg='white')
                self.labelMEEO.pack(side='left')

                self.FrameSc= Frame(self.FrameB,bg='white')
                self.FrameSc.pack(anchor='w',expand=True)

                self.ButtonSc = Button(self.FrameSc, text="Scapho-lunate",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('SCA'))
                self.ButtonSc.pack(padx=20,side='left')

                self.Check66 = Checkbutton(self.FrameSc,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck66,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(66,self.VarCheck66.get()))
                self.Check66.pack(side='left')


                self.FramePy= Frame(self.FrameB,bg='white')
                self.FramePy.pack(anchor='w',expand=True)

                self.ButtonPy = Button(self.FramePy, text="Pyramidal(triquetral)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PYR'))
                self.ButtonPy.pack(padx=20,side='left')

                self.Check68 = Checkbutton(self.FramePy,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck68,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(68,self.VarCheck68.get()))
                self.Check68.pack(side='left')


                self.FramePi= Frame(self.FrameB,bg='white')
                self.FramePi.pack(anchor='w',expand=True)

                self.ButtonPi = Button(self.FramePi, text="pisiform",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('PIS'))
                self.ButtonPi.pack(padx=20,side='left')

                self.Check69 = Checkbutton(self.FramePi,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck69,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(69,self.VarCheck69.get()))
                self.Check69.pack(side='left')

                self.FrameB2 = Frame(self.FrameOtherMT)
                self.FrameB2.pack(fill='y',expand=True,side=LEFT)

                self.FrameLab2 = Frame(self.FrameB2,bg='white')
                self.FrameLab2.pack(anchor='w')

                self.labelMEEO22 = Label(self.FrameLab2,text='Distal row:',bg='white')
                self.labelMEEO22.pack(side='left',padx=20)

                self.labelMEEO222 = Label(self.FrameLab2,text='50%:',bg='white')
                self.labelMEEO222.pack(side='left')


                self.FrameTra2= Frame(self.FrameB2,bg='white')
                self.FrameTra2.pack(anchor='w',expand=True)

                self.ButtonTra2 = Button(self.FrameTra2, text="Trapeze\r(trapezium)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra2.pack(padx=20,side='left')

                self.Check75 = Checkbutton(self.FrameTra2,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck75,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(75,self.VarCheck75.get()))
                self.Check75.pack(side='left')


                self.FrameTra= Frame(self.FrameB2,bg='white')
                self.FrameTra.pack(anchor='w',expand=True)

                self.ButtonTra = Button(self.FrameTra, text="Trapezoid",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonTra.pack(padx=20,side='left')

                self.Check76 = Checkbutton(self.FrameTra,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck76,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(76,self.VarCheck76.get()))
                self.Check76.pack(side='left')


                self.FrameCap= Frame(self.FrameB2,bg='white')
                self.FrameCap.pack(anchor='w',expand=True)

                self.ButtonCap = Button(self.FrameCap, text="Capitatum",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('CTT'))
                self.ButtonCap.pack(padx=20,side='left')

                self.Check74 = Checkbutton(self.FrameCap,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck74,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(74,self.VarCheck74.get()))
                self.Check74.pack(side='left')

                self.FrameHam= Frame(self.FrameB2,bg='white')
                self.FrameHam.pack(anchor='w',expand=True)

                self.ButtonHam = Button(self.FrameHam, text="Hamatum\r(unciform)",bd=0,font=font_ecriture,bg=color_button,fg='black',command=lambda:self.controller.set_but('HAM'))
                self.ButtonHam.pack(padx=20,side='left')

                self.Check77 = Checkbutton(self.FrameHam,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck77,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(77,self.VarCheck77.get()))
                self.Check77.pack(side='left')


            if tab == "Patella":
                         
                    self.NotebookP = ttk.Notebook(self.FrameMidhaut)
                    self.NotebookP.pack(fill='both',side="right",expand=True)
                    style = ttk.Style()
                    style.configure('TNotebook.Tab', padding=[20, 10])

                    self.FrameBovidP = Frame(self.NotebookP,bg='white')
                    self.FrameEquidP = Frame(self.NotebookP,bg='white')
                    self.FrameSuiformP = Frame(self.NotebookP,bg='white')
                    self.FrameUrsidP = Frame(self.NotebookP,bg='white')
                    self.FrameOtherP = Frame(self.NotebookP,bg='white')

                    ListePageSc =[self.FrameBovidP,self.FrameEquidP,self.FrameSuiformP,self.FrameUrsidP,self.FrameOtherP]

                    for tabSc, pageSc in zip(ListeTab, ListePageSc):
                        self.NotebookP.add(pageSc, text=tabSc)

                    self.VarCheck81= StringVar()
                    self.VarCheck81.set(self.controller.getNDe(81))

                    self.VarCheck82= StringVar()
                    self.VarCheck82.set(self.controller.getNDe(82))

                
                    self.canvaSB = Canvas(self.FrameBovidP,bg='white')
                    self.canvaSB.pack(expand=True,fill=BOTH)


                    self.image_fondSB = PhotoImage(file="View/Skull/SBN/patella_img/b.png")
                    #self.image_fondSB = self.image_fondSB.subsample(2)
                    self.canvaSB.create_image(0, 0, anchor="nw", image=self.image_fondSB)

                    self.CheckS81 = Checkbutton(self.canvaSB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck81.get()))
                    self.canvaSB.create_window(155,105, anchor="nw", window= self.CheckS81)

                    self.CheckS82 = Checkbutton(self.canvaSB,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck82,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(82,self.VarCheck82.get()))
                    self.canvaSB.create_window(330,180, anchor="nw", window= self.CheckS82)


                    self.canvaSE = Canvas(self.FrameEquidP,bg='white')
                    self.canvaSE.pack(expand=True,fill=BOTH)

                    self.image_fondSE = PhotoImage(file="View/Skull/SBN/patella_img/e.png")
                    self.image_fondSE = self.image_fondSE.subsample(2)
                    self.canvaSE.create_image(0, 0, anchor="nw", image=self.image_fondSE)

                    self.CheckSE81 = Checkbutton(self.canvaSE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck81.get()))
                    self.canvaSE.create_window(140,125, anchor="nw", window= self.CheckSE81)

                    self.CheckSE82 = Checkbutton(self.canvaSE,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck82,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(82,self.VarCheck82.get()))
                    self.canvaSE.create_window(230,210, anchor="nw", window= self.CheckSE82)


                    self.canvaSS = Canvas(self.FrameSuiformP,bg='white')
                    self.canvaSS.pack(expand=True,fill=BOTH)

                    self.image_fondSS = PhotoImage(file="View/Skull/SBN/patella_img/s.png")
                    #self.image_fondSS = self.image_fondSS.subsample(2)
                    self.canvaSS.create_image(0, 0, anchor="nw", image=self.image_fondSS)

                    self.CheckSS81 = Checkbutton(self.canvaSS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck81.get()))
                    self.canvaSS.create_window(140,125, anchor="nw", window= self.CheckSS81)

                    self.CheckSS82 = Checkbutton(self.canvaSS,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck82,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(82,self.VarCheck82.get()))
                    self.canvaSS.create_window(190,200, anchor="nw", window= self.CheckSS82)



                    self.canvaSU = Canvas(self.FrameUrsidP,bg='white')
                    self.canvaSU.pack(expand=True,fill=BOTH)

                    self.image_fondSU = PhotoImage(file="View/Skull/SBN/patella_img/u.png")
                    self.image_fondSU = self.image_fondSU.subsample(2)
                    self.canvaSU.create_image(0, 0, anchor="nw", image=self.image_fondSU)

                    self.CheckSU81 = Checkbutton(self.canvaSU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck81.get()))
                    self.canvaSU.create_window(130,45, anchor="nw", window= self.CheckSU81)

                    self.CheckSU82 = Checkbutton(self.canvaSU,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck82,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(82,self.VarCheck82.get()))
                    self.canvaSU.create_window(150,190, anchor="nw", window= self.CheckSU82)


                    self.canvaSO = Canvas(self.FrameOtherP,bg='white')
                    self.canvaSO.pack(expand=True,fill=BOTH)

                    self.image_fondSO = PhotoImage(file="View/Skull/SBN/patella_img/o.png")
                    #self.image_fondSO = self.image_fondSO.subsample(2)
                    self.canvaSO.create_image(0, 0, anchor="nw", image=self.image_fondSO)

                    self.CheckSO81 = Checkbutton(self.canvaSO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck81.get()))
                    self.canvaSO.create_window(170,85, anchor="nw", window= self.CheckSO81)

                    self.CheckSO82 = Checkbutton(self.canvaSO,bd=0,fg='red',bg='yellow',
                                            onvalue=1,offvalue=0,variable=self.VarCheck82,
                                            image=self.img_off, selectimage=self.img_on,
                                                compound='left', indicatoron=False,
                                            command=lambda:self.controller.landmark(82,self.VarCheck82.get()))
                    self.canvaSO.create_window(250,190, anchor="nw", window= self.CheckSO82)


            if tab == "Malleol":
                         
                   
                    self.FrameBovidM = Frame(self.FrameMidhaut,bg='white')
                    self.FrameBovidM.pack()
                    

                    self.VarCheck83= StringVar()
                    self.VarCheck83.set(self.controller.getNDe(83))
                
                    self.canvaSM = Canvas(self.FrameBovidM,bg='white')
                    self.canvaSM.pack(expand=True,fill=BOTH)


                    self.image_fondSM = PhotoImage(file="View/Skull/SBN/malleol_img/b.png")
                    #self.image_fondSB = self.image_fondSB.subsample(2)
                    self.canvaSM.create_image(0, 0, anchor="nw", image=self.image_fondSM)

                    self.CheckS83 = Checkbutton(self.canvaSM,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck83,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(81,self.VarCheck83.get()))
                    self.canvaSM.create_window(325,105, anchor="nw", window= self.CheckS83)

            if tab == "Sesamoids":

                self.VarAnat = StringVar()
                self.VarAnat.set(self.controller.getAnat_Detail())

                self.VarCheck110= StringVar()
                self.VarCheck110.set(self.controller.getNDe(110))

                self.FramePortion = Frame(self.FrameMidhaut)
                self.FramePortion.pack(side=LEFT,padx=20,pady=(20,10),anchor='n',fill='y')

                self.Frameportion2 = Frame(self.FramePortion)
                self.Frameportion2.pack(side=LEFT,anchor='nw')

                self.CheckIli = Radiobutton(self.Frameportion2, text="Meta",font=font_ecriture,
                                    variable=self.VarAnat,value='Meta',
                                    command=lambda:self.controller.update_skel('Skel_Anat_Detail',self.VarAnat.get()))
                self.CheckIli.pack(padx=5,anchor='w',pady=7)

                self.CheckIsc = Radiobutton(self.Frameportion2, text="Big thin",font=font_ecriture,
                                    variable=self.VarAnat,value='Big thin',
                                    command=lambda:self.controller.update_skel('Skel_Anat_Detail',self.VarAnat.get()))
                self.CheckIsc.pack(padx=5,anchor='w',pady=7)

                self.CheckPub = Radiobutton(self.Frameportion2, text="Big large",font=font_ecriture,
                                    variable=self.VarAnat,value='Big large',
                                    command=lambda:self.controller.update_skel('Skel_Anat_Detail',self.VarAnat.get()))
                self.CheckPub.pack(padx=5,anchor='w',pady=7)

                self.CheckAce = Radiobutton(self.Frameportion2, text="Small",font=font_ecriture,fg='black',
                                    variable=self.VarAnat,value='Small',
                                    command=lambda:self.controller.update_skel('Skel_Anat_Detail',self.VarAnat.get()))
                self.CheckAce.pack(padx=5,anchor='w',pady=7)

                self.CheckIli = Radiobutton(self.Frameportion2, text="NID",font=font_ecriture,
                                    variable=self.VarAnat,value='NID',
                                    command=lambda:self.controller.update_skel('Skel_Anat_Detail',self.VarAnat.get()))
                self.CheckIli.pack(padx=5,anchor='w',pady=7)

                self.FrameImg = Frame(self.FramePortion)
                self.FrameImg.pack(side=LEFT,anchor='nw')

                self.canvaCox = Canvas(self.FrameImg,width=120)
                self.canvaCox.pack(side=RIGHT,expand=True)

                self.image_coxal = PhotoImage(file="View/Skull/SBN/sesamoid_img/i.png")
                self.image_coxal = self.image_coxal.subsample(3)
                self.canvaCox.create_image(0, 0, anchor="nw", image=self.image_coxal)



                self.FrameMEEO2 = Frame(self.FramePortion,bg='white')
                self.FrameMEEO2.pack(side=LEFT)

                self.labelMEEO2 = Label(self.FrameMEEO2,text='Metacarpal distal portion : ',bg='white')
                self.labelMEEO2.pack(side=LEFT)

                self.CheckMEEO2 = Checkbutton(self.FrameMEEO2,bd=0,fg='red',text='>50%',bg='yellow',
                                        onvalue=1,offvalue=0,variable=self.VarCheck110,
                                        image=self.img_off, selectimage=self.img_on,
                                            compound='left', indicatoron=False,
                                        command=lambda:self.controller.landmark(110,self.VarCheck110.get()))
                self.CheckMEEO2.pack(side=LEFT)
                
            

        self.Notebook.select(self.controller.getOnglet('SBN'))

        self.Notebook.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.Notebook.index("current"),'SBN'))

        self.LabelExpl = Label(self.FrameRien,text='SELECT SKELETAL ELEMENT IN THE PANEL ABOVE\rOR SBN NID IF NOT IDENTIFIABLE'
                               ,bg='white',font=("Helvetica  20 bold" ))
        self.LabelExpl.pack(expand=True,fill=BOTH)


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
