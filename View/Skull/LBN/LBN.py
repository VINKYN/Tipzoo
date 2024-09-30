from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

from Controller.Bulk import Bulk

class LBNInterface(Frame):
    def __init__(self, master=None, controller=None,bulk=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.configure(bg='white')

        self.bulk = bulk

        font_button = ("Helvetica  13 bold" )

        font_ecriture =("Helvetica  16" )

        color_button = '#F2E2CE'

        color_bleu ='#b9e2f9'

        color_police ='#1b1b1b'

        self.listeCirc =[]
        self.listeEfus =[]

        self.img_on = PhotoImage(file="View\img\check.png")  
        self.img_off = PhotoImage(file="View\img\stop-fill.png")

        self.custom_font = ('Helvetica', 13)       
        # Appliquer la police Roboto en taille 12
        self.pack(expand=True, fill='both')

        """self.Frame1 = Frame(self,bg="white")
        self.Frame1.pack(side=TOP, fill='both')

        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')"""

        self.Frame4 = Frame(self,bg='white')
        self.Frame4.pack(expand=True,fill=BOTH)

        self.Notebook = ttk.Notebook(self.Frame4)
        self.Notebook.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        ListeTab =["","LBN NID","Humerus","Radio-ulna","Femur","Tibia","Fibulla","Metacarpal","Metatarsal","Metapodial","Phalanx"]

        self.FrameRien = Frame(self.Notebook,bg='white')
        self.FrameNID = Frame(self.Notebook,bg='white')
        self.FrameHumerus = Frame(self.Notebook,bg='white')
        self.FrameFemur = Frame(self.Notebook,bg='white')
        self.FrameRadioUlna = Frame(self.Notebook,bg='white')
        self.FrameTibia = Frame(self.Notebook,bg='white')
        self.FrameFibulla = Frame(self.Notebook,bg='white')
        self.FrameMetacarpal = Frame(self.Notebook,bg='white')
        self.FrameMetatarsal = Frame(self.Notebook,bg='white')
        self.FrameMetapodial = Frame(self.Notebook,bg='white')
        self.FramePhalanx = Frame(self.Notebook,bg='white')
       
        ListePage =[self.FrameRien,self.FrameNID,self.FrameHumerus,self.FrameRadioUlna,self.FrameFemur,self.FrameTibia,self.FrameFibulla,self.FrameMetacarpal,self.FrameMetatarsal,self.FrameMetapodial,self.FramePhalanx]

        self.VarSpong = IntVar()

        self.VarFrag = StringVar()

        self.VarAgeCort = StringVar()

        self.VarSide = StringVar()

        self.VarPotionP = StringVar()
        self.VarPotionS = StringVar()
        self.VarPotionD = StringVar()
        self.VarPotionE = StringVar()

        p ,s ,d ,e = self.controller.portion()

        self.VarPotionP.set(p)
        self.VarPotionS.set(s)
        self.VarPotionD.set(d)
        self.VarPotionE.set(e)

        self.VarSegP = StringVar()
        self.VarSegM = StringVar()
        self.VarSegD = StringVar()

        self.VarSegAnt = StringVar()
        self.VarSegPost = StringVar()

        self.VarSegMed = StringVar()
        self.VarSegLat = StringVar()
        self.VarSegNid = StringVar()

        self.VarPh = StringVar()
        self.VarPh.set(self.controller.getAnat_Detail())

        sp ,sm ,sd ,sa,spos,smed,slat,snid = self.controller.segment()

        self.VarSegP.set(sp)
        self.VarSegM.set(sm)
        self.VarSegD.set(sd)
        self.VarSegAnt.set(sa)
        self.VarSegPost.set(spos)
        self.VarSegMed.set(smed)
        self.VarSegLat.set(slat)
        self.VarSegNid.set(snid)

        self.VarAgePf = StringVar()
        self.VarAgePj = StringVar()
        self.VarAgePu = StringVar()

        self.VarAgeDf = StringVar()
        self.VarAgeDj = StringVar()
        self.VarAgeDu = StringVar()

        self.VarAgeEf = StringVar()
        self.VarAgeEj = StringVar()
        self.VarAgeEu = StringVar()

        apf ,apj ,apu ,adf,adj,adu,aef,aej,aeu = self.controller.AgeFus()

        self.VarAgePf.set(apf)
        self.VarAgePj.set(apj)
        self.VarAgePu.set(apu)

        self.VarAgeDf.set(adf)
        self.VarAgeDj.set(adj)
        self.VarAgeDu.set(adu)


        self.VarAgeEf.set(aef)
        self.VarAgeEj.set(aej)
        self.VarAgeEu.set(aeu)

        self.VarCir = StringVar()
        self.VarCir.set(self.controller.getCirc())

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
                #Portion
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
                                    #command=lambda:self.controller.updatePortion(self.VarPotionS.get(),'S')
                                    command=lambda: self.toggle_shaft_circumference())
                self.CheckS.pack(side=LEFT, padx=5)

                #self.VarPotionS.trace_add("write", self.showS)
                #self.CheckS.bind('<Button-1>',lambda event: self.showS())

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
                                    command=lambda: self.toggle_Age_E())
                                    #command=lambda:self.controller.updatePortion(self.VarPotionE.get(),'E'))
                self.CheckE.pack(side=LEFT, padx=5)

                self.LabelE = Label(self.FrameE,text='Ext. indet.',font=font_ecriture)
                self.LabelE.pack(side=LEFT,padx=(0,5))



                #Segment
                if tab != 'Phalanx' and tab !='LBN NID':
                    self.FrameSeg = Frame(self.FrameMidhaut)
                    self.FrameSeg.pack(side=RIGHT,padx=20,pady=(20,10),anchor='n',fill="y")

                    self.LabelSeg = Label(self.FrameSeg,text='Segment of the shaft',font=font_ecriture)
                    self.LabelSeg.pack()

                    self.FrameSeg1 = Frame(self.FrameSeg)
                    self.FrameSeg1.pack(anchor='w',side=LEFT)

                    self.CheckSegP = Checkbutton(self.FrameSeg1, text="P",font=font_ecriture,
                                        variable=self.VarSegP,onvalue='P',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegP.get(),'P'))
                    self.CheckSegP.pack(padx=5,anchor='w')

                    self.CheckSegM = Checkbutton(self.FrameSeg1, text="M",font=font_ecriture,
                                        variable=self.VarSegM,onvalue='M',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegM.get(),'M'))
                    self.CheckSegM.pack(padx=5,anchor='w')

                    self.CheckSegD = Checkbutton(self.FrameSeg1, text="D",font=font_ecriture,
                                        variable=self.VarSegD,onvalue='D',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegD.get(),'D'))
                    self.CheckSegD.pack(padx=5,anchor='w')

                    self.FrameSeg2 = Frame(self.FrameSeg)
                    self.FrameSeg2.pack(anchor='w',side=LEFT)

                    self.CheckSegAnt = Checkbutton(self.FrameSeg2, text="Ant",font=font_ecriture,
                                        variable=self.VarSegAnt,onvalue='Ant',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegAnt.get(),'Ant'))
                    self.CheckSegAnt.pack(padx=5,anchor='w')

                    self.CheckSegPost = Checkbutton(self.FrameSeg2, text="Post",font=font_ecriture,
                                        variable=self.VarSegPost,onvalue='Post',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegPost.get(),'Post'))
                    self.CheckSegPost.pack(padx=5,anchor='w')

                    self.FrameSeg3 = Frame(self.FrameSeg)
                    self.FrameSeg3.pack(anchor='w',side=LEFT)

                    self.CheckSegMed = Checkbutton(self.FrameSeg3, text="Med",font=font_ecriture,
                                        variable=self.VarSegMed,onvalue='Med',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegMed.get(),'Med'))
                    self.CheckSegMed.pack(padx=5,anchor='w')

                    self.CheckSegLat = Checkbutton(self.FrameSeg3, text="Lat",font=font_ecriture,
                                        variable=self.VarSegLat,onvalue='Lat',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegLat.get(),'Lat'))
                    self.CheckSegLat.pack(padx=5,anchor='w')

                    self.CheckSegNid = Checkbutton(self.FrameSeg3, text="Nid",font=font_ecriture,
                                        variable=self.VarSegNid,onvalue='Nid',offvalue='',
                                        command=lambda:self.controller.updateSegment(self.VarSegNid.get(),'Nid'))
                    self.CheckSegNid.pack(padx=5,anchor='w')

                elif tab =='Phalanx':
                    
                    self.FramePh = Frame(self.FrameMidhaut)
                    self.FramePh.pack(side=RIGHT,padx=20,pady=(20,10),anchor='n',fill="y")

                    self.LabelPh = Label(self.FramePh,text='Precise identifiacation',font=font_ecriture)
                    self.LabelPh.pack()

                    self.FramePh1 = Frame(self.FramePh)
                    self.FramePh1.pack(anchor='w',side=LEFT)
                
                    
                    self.RadioPH1 = Radiobutton(self.FramePh1, text="PH1",value="PH1", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPH1.pack(padx=5,anchor='w')

                    self.RadioPH2 = Radiobutton(self.FramePh1, text="PH2",value="PH2", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPH2.pack(padx=5,anchor='w')

                    self.RadioPH3 = Radiobutton(self.FramePh1, text="PH3",value="PH3", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPH3.pack(padx=5,anchor='w')

                    self.FramePh2 = Frame(self.FramePh)
                    self.FramePh2.pack(anchor='w',side=LEFT)
                
                    self.RadioPH1v = Radiobutton(self.FramePh2, text="PH1v",value="PH1v", variable=self.VarPh,font=font_ecriture,
                                                command=lambda:self.toggle_PH())
                                #command=lambda:self.controller.update_skel(self.VarPh.get(),'Skel_Anat_Detail'))
                    self.RadioPH1v.pack(padx=5,anchor='w')

                    self.RadioPH2v = Radiobutton(self.FramePh2, text="PH2v",value="PH2v", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPH2v.pack(padx=5,anchor='w')

                    self.RadioPH3v = Radiobutton(self.FramePh2, text="PH3v",value="PH3v", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPH3v.pack(padx=5,anchor='w')

                    self.FramePh3 = Frame(self.FramePh)
                    self.FramePh3.pack(anchor='w',side=LEFT)
                
                    self.RadioPHA = Radiobutton(self.FramePh3, text="PHA",value="PHA", variable=self.VarPh,font=font_ecriture,
                                command=lambda:self.toggle_PH())
                    self.RadioPHA.pack(padx=5,anchor='w')

                

                    

                      
                self.FrameMidbas = Frame(self.FrameMid,bg='white')
                self.FrameMidbas.pack(expand=True,fill="both")

                #AgeFus

                self.FrameAge = Frame(self.FrameMidbas)
                self.FrameAge.pack(side=LEFT,padx=20,pady=(10,20),anchor='s',fill='y')

                

                self.LabelAge = Label(self.FrameAge,text='AgeFus',font=font_ecriture)
                self.LabelAge.pack()

                self.FrameAge1 = Frame(self.FrameAge)
                self.FrameAge1.pack(anchor='w',side=LEFT)

                self.CheckAgePf = Checkbutton(self.FrameAge1, text="Pfus",font=font_ecriture,
                                    variable=self.VarAgePf,onvalue='Pfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgePf.get(),'Pfus'))
                self.CheckAgePf.pack(padx=5,anchor='w')

                self.CheckAgePj = Checkbutton(self.FrameAge1, text="Pjustfus",font=font_ecriture,
                                    variable=self.VarAgePj,onvalue='Pjustfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgePj.get(),'Pjustfus'))
                self.CheckAgePj.pack(padx=5,anchor='w')

                self.CheckAgePu = Checkbutton(self.FrameAge1, text="Punfus",font=font_ecriture,
                                    variable=self.VarAgePu,onvalue='Punfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgePu.get(),'Punfus'))
                self.CheckAgePu.pack(padx=5,anchor='w')

                self.FrameAge2 = Frame(self.FrameAge)
                self.FrameAge2.pack(anchor='w',side=LEFT)

                self.CheckAgeDf = Checkbutton(self.FrameAge2, text="Dfus",font=font_ecriture,
                                    variable=self.VarAgeDf,onvalue='Dfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeDf.get(),'Dfus'))
                self.CheckAgeDf.pack(padx=5,anchor='w')

                self.CheckAgeDj = Checkbutton(self.FrameAge2, text="Djustfus",font=font_ecriture,
                                    variable=self.VarAgeDj,onvalue='Djustfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeDj.get(),'Djustfus'))
                self.CheckAgeDj.pack(padx=5,anchor='w')

                self.CheckAgeDu = Checkbutton(self.FrameAge2, text="Dunfus",font=font_ecriture,
                                    variable=self.VarAgeDu,onvalue='Dunfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeDu.get(),'Dunfus'))
                self.CheckAgeDu.pack(padx=5,anchor='w')

                
                self.FrameAge3 = Frame(self.FrameAge)
                self.FrameAge3.pack(anchor='w',side=LEFT)

                self.CheckAgeEf = Checkbutton(self.FrameAge3, text="Efus",font=font_ecriture,
                                    variable=self.VarAgeEf,onvalue='Efus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeEf.get(),'Efus'))
                self.CheckAgeEf.pack(padx=5,anchor='w')

                self.CheckAgeEj = Checkbutton(self.FrameAge3, text="Ejustfus",font=font_ecriture,
                                    variable=self.VarAgeEj,onvalue='Ejustfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeEj.get(),'Ejustfus'))
                self.CheckAgeEj.pack(padx=5,anchor='w')

                self.CheckAgeEu = Checkbutton(self.FrameAge3, text="Eunfus",font=font_ecriture,
                                    variable=self.VarAgeEu,onvalue='Eunfus',offvalue='',
                                    command=lambda:self.controller.updateAgefus(self.VarAgeEu.get(),'Eunfus'))
                self.CheckAgeEu.pack(padx=5,anchor='w')

                self.listeEfus.append(self.CheckAgeEf)
                self.listeEfus.append(self.CheckAgeEj)
                self.listeEfus.append(self.CheckAgeEu)

                if self.controller.getPortion() != None:
                    if 'E' in self.controller.getPortion():
                        for i in self.listeEfus:
                            i.config(state='normal')
                    else : 
                        for j in self.listeEfus:
                            j.config(state='disabled')


                #Shaft circumference
                self.FrameCir = Frame(self.FrameMidbas)
                self.FrameCir.pack(side=RIGHT,padx=20,pady=(10,20),anchor='s',fill="y")

                self.LabelCir = Label(self.FrameCir,text='Shaft Circumference',font=font_ecriture)
                self.LabelCir.pack()

                self.Frame50 = Frame(self.FrameCir)
                self.Frame50.pack(anchor='w',side=LEFT)

                self.RadioM50 = Radiobutton(self.Frame50, text=">50%",value=">50%", variable=self.VarCir,font=font_ecriture,
                                    command=lambda:self.controller.update_skel(self.VarCir.get(),'Skel_SHC'))
                
                self.RadioM50.pack(padx=5,anchor='w')

                self.RadioP50 = Radiobutton(self.Frame50, text="<50%", value="<50%",variable=self.VarCir,font=font_ecriture,
                                            command=lambda:self.controller.update_skel(self.VarCir.get(),'Skel_SHC'))
                self.RadioP50.pack(padx=5,anchor='w')

                self.RadioCo = Radiobutton(self.Frame50, text="CO", value="CO",variable=self.VarCir,font=font_ecriture,
                                        command=lambda:self.controller.update_skel(self.VarCir.get(),'Skel_SHC'))
                self.RadioCo.pack(padx=5,anchor='w')

                self.listeCirc.append(self.RadioCo)
                self.listeCirc.append(self.RadioP50)
                self.listeCirc.append(self.RadioM50)


                
                if self.controller.getPortion() != None:
                    if 'S' in self.controller.getPortion():
                        for i in self.listeCirc:
                            i.config(state='normal')
                    else : 
                        for j in self.listeCirc:
                            j.config(state='disabled')

                        
                
                self.FrameBas = Frame(self.FrameDroite,bg=color_button)
                self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)


                if tab !="LBN NID":
                    #self.FrameBas = Frame(self.FrameDroite,bg=color_bleu,relief="solid",bd=1)
                    #self.FrameBas.pack(fill="x", side=BOTTOM,padx=10,pady=10)
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

                

               

                

        self.Notebook.select(self.controller.getOnglet('LBN'))

        self.Notebook.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.Notebook.index("current"),'LBN'))
            
        self.LabelExpl = Label(self.FrameRien,text='SELECT SKELETAL ELEMENT IN THE PANEL ABOVE\rOR LBN NID IF NOT IDENTIFIABLE'
                               ,bg='white',font=("Helvetica  20 bold" ))
        self.LabelExpl.pack(expand=True,fill=BOTH)



        self.FrameLeftNID = Frame(self.FrameNID,bg='white')
        self.FrameLeftNID.pack(expand=True,fill=BOTH)

        listeNid = ['NID','SVERT','MAM1','MAM12', 'MAM2','MAM23','MAM3','MAM34','MAM45','MAM4', 'MAM5']

        self.VarSpecies = StringVar()

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
        
        

        


        ListeTab =['Bovid-Cervid','Equid','Suiform','ursid','Other carn.']

        self.Notebookh = ttk.Notebook(self.FrameHumerus)
        self.Notebookh.pack(fill='both',side="right")
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidH = Frame(self.Notebookh,bg='white')
        self.FrameEquidH = Frame(self.Notebookh,bg='white')
        self.FrameSuiformH = Frame(self.Notebookh,bg='white')
        self.FrameUrsid = Frame(self.Notebookh,bg='white')
        self.FrameOtherH = Frame(self.Notebookh,bg='white')

        ListePageH =[self.FrameBovidH,self.FrameEquidH,self.FrameSuiformH,self.FrameUrsid,self.FrameOtherH]
        

        for tabH, pageH in zip(ListeTab, ListePageH):
            self.Notebookh.add(pageH, text=tabH)

        self.canvaHB = Canvas(self.FrameBovidH,bg='white')
        self.canvaHB.pack(expand=True,fill=BOTH)

        self.image_fondHB = PhotoImage(file="View/Skull/LBN/humerus_img/b.png")
        self.image_fondHB = self.image_fondHB.subsample(3)
        self.canvaHB.create_image(0, 0, anchor="nw", image=self.image_fondHB)

        

        self.VarCheckH1 = IntVar()
        self.VarCheckH1.set(self.controller.getNDe(1))

        self.VarCheckH2 = IntVar()
        self.VarCheckH2.set(self.controller.getNDe(2))

        self.VarCheckH4 = IntVar()
        self.VarCheckH4.set(self.controller.getNDe(4))

        self.VarCheckH3 = IntVar()
        self.VarCheckH3.set(self.controller.getNDe(3))

        self.CheckHB1 = Checkbutton(self.canvaHB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(1,self.VarCheckH1.get()))
        self.canvaHB.create_window(85,115, anchor="nw", window= self.CheckHB1)

        

        self.CheckHB2 = Checkbutton(self.canvaHB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(2,self.VarCheckH2.get()))
        self.canvaHB.create_window(400,170, anchor="nw", window= self.CheckHB2)

        

        self.CheckHB3 = Checkbutton(self.canvaHB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(3,self.VarCheckH3.get()))
        self.canvaHB.create_window(95,220, anchor="nw", window= self.CheckHB3)

        

        self.CheckHB4 = Checkbutton(self.canvaHB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(4,self.VarCheckH4.get()))
        self.canvaHB.create_window(350,325, anchor="nw", window= self.CheckHB4)



        self.canvaHE = Canvas(self.FrameEquidH,bg='white')
        self.canvaHE.pack(expand=True,fill=BOTH)

        self.image_fondHE = PhotoImage(file="View/Skull/LBN/humerus_img/e.png") 
        self.image_fondHE = self.image_fondHE.subsample(3)
        
        self.canvaHE.create_image(0, 0, anchor="nw", image=self.image_fondHE)


        self.CheckHE1 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(1,self.VarCheckH1.get()))
        self.canvaHE.create_window(50,45, anchor="nw", window= self.CheckHE1)

        self.CheckHE2 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(2,self.VarCheckH2.get()))
        self.canvaHE.create_window(325,190, anchor="nw", window= self.CheckHE2)


        self.CheckHE3 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(3,self.VarCheckH3.get()))
        self.canvaHE.create_window(100,255, anchor="nw", window= self.CheckHE3)

        self.CheckHE4 = Checkbutton(self.canvaHE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(4,self.VarCheckH4.get()))
        self.canvaHE.create_window(310,330, anchor="nw", window= self.CheckHE4)


        self.canvaHS = Canvas(self.FrameSuiformH,bg='white')
        self.canvaHS.pack(expand=True,fill=BOTH)

        self.image_fondHS = PhotoImage(file="View/Skull/LBN/humerus_img/s.png") 
        self.image_fondHS = self.image_fondHS.subsample(2)
         
        self.canvaHS.create_image(0, 0, anchor="nw", image=self.image_fondHS)

        self.CheckHS1 = Checkbutton(self.canvaHS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(1,self.VarCheckH1.get()))
        self.canvaHS.create_window(70,155, anchor="nw", window= self.CheckHS1)

        self.CheckHS2 = Checkbutton(self.canvaHS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(2,self.VarCheckH2.get()))
        self.canvaHS.create_window(395,160, anchor="nw", window= self.CheckHS2)


        self.CheckHS3 = Checkbutton(self.canvaHS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(3,self.VarCheckH3.get()))
        self.canvaHS.create_window(130,220, anchor="nw", window= self.CheckHS3)

        self.CheckHS4 = Checkbutton(self.canvaHS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(4,self.VarCheckH4.get()))
        self.canvaHS.create_window(230,330, anchor="nw", window= self.CheckHS4)

        self.canvaHU = Canvas(self.FrameUrsid,bg='white')
        self.canvaHU.pack(expand=True,fill=BOTH)

        self.image_fondHU = PhotoImage(file="View/Skull/LBN/humerus_img/u.png") 
        self.image_fondHU = self.image_fondHU.subsample(3)
        self.canvaHU.create_image(0, 0, anchor="nw", image=self.image_fondHU)

        self.CheckHU1 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(1,self.VarCheckH1.get()))
        self.canvaHU.create_window(50,135, anchor="nw", window= self.CheckHU1)

        self.CheckHU2 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(2,self.VarCheckH2.get()))
        self.canvaHU.create_window(225,225, anchor="nw", window= self.CheckHU2)


        self.CheckHU3 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(3,self.VarCheckH3.get()))
        self.canvaHU.create_window(410,253, anchor="nw", window= self.CheckHU3)

        self.CheckHU4 = Checkbutton(self.canvaHU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(4,self.VarCheckH4.get()))
        self.canvaHU.create_window(75,430, anchor="nw", window= self.CheckHU4)

        

        self.canvaHO = Canvas(self.FrameOtherH,bg='white')
        self.canvaHO.pack(expand=True,fill=BOTH)

        self.image_fondHO = PhotoImage(file="View/Skull/LBN/humerus_img/o.png") 
        self.image_fondHO = self.image_fondHO.subsample(2)
        self.canvaHO.create_image(0, 0, anchor="nw", image=self.image_fondHO)

        self.CheckHO1 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(1,self.VarCheckH1.get()))
        self.canvaHO.create_window(135,40, anchor="nw", window= self.CheckHO1)

        self.CheckHO2 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(2,self.VarCheckH2.get()))
        self.canvaHO.create_window(355,165, anchor="nw", window= self.CheckHO2)


        self.CheckHO3 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(3,self.VarCheckH3.get()))
        self.canvaHO.create_window(70,150, anchor="nw", window= self.CheckHO3)

        self.CheckHO4 = Checkbutton(self.canvaHO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckH4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(4,self.VarCheckH4.get()))
        self.canvaHO.create_window(300,310, anchor="nw", window= self.CheckHO4)








        self.Notebookr = ttk.Notebook(self.FrameRadioUlna)
        self.Notebookr.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidR = Frame(self.Notebookr,bg='white')
        self.FrameEquidR = Frame(self.Notebookr,bg='white')
        self.FrameSuiformR = Frame(self.Notebookr,bg='white')
        self.FrameUrsidR = Frame(self.Notebookr,bg='white')
        self.FrameOtherR = Frame(self.Notebookr,bg='white')

        ListePageR =[self.FrameBovidR,self.FrameEquidR,self.FrameSuiformR,self.FrameUrsidR,self.FrameOtherR]
        
        for tabR, pageR in zip(ListeTab, ListePageR):
            self.Notebookr.add(pageR, text=tabR)

        self.VarCheckR1 = IntVar()
        self.VarCheckR1.set(self.controller.getNDe(5))

        self.VarCheckR2 = IntVar()
        self.VarCheckR2.set(self.controller.getNDe(6))

        self.VarCheckR3 = IntVar()
        self.VarCheckR3.set(self.controller.getNDe(7))

        self.VarCheckR4 = IntVar()
        self.VarCheckR4.set(self.controller.getNDe(8))

        self.VarCheckR5 = IntVar()
        self.VarCheckR5.set(self.controller.getNDe(9))

        self.VarCheckR6 = IntVar()
        self.VarCheckR6.set(self.controller.getNDe(10))

        self.VarCheckR7 = IntVar()
        self.VarCheckR7.set(self.controller.getNDe(11))

        self.VarCheckR8 = IntVar()
        self.VarCheckR8.set(self.controller.getNDe(12))

        self.canvaRB = Canvas(self.FrameBovidR,bg='white')
        self.canvaRB.pack(expand=True,fill=BOTH)

        self.image_fondRB = PhotoImage(file="View/Skull/LBN/radioulna_img/b.png") 
        self.image_fondRB = self.image_fondRB.subsample(3)
        self.canvaRB.create_image(0, 0, anchor="nw", image=self.image_fondRB)

        self.CheckRB1 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(5,self.VarCheckR1.get()))
        self.canvaRB.create_window(75,35, anchor="nw", window= self.CheckRB1)

        self.CheckRB2 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(6,self.VarCheckR2.get()))
        self.canvaRB.create_window(270,40, anchor="nw", window= self.CheckRB2)


        self.CheckRB3 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(7,self.VarCheckR3.get()))
        self.canvaRB.create_window(275,125, anchor="nw", window= self.CheckRB3)

        self.CheckRB4 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(8,self.VarCheckR4.get()))
        self.canvaRB.create_window(40,255, anchor="nw", window= self.CheckRB4)

        self.CheckRB5 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR5,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(9,self.VarCheckR5.get()))
        self.canvaRB.create_window(115,360, anchor="nw", window= self.CheckRB5)

        self.CheckRB6 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR6,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(10,self.VarCheckR6.get()))
        self.canvaRB.create_window(290,235, anchor="nw", window= self.CheckRB6)

        self.CheckRB7 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR7,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(11,self.VarCheckR7.get()))
        self.canvaRB.create_window(355,275, anchor="nw", window= self.CheckRB7)

        self.CheckRB8 = Checkbutton(self.canvaRB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR8,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(12,self.VarCheckR8.get()))
        self.canvaRB.create_window(170,240, anchor="nw", window= self.CheckRB8)

        self.canvaRE = Canvas(self.FrameEquidR,bg='white')
        self.canvaRE.pack(expand=True,fill=BOTH)

        self.image_fondRE = PhotoImage(file="View/Skull/LBN/radioulna_img/e.png") 
        self.image_fondRE = self.image_fondRE.subsample(3)
        
        self.canvaRE.create_image(0, 0, anchor="nw", image=self.image_fondRE)

        self.CheckRE1 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(5,self.VarCheckR1.get()))
        self.canvaRE.create_window(75,105, anchor="nw", window= self.CheckRE1)

        self.CheckRE2 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(6,self.VarCheckR2.get()))
        self.canvaRE.create_window(285,45, anchor="nw", window= self.CheckRE2)


        self.CheckRE3 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(7,self.VarCheckR3.get()))
        self.canvaRE.create_window(300,185, anchor="nw", window= self.CheckRE3)

        self.CheckRE4 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(8,self.VarCheckR4.get()))
        self.canvaRE.create_window(35,245, anchor="nw", window= self.CheckRE4)

        self.CheckRE5 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR5,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(9,self.VarCheckR5.get()))
        self.canvaRE.create_window(88,300, anchor="nw", window= self.CheckRE5)

        self.CheckRE6 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR6,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(10,self.VarCheckR6.get()))
        self.canvaRE.create_window(305,220, anchor="nw", window= self.CheckRE6)

        self.CheckRE7 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR7,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(11,self.VarCheckR7.get()))
        self.canvaRE.create_window(340,335, anchor="nw", window= self.CheckRE7)

        self.CheckRE8 = Checkbutton(self.canvaRE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR8,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(12,self.VarCheckR8.get()))
        self.canvaRE.create_window(185,270, anchor="nw", window= self.CheckRE8)

        self.canvaRS = Canvas(self.FrameSuiformR,bg='white')
        self.canvaRS.pack(expand=True,fill=BOTH)

        self.image_fondRS = PhotoImage(file="View/Skull/LBN/radioulna_img/s.png") 
        self.image_fondRS = self.image_fondRS.subsample(2)
        
        self.canvaRS.create_image(0, 0, anchor="nw", image=self.image_fondRS)

        self.CheckRS1 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(5,self.VarCheckR1.get()))
        self.canvaRS.create_window(55,120, anchor="nw", window= self.CheckRS1)

        self.CheckRS2 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(6,self.VarCheckR2.get()))
        self.canvaRS.create_window(305,110, anchor="nw", window= self.CheckRS2)


        self.CheckRS3 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(7,self.VarCheckR3.get()))
        self.canvaRS.create_window(325,220, anchor="nw", window= self.CheckRS3)

        self.CheckRS4 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(8,self.VarCheckR4.get()))
        self.canvaRS.create_window(50,280, anchor="nw", window= self.CheckRS4)

        self.CheckRS5 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR5,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(9,self.VarCheckR5.get()))
        self.canvaRS.create_window(80,325, anchor="nw", window= self.CheckRS5)

        self.CheckRS6 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR6,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(10,self.VarCheckR6.get()))
        self.canvaRS.create_window(370,265, anchor="nw", window= self.CheckRS6)

        self.CheckRS7 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR7,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(11,self.VarCheckR7.get()))
        self.canvaRS.create_window(365,345, anchor="nw", window= self.CheckRS7)

        self.CheckRS8 = Checkbutton(self.canvaRS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR8,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(12,self.VarCheckR8.get()))
        self.canvaRS.create_window(155,215, anchor="nw", window= self.CheckRS8)

        self.canvaRU = Canvas(self.FrameUrsidR,bg='white')
        self.canvaRU.pack(expand=True,fill=BOTH)

        self.image_fondRU = PhotoImage(file="View/Skull/LBN/radioulna_img/u.png") 
        self.image_fondRU = self.image_fondRU.subsample(5)
        
        self.canvaRU.create_image(0, 0, anchor="nw", image=self.image_fondRU)

        self.CheckRU1 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(5,self.VarCheckR1.get()))
        self.canvaRU.create_window(70,90, anchor="nw", window= self.CheckRU1)

        self.CheckRU2 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(6,self.VarCheckR2.get()))
        self.canvaRU.create_window(120,155, anchor="nw", window= self.CheckRU2)


        self.CheckRU3 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(7,self.VarCheckR3.get()))
        self.canvaRU.create_window(17,420, anchor="nw", window= self.CheckRU3)

        self.CheckRU4 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(8,self.VarCheckR4.get()))
        self.canvaRU.create_window(13,547, anchor="nw", window= self.CheckRU4)

        self.CheckRU5 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR5,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(9,self.VarCheckR5.get()))
        self.canvaRU.create_window(278,26, anchor="nw", window= self.CheckRU5)

        self.CheckRU6 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR6,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(10,self.VarCheckR6.get()))
        self.canvaRU.create_window(225,52, anchor="nw", window= self.CheckRU6)

        self.CheckRU7 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR7,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(11,self.VarCheckR7.get()))
        self.canvaRU.create_window(249,271, anchor="nw", window= self.CheckRU7)

        self.CheckRU8 = Checkbutton(self.canvaRU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR8,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(12,self.VarCheckR8.get()))
        self.canvaRU.create_window(219,568, anchor="nw", window= self.CheckRU8)

        self.canvaRO = Canvas(self.FrameOtherR,bg='white')
        self.canvaRO.pack(expand=True,fill=BOTH)

        self.image_fondRO = PhotoImage(file="View/Skull/LBN/radioulna_img/o.png") 
        self.image_fondRO = self.image_fondRO.subsample(2)
        self.canvaRO.create_image(0, 0, anchor="nw", image=self.image_fondRO)

        self.CheckRO1 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(5,self.VarCheckR1.get()))
        self.canvaRO.create_window(30,83, anchor="nw", window= self.CheckRO1)

        self.CheckRO2 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(6,self.VarCheckR2.get()))
        self.canvaRO.create_window(230,42, anchor="nw", window= self.CheckRO2)


        self.CheckRO3 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(7,self.VarCheckR3.get()))
        self.canvaRO.create_window(265,105, anchor="nw", window= self.CheckRO3)

        self.CheckRO4 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(8,self.VarCheckR4.get()))
        self.canvaRO.create_window(135,235, anchor="nw", window= self.CheckRO4)

        self.CheckRO5 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR5,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(9,self.VarCheckR5.get()))
        self.canvaRO.create_window(95,350, anchor="nw", window= self.CheckRO5)

        self.CheckRO6 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR6,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(10,self.VarCheckR6.get()))
        self.canvaRO.create_window(360,245, anchor="nw", window= self.CheckRO6)

        self.CheckRO7 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR7,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(11,self.VarCheckR7.get()))
        self.canvaRO.create_window(365,345, anchor="nw", window= self.CheckRO7)

        self.CheckRO8 = Checkbutton(self.canvaRO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckR8,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(12,self.VarCheckR8.get()))
        self.canvaRO.create_window(65,290, anchor="nw", window= self.CheckRO8)

        
        self.Notebookf = ttk.Notebook(self.FrameFemur)
        self.Notebookf.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidF = Frame(self.Notebookf,bg='white')
        self.FrameEquidF = Frame(self.Notebookf,bg='white')
        self.FrameSuiformF = Frame(self.Notebookf,bg='white')
        self.FrameUrsidF = Frame(self.Notebookf,bg='white')
        self.FrameOtherF = Frame(self.Notebookf,bg='white')

        ListePageF =[self.FrameBovidF,self.FrameEquidF,self.FrameSuiformF,self.FrameUrsidF,self.FrameOtherF]
        
        for tabF, pageF in zip(ListeTab, ListePageF):
            self.Notebookf.add(pageF, text=tabF)

        self.VarCheckF1 = IntVar()
        self.VarCheckF1.set(self.controller.getNDe(18))

        self.VarCheckF2 = IntVar()
        self.VarCheckF2.set(self.controller.getNDe(19))

        self.VarCheckF3 = IntVar()
        self.VarCheckF3.set(self.controller.getNDe(20))

        self.VarCheckF4 = IntVar()
        self.VarCheckF4.set(self.controller.getNDe(21))

        self.VarCheck91 = StringVar()
        self.VarCheck91.set(self.controller.getNDe(114))

        self.FrameBon = Frame(self.FrameBovidF)
        self.FrameBon.pack()

        self.canvaFB = Canvas(self.FrameBon,width=300,height=210,bg='white')
        self.canvaFB.pack(side=LEFT,expand=True,fill=BOTH)

        self.image_fondFB = PhotoImage(file="View/Skull/LBN/femur_img/b.png") 
        self.image_fondFB = self.image_fondFB.subsample(4)
        self.canvaFB.create_image(0, 0, anchor="nw", image=self.image_fondFB)

        self.CheckFB1 = Checkbutton(self.canvaFB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(18,self.VarCheckF1.get()))
        self.canvaFB.create_window(80,110, anchor="nw", window= self.CheckFB1)

        

        self.CheckFB2 = Checkbutton(self.canvaFB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(19,self.VarCheckF2.get()))
        self.canvaFB.create_window(245,125, anchor="nw", window= self.CheckFB2)

        

        self.CheckFB3 = Checkbutton(self.canvaFB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(20,self.VarCheckF3.get()))
        self.canvaFB.create_window(70,180, anchor="nw", window= self.CheckFB3)

        

        self.CheckFB4 = Checkbutton(self.canvaFB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(21,self.VarCheckF4.get()))
        self.canvaFB.create_window(245,190, anchor="nw", window= self.CheckFB4)

    
        self.canvaAspera = Canvas(self.FrameBon,height=400,width=100)
        self.canvaAspera.pack(side=LEFT,expand=True,fill=BOTH)

        self.image_fondAspera = PhotoImage(file="View/Skull/LBN/femur_img/b2.png") 
        self.image_fondAspera = self.image_fondAspera.subsample(6)
        
        self.canvaAspera.create_image(0, 0, anchor="nw", image=self.image_fondAspera)


        self.FrameAspera = Frame(self.FrameBovidF,bg='white')
        self.FrameAspera.pack()

        self.LabelAspera = Label(self.FrameAspera,text='Lenght of the linea aspera (mm)',bg='white')
        self.LabelAspera.pack(side=LEFT)

        self.EntryAspera = NumpadEntry(self.FrameAspera,width=8,bg='white',bd=1 ,relief='solid',
                                       textvariable=self.VarCheck91)
        self.EntryAspera.pack(side=LEFT)

        self.VarCheck91.trace_add("write", lambda *args:self.controller.landmark(114,self.VarCheck91.get()))

        self.LabelAspera2 = Label(self.FrameAspera,text='( measure/2 \r if incomplete groove )',bg='white')
        self.LabelAspera2.pack(side=LEFT)





        self.canvaFE = Canvas(self.FrameEquidF,bg='white')
        self.canvaFE.pack(expand=True,fill=BOTH)

        self.image_fondFE = PhotoImage(file="View/Skull/LBN/femur_img/e.png") 
        self.image_fondFE = self.image_fondFE.subsample(3)
        
        self.canvaFE.create_image(0, 0, anchor="nw", image=self.image_fondFE)

        self.CheckFE1 = Checkbutton(self.canvaFE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(18,self.VarCheckF1.get()))
        self.canvaFE.create_window(30,95, anchor="nw", window= self.CheckFE1)

        

        self.CheckFE2 = Checkbutton(self.canvaFE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(19,self.VarCheckF2.get()))
        self.canvaFE.create_window(330,155, anchor="nw", window= self.CheckFE2)

        

        self.CheckFE3 = Checkbutton(self.canvaFE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(20,self.VarCheckF3.get()))
        self.canvaFE.create_window(95,170, anchor="nw", window= self.CheckFE3)

        

        self.CheckFE4 = Checkbutton(self.canvaFE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(21,self.VarCheckF4.get()))
        self.canvaFE.create_window(255,270, anchor="nw", window= self.CheckFE4)


        self.FrameAspera2 = Frame(self.FrameEquidF,bg='white')
        self.FrameAspera2.pack()

        self.LabelAspera2 = Label(self.FrameAspera2,text='Lenght of the linea aspera (mm)',bg='white')
        self.LabelAspera2.pack(side=LEFT)

        self.EntryAspera2 = NumpadEntry(self.FrameAspera2,width=8,bg='white',bd=1 ,relief='solid',
                                       textvariable=self.VarCheck91)
        self.EntryAspera2.pack(side=LEFT)

        self.VarCheck91.trace_add("write", lambda *args:self.controller.landmark(114,self.VarCheck91.get()))

        self.LabelAspera22 = Label(self.FrameAspera2,text='( measure/2 \r if incomplete groove )',bg='white')
        self.LabelAspera22.pack(side=LEFT)

        self.canvaFS = Canvas(self.FrameSuiformF,bg='white')
        self.canvaFS.pack(expand=True,fill=BOTH)
        
        self.image_fondFS = PhotoImage(file="View/Skull/LBN/femur_img/s.png") 
        self.image_fondFS = self.image_fondFS.subsample(2)
        self.canvaFS.create_image(0, 0, anchor="nw", image=self.image_fondFS)

        self.CheckFS1 = Checkbutton(self.canvaFS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(18,self.VarCheckF1.get()))
        self.canvaFS.create_window(50,95, anchor="nw", window= self.CheckFS1)

        

        self.CheckFS2 = Checkbutton(self.canvaFS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(19,self.VarCheckF2.get()))
        self.canvaFS.create_window(260,100, anchor="nw", window= self.CheckFS2)

        

        self.CheckFS3 = Checkbutton(self.canvaFS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(20,self.VarCheckF3.get()))
        self.canvaFS.create_window(80,225, anchor="nw", window= self.CheckFS3)

        

        self.CheckFS4 = Checkbutton(self.canvaFS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(21,self.VarCheckF4.get()))
        self.canvaFS.create_window(260,205, anchor="nw", window= self.CheckFS4)

        self.canvaFU = Canvas(self.FrameUrsidF,bg='white')
        self.canvaFU.pack(expand=True,fill=BOTH)

        self.image_fondFU = PhotoImage(file="View/Skull/LBN/femur_img/u.png") 
        self.image_fondFU = self.image_fondFU.subsample(4)
        self.canvaFU.create_image(0, 0, anchor="nw", image=self.image_fondFU)

        self.CheckFU1 = Checkbutton(self.canvaFU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(18,self.VarCheckF1.get()))
        self.canvaFU.create_window(175,90, anchor="nw", window= self.CheckFU1)

        

        self.CheckFU2 = Checkbutton(self.canvaFU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(19,self.VarCheckF2.get()))
        self.canvaFU.create_window(59,130, anchor="nw", window= self.CheckFU2)

        

        self.CheckFU3 = Checkbutton(self.canvaFU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(20,self.VarCheckF3.get()))
        self.canvaFU.create_window(60,225, anchor="nw", window= self.CheckFU3)

        

        self.CheckFU4 = Checkbutton(self.canvaFU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(21,self.VarCheckF4.get()))
        self.canvaFU.create_window(60,385, anchor="nw", window= self.CheckFU4)


        self.canvaFO = Canvas(self.FrameOtherF,bg='white')
        self.canvaFO.pack(expand=True,fill=BOTH)

        self.image_fondFO = PhotoImage(file="View/Skull/LBN/femur_img/o.png") 
        self.image_fondFO = self.image_fondFO.subsample(2)
        self.canvaFO.create_image(0, 0, anchor="nw", image=self.image_fondFO)

        self.CheckFO1 = Checkbutton(self.canvaFO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(18,self.VarCheckF1.get()))
        self.canvaFO.create_window(25,75, anchor="nw", window= self.CheckFO1)

        

        self.CheckFO2 = Checkbutton(self.canvaFO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(19,self.VarCheckF2.get()))
        self.canvaFO.create_window(240,165, anchor="nw", window= self.CheckFO2)

        

        self.CheckFO3 = Checkbutton(self.canvaFO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(20,self.VarCheckF3.get()))
        self.canvaFO.create_window(45,220, anchor="nw", window= self.CheckFO3)

        

        self.CheckFO4 = Checkbutton(self.canvaFO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckF4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(21,self.VarCheckF4.get()))
        self.canvaFO.create_window(195,245, anchor="nw", window= self.CheckFO4)




        self.Notebookt = ttk.Notebook(self.FrameTibia)
        self.Notebookt.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidT = Frame(self.Notebookt,bg='white')
        self.FrameEquidT = Frame(self.Notebookt,bg='white')
        self.FrameSuiformT = Frame(self.Notebookt,bg='white')
        self.FrameUrsidT = Frame(self.Notebookt,bg='white')
        self.FrameOtherT = Frame(self.Notebookt,bg='white')

        ListePageT =[self.FrameBovidT,self.FrameEquidT,self.FrameSuiformT,self.FrameUrsidT,self.FrameOtherT]
        
        for tabT, pageT in zip(ListeTab, ListePageT):
            self.Notebookt.add(pageT, text=tabT)

        self.VarCheckT1 = IntVar()
        self.VarCheckT1.set(self.controller.getNDe(22))

        self.VarCheckT2 = IntVar()
        self.VarCheckT2.set(self.controller.getNDe(23))

        self.VarCheckT3 = IntVar()
        self.VarCheckT3.set(self.controller.getNDe(24))

        self.VarCheckT4 = IntVar()
        self.VarCheckT4.set(self.controller.getNDe(25))

        self.VarCheckT71 = IntVar()
        self.VarCheckT71.set(self.controller.getNDe(83))

        self.canvaTB = Canvas(self.FrameBovidT,bg='white')
        self.canvaTB.pack(expand=True,fill=BOTH)

        self.image_fondTB = PhotoImage(file="View/Skull/LBN/tibia_img/b.png") 
        self.image_fondTB = self.image_fondTB.subsample(3)
        
        self.canvaTB.create_image(0, 0, anchor="nw", image=self.image_fondTB)

        self.CheckTB1 = Checkbutton(self.canvaTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaTB.create_window(135,95, anchor="nw", window= self.CheckTB1)

        

        self.CheckTB2 = Checkbutton(self.canvaTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaTB.create_window(295,186, anchor="nw", window= self.CheckTB2)

        

        self.CheckTB3 = Checkbutton(self.canvaTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaTB.create_window(130,186, anchor="nw", window= self.CheckTB3)

        

        self.CheckTB4 = Checkbutton(self.canvaTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaTB.create_window(225,365, anchor="nw", window= self.CheckTB4)

        self.canvaTE = Canvas(self.FrameEquidT,bg='white')
        self.canvaTE.pack(expand=True,fill=BOTH)

        self.image_fondTE = PhotoImage(file="View/Skull/LBN/tibia_img/e.png") 
        self.image_fondTE = self.image_fondTE.subsample(3)
        self.canvaTE.create_image(0, 0, anchor="nw", image=self.image_fondTE)

        self.CheckTE1 = Checkbutton(self.canvaTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaTE.create_window(125,115, anchor="nw", window= self.CheckTE1)

        

        self.CheckTE2 = Checkbutton(self.canvaTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaTE.create_window(275,142, anchor="nw", window= self.CheckTE2)

        

        self.CheckTE3 = Checkbutton(self.canvaTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaTE.create_window(90,196, anchor="nw", window= self.CheckTE3)

        

        self.CheckTE4 = Checkbutton(self.canvaTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaTE.create_window(180,319, anchor="nw", window= self.CheckTE4)

        self.CheckTE71 = Checkbutton(self.canvaTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT71,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(83,self.VarCheckT71.get()))
        self.canvaTE.create_window(170,100, anchor="nw", window= self.CheckTE71)

        self.canvaTS = Canvas(self.FrameSuiformT,bg='white')
        self.canvaTS.pack(expand=True,fill=BOTH)

        self.image_fondTS = PhotoImage(file="View/Skull/LBN/tibia_img/s.png") 
        self.image_fondTS = self.image_fondTS.subsample(2)
        self.canvaTS.create_image(0, 0, anchor="nw", image=self.image_fondTS)

        self.CheckTS1 = Checkbutton(self.canvaTS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaTS.create_window(95,70, anchor="nw", window= self.CheckTS1)

        

        self.CheckTS2 = Checkbutton(self.canvaTS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaTS.create_window(260,156, anchor="nw", window= self.CheckTS2)

        

        self.CheckTS3 = Checkbutton(self.canvaTS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaTS.create_window(56,230, anchor="nw", window= self.CheckTS3)

        

        self.CheckTS4 = Checkbutton(self.canvaTS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaTS.create_window(192,300, anchor="nw", window= self.CheckTS4)

        self.canvaTU = Canvas(self.FrameUrsidT,width=220,bg='white')
        self.canvaTU.pack(expand=True,fill=BOTH,side=LEFT)

        self.image_fondTU = PhotoImage(file="View/Skull/LBN/tibia_img/u.png") 
        self.image_fondTU = self.image_fondTU.subsample(4)
        
        self.canvaTU.create_image(0, 0, anchor="nw", image=self.image_fondTU)

        self.CheckTU2 = Checkbutton(self.canvaTU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaTU.create_window(15,88, anchor="nw", window= self.CheckTU2)

        

        self.CheckTU3 = Checkbutton(self.canvaTU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaTU.create_window(15,129, anchor="nw", window= self.CheckTU3)

        

        self.CheckTU4 = Checkbutton(self.canvaTU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaTU.create_window(160,346, anchor="nw", window= self.CheckTU4)


        self.canvaTU2 = Canvas(self.FrameUrsidT,bg='white')
        self.canvaTU2.pack(expand=True,fill=BOTH,side=LEFT)

        self.image_fondTU2 = PhotoImage(file="View/Skull/LBN/tibia_img/u2.png") 
        self.image_fondTU2 = self.image_fondTU2.subsample(3)
        
        self.canvaTU2.create_image(0, 0, anchor="nw", image=self.image_fondTU2)

        self.CheckTU2 = Checkbutton(self.canvaTU2,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaTU2.create_window(58,75, anchor="nw", window= self.CheckTU2)

        self.canvaTO = Canvas(self.FrameOtherT,bg='white')
        self.canvaTO.pack(expand=True,fill=BOTH)

        self.image_fondTO = PhotoImage(file="View/Skull/LBN/tibia_img/o.png") 
        self.image_fondTO = self.image_fondTO.subsample(2)
        self.canvaTO.create_image(0, 0, anchor="nw", image=self.image_fondTO)

        self.CheckTO1 = Checkbutton(self.canvaTO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaTO.create_window(82,65, anchor="nw", window= self.CheckTO1)

        

        self.CheckTO2 = Checkbutton(self.canvaTO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaTO.create_window(206,140, anchor="nw", window= self.CheckTO2)

        

        self.CheckTO3 = Checkbutton(self.canvaTO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaTO.create_window(47,250, anchor="nw", window= self.CheckTO3)

        

        self.CheckTO4 = Checkbutton(self.canvaTO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaTO.create_window(166,325, anchor="nw", window= self.CheckTO4)
        

        self.Notebookfi = ttk.Notebook(self.FrameFibulla)
        self.Notebookfi.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidFI = Frame(self.Notebookfi,bg='white')
        self.FrameEquidFI = Frame(self.Notebookfi,bg='white')
        self.FrameSuiformFI = Frame(self.Notebookfi,bg='white')
        self.FrameUrsidFI = Frame(self.Notebookfi,bg='white')
        self.FrameOtherFI = Frame(self.Notebookfi,bg='white')

        ListePageFI =[self.FrameBovidFI,self.FrameEquidFI,self.FrameSuiformFI,self.FrameUrsidFI,self.FrameOtherFI]
        
        for tabFI, pageFI in zip(ListeTab, ListePageFI):
            self.Notebookfi.add(pageFI, text=tabFI)

        self.VarCheckFI1 = IntVar()
        self.VarCheckFI1.set(self.controller.getNDe(86))

        self.VarCheckFI2 = IntVar()
        self.VarCheckFI2.set(self.controller.getNDe(87))

        self.VarCheckFI3 = IntVar()
        self.VarCheckFI3.set(self.controller.getNDe(85))

        self.VarCheckFI4 = IntVar()
        self.VarCheckFI4.set(self.controller.getNDe(84))

        self.FrameFIB = Frame(self.FrameBovidFI,bg='white')
        self.FrameFIB.pack(expand=True,fill=BOTH)

        self.ButtonFIB =Button(self.FrameFIB,text='Os malleolus \r(> short bones)',bg=color_police,
                                fg=color_button,font=font_button,bd=0,height=4, width=35,
                               )
        self.ButtonFIB.pack(expand=True)

        self.canvaFIE = Canvas(self.FrameEquidFI,bg='white')
        self.canvaFIE.pack(expand=True,fill=BOTH)

        self.image_fondFIE = PhotoImage(file="View/Skull/LBN/fibulla_img/e.png") 
        self.image_fondFIE = self.image_fondFIE.subsample(3)
        
        self.canvaFIE.create_image(0, 0, anchor="nw", image=self.image_fondFIE)

        self.CheckFIE1 = Checkbutton(self.canvaFIE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(22,self.VarCheckT1.get()))
        self.canvaFIE.create_window(60,110, anchor="nw", window= self.CheckFIE1)

        

        self.CheckFIE2 = Checkbutton(self.canvaFIE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(23,self.VarCheckT2.get()))
        self.canvaFIE.create_window(285,140, anchor="nw", window= self.CheckFIE2)

        

        self.CheckFIE3 = Checkbutton(self.canvaFIE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(24,self.VarCheckT3.get()))
        self.canvaFIE.create_window(64,230, anchor="nw", window= self.CheckFIE3)

        

        self.CheckFIE4 = Checkbutton(self.canvaFIE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(25,self.VarCheckT4.get()))
        self.canvaFIE.create_window(210,290, anchor="nw", window= self.CheckFIE4)

        self.CheckTE71 = Checkbutton(self.canvaFIE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckT71,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(83,self.VarCheckT71.get()))
        self.canvaFIE.create_window(220,97, anchor="nw", window= self.CheckTE71)

        self.canvaFIS = Canvas(self.FrameSuiformFI,bg='white')
        self.canvaFIS.pack(expand=True,fill=BOTH)

        self.image_fondFIS = PhotoImage(file="View/Skull/LBN/fibulla_img/s.png") 
        self.image_fondFIS = self.image_fondFIS.subsample(2)
        self.canvaFIS.create_image(0, 0, anchor="nw", image=self.image_fondFIS)

        self.CheckFIS1 = Checkbutton(self.canvaFIS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(86,self.VarCheckFI1.get()))
        self.canvaFIS.create_window(90,34, anchor="nw", window= self.CheckFIS1)

        

        self.CheckFIS2 = Checkbutton(self.canvaFIS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(87,self.VarCheckFI2.get()))
        self.canvaFIS.create_window(90,72, anchor="nw", window= self.CheckFIS2)

        

        self.CheckFIS3 = Checkbutton(self.canvaFIS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(85,self.VarCheckFI3.get()))
        self.canvaFIS.create_window(90,228, anchor="nw", window= self.CheckFIS3)

        

        self.CheckFIS4 = Checkbutton(self.canvaFIS,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(84,self.VarCheckFI4.get()))
        self.canvaFIS.create_window(90,266, anchor="nw", window= self.CheckFIS4)

        self.canvaFIU = Canvas(self.FrameUrsidFI,bg='white')
        self.canvaFIU.pack(expand=True,fill=BOTH)

        self.image_fondFIU = PhotoImage(file="View/Skull/LBN/fibulla_img/u.png") 
        self.image_fondFIU = self.image_fondFIU.subsample(4)
        
        self.canvaFIU.create_image(0, 0, anchor="nw", image=self.image_fondFIU)

        self.CheckFIU1 = Checkbutton(self.canvaFIU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(86,self.VarCheckFI1.get()))
        self.canvaFIU.create_window(10,14, anchor="nw", window= self.CheckFIU1)

        

        self.CheckFIU2 = Checkbutton(self.canvaFIU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(87,self.VarCheckFI2.get()))
        self.canvaFIU.create_window(90,50, anchor="nw", window= self.CheckFIU2)

        

        self.CheckFIU3 = Checkbutton(self.canvaFIU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(85,self.VarCheckFI3.get()))
        self.canvaFIU.create_window(90,200, anchor="nw", window= self.CheckFIU3)

        

        self.CheckFIU4 = Checkbutton(self.canvaFIU,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(84,self.VarCheckFI4.get()))
        self.canvaFIU.create_window(90,240, anchor="nw", window= self.CheckFIU4)

        self.canvaFIO = Canvas(self.FrameOtherFI,bg='white')
        self.canvaFIO.pack(expand=True,fill=BOTH)

        self.image_fondFIO = PhotoImage(file="View/Skull/LBN/fibulla_img/o.png") 
        self.image_fondFIO = self.image_fondFIO.subsample(2)
        self.canvaFIO.create_image(0, 0, anchor="nw", image=self.image_fondFIO)

        self.CheckFIO1 = Checkbutton(self.canvaFIO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(86,self.VarCheckFI1.get()))
        self.canvaFIO.create_window(90,28, anchor="nw", window= self.CheckFIO1)

        

        self.CheckFIO2 = Checkbutton(self.canvaFIO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(87,self.VarCheckFI2.get()))
        self.canvaFIO.create_window(90,56, anchor="nw", window= self.CheckFIO2)

        

        self.CheckFIO3 = Checkbutton(self.canvaFIO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(85,self.VarCheckFI3.get()))
        self.canvaFIO.create_window(90,215, anchor="nw", window= self.CheckFIO3)

        

        self.CheckFIO4 = Checkbutton(self.canvaFIO,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckFI4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(84,self.VarCheckFI4.get()))
        self.canvaFIO.create_window(90,240, anchor="nw", window= self.CheckFIO4)



        self.Notebookme = ttk.Notebook(self.FrameMetacarpal)
        self.Notebookme.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidME = Frame(self.Notebookme,bg='white')
        self.FrameEquidME = Frame(self.Notebookme,bg='white')
        self.FrameSuiformME = Frame(self.Notebookme,bg='white')
        self.FrameUrsidME = Frame(self.Notebookme,bg='white')
        self.FrameOtherME = Frame(self.Notebookme,bg='white')

        ListePageME =[self.FrameBovidME,self.FrameEquidME,self.FrameSuiformME,self.FrameUrsidME,self.FrameOtherME]
        
        for tabME, pageME in zip(ListeTab, ListePageME):
            self.Notebookme.add(pageME, text=tabME)

        self.VarCheckME1 = IntVar()
        self.VarCheckME1.set(self.controller.getNDe(13))

        self.VarCheckME2 = IntVar()
        self.VarCheckME2.set(self.controller.getNDe(14))

        self.VarCheckME3 = IntVar()
        self.VarCheckME3.set(self.controller.getNDe(15))

        self.VarCheckME4 = StringVar()
        self.VarCheckME4.set(self.controller.getNDe(16))

        self.VarCheckME5 = StringVar()
        self.VarCheckME5.set(self.controller.getNDe(17))


        self.canvaMEB = Canvas(self.FrameBovidME,height=400,bg='white')
        self.canvaMEB.pack(expand=True,fill=BOTH)

        self.image_fondMEB = PhotoImage(file="View/Skull/LBN/metacarpal_img/b.png") 
        self.image_fondMEB = self.image_fondMEB.subsample(2)
        
        self.canvaMEB.create_image(0, 0, anchor="nw", image=self.image_fondMEB)

        self.CheckMEB1 = Checkbutton(self.canvaMEB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(13,self.VarCheckME1.get()))
        self.canvaMEB.create_window(135,44, anchor="nw", window= self.CheckMEB1)

        

        self.CheckMEB2 = Checkbutton(self.canvaMEB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(14,self.VarCheckME2.get()))
        self.canvaMEB.create_window(340,37, anchor="nw", window= self.CheckMEB2)

        

        self.CheckMEB3 = Checkbutton(self.canvaMEB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(15,self.VarCheckME3.get()))
        self.canvaMEB.create_window(155,237, anchor="nw", window= self.CheckMEB3)

        self.FrameRadio16B = Frame(self.canvaMEB,bg='white')

        self.LabelCondyleB = Label(self.FrameRadio16B,text='Condyles',bg='white')
        self.LabelCondyleB.pack()

        self.Radio216B = Radiobutton(self.FrameRadio16B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckME4,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.Radio216B.pack()

        self.Radio216B = Radiobutton(self.FrameRadio16B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckME4,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.Radio216B.pack()

        self.Radio216B = Radiobutton(self.FrameRadio16B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckME4,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        
        self.Radio216B.pack()
        self.canvaMEB.create_window(300,180, anchor="nw", window= self.FrameRadio16B)



        self.Framegroove17 = Frame(self.FrameBovidME,bg='white')
        self.Framegroove17.pack()

        self.canvaGroove17 = Canvas(self.Framegroove17,height=50,width=200,bg='white')
        self.canvaGroove17.pack(side=LEFT)

        self.image_fondGroove17 = PhotoImage(file="View/Skull/LBN/metacarpal_img/b2.png") 
        self.image_fondGroove17 = self.image_fondGroove17.subsample(4)
        
        self.canvaGroove17.create_image(0, 0, anchor="nw", image=self.image_fondGroove17)

        self.LabelGroove17 = Label(self.Framegroove17,text='Lenght of \rthe groove\r (17) (mm)',bg='white')
        self.LabelGroove17.pack(side=LEFT)

        self.EntryGroove17 = NumpadEntry(self.Framegroove17,width=8,bg='white',bd=1 ,relief='solid',
                                       textvariable=self.VarCheckME5)
        self.EntryGroove17.pack(side=LEFT)

        self.VarCheckME5.trace_add("write", lambda *args:self.controller.landmark(17,self.VarCheckME5.get()))

        self.LabelGroove217 = Label(self.Framegroove17,text='( measure/2 \r if incomplete groove )',bg='white')
        self.LabelGroove217.pack(side=LEFT)




        self.canvaMEE = Canvas(self.FrameEquidME,bg='white')
        self.canvaMEE.pack(expand=True,fill=BOTH)

        self.image_fondMEE = PhotoImage(file="View/Skull/LBN/metacarpal_img/e.png") 
        self.image_fondMEE = self.image_fondMEE.subsample(3)
        self.canvaMEE.create_image(0, 0, anchor="nw", image=self.image_fondMEE)

        self.CheckMEE1 = Checkbutton(self.canvaMEE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(13,self.VarCheckME1.get()))
        self.canvaMEE.create_window(40,49, anchor="nw", window= self.CheckMEE1)

        

        self.CheckMEE2 = Checkbutton(self.canvaMEE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(14,self.VarCheckME2.get()))
        self.canvaMEE.create_window(294,65, anchor="nw", window= self.CheckMEE2)

        

        self.CheckMEE3 = Checkbutton(self.canvaMEE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(15,self.VarCheckME3.get()))
        self.canvaMEE.create_window(86,265, anchor="nw", window= self.CheckMEE3)


        self.FrameRadio16E = Frame(self.canvaMEE,bg='white')

        self.LabelCondyleE = Label(self.FrameRadio16E,text='Condyles',bg='white')
        self.LabelCondyleE.pack()

        self.Radio216E = Radiobutton(self.FrameRadio16E,bd=0,fg='red',
                                   variable=self.VarCheckME4,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.Radio216E.pack()

        self.Radio216E = Radiobutton(self.FrameRadio16E,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckME4,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.Radio216E.pack()

        self.Radio216E = Radiobutton(self.FrameRadio16E,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckME4,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        
        self.Radio216E.pack()
        self.canvaMEE.create_window(350,180, anchor="nw", window= self.FrameRadio16E)

        self.FrameMEES1 = Frame(self.FrameSuiformME,bg='white')
        self.FrameMEES1.pack()

        self.labelMEES1 = Label(self.FrameMEES1,text='Metacarpal proximal portion : ',bg='white')
        self.labelMEES1.pack(side=LEFT)

        self.CheckMEES1 = Checkbutton(self.FrameMEES1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(13,self.VarCheckME1.get()))
        self.CheckMEES1.pack(side=LEFT)
        
        self.FrameMEES2 = Frame(self.FrameSuiformME,bg='white')
        self.FrameMEES2.pack()

        self.labelMEES2 = Label(self.FrameMEES2,text='Metacarpal distal portion : ',bg='white')
        self.labelMEES2.pack(side=LEFT)

        self.CheckMEES2 = Checkbutton(self.FrameMEES2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.CheckMEES2.pack(side=LEFT)



        self.labeldig = Label(self.FrameUrsidME,text='digits I–V:',bg='white')
        self.labeldig.pack()

        self.FrameMEEU1 = Frame(self.FrameUrsidME)
        self.FrameMEEU1.pack()

        

        self.labelMEEU1 = Label(self.FrameMEEU1,text='Metacarpal proximal portion : ',bg='white')
        self.labelMEEU1.pack(side=LEFT)

        self.CheckMEEU1 = Checkbutton(self.FrameMEEU1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(13,self.VarCheckME1.get()))
        self.CheckMEEU1.pack(side=LEFT)
        
        self.FrameMEEU2 = Frame(self.FrameUrsidME,bg='white')
        self.FrameMEEU2.pack()

        self.labelMEEU2 = Label(self.FrameMEEU2,text='Metacarpal distal portion : ')
        self.labelMEEU2.pack(side=LEFT)

        self.CheckMEEU2 = Checkbutton(self.FrameMEEU2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.CheckMEEU2.pack(side=LEFT)

        

        self.labeldig2 = Label(self.FrameOtherME,text='felids: digits I–V  \r canids & hyaenids: digits II–V',bg='white')
        self.labeldig2.pack()

        self.FrameMEEO1 = Frame(self.FrameOtherME,bg='white')
        self.FrameMEEO1.pack()

        

        self.labelMEEO1 = Label(self.FrameMEEO1,text='Metacarpal proximal portion : ',bg='white')
        self.labelMEEO1.pack(side=LEFT)

        self.CheckMEEO1 = Checkbutton(self.FrameMEEO1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(13,self.VarCheckME1.get()))
        self.CheckMEEO1.pack(side=LEFT)
        
        self.FrameMEEO2 = Frame(self.FrameOtherME,bg='white')
        self.FrameMEEO2.pack()

        self.labelMEEO2 = Label(self.FrameMEEO2,text='Metacarpal distal portion : ',bg='white')
        self.labelMEEO2.pack(side=LEFT)

        self.CheckMEEO2 = Checkbutton(self.FrameMEEO2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckME4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(16,self.VarCheckME4.get()))
        self.CheckMEEO2.pack(side=LEFT)

        self.Notebookmt = ttk.Notebook(self.FrameMetatarsal)
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

        self.VarCheckMT1 = IntVar()
        self.VarCheckMT1.set(self.controller.getNDe(26))

        self.VarCheckMT2 = IntVar()
        self.VarCheckMT2.set(self.controller.getNDe(27))

        self.VarCheckMT3 = IntVar()
        self.VarCheckMT3.set(self.controller.getNDe(28))

        self.VarCheckMT4 = StringVar()
        self.VarCheckMT4.set(self.controller.getNDe(29))

        self.VarCheckMT5 = StringVar()
        self.VarCheckMT5.set(self.controller.getNDe(30))
        

        self.canvaMTB = Canvas(self.FrameBovidMT,height=400,bg='white')
        self.canvaMTB.pack()

        self.image_fondMTB = PhotoImage(file="View/Skull/LBN/metatarsal_img/b.png") 
        self.image_fondMTB = self.image_fondMTB.subsample(2)
        
        self.canvaMTB.create_image(0, 0, anchor="nw", image=self.image_fondMTB)

        
        self.CheckMTB1 = Checkbutton(self.canvaMTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(26,self.VarCheckMT1.get()))
        self.canvaMTB.create_window(130,11, anchor="nw", window= self.CheckMTB1)

        

        self.CheckMTB2 = Checkbutton(self.canvaMTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(27,self.VarCheckMT2.get()))
        self.canvaMTB.create_window(315,29, anchor="nw", window= self.CheckMTB2)

        

        self.CheckMTB3 = Checkbutton(self.canvaMTB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(28,self.VarCheckMT3.get()))
        self.canvaMTB.create_window(135,222, anchor="nw", window= self.CheckMTB3)


        self.Framegroove = Frame(self.FrameBovidMT,bg='white')
        self.Framegroove.pack()

        self.canvaGroove = Canvas(self.Framegroove,height=50,width=200)
        self.canvaGroove.pack(side=LEFT)

        self.image_fondGroove = PhotoImage(file="View/Skull/LBN/metatarsal_img/b2.png") 
        self.image_fondGroove = self.image_fondGroove.subsample(4)
        
        self.canvaGroove.create_image(0, 0, anchor="nw", image=self.image_fondGroove)

        self.LabelGroove = Label(self.Framegroove,text='Lenght of \rthe groove\r (30) (mm)',bg='white')
        self.LabelGroove.pack(side=LEFT)

        self.EntryGroove = NumpadEntry(self.Framegroove,width=8,bg='white',bd=1 ,relief='solid',
                                       textvariable=self.VarCheckMT5)
        self.EntryGroove.pack(side=LEFT)

        self.VarCheckMT5.trace_add("write", lambda *args:self.controller.landmark(30,self.VarCheckMT5.get()))

        self.LabelGroove2 = Label(self.Framegroove,text='( measure/2 \r if incomplete groove )',bg='white')
        self.LabelGroove2.pack(side=LEFT)






        self.FrameRadio29B = Frame(self.canvaMTB,bg='white')

        self.LabelCondyB = Label(self.FrameRadio29B,text='Condyles',bg='white')
        self.LabelCondyB.pack()

        self.Radio291B = Radiobutton(self.FrameRadio29B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.Radio291B.pack()

        self.Radio292B = Radiobutton(self.FrameRadio29B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.Radio292B.pack()

        self.Radio293B = Radiobutton(self.FrameRadio29B,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        
        self.Radio293B.pack()
        self.canvaMTB.create_window(260,180, anchor="nw", window= self.FrameRadio29B)





        self.canvaMTE = Canvas(self.FrameEquidMT,bg='white')
        self.canvaMTE.pack(expand=True,fill=BOTH)

        self.image_fondMTE = PhotoImage(file="View/Skull/LBN/metatarsal_img/e.png") 
        self.image_fondMTE = self.image_fondMTE.subsample(3)
        
        self.canvaMTE.create_image(0, 0, anchor="nw", image=self.image_fondMTE)

        self.CheckMTE1 = Checkbutton(self.canvaMTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(26,self.VarCheckMT1.get()))
        self.canvaMTE.create_window(95,50, anchor="nw", window= self.CheckMTE1)

        

        self.CheckMTE2 = Checkbutton(self.canvaMTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT2,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(27,self.VarCheckMT2.get()))
        self.canvaMTE.create_window(359,15, anchor="nw", window= self.CheckMTE2)

        

        self.CheckMTE3 = Checkbutton(self.canvaMTE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT3,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(28,self.VarCheckMT3.get()))
        self.canvaMTE.create_window(91,265, anchor="nw", window= self.CheckMTE3)

        self.FrameRadio29 = Frame(self.canvaMTE)

        self.LabelCondy = Label(self.FrameRadio29,text='Condyles',bg='white')
        self.LabelCondy.pack()

        self.Radio291 = Radiobutton(self.FrameRadio29,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.Radio291.pack()

        self.Radio292 = Radiobutton(self.FrameRadio29,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.Radio292.pack()

        self.Radio293 = Radiobutton(self.FrameRadio29,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckMT4,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        
        self.Radio293.pack()
        self.canvaMTE.create_window(340,200, anchor="nw", window= self.FrameRadio29)


        self.FrameMES1 = Frame(self.FrameSuiformMT,bg='white')
        self.FrameMES1.pack()

        self.labelMES1 = Label(self.FrameMES1,text='Metatarsal proximal portion: ',bg='white')
        self.labelMES1.pack(side=LEFT)

        self.CheckMES1 = Checkbutton(self.FrameMES1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(26,self.VarCheckMT1.get()))
        self.CheckMES1.pack(side=LEFT)
        
        self.FrameMES2 = Frame(self.FrameSuiformMT,bg='white')
        self.FrameMES2.pack()

        self.labelMES2 = Label(self.FrameMES2,text='Metatarsal proximal portion: ',bg='white')
        self.labelMES2.pack(side=LEFT)

        self.CheckMES2 = Checkbutton(self.FrameMES2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.CheckMES2.pack(side=LEFT)





        self.labelU = Label(self.FrameUrsidMT,text='digits I–V:',bg='white')
        self.labelU.pack()

        self.FrameMEU1 = Frame(self.FrameUrsidMT,bg='white')
        self.FrameMEU1.pack()

        self.labelMEU1 = Label(self.FrameMEU1,text='Metatarsal proximal portion: ',bg='white')
        self.labelMEU1.pack(side=LEFT)

        self.CheckMEU1 = Checkbutton(self.FrameMEU1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(26,self.VarCheckMT1.get()))
        self.CheckMEU1.pack(side=LEFT)
        
        self.FrameMEU2 = Frame(self.FrameUrsidMT,bg='white')
        self.FrameMEU2.pack()

        self.labelMEU2 = Label(self.FrameMEU2,text='Metatarsal proximal portion: ',bg='white')
        self.labelMEU2.pack(side=LEFT)

        self.CheckMEU2 = Checkbutton(self.FrameMEU2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.CheckMEU2.pack(side=LEFT)






        self.labelO1 = Label(self.FrameOtherMT,text='digits II–V:',bg='white')
        self.labelO1.pack()

        self.FrameMEO1 = Frame(self.FrameOtherMT,bg='white')
        self.FrameMEO1.pack()

        self.labelMEO1 = Label(self.FrameMEO1,text='Metatarsal proximal portion: ',bg='white')
        self.labelMEO1.pack(side=LEFT)

        self.CheckMEO1 = Checkbutton(self.FrameMEO1,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT1,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(26,self.VarCheckMT1.get()))
        self.CheckMEO1.pack(side=LEFT)

        self.labelO2 = Label(self.FrameOtherMT,text='digits I–V:',bg='white')
        self.labelO2.pack()
        
        self.FrameMEO2 = Frame(self.FrameOtherMT,bg='white')
        self.FrameMEO2.pack()

        self.labelMEO2 = Label(self.FrameMEO2,text='Metatarsal proximal portion: ',bg='white')
        self.labelMEO2.pack(side=LEFT)

        self.CheckMEO2 = Checkbutton(self.FrameMEO2,bd=0,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckMT4,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(29,self.VarCheckMT4.get()))
        self.CheckMEO2.pack(side=LEFT)

        
        


        self.NotebookMP = ttk.Notebook(self.FrameMetapodial)
        self.NotebookMP.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])


        self.FrameMeta = Frame(self.NotebookMP,bg='white')
        self.FrameVestigalM = Frame(self.NotebookMP,bg='white')
        
        ListePageP =[self.FrameMeta,self.FrameVestigalM]
        ListeMeta =['Metapodial','Vestigial Metapodial']
        
        for tabMP, pageMP in zip(ListeMeta, ListePageP):
            self.NotebookMP.add(pageMP, text=tabMP)

        self.VarCheckPM31 = StringVar()
        self.VarCheckPM31.set(self.controller.getNDe(31))

        self.VarCheckPM86 = StringVar()
        self.VarCheckPM86.set(self.controller.getNDe(109))

        self.FrameM1 = Frame(self.FrameMeta)
        self.FrameM1.pack()

        self.labelM1 = Label(self.FrameM1,text='Bovids, cervids, equids :')
        self.labelM1.pack()

        self.canvaMP = Canvas(self.FrameM1,height=150,width=240,bg='white')
        self.canvaMP.pack(side=LEFT)

        self.image_fondMP = PhotoImage(file="View\Skull\LBN\metapodial_img\meta.png") 
        self.image_fondMP = self.image_fondMP.subsample(3)
        
        self.canvaMP.create_image(0, 0, anchor="nw", image=self.image_fondMP)

        self.FrameRadio86 = Frame(self.FrameM1,bg='white')
        self.FrameRadio86.pack()
        
        self.LabelCondy = Label(self.FrameRadio86,text='Condyles',bg='white')
        self.LabelCondy.pack()

        self.Radio861 = Radiobutton(self.FrameRadio86,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckPM31,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(31,self.VarCheckPM31.get()))
        self.Radio861.pack()

        self.Radio862 = Radiobutton(self.FrameRadio86,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckPM31,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(31,self.VarCheckPM31.get()))
        self.Radio862.pack()

        self.Radio863 = Radiobutton(self.FrameRadio86,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckPM31,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(31,self.VarCheckPM31.get()))
        self.Radio863.pack()

        self.FrameS1 = Frame(self.FrameMeta,bg='white')
        self.FrameS1.pack()

        self.labelM1 = Label(self.FrameS1,text='Suiform :',bg='white')
        self.labelM1.pack()

        self.FrameDE = Frame(self.FrameS1,bg='white')
        self.FrameDE.pack()

        self.LabelDE = Label(self.FrameDE,text='Distal epiphysis : ',bg='white')
        self.LabelDE.pack(side=LEFT)

        self.CheckDE = Checkbutton(self.FrameDE,text='>50%',variable=self.VarCheckPM31,onvalue=1,offvalue=0,bg='yellow',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(31,self.VarCheckPM31.get()))
        self.CheckDE.pack(side=LEFT)

        self.FrameM2 = Frame(self.FrameVestigalM,bg='white')
        self.FrameM2.pack()

        self.FrameVE = Frame(self.FrameM2,bg='white')
        self.FrameVE.pack()

        self.LabelVE = Label(self.FrameVE,text='Vestigial NDE : ',bg='white')
        self.LabelVE.pack(side=LEFT)

        self.CheckVE = Checkbutton(self.FrameVE,text='>50% or complete end',variable=self.VarCheckPM86,bg='yellow',
                                   onvalue=1,offvalue=0,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(31,self.VarCheckPM86.get()))
        self.CheckVE.pack(side=LEFT)

        self.NotebookMP.bind("<<NotebookTabChanged>>",lambda event:self.controller.update_Anat(self.NotebookMP.index("current"),'MP'))


        

         


        
        self.Notebookp = ttk.Notebook(self.FramePhalanx)
        self.Notebookp.pack(expand=True, fill='both')
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[20, 10])

        self.FrameBovidP = Frame(self.Notebookp,bg='white')
        self.FrameEquidP = Frame(self.Notebookp,bg='white')
        self.FrameSuiformP = Frame(self.Notebookp,bg='white')
        self.FrameUrsidP = Frame(self.Notebookp,bg='white')
        self.FrameOtherP = Frame(self.Notebookp,bg='white')

        ListePageP =[self.FrameBovidP,self.FrameEquidP,self.FrameSuiformP,self.FrameUrsidP,self.FrameOtherP]
        
        for tabP, pageP in zip(ListeTab, ListePageP):
            self.Notebookp.add(pageP, text=tabP)

        self.VarCheckP94 = StringVar()
        self.VarCheckP94.set(self.controller.getNDe(117))

        self.VarCheckP93 = StringVar()
        self.VarCheckP93.set(self.controller.getNDe(116))

        self.VarCheckP92 = StringVar()
        self.VarCheckP92.set(self.controller.getNDe(115))

        self.VarCheckP80 = StringVar()
        self.VarCheckP80.set(self.controller.getNDe(103))

        self.VarCheck81 = StringVar()
        self.VarCheck81.set(self.controller.getNDe(104))

        self.VarCheck82= StringVar()
        self.VarCheck82.set(self.controller.getNDe(105))


        self.canvaPB = Canvas(self.FrameBovidP,bg='white')
        self.canvaPB.pack(expand=True,fill=BOTH)

        self.image_fondPB = PhotoImage(file="View/Skull/LBN/phalanx_img/b.png") 
        self.image_fondPB = self.image_fondPB.subsample(4)
        self.canvaPB.create_image(0, 0, anchor="nw", image=self.image_fondPB)

        self.FrameRadio92 = Frame(self.canvaPB,bg='white')

        self.Radio921 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio921.pack()

        self.Radio922 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio922.pack()

        self.Radio923 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio923.pack()
        self.canvaPB.create_window(75,62, anchor="nw", window= self.FrameRadio92)

        self.FrameRadio93 = Frame(self.canvaPB,bg='white')

        self.Radio931 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio931.pack()

        self.Radio932 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio932.pack()

        self.Radio933 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio933.pack()

        
        self.canvaPB.create_window(210,62, anchor="nw", window= self.FrameRadio93)

        self.CheckPB1 = Checkbutton(self.canvaPB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP94,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(117,self.VarCheckP94.get()))
        self.canvaPB.create_window(300,89, anchor="nw", window= self.CheckPB1)

        

        self.CheckPB2 = Checkbutton(self.canvaPB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP80,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(103,self.VarCheckP80.get()))
        self.canvaPB.create_window(75,155, anchor="nw", window= self.CheckPB2)


        self.CheckPB3 = Checkbutton(self.canvaPB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(104,self.VarCheck81.get()))
        self.canvaPB.create_window(225,155, anchor="nw", window= self.CheckPB3)

        self.CheckPB4 = Checkbutton(self.canvaPB,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck82,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(105,self.VarCheck82.get()))
        self.canvaPB.create_window(345,155, anchor="nw", window= self.CheckPB4)


        self.FrameCheckPE = Frame(self.FrameEquidP,bg='white')
        self.FrameCheckPE.pack()

        self.FramePE1 = Frame(self.FrameCheckPE,bg='white')
        self.FramePE1.pack(side=LEFT)

        self.LabelPE1 = Label(self.FramePE1,text='distal',bg='white')
        self.LabelPE1.pack(side=LEFT)

        self.FrameRadio92 = Frame(self.FramePE1,bg='white')
        self.FrameRadio92.pack()

        self.Radio921 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio921.pack()

        self.Radio922 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio922.pack()

        self.Radio923 = Radiobutton(self.FrameRadio92,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP92,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.Radio923.pack()

        

        self.FramePE2 = Frame(self.FrameCheckPE,bg='white')
        self.FramePE2.pack(side=LEFT)

        self.LabelPE2 = Label(self.FramePE2,text='distal',bg='white')
        self.LabelPE2.pack(side=LEFT)

        self.FrameRadio93 = Frame(self.FramePE2,bg='white')
        self.FrameRadio93.pack()

        self.Radio931 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=0, text='0/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio931.pack()

        self.Radio932 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=0.5, text='1/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio932.pack()

        self.Radio933 = Radiobutton(self.FrameRadio93,bd=0,fg='red',bg='yellow',
                                   variable=self.VarCheckP93,value=1, text='2/2',
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.Radio933.pack()

        

        self.FramePE3 = Frame(self.FrameCheckPE,bg='white')
        self.FramePE3.pack(side=LEFT)

        self.LabelPE3 = Label(self.FramePE3,text='distal',bg='white')
        self.LabelPE3.pack(side=LEFT)

        self.CheckPE3 = Checkbutton(self.FramePE3,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP94,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(117,self.VarCheckP94.get()))
        
        self.CheckPE3.pack()


        self.canvaPE = Canvas(self.FrameEquidP,bg='white')
        self.canvaPE.pack(expand=True,fill=BOTH)

        self.image_fondPE = PhotoImage(file="View/Skull/LBN/phalanx_img/e.png") 
        self.image_fondPE = self.image_fondPE.subsample(3)
        self.canvaPE.create_image(0, 0, anchor="nw", image=self.image_fondPE)


        self.CheckPB2 = Checkbutton(self.canvaPE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP80,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(103,self.VarCheckP80.get()))
        self.canvaPE.create_window(100,45, anchor="nw", window= self.CheckPB2)


        self.CheckPB3 = Checkbutton(self.canvaPE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(104,self.VarCheck81.get()))
        self.canvaPE.create_window(250,50, anchor="nw", window= self.CheckPB3)

        self.CheckPB4 = Checkbutton(self.canvaPE,bd=0,fg='red',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck82,
                                   image=self.img_off, selectimage=self.img_on,
                                    compound='left', indicatoron=False,
                                   command=lambda:self.controller.landmark(105,self.VarCheck82.get()))
        self.canvaPE.create_window(400,50, anchor="nw", window= self.CheckPB4)


        

        self.FramePO = Frame(self.FrameSuiformP,bg='white')
        self.FramePO.pack(expand=True,fill=BOTH)

        self.FramePO1 = Frame(self.FramePO,bg='white')
        self.FramePO1.pack(side=LEFT)

        self.LabelPO1 = Label(self.FramePO1,text='Phalanx 1 :',bg='white')
        self.LabelPO1.pack()

        self.LabelPO2 = Label(self.FramePO1,text='Phalanx 2 :',bg='white')
        self.LabelPO2.pack()

        self.LabelPO3 = Label(self.FramePO1,text='Phalanx 3 :',bg='white')
        self.LabelPO3.pack()

        self.FramePO2 = Frame(self.FramePO,bg='white')
        self.FramePO2.pack(side=LEFT)

        self.LabelP = Label(self.FramePO2,text='Proximal',bg='white')
        self.LabelP.pack()

        self.CheckPO1 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP80,
                                   command=lambda:self.controller.landmark(103,self.VarCheckP80.get()))
        self.CheckPO1.pack()

        self.CheckPO2 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   command=lambda:self.controller.landmark(104,self.VarCheck81.get()))
        self.CheckPO2.pack()

        self.CheckPO3 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck82,
                                   command=lambda:self.controller.landmark(105,self.VarCheck82.get()))
        self.CheckPO3.pack()

        self.FramePO3 = Frame(self.FramePO,bg='white')
        self.FramePO3.pack(side=LEFT)

        self.LabelD = Label(self.FramePO3,text='Distal',bg='white')
        self.LabelD.pack()

        self.CheckPO1D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP92,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.CheckPO1D.pack()

        self.CheckPO2D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP93,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.CheckPO2D.pack()

        self.CheckPO3D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP94,
                                   command=lambda:self.controller.landmark(117,self.VarCheckP94.get()))
        self.CheckPO3D.pack()

        self.labelPro = Label(self.FramePO,text='proximal = portion of the proximal\rarticular surface near the anterior aspect',bg='white')
        self.labelPro.pack(side=BOTTOM)

        self.FramePO = Frame(self.FrameUrsidP,bg='white')
        self.FramePO.pack(expand=True,fill=BOTH)

        self.FramePO1 = Frame(self.FramePO,bg='white')
        self.FramePO1.pack(side=LEFT)

        self.LabelPO1 = Label(self.FramePO1,text='Phalanx 1 :',bg='white')
        self.LabelPO1.pack()

        self.LabelPO2 = Label(self.FramePO1,text='Phalanx 2 :',bg='white')
        self.LabelPO2.pack()

        self.LabelPO3 = Label(self.FramePO1,text='Phalanx 3 :',bg='white')
        self.LabelPO3.pack()

        self.FramePO2 = Frame(self.FramePO,bg='white')
        self.FramePO2.pack(side=LEFT)

        self.LabelP = Label(self.FramePO2,text='Proximal',bg='white')
        self.LabelP.pack()

        self.CheckPO1 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP80,
                                   command=lambda:self.controller.landmark(103,self.VarCheckP80.get()))
        self.CheckPO1.pack()

        self.CheckPO2 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   command=lambda:self.controller.landmark(104,self.VarCheck81.get()))
        self.CheckPO2.pack()

        self.CheckPO3 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck82,
                                   command=lambda:self.controller.landmark(105,self.VarCheck82.get()))
        self.CheckPO3.pack()

        self.FramePO3 = Frame(self.FramePO,bg='white')
        self.FramePO3.pack(side=LEFT)

        self.LabelD = Label(self.FramePO3,text='Distal',bg='white')
        self.LabelD.pack()

        self.CheckPO1D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP92,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.CheckPO1D.pack()

        self.CheckPO2D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP93,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.CheckPO2D.pack()

        self.CheckPO3D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP94,
                                   command=lambda:self.controller.landmark(117,self.VarCheckP94.get()))
        self.CheckPO3D.pack()

        self.labelPro = Label(self.FramePO,text='proximal = portion of the proximal\rarticular surface near the anterior aspect',bg='white')
        self.labelPro.pack(side=BOTTOM)

        self.FramePO = Frame(self.FrameOtherP,bg='white')
        self.FramePO.pack(expand=True,fill=BOTH)

        self.FramePO1 = Frame(self.FramePO)
        self.FramePO1.pack(side=LEFT)

        self.LabelPO1 = Label(self.FramePO1,text='Phalanx 1 :')
        self.LabelPO1.pack()

        self.LabelPO2 = Label(self.FramePO1,text='Phalanx 2 :')
        self.LabelPO2.pack()

        self.LabelPO3 = Label(self.FramePO1,text='Phalanx 3 :')
        self.LabelPO3.pack()

        self.FramePO2 = Frame(self.FramePO,bg='white')
        self.FramePO2.pack(side=LEFT)

        self.LabelP = Label(self.FramePO2,text='Proximal',bg='white')
        self.LabelP.pack()

        self.CheckPO1 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP80,
                                   command=lambda:self.controller.landmark(103,self.VarCheckP80.get()))
        self.CheckPO1.pack()

        self.CheckPO2 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck81,
                                   command=lambda:self.controller.landmark(104,self.VarCheck81.get()))
        self.CheckPO2.pack()

        self.CheckPO3 = Checkbutton(self.FramePO2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheck82,
                                   command=lambda:self.controller.landmark(105,self.VarCheck82.get()))
        self.CheckPO3.pack()

        self.FramePO3 = Frame(self.FramePO,bg='white')
        self.FramePO3.pack(side=LEFT)

        self.LabelD = Label(self.FramePO3,text='Distal',bg='white')
        self.LabelD.pack()

        self.CheckPO1D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP92,
                                   command=lambda:self.controller.landmark(115,self.VarCheckP92.get()))
        self.CheckPO1D.pack()

        self.CheckPO2D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP93,
                                   command=lambda:self.controller.landmark(116,self.VarCheckP93.get()))
        self.CheckPO2D.pack()

        self.CheckPO3D = Checkbutton(self.FramePO3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarCheckP94,
                                   command=lambda:self.controller.landmark(117,self.VarCheckP94.get()))
        self.CheckPO3D.pack()

        self.labelPro = Label(self.FramePO,text='proximal = portion of the proximal\rarticular surface near the anterior aspect',bg='white')
        self.labelPro.pack(side=BOTTOM)


        self.FrameVestigal = Frame(self.FramePhalanx,bg='white')
        self.FrameVestigal.pack(expand=True,fill=BOTH,anchor='center')
        
        self.LabelVestigal = Label(self.FrameVestigal,text='Vestigial Phalanges NDE',bg='white',
                                   font=font_ecriture)
        self.LabelVestigal.pack()

        self.VarPH1 = StringVar()
        self.VarPH1.set(self.controller.getNDe(106))

        self.VarPH2 = StringVar()
        self.VarPH2.set(self.controller.getNDe(107))

        self.VarPH3 = StringVar()
        self.VarPH3.set(self.controller.getNDe(108))

        self.FramePV = Frame(self.FrameVestigal,bg='white')
        self.FramePV.pack(expand=True)

        self.FramePH1 = Frame(self.FramePV,bg='white')
        self.FramePH1.pack(side=LEFT,padx=20)

        self.LabelPH1 = Label(self.FramePH1,text='PH1v',bg='white',
                                   font=font_ecriture)
        self.LabelPH1.pack()

        self.CheckPH1 = Checkbutton(self.FramePH1,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarPH1,
                                   command=lambda:self.controller.landmark(106,self.VarPH1.get()))
        self.CheckPH1.pack()

        self.FramePH2 = Frame(self.FramePV,bg='white')
        self.FramePH2.pack(side=LEFT,padx=20)

        self.LabelPH2 = Label(self.FramePH2,text='PH2v',bg='white',
                                   font=font_ecriture)
        self.LabelPH2.pack()

        self.CheckPH2 = Checkbutton(self.FramePH2,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarPH2,
                                   command=lambda:self.controller.landmark(107,self.VarPH2.get()))
        self.CheckPH2.pack()

        self.FramePH3 = Frame(self.FramePV,bg='white')
        self.FramePH3.pack(side=LEFT,padx=20)

        self.LabelPH3 = Label(self.FramePH3,text='PH3v',bg='white',
                                   font=font_ecriture)
        self.LabelPH3.pack()

        self.CheckPH3 = Checkbutton(self.FramePH3,fg='red',text='>50%',bg='yellow',
                                   onvalue=1,offvalue=0,variable=self.VarPH3,
                                   command=lambda:self.controller.landmark(108,self.VarPH3.get()))
        self.CheckPH3.pack()

        self.toggle_PH()

        self.toggle_button('yo')

        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()

        

    def toggle_shaft_circumference(self):
        if self.VarPotionS.get() == 'S':
            state = 'normal' 
        else: 
            state ='disabled'
            self.VarCir.set(None)
            self.controller.update_skel(self.VarCir.get(),'Skel_SHC')

        for i in self.listeCirc:
                i.config(state=state)
        self.controller.updatePortion(self.VarPotionS.get(),'S')

    def toggle_Age_E(self):
        if self.VarPotionE.get() == 'E':
            state = 'normal' 
        else: 
            state ='disabled'

        for i in self.listeEfus:
                        i.config(state=state)
        
        self.controller.updatePortion(self.VarPotionE.get(),'E')

    def toggle_PH(self):
        if self.VarPh.get()=='PH1v':
            self.CheckPH1.config(state='normal')
            self.CheckPH2.config(state='disabled')
            self.CheckPH3.config(state='disabled')

        elif self.VarPh.get()=='PH2v':
            self.CheckPH1.config(state='disabled')
            self.CheckPH2.config(state='normal')
            self.CheckPH3.config(state='disabled')

        elif self.VarPh.get()=='PH3v':
            self.CheckPH1.config(state='disabled')
            self.CheckPH2.config(state='disabled')
            self.CheckPH3.config(state='normal')
        else :
            self.CheckPH1.config(state='disabled')
            self.CheckPH2.config(state='disabled')
            self.CheckPH3.config(state='disabled')


        self.controller.update_skel(self.VarPh.get(),'Skel_Anat_Detail')

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




            

