from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry
from View.Skull.Bande import Bande
from View.Skull.Side import Side

class AddTeethInterface(Frame):
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

        self.Frame1 = Frame(self, bg='#b9e2f9')
        self.Frame1.pack(fill='x', side=TOP,ipady=20)  # Ajout de padx et pady pour l'espacement

        self.ButtonMenu = Button(self.Frame1, text="Back", width=15, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Roboto", 12),
                                command=self.controller.show_Skel_page)
        self.ButtonMenu.pack(side=LEFT, padx=20)


        self.Frame2 = Frame(self,bg=color_button)
        self.Frame2.pack(fill='x',padx=20,pady=(40,20))

        self.FrameLower = Frame(self.Frame2,bg='white')
        self.FrameLower.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelLower = Label(self.FrameLower,text='Lower',font=font_ecriture,bg='white')
        self.LabelLower.pack()

        self.VarLower = StringVar()

        val_lower = ['Lower','Upper','?']

        self.comboLower = ttk.Combobox(self.FrameLower,values=val_lower,font=font_ecriture,state='readonly',
                                        textvariable=self.VarLower)
        self.comboLower.pack()

        self.comboLower.current(self.controller.getLowerUpper())
        
        self.comboLower.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_LowerUpper',self.VarLower.get()))

        popdown = self.comboLower.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboLower)
        self.comboLower.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboLower['font'])


        self.FrameSide = Frame(self.Frame2,bg='white')
        self.FrameSide.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelSide = Label(self.FrameSide,text='Side',font=font_ecriture,bg='white')
        self.LabelSide.pack()

        self.VarSide = StringVar()

        val_Side = ["Left","Right","?"]

        self.comboSide = ttk.Combobox(self.FrameSide,values=val_Side,font=font_ecriture,state='readonly',
                                        textvariable=self.VarSide)
        self.comboSide.pack()

        self.comboSide.current(self.controller.getSide())

        self.comboSide.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_Side',self.VarSide.get()))

        popdown = self.comboSide.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboSide)
        self.comboSide.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboSide['font'])

        self.FrameType = Frame(self.Frame2,bg='white')
        self.FrameType.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelType = Label(self.FrameType,text='Type',font=font_ecriture,bg='white')
        self.LabelType.pack()

        self.VarType = StringVar()

        val_Type = ['ANTERIOR','Cheek','?']

        self.comboType = ttk.Combobox(self.FrameType,values=val_Type,font=font_ecriture,state='readonly',
                                        textvariable=self.VarType)
        self.comboType.pack()

        self.comboType.current(self.controller.getType())

        popdown = self.comboType.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboType)
        self.comboType.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboType['font'])

        self.comboType.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_Type',self.VarType.get()))



        self.FrameDentition = Frame(self.Frame2,bg='white')
        self.FrameDentition.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelDentition = Label(self.FrameDentition,text='Dentition',font=font_ecriture,bg='white')
        self.LabelDentition.pack()

        self.VarDentition = StringVar()

        val_Dentition = ['Permanent','Deciduous','?']

        self.comboDentition = ttk.Combobox(self.FrameDentition,values=val_Dentition,font=font_ecriture,state='readonly',
                                        textvariable=self.VarDentition)
        self.comboDentition.pack()

        self.comboDentition.current(self.controller.getDentition())

        self.comboDentition.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_Dentition',self.VarDentition.get()))

        popdown = self.comboDentition.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboDentition)
        self.comboDentition.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboDentition['font'])


        self.FrameClass = Frame(self.Frame2,bg='white')
        self.FrameClass.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelClass = Label(self.FrameClass,text='Class',font=font_ecriture,bg='white')
        self.LabelClass.pack()

        self.VarClass = StringVar()

        val_Class = ['Incisor','Canine','Premolar','Molar','Postcanine','?']

        self.comboClass = ttk.Combobox(self.FrameClass,values=val_Class,font=font_ecriture,state='readonly',
                                        textvariable=self.VarClass)
        self.comboClass.pack()

        self.comboClass.current(self.controller.getClass())

        self.comboClass.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_Class',self.VarClass.get()))

        popdown = self.comboClass.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboClass)
        self.comboClass.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboClass['font'])


        self.FrameNumber = Frame(self.Frame2,bg='white')
        self.FrameNumber.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelNumber = Label(self.FrameNumber,text='Number',font=font_ecriture,bg='white')
        self.LabelNumber.pack()

        self.VarNumber = StringVar()

        val_Number = ['1','2','3','4','1-2','3-4','NID']

        self.comboNumber = ttk.Combobox(self.FrameNumber,values=val_Number,font=font_ecriture,state='readonly',
                                        textvariable=self.VarNumber)
        self.comboNumber.pack()

        self.comboNumber.current(self.controller.getNumber())

        self.comboNumber.bind('<<ComboboxSelected>>',lambda event: self.controller.update_combo('Teeth_Number',self.VarNumber.get()))

        popdown = self.comboNumber.tk.eval('ttk::combobox::PopdownWindow %s' % self.comboNumber)
        self.comboNumber.tk.call('%s.f.l' % popdown, 'configure', '-font', self.comboNumber['font'])



        self.Frame3 = Frame(self,bg=color_button)
        self.Frame3.pack(fill='x',padx=20,pady=20)

        self.FrameNom = Frame(self.Frame3,bg=color_button)
        self.FrameNom.pack(side=LEFT,padx=20,pady=(20,10),anchor='nw')


        self.FrameFragmentation = Frame(self.FrameNom,bg='white')
        self.FrameFragmentation.pack(fill='y',expand=True)

        self.VarFram = StringVar()
        self.VarFram.set(self.controller.getFr())

        self.RadioCO = Radiobutton(self.FrameFragmentation, text="CO",value="CO", variable=self.VarFram,font=font_ecriture,bg='white',
                                   command=lambda:self.fill_portions(self.VarFram.get()))
                
        self.RadioCO.pack(padx=5,anchor='w',side=LEFT)

        self.RadioACO = Radiobutton(self.FrameFragmentation, text="ACO", value="ACO",variable=self.VarFram,font=font_ecriture,bg='white',
                                     command=lambda:self.fill_portions(self.VarFram.get()))
        self.RadioACO.pack(padx=5,anchor='w',side=LEFT)

        self.RadioFR = Radiobutton(self.FrameFragmentation, text="FR", value="FR",variable=self.VarFram,font=font_ecriture,bg='white',
                                    command=lambda:self.controller.updateFr(self.VarFram.get()))
        self.RadioFR.pack(padx=5,anchor='w',side=LEFT)


        self.FramePortion = Frame(self.FrameNom,bg='white')
        self.FramePortion.pack()
            
        self.VarPortion1 = StringVar()
        self.VarPortion2 = StringVar()

        p1,p2 = self.controller.getPortion()
        
        self.VarPortion1.set(p1)
        self.VarPortion2.set(p2)

        self.CheckCRN = Checkbutton(self.FramePortion, text="CRN",variable=self.VarPortion1,font=font_ecriture,
                                   onvalue='CRN',offvalue='',bg='white',
                                   command=lambda:self.controller.updatePortion(self.VarPortion1.get(),'CRN'))
        self.CheckCRN.pack(padx=5,anchor='w',side=LEFT)

        self.CheckROOT= Checkbutton(self.FramePortion, text="ROOT", variable=self.VarPortion2,font=font_ecriture,
                                   onvalue='ROOT',offvalue='',bg='white',
                                   command=lambda:self.controller.updatePortion(self.VarPortion2.get(),'ROOT'))
        self.CheckROOT.pack(padx=5,anchor='w',side=LEFT)


        self.FrameSurf = Frame(self.FrameNom,bg='white')
        self.FrameSurf.pack(padx=20,pady=(20,10),anchor='nw')

        self.VarSurf = IntVar()
        self.VarSurf.set(self.controller.getSurf())

        self.RadioSurf = Checkbutton(self.FrameSurf, text="Occl. surf\r50%?",variable=self.VarSurf,font=font_ecriture,
                                   onvalue=1,offvalue=None,bg='white',command=lambda:self.controller.updateSurf(self.VarSurf.get()))
        self.RadioSurf.pack(padx=5,anchor='w',side=LEFT)


        self.FrameAge = Frame(self.FrameNom,bg='white')
        self.FrameAge.pack(padx=20,pady=(20,10),anchor='nw')

        self.VarAge = StringVar()
        varAge = self.controller.getAge()

       

        self.LabelAge = Label(self.FrameAge,text="Age Class \r(note)",bg='white')
        self.LabelAge.pack(side=LEFT)

        self.EntryAge = NumpadEntry(self.FrameAge,textvariable=self.VarAge,bg='white')
        self.EntryAge.pack(side=LEFT)

        if varAge == None:
           self.EntryAge.delete(0,END)
        else :
            self.VarAge.set(varAge)

        self.VarAge.trace_add("write", lambda *args:self.controller.updateAge(self.VarAge.get()))


        self.FrameCrown = Frame(self.Frame3,bg='white')
        self.FrameCrown.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelCrown = Label(self.FrameCrown,text="Crown",bg='white')
        self.LabelCrown.pack()

        self.FrameUse = Frame(self.FrameCrown,bg='white')
        self.FrameUse.pack(side=LEFT)

        self.VarCrown = IntVar()
        self.VarCrown.set(self.controller.getCrown())

        self.buttonReset = Button(self.FrameUse,text='Reset',fg=color_button,bg=color_police,
                                  command=lambda:self.reset1())
        
        self.buttonReset.pack()

        self.RadioNoUse = Radiobutton(self.FrameUse, text="No Use",value=0, variable=self.VarCrown,font=font_ecriture,bg='white',
                                      command=lambda:self.controller.updateCrown(self.VarCrown.get()))
        self.RadioNoUse.pack(padx=5,anchor='w')

        self.RadioLUse = Radiobutton(self.FrameUse, text="Little use",value=1, variable=self.VarCrown,font=font_ecriture,bg='white',
                                      command=lambda:self.controller.updateCrown(self.VarCrown.get()))
        self.RadioLUse.pack(padx=5,anchor='w')

        self.RadioFUse = Radiobutton(self.FrameUse, text="In full use",value=2, variable=self.VarCrown,font=font_ecriture,bg='white',
                                      command=lambda:self.controller.updateCrown(self.VarCrown.get()))
        self.RadioFUse.pack(padx=5,anchor='w')

        self.RadioVUse = Radiobutton(self.FrameUse, text="Very used",value=3, variable=self.VarCrown,font=font_ecriture,bg='white',
                                     command=lambda:self.controller.updateCrown(self.VarCrown.get()))
        self.RadioVUse.pack(padx=5,anchor='w')

        self.VarCr = StringVar()
        varCr =self.controller.getCr()

        self.LabelCr = Label(self.FrameCrown,text="Crown Height \r(mm)",bg='white')
        self.LabelCr.pack(side=LEFT)

        self.EntryCrown = NumpadEntry(self.FrameCrown,textvariable=self.VarCr,bg='white')
        self.EntryCrown.pack(side=LEFT)

        if varCr == None:
           self.EntryCrown.delete(0,END)
        else :
            self.VarCr.set(varCr)

        self.VarCr.trace_add("write", lambda *args:self.controller.updateCr(self.VarCr.get()))



        self.FrameRoot = Frame(self.Frame3,bg='white')
        self.FrameRoot.pack(side=LEFT,padx=20,pady=(20,10),anchor='n')

        self.LabelRoot = Label(self.FrameRoot,text="Root",bg='white')
        self.LabelRoot.pack()

        self.FrameOpen = Frame(self.FrameRoot,bg='white')
        self.FrameOpen.pack(side=LEFT)

        self.VarRoot2 = IntVar()
        self.VarRoot2.set(self.controller.getRoot())

        self.buttonReset2 = Button(self.FrameOpen,text='Reset',fg=color_button,bg=color_police,
                                  command=lambda:self.reset2())
        
        self.buttonReset2.pack()

        self.RadioClosed = Radiobutton(self.FrameOpen, text="Closed, CO",value=0, variable=self.VarRoot2,font=font_ecriture,bg='white',
                                       command=lambda:self.controller.updateRoot(self.VarRoot2.get()))
        self.RadioClosed.pack(padx=5,anchor='w')

        self.RadioOpen1 = Radiobutton(self.FrameOpen, text='Open, >50% formed',value=1, variable=self.VarRoot2,font=font_ecriture,bg='white',
                                       command=lambda:self.controller.updateRoot(self.VarRoot2.get()))
        self.RadioOpen1.pack(padx=5,anchor='w')

        self.RadioOpen2 = Radiobutton(self.FrameOpen, text='Open, <50% formed',value=2, variable=self.VarRoot2,font=font_ecriture,bg='white',
                                       command=lambda:self.controller.updateRoot(self.VarRoot2.get()))
        self.RadioOpen2.pack(padx=5,anchor='w')

        self.VarRootRe = IntVar()
        self.VarRootRe.set(self.controller.getRootRe())

        self.RadioSurf = Checkbutton(self.FrameOpen, text="Root resorption",variable=self.VarRootRe,font=font_ecriture,
                                   onvalue=1,bg='white',
                                    command=lambda:self.controller.updateRootRe(self.VarRootRe.get()))
        self.RadioSurf.pack(padx=5,anchor='w')


    def fill_portions(self,val):
        self.controller.updateFr(val)
        self.VarPortion1.set('CRN')
        self.VarPortion2.set('ROOT') 
        self.controller.updatePortionNone()
        self.controller.updatePortion(self.VarPortion1.get(),'CRN')
        self.controller.updatePortion(self.VarPortion2.get(),'ROOT')

    def reset1(self):
        self.controller.updateCrown(None)
        self.VarCrown.set(None)

    def reset2(self):
        self.controller.updateRoot(None)
        self.VarRoot2.set(None)

   
        
        






        











        