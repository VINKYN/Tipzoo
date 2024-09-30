from tkinter import *

class frameBase(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.configure(bg='white')

        self.pack(expand=True, fill='both')

        self.Frame2 = Frame(self, bg='white')
        self.Frame2.pack(fill=BOTH, expand=True)

        self.FrameLeft = Frame(self.Frame2, bg='white')
        self.FrameLeft.pack(side=LEFT, expand=True, fill=BOTH)

        self.FrameLeftL = Frame(self.FrameLeft, bg='white')
        self.FrameLeftL.pack(side=LEFT, expand=True, fill=BOTH,pady=10,padx=10)


        self.FrameFracture = Frame(self.FrameLeftL,bg='#F2F2F2',bd=1,relief=SOLID)
        self.FrameFracture.pack()

        self.LabelFracture = Label(self.FrameFracture,text='Fractures',font=("Roboto 12"),bg='#F2F2F2')
        self.LabelFracture.pack(pady=(10,5),padx=20)

        self.LabelFrac = Label(self.FrameFracture,text="Green = acute/obtuse angle\r+ diagonal/helical outline\r + generally smooth texture\r(disregard stress relief features)")
        self.LabelFrac.pack(pady=5,padx=20)


        self.FrameFrac = Frame(self.FrameFracture,bg='#F2F2F2')
        self.FrameFrac.pack(pady=5)

        self.FrameFracC = Frame(self.FrameFrac,bg='#F2F2F2')
        self.FrameFracC.pack(side=LEFT)

        self.CheckGFR1 = Checkbutton(self.FrameFracC,font=("Roboto 12"),bg='#F2F2F2')
        self.CheckGFR1.pack(anchor='w',pady=5)

        self.CheckDFR1 = Checkbutton(self.FrameFracC,font=("Roboto 12"),bg='#F2F2F2')
        self.CheckDFR1.pack(anchor='w',pady=5) 

        self.CheckRFR1 = Checkbutton(self.FrameFracC,font=("Roboto 12"),bg='#F2F2F2')
        self.CheckRFR1.pack(anchor='w',pady=5) 


        self.FrameFracC2 = Frame(self.FrameFrac,bg='#F2F2F2')
        self.FrameFracC2.pack(side=LEFT)

        self.CheckGFR2 = Checkbutton(self.FrameFracC2,font=("Roboto 12"),bg='#F2F2F2',text="Green")
        self.CheckGFR2.pack(anchor='w',pady=5)

        self.CheckDFR2 = Checkbutton(self.FrameFracC2,font=("Roboto 12"),bg='#F2F2F2',text="Dry")
        self.CheckDFR2.pack(anchor='w',pady=5) 

        self.CheckRFR2 = Checkbutton(self.FrameFracC2,font=("Roboto 12"),bg='#F2F2F2',text="Recent")
        self.CheckRFR2.pack(anchor='w',pady=5) 


        self.LabelFrac = Label(self.FrameFracture,text="do not record when \r unsure or burnt!",bg='#F2F2F2')
        self.LabelFrac.pack(pady=(0,10))






        self.FrameLeftR = Frame(self.FrameLeft, bg='white')
        self.FrameLeftR.pack(side=LEFT, expand=True, fill=BOTH)

    
        self.FrameLBas =Frame(self.FrameLeftR,bg='#D9D9D9',bd=1 , relief='solid')
        self.FrameLBas.pack(padx=10,pady=10)

        self.LabelLbas1 = Label(self.FrameLBas , text='Post-depositional breakage',font=("Roboto 12"),bg='#D9D9D9')
        self.LabelLbas1.pack(pady=(5,0))


        self.FrameP1 = Frame(self.FrameLBas,bg='#F2F2F2',bd=1,relief='solid')
        self.FrameP1.pack(pady=5,anchor='w',padx=20)

        self.FrameP1L = Frame(self.FrameP1,bg='#F2F2F2')
        self.FrameP1L.pack(side=LEFT,anchor='w',padx=10)

        self.LabelP1L = Label(self.FrameP1L,text="Long. cracks\r(cort. surface)", font=("Roboto 12"),bg='#F2F2F2')
        self.LabelP1L.pack(pady=5)

        self.ButtonP1L = Button(self.FrameP1L ,text="Reset", font=("Roboto 12"))
        self.ButtonP1L.pack()

        self.FrameS1R = Frame(self.FrameP1,bg='#F2F2F2')
        self.FrameS1R.pack(side=LEFT,padx=10)

        self.RadioS1RS = Radiobutton(self.FrameS1R,text="shallow only",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioS1RS.pack(anchor="w",pady=5)

        self.RadioS1RF = Radiobutton(self.FrameS1R,text="deep (space between walls)",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioS1RF.pack(anchor='w',pady=5)


        self.FrameS2 = Frame(self.FrameLBas,bg='#F2F2F2',bd=1,relief='solid')
        self.FrameS2.pack(pady=5,anchor='w',padx=20)

        self.FrameS2L = Frame(self.FrameS2,bg='#F2F2F2')
        self.FrameS2L.pack(side=LEFT,anchor='w',padx=5)

        self.LabelS2L = Label(self.FrameS2L,text="Sheeting", font=("Roboto 12"),bg='#F2F2F2')
        self.LabelS2L.pack(pady=5)

        self.ButtonS2L = Button(self.FrameS2L ,text="Reset", font=("Roboto 12"))
        self.ButtonS2L.pack()

        self.FrameS2R = Frame(self.FrameS2,bg='#F2F2F2')
        self.FrameS2R.pack(side=LEFT,padx=10)

        self.RadioS2RS = Radiobutton(self.FrameS2R,text="shallow to deep, no fragmentation",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioS2RS.pack(anchor="w",pady=5)

        self.RadioS2RDEP = Radiobutton(self.FrameS2R,text="deep, causing fragmentation",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioS2RDEP.pack(anchor='w',pady=5)



    
        self.FrameLBas =Frame(self.FrameLeftR,bg='#D9D9D9',bd=1,relief='solid')
        self.FrameLBas.pack(padx=10)

        self.LabelLbas1 = Label(self.FrameLBas , text='Surface deposits ',font=("Roboto 12"),bg='#D9D9D9')
        self.LabelLbas1.pack()


        self.FrameC1 = Frame(self.FrameLBas,bg='#F2F2F2',bd=1,relief=SOLID)
        self.FrameC1.pack(pady=(0,5),anchor='w',padx=20)

        self.FrameC1L = Frame(self.FrameC1,bg='#F2F2F2')
        self.FrameC1L.pack(side=LEFT,anchor='w')

        self.LabelC1L = Label(self.FrameC1L,text="Concretions,\radhering matrix", font=("Roboto 12"),bg='#F2F2F2')
        self.LabelC1L.pack(pady=5,padx=5)

        self.ButtonC1L = Button(self.FrameC1L ,text="Reset", font=("Roboto 12"))
        self.ButtonC1L.pack()

        self.FrameC1R = Frame(self.FrameC1,bg='#F2F2F2')
        self.FrameC1R.pack(side=LEFT,padx=10)

        self.RadioC1LT = Radiobutton(self.FrameC1R,text="less than 1/3",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioC1LT.pack(anchor="w",pady=5)

        self.RadioC1TO = Radiobutton(self.FrameC1R,text="1/3 to 2/3",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioC1TO.pack(anchor="w",pady=5)

        self.RadioC1MO = Radiobutton(self.FrameC1R,text="most (>2/3)",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioC1MO.pack(anchor='w',pady=5)


        self.FrameTC = Frame(self.FrameC1,bg='#F2F2F2')
        self.FrameTC.pack()

        self.LabelTC = Label(self.FrameTC , text="Type of concretion",bg='#F2F2F2', font=("Roboto 12"))
        self.LabelTC.pack(padx=5)

        self.RadioC = Radiobutton(self.FrameTC,text="calc",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioC.pack(anchor='w',pady=5)

        self.RadioD = Radiobutton(self.FrameTC,text="dirt",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioD.pack(anchor='w',pady=5)



        self.FrameB2 = Frame(self.FrameLBas,bg='#F2F2F2',bd=1 , relief='solid')
        self.FrameB2.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.FrameB2L = Frame(self.FrameB2,bg='#F2F2F2')
        self.FrameB2L.pack(side=LEFT,anchor='w')

        self.LabelB2L = Label(self.FrameB2L,text="Black deposits\r(e.g. manganese)", font=("Roboto 12"),bg='#F2F2F2')
        self.LabelB2L.pack(pady=5)

        self.ButtonB2L = Button(self.FrameB2L ,text="Reset", font=("Roboto 12"))
        self.ButtonB2L.pack()

        self.FrameB2R = Frame(self.FrameB2,bg='#F2F2F2')
        self.FrameB2R.pack(side=LEFT,padx=10)

        self.RadioB1LT = Radiobutton(self.FrameB2R,text="less than 1/3",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioB1LT.pack(anchor="w",pady=5)

        self.RadioB1TO = Radiobutton(self.FrameB2R,text="1/3 to 2/3",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioB1TO.pack(anchor="w",pady=5)

        self.RadioB1MO = Radiobutton(self.FrameB2R,text="most (>2/3)",
                                      font=("Roboto 12"),bg='#F2F2F2')
        self.RadioB1MO.pack(anchor='w',pady=5)


        self.FrameS4 = Frame(self.FrameLBas,bg='#F2F2F2',bd=1,relief='solid')
        self.FrameS4.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.CheckDen = Checkbutton(self.FrameS4,text="Dendritic deposits (e.g. roots)",
                                   font=("Roboto 12"),bg='#F2F2F2')
        self.CheckDen.pack(anchor='w')






        self.FrameRight = Frame(self.Frame2)
        self.FrameRight.pack(expand=False, fill='y', side=RIGHT)

        self.FrameRlong = Frame(self.FrameRight,bg='white')
        self.FrameRlong.pack(expand=True, fill=BOTH)

        self.FrameAge = Frame(self.FrameRlong,bg="#F2F2F2",bd=1,relief='solid')
        self.FrameAge.pack(pady=10)

        self.LabelAge = Label(self.FrameAge,text='Age Cort',font=("Roboto 12"),bg='#F2F2F2')
        self.LabelAge.pack(side='left',padx=10)

        self.RadioF = Radiobutton(self.FrameAge,text='F',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioF.pack(side='left',padx=10,pady=5)

        self.RadioJ = Radiobutton(self.FrameAge,text='J',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioJ.pack(side='left',padx=10,)

        self.RadioA = Radiobutton(self.FrameAge,text='A',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioA.pack(side='left',padx=10,)

        self.RadioQ = Radiobutton(self.FrameAge,text='?',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioQ.pack(side='left',padx=10,)



        self.FrameHomi = Frame(self.FrameRlong,bg='#cadbfe',bd=1, relief='solid')
        self.FrameHomi.pack(padx=30,pady=(0,10))
        
        self.LabelHomi = Label(self.FrameHomi,text='HOMINIDS or CARNIVORES?',font=("Roboto 12"),bg='#cadbfe')
        self.LabelHomi.pack(pady=5)

        listHomi = ['Medullar flake scar ("notctî")',
        'Opposed medullar flake scar',
        'Cortical flake scar',
        'Bone flake',
        'Peellng (e.g on rib fragments)',
        '"Clean" oblique break of tooth',
        '"Clean" break ot spongious bone']

        self.VarMed = StringVar()
        self.VarOpp = StringVar()
        self.VarCor = StringVar()
        self.VarBon = StringVar()
        self.VarClo = StringVar()
        self.VarClb = StringVar()

        var =[self.VarMed,self.VarOpp,self.VarCor,
        self.VarBon,self.VarClo,self.VarClb]

        for label, var_item in zip(listHomi, var):
            self.FrameHo = Frame(self.FrameHomi,bg='#cadbfe')
            self.FrameHo.pack(anchor='w',padx=10,pady=2)

            self.radioHo = Radiobutton(self.FrameHo, text='0', variable=var_item , value='0',font=("Roboto 12"),bg='#cadbfe')
            self.radioHo.pack(side=LEFT,padx=10,pady=2)

            self.radioHu = Radiobutton(self.FrameHo, text='1', variable=var_item , value='1',font=("Roboto 12"),bg='#cadbfe')
            self.radioHu.pack(side=LEFT,padx=10,pady=2)

            self.radioHq = Radiobutton(self.FrameHo, text='?', variable=var_item , value='?',font=("Roboto 12"),bg='#cadbfe')
            self.radioHq.pack(side=LEFT,padx=10,pady=2)

            self.LabelH = Label(self.FrameHo, text=label,font=("Roboto 12"),bg='#cadbfe')
            self.LabelH.pack(side=LEFT,padx=10,pady=2)

    

        self.FrameCar = Frame(self.FrameRlong,bg='#a3d979',bd=1,relief=SOLID)
        self.FrameCar.pack(padx=30,pady=10)
        
        self.LabelCar = Label(self.FrameCar,text='CARNIVORES ?',bg='#a3d979',font=("Roboto 12"))
        self.LabelCar.pack(pady=5)

        listCar =  ['Crenulated (diaphysis)',
                     'Scooping out (crenulated spongy)',
                     'Rodent marks']
        self.VarCre = StringVar()
        self.VarSco = StringVar()
        self.VarRo = StringVar()

        var2 =[self.VarCre,self.VarSco,self.VarRo]

        for label, var_item in zip(listCar, var2):
            self.FrameCa = Frame(self.FrameCar,bg='#a3d979')
            self.FrameCa.pack(anchor='w' ,padx=10,pady=5)

            self.radioHo2 = Radiobutton(self.FrameCa, text='0', variable=var_item , value='0',bg='#a3d979',font=("Roboto 12"))
            self.radioHo2.pack(side=LEFT,padx=10)

            self.radioHu2 = Radiobutton(self.FrameCa, text='1', variable=var_item , value='1',bg='#a3d979',font=("Roboto 12"))
            self.radioHu2.pack(side=LEFT,padx=10)

            self.radioHq2 = Radiobutton(self.FrameCa, text='?', variable=var_item , value='?',bg='#a3d979',font=("Roboto 12"))
            self.radioHq2.pack(side=LEFT,padx=10)

            self.LabelC = Label(self.FrameCa, text=label,bg='#a3d979',font=("Roboto 12"))
            self.LabelC.pack(side=LEFT,padx=10)

    