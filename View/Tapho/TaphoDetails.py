from tkinter import *

class frameDetail(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.configure(bg='white')

        self.pack(expand=True, fill='both')

        self.Frame2 = Frame(self, bg='white')
        self.Frame2.pack(fill=BOTH, expand=True)

        self.FrameLeft = Frame(self.Frame2, bg='white')
        self.FrameLeft.pack(side=LEFT, expand=True, fill=BOTH)

        self.FrameLlong = Frame(self.FrameLeft,bg="white")
        self.FrameLlong.pack(expand=True, fill=BOTH)

        self.FrameRead = Frame(self.FrameLlong,bg="#F2F2F2",bd=1 , relief=SOLID)
        self.FrameRead.pack(pady=10)

        self.LabelRead = Label(self.FrameRead,text="Percentage readable surface",bg="#F2F2F2",
                               font=("Roboto 12"))
        self.LabelRead.pack(pady=5)

        self.FrameRRead = Frame(self.FrameRead,bg="#F2F2F2")
        self.FrameRRead.pack()

        self.Radio1 = Radiobutton(self.FrameRRead,text='2',font=("Roboto 12"),bg="#F2F2F2")
        self.Radio1.pack(side='left',padx=10,pady=5)

        self.Radio2 = Radiobutton(self.FrameRRead,text='2',font=("Roboto 12"),bg="#F2F2F2")
        self.Radio2.pack(side='left',padx=10,)

        self.Radio3 = Radiobutton(self.FrameRRead,text='3',font=("Roboto 12"),bg="#F2F2F2")
        self.Radio3.pack(side='left',padx=10,)

        self.Radio4 = Radiobutton(self.FrameRRead,text='4',font=("Roboto 12"),bg="#F2F2F2")
        self.Radio4.pack(side='left',padx=10,)

        self.RadioNa = Radiobutton(self.FrameRRead,text='Na',font=("Roboto 12"),bg="#F2F2F2")
        self.RadioNa.pack(side='left',padx=10,)


        self.LabelReadE = Label(self.FrameRead , text="NA = no cortical surtace (due tc green break or anatomy) \r 1 = 0-250/0 25-50%. 3 = 50-75% 75-1000/0",
                                font=("Roboto 10"),fg='#45464b',bg="#F2F2F2")
        self.LabelReadE.pack(pady=(0,5),padx=10)


        self.FrameLBas =Frame(self.FrameLlong,bg="#D9D9D9",bd=1 , relief='solid')
        self.FrameLBas.pack(padx=10,pady=10)

        self.LabelLbas = Label(self.FrameLBas , text='Surface alterations',font=("Roboto 12"),bg="#D9D9D9")
        self.LabelLbas.pack(pady=5)

        self.FrameS1 = Frame(self.FrameLBas,bg="#F2F2F2",bd=1 , relief='solid')
        self.FrameS1.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.CheckEx = Checkbutton(self.FrameS1,text="Exfoliation (desquamation first mm of cortical surface)",
                                   font=("Roboto 12"),bg="#F2F2F2")
        self.CheckEx.pack(anchor='w')


        self.FrameS2 = Frame(self.FrameLBas,bg="#F2F2F2",bd=1,relief=SOLID)
        self.FrameS2.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.FrameS2L = Frame(self.FrameS2,bg="#F2F2F2")
        self.FrameS2L.pack(side=LEFT,anchor='w')

        self.LabelS2L = Label(self.FrameS2L,text="Abrasion", font=("Roboto 12"),bg="#F2F2F2")
        self.LabelS2L.pack(pady=5)

        self.ButtonS2L = Button(self.FrameS2L ,text="Reset", font=("Roboto 12"))
        self.ButtonS2L.pack()

        self.FrameS2R = Frame(self.FrameS2,bg="#F2F2F2")
        self.FrameS2R.pack(side=LEFT,padx=10)

        self.RadioS2RS = Radiobutton(self.FrameS2R,text="slight rounding of edges only",
                                      font=("Roboto 12"),bg="#F2F2F2")
        self.RadioS2RS.pack(anchor="w",pady=5)

        self.RadioS2RF = Radiobutton(self.FrameS2R,text="fully rounded",
                                      font=("Roboto 12"),bg="#F2F2F2")
        self.RadioS2RF.pack(anchor='w',pady=5)


        self.FrameS3 = Frame(self.FrameLBas,bg="#F2F2F2",bd=1,relief='solid')
        self.FrameS3.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.FrameS3L = Frame(self.FrameS3,bg="#F2F2F2",)
        self.FrameS3L.pack(side=LEFT,anchor='w')

        self.LabelS3L = Label(self.FrameS3L,text="Corrosion & \r digestion \r(chemical \r action)", font=("Roboto 12"),bg="#F2F2F2")
        self.LabelS3L.pack(pady=5)

        self.ButtonS3L = Button(self.FrameS3L ,text="Reset", font=("Roboto 12"))
        self.ButtonS3L.pack()

        self.FrameS3R = Frame(self.FrameS3,bg="#F2F2F2",)
        self.FrameS3R.pack(side=LEFT,padx=10)

        self.RadioS3RL = Radiobutton(self.FrameS3R,text="limited corrosion (loss of tissue, slimed edges...)",
                                      font=("Roboto 12"),bg="#F2F2F2")
        self.RadioS3RL.pack(anchor="w",pady=5)

        self.RadioS3REC = Radiobutton(self.FrameS3R,text="extreme corrosion (little to no cortical surface left)",
                                      font=("Roboto 12"),bg="#F2F2F2")
        self.RadioS3REC.pack(anchor='w',pady=5)

        self.RadioS3RD = Radiobutton(self.FrameS3R,text="Digested ? (ultra-microscopic cracking, holes \r or strong enamel removal and dentine rounding)",
                                      font=("Roboto 12"),bg="#F2F2F2")
        self.RadioS3RD.pack(anchor='w',pady=5)
        
        self.FrameS4 = Frame(self.FrameLBas,bg="#F2F2F2",bd=1,relief='solid')
        self.FrameS4.pack(pady=5,anchor='w',padx=20,fill=BOTH)

        self.CheckCir = Checkbutton(self.FrameS4,text="Circular etching ('cupules')",
                                   font=("Roboto 12"),bg="#F2F2F2")
        self.CheckCir.pack(anchor='w',pady=5)

        self.CheckDe = Checkbutton(self.FrameS4,text="Dendritic etching (e.g. root grooves)",
                                   font=("Roboto 12"),bg='#F2F2F2')
        self.CheckDe.pack(anchor='w',pady=5) 














        self.FrameRight = Frame(self.Frame2)
        self.FrameRight.pack(expand=False, fill='y', side=RIGHT)

        self.FrameRlong = Frame(self.FrameRight,bg='white')
        self.FrameRlong.pack(expand=True, fill=BOTH)

        self.FrameTramp = Frame(self.FrameRlong,bg="#F2F2F2",bd=1 , relief=SOLID)
        self.FrameTramp.pack(pady=10)

        self.LabelTramp = Label(self.FrameTramp,text='Trampling',font=("Roboto 12"),bg='#F2F2F2')
        self.LabelTramp.pack(side='left',padx=10,pady=10)

        self.RadioN = Radiobutton(self.FrameTramp,text='N',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioN.pack(side='left',padx=10,pady=5)

        self.RadioQ = Radiobutton(self.FrameTramp,text='1',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioQ.pack(side='left',padx=10,)

        self.RadioO = Radiobutton(self.FrameTramp,text='A',font=("Roboto 12"),bg='#F2F2F2')
        self.RadioO.pack(side='left',padx=10,)

        #Mettre le var et variable 

        self.FrameHomi = Frame(self.FrameRlong,bg='#cadbfe' ,bd=1 ,relief='solid')
        self.FrameHomi.pack(padx=30,pady=(0,10))
        
        self.LabelHomi = Label(self.FrameHomi,text='HOMINIDS ?',font=("Roboto 12"),bg='#cadbfe')
        self.LabelHomi.pack(pady=5)


       

        listHomi = ['Cut',
        "Percussion marks (Pits and/or striae)",
        'Chop marks',
        'Scraping',
        'Retouchers',
        'Other bone tools']

        self.VarCut = StringVar()
        self.VarPerc = StringVar()
        self.VarChop = StringVar()
        self.VarScra = StringVar()
        self.VarRet = StringVar()
        self.VarOth = StringVar()

        var =[self.VarCut,self.VarPerc,self.VarChop,self.VarScra,
        self.VarRet,self.VarOth]

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

            if (label =="Scraping"):
                self.LabelR = Label(self.FrameHo, text='Associated with',font=("Roboto 10"),bg='#cadbfe',fg='#45464b')
                self.LabelR.pack(side=LEFT,padx=10,pady=2)

                self.EntryR =Entry(self.FrameHo,font=("Roboto 10"),width=10)
                self.EntryR.pack(side=LEFT,pady=2)
            if (label =="Cut"):
                self.ButtonCut = Button(self.FrameHo,text="cut-mark-code",bg='red'
                                        ,bd=1,relief='solid',font=("Roboto 12"),fg='white')
                self.ButtonCut.pack(side=LEFT,pady=2)



    

        self.FrameCar = Frame(self.FrameRlong,bg='#a3d979',bd=1 ,relief='solid')
        self.FrameCar.pack(padx=30,pady=10)
        
        self.LabelCar = Label(self.FrameCar,text='CARNIVORES ?',bg='#a3d979',font=("Roboto 12"))
        self.LabelCar.pack(pady=5)

        listCar =  ['Pits Choles compact bone',
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

    

    """:
        Punctures Choles spongy bone)
        Scores Clines compact bane)
        (Ines spongv bane)"""