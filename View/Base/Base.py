from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk , ImageColor
from tkinter import colorchooser


from View.Base.treeview_haut import Treeview_haut
from View.Base.Menu import Menu
from View.Clavier import NumpadEntry


class BaseInterface(Frame):
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

        self.LabelNid =None

        self.custom_font = ('Helvetica', 13)       
        # Appliquer la police Roboto en taille 12
        self.pack(expand=True, fill='both')

        """self.Frame1 = Frame(self)
        self.Frame1.pack(side=TOP, fill='both')

        self.Tab = Treeview_haut(self.Frame1)
        self.Tab.pack(fill='both')"""

        self.Frame2 = Frame(self)
        self.Frame2.pack(fill=BOTH, expand=True)




        self.FrameLeft = Frame(self.Frame2, bg=color_button)
        self.FrameLeft.pack(side=LEFT, expand=True, fill=BOTH)

        self.FrameL = Frame(self.FrameLeft, bg='white',bd=1,relief='solid')
        self.FrameL.pack(side=TOP, fill=BOTH,padx=20,pady=10)

        self.ButtonP = Button(self.FrameL,text="Previous Record",bg=color_police,fg=color_button,bd=1,font=font_button,relief='solid',
                              command=self.controller.show_Base_pre)
        self.ButtonP.pack(expand=True,fill=BOTH,pady=10,padx=10,side=LEFT)

        self.ButtonN = Button(self.FrameL,text="Next Record",bg=color_police,fg=color_button,bd=1,font=font_button,relief='solid',
                              command=self.controller.show_Base_next)
        self.ButtonN.pack(expand=True,fill=BOTH,pady=10,padx=10,side=LEFT)



        self.FrameLH = Frame(self.FrameLeft, bg='white',bd=1,relief='solid')
        self.FrameLH.pack(side=TOP, fill=BOTH,padx=20,pady=10)
        
        self.FrameID = Frame(self.FrameLH,bg='white')
        self.FrameID.pack(anchor='w',side='bottom',fill='x')

        
        self.FrameRadioPS = Frame(self.FrameID,bg='white')
        self.FrameRadioPS.pack(side=LEFT,anchor='n',padx=10,pady=5)

        self.VarPS = StringVar() 

        self.VarPS.set(self.controller.get_plot_screen())

        self.RadioP = Radiobutton(self.FrameRadioPS , variable=self.VarPS,fg=color_police,
                                  font=("Roboto 12") , text="Plotted",value="Plotted",bg='white'
                                  ,command=self.toggle_id)

        self.RadioP.pack(padx=10,pady=5)

        self.RadioS = Radiobutton(self.FrameRadioPS , variable=self.VarPS,fg=color_police,
                                 font=("Roboto 12") , text="Screen",value="Screen",bg='white',
                                 command=self.toggle_id)

        self.RadioS.pack(padx=10,pady=5)

        self.FrameIDGlob = Frame(self.FrameID,bg='white')
        self.FrameIDGlob.pack(side=LEFT,padx=10,pady=5)

        self.FrameSQF = Frame(self.FrameIDGlob ,bg='white')
        self.FrameSQF.pack(anchor='w',padx=10,pady=5)
        
        self.FrameSquare = Frame(self.FrameSQF,bg='white')
        self.FrameSquare.pack(side='left',padx=(0,20))

        self.LabelSquare = Label(self.FrameSquare,text="Square ID number",font=("Roboto 12"),bg='white')
        self.LabelSquare.pack(side='left')

        
        #self.EntrySquare = NumpadEntry(self.FrameSquare,font=("Roboto 12"),width=8,bd=1,relief='solid')
        #self.EntrySquare.pack(side='left')

        self.EntrySQR_var = StringVar()

        val_square = self.controller.put_square()

        self.comboSquare = ttk.Combobox(self.FrameSquare,values=val_square,font=("Roboto 12"),width=7,
                                        textvariable=self.EntrySQR_var)
        self.comboSquare.pack(side='left')

        sqr = self.controller.get_fields('Base_Square')
        current = 0
        for c in range(len(val_square)):
            if val_square[c] == sqr :
                current = c

        if sqr != None :
            self.comboSquare.current(current)
 
        self.EntrySQR_var.trace_add("write", lambda *args:self.controller.update_Field(self.EntrySQR_var.get(),"Base_Square"))

        if self.controller.get_param('Param_IDNumb') == 'Unique ID':
            self.comboSquare.config(state='disabled')
        else:
            self.comboSquare.config(state='normal')

 

        self.FrameField = Frame(self.FrameSQF,bg='white')
        self.FrameField.pack(side='left')

        self.LabelID = Label(self.FrameField,text="Field ID number",font=("Roboto 12"),bg='white')
        self.LabelID.pack(side='left')


        self.EntryID_var = StringVar()
        self.EntryID = NumpadEntry(self.FrameField,font=("Roboto 12"),width=8,bd=1,relief='solid',
                                   textvariable=self.EntryID_var)
        self.EntryID.pack(side='left')

        field = self.controller.get_fields('Base_ID')

        if field != None :
            self.EntryID.delete(0, 'end')
            self.EntryID.insert(0, field)

        self.EntryID_var.trace_add("write", lambda *args:self.fill_spatial(self.EntryID_var.get(),"Base_Id"))

        sub = self.controller.get_fields('Base_Sub')
            
        self.FrameQSub = Frame(self.FrameIDGlob)
        self.FrameQSub.pack(anchor='w',padx=10,pady=5)
        
        self.VarSub = IntVar()

        self.CheckBSub = Checkbutton(self.FrameQSub , text="Normal that multiple remains with the same field number ?",
                                    variable=self.VarSub,onvalue=1, offvalue=0,bg='white',
                                    command=self.toggle_check)
        self.CheckBSub.pack(anchor='w')

        

        self.FrameSub = Frame(self.FrameIDGlob,bg='white')
        self.FrameSub.pack(anchor='w',padx=10,pady=5)

        self.FrameSubTop = Frame(self.FrameSub,bg='white')
        self.FrameSubTop.pack(anchor='w')

        self.LabelSub = Label(self.FrameSubTop,text="SubID",font=("Roboto 12"),bg='white')
        self.LabelSub.pack(side=LEFT)

        self.EntrySub_var = StringVar()

        self.EntrySub = NumpadEntry(self.FrameSubTop,font=("Roboto 12"),width=8,bg='white',bd=1 ,relief='solid',
                                    textvariable=self.EntrySub_var)
        self.EntrySub.pack(side=LEFT,)

        if sub != None :
            self.EntrySub.delete(0, 'end')
            self.EntrySub.insert(0, sub)

        self.EntrySub_var.trace_add("write", lambda *args:self.controller.update_Field(self.EntrySub_var.get(),"Base_Sub"))

        #self.EntrySub.bind('<FocusOut>',lambda event: self.controller.update_Field(self.EntrySub.get(),"Base_Sub",self.FrameID))


        self.ButtonSub = Button(self.FrameSubTop,text="Next SubID",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',
                                command=lambda:self.controller.next_sub(self.controller.get_fields('Base_ID'),self.LabelNextSub))
        self.ButtonSub.pack(side=LEFT,padx=(20,0))

        self.LabelNextSub = Label(self.FrameSubTop,font=("Roboto 12"),fg="#ff0033",bg='white')
        self.LabelNextSub.pack(side=LEFT,padx=(5,20))

        self.toggle_id()

        self.toggle_check()


        self.FrameLM = Frame(self.FrameLeft, bg='white',bd=1,relief='solid')
        self.FrameLM.pack(anchor='w',padx=20,pady=10,fill='x')

        self.FrameL1 = Frame(self.FrameLM,bg='white')
        self.FrameL1.pack(anchor='w',pady=(0,5))

        self.FrameCheck = Frame(self.FrameL1,bg='white')
        self.FrameCheck.pack(anchor='w',padx=10,pady=(10,0),side=LEFT)

        self.LabelCheck = Label(self.FrameCheck , text="Check Code", font=("Roboto 12"),bg='white')
        self.LabelCheck.pack(anchor='w',side=LEFT)

        self.VarCheckV = StringVar()
    
        self.LabelCheckV = Label(self.FrameCheck ,textvariable=self.VarCheckV, font=("Roboto 12"),bg='white')
        self.LabelCheckV.pack(anchor='w')

        self.FrameCheckF = Frame(self.FrameL1,bg='white')
        self.FrameCheckF.pack(padx=10,pady=(10,0),side=LEFT)

        self.LabelCheckF = Label(self.FrameCheckF ,text="LONGATED BONE ? (check for fabric)", font=("Roboto 12"),bg='white',fg="#ff0033")
        self.LabelCheckF.pack(anchor='w',side=LEFT)


        self.VarCheckCode = StringVar()
        self.VarCheckCode.set(self.controller.get_CheckCode())

        self.CheckCodeYes = Checkbutton(self.FrameCheckF , text="Yes",
                                        variable=self.VarCheckCode,onvalue='Yes', offvalue='No',bg='white',
                                        command=lambda:self.controller.update_checkCode(self.VarCheckCode.get()))
        self.CheckCodeYes.pack(anchor='w',side=LEFT)

        self.checkfab()
        
        self.FrameL2 = Frame(self.FrameLM)
        self.FrameL2.pack()

        self.FrameTab = Frame(self.FrameL2)
        self.FrameTab.pack()

        colonnes = ('Year','Code', 'fieldID', 'Square_Field','Dec','USField','Group1')

        style = ttk.Style(self.FrameTab)
        style.configure('Treeview', rowheight=20,foreground =color_police) 

        style.configure('Treeview.Heading', rowheight=20) 

    
        self.tableau = ttk.Treeview(self.FrameTab,columns=colonnes , show='headings')
        
        self.tableau.heading('Year', text='Year')
        self.tableau.heading('Code', text='Code')
        self.tableau.heading('fieldID', text='field ID')
        self.tableau.heading('Square_Field', text='Square Field')
        self.tableau.heading('Dec', text='Dec')
        self.tableau.heading('USField', text='USField')
        self.tableau.heading('Group1', text='Group1')

        for col in colonnes:
            self.tableau.column(col, width=int((self.winfo_screenwidth()/2)/(len(colonnes))))
            self.tableau.config(displaycolumns=('Year','Code', 'fieldID', 'Square_Field','Dec','USField','Group1'))

        if self.EntryID_var.get():

            valSpa = self.controller.get_Spa(self.EntryID_var.get())

            for colonnes in valSpa:
                self.tableau.insert('', END, values=colonnes)
                if self.VarPS.get() == "Plotted":
                    if colonnes[1] in ["FAUNE", "FAUNA"]:
                        label = "OK"
                    elif colonnes[1] in ["SEAU", "BUCKET"]:
                        label = "OK"
                    else:
                        label = "PROBLEM"
                        self.LabelCheckV.config(background='#ff0033',fg='white')
                else:
                    label = "PROBLEM"
                    self.LabelCheckV.config(background='#ff0033',fg='white')
            
                self.VarCheckV.set(label)

        self.tableau.config(height=3)

        self.tableau.pack(side=LEFT,fill=X)

        
        
        self.FrameLB = Frame(self.FrameLeft, bg='white',bd=1,relief='solid')
        self.FrameLB.pack(side='bottom', fill=BOTH,expand=TRUE,anchor='w',padx=20,pady=10)

        self.LabelEnlever = Label(self.FrameLB,text='Refits')
        self.LabelEnlever.pack()

        self.FrameRight = Frame(self.Frame2,bg='white')
        self.FrameRight.pack(fill=BOTH, side=RIGHT)

        self.FrameRH = Frame(self.FrameRight, bg='white')
        self.FrameRH.pack(side=TOP, fill=BOTH,padx=10,pady=5)

        self.FrameBurnt = Frame(self.FrameRH, bg='white',bd=1,relief='solid')
        self.FrameBurnt.pack(side=LEFT, expand=True,anchor='nw',padx=10,pady=5,fill='both')

        self.LabelBurnt = Label(self.FrameBurnt , text="Burnt Degree",font=("Roboto 12"),bg='white')
        self.LabelBurnt.pack(pady=(5,0))

        self.VarBurnt = StringVar()

        self.VarBurnt.set(self.controller.get_Burnt())


        self.BurntRadioNo = Radiobutton(self.FrameBurnt, text="No", value='No', variable=self.VarBurnt, font=("Roboto 12"),bg='white',fg=color_police,
                                        command=lambda:self.controller.update_burnt('No'))
        self.BurntRadioNo.pack(anchor='w',padx=10,pady=5)

        self.BurntRadioPar = Radiobutton(self.FrameBurnt, text="Partially", value='Partially', variable=self.VarBurnt, font=("Roboto 12"),bg='white',fg=color_police,
                                         command=lambda:self.controller.update_burnt('Partially'))
        self.BurntRadioPar.pack(anchor='w',padx=10,pady=5)

        self.BurntRadioMosB = Radiobutton(self.FrameBurnt, text="Mostly black", value='Mostly black', variable=self.VarBurnt, font=("Roboto 12"),bg='white',fg=color_police,
                                           command=lambda:self.controller.update_burnt('Mostly black'))
        self.BurntRadioMosB.pack(anchor='w',padx=10,pady=5)

        self.BurntRadioMosG = Radiobutton(self.FrameBurnt, text="Mostly grey", value='Mostly grey', variable=self.VarBurnt, font=("Roboto 12"),bg='white',fg=color_police,
                                          command=lambda:self.controller.update_burnt('Mostly grey'))
        self.BurntRadioMosG.pack(anchor='w',padx=10,pady=5)

        self.BurntRadioMosW = Radiobutton(self.FrameBurnt, text="Mostly white", value='Mostly white', variable=self.VarBurnt, font=("Roboto 12"),bg='white',fg=color_police,
                                           command=lambda:self.controller.update_burnt('Mostly white'))
        self.BurntRadioMosW.pack(anchor='w',padx=10,pady=5)

        self.FrameColor = Frame(self.FrameRH, bg='white',bd=1,relief='solid')
        self.FrameColor.pack(side=LEFT, expand=True, anchor='nw',padx=10,pady=5,fill='both')

        self.LabelColor = Label(self.FrameColor , text="Bone Color", font=("Roboto 12"),bg='white')
        self.LabelColor.pack(pady=(5,0))

        boneColor =self.controller.get_Allcolor()
        self.VarCol = IntVar()
        self.VarCol.set(self.controller.get_color())

        for id , color,hex,path in boneColor:
            if color != None or hex != None:
                RGBhex =ImageColor.getcolor(hex,'RGB')
                lum = 0.2126*RGBhex[0] + 0.7152*RGBhex[1]+ 0.0722*RGBhex[1]
                if lum < 128 :
                    hexfg = 'white'
                else :
                    hexfg =color_police


                self.FrameC = Frame(self.FrameColor,bg=hex)
                self.FrameC.pack(fill='x',pady=(0,10),padx=10)

                self.RadioColor = Radiobutton(self.FrameC,value=id, variable=self.VarCol, font=font_ecriture,bg=hex,
                                            command=lambda:self.controller.update_color(self.VarCol.get()))
                self.RadioColor.pack(anchor='w',padx=(10,0),pady=2,side=LEFT)

                self.LabelCo = Label(self.FrameC,text=color,font=font_ecriture,bg=hex,fg=hexfg)
                self.LabelCo.pack(side=LEFT,anchor='w',pady=2)

        

        self.FrameCb = Frame(self.FrameColor,bg='white')
        self.FrameCb.pack(side=BOTTOM,fill='x',pady=(0,5))

        self.FrameBasCOlor = Frame(self.FrameCb,bg='white')
        self.FrameBasCOlor.pack()

        self.ButtonAddC = Button(self.FrameBasCOlor,text='Add',bg=color_button,
                                fg=color_police,font=font_button,bd=0,
                                command=self.controller.show_color_page)
        self.ButtonAddC.pack(side=LEFT,padx=(10,5))

        self.ButtonReset = Button(self.FrameBasCOlor,text='Reset',bg=color_police,
                                fg=color_button,font=font_button,bd=0,
                                command=lambda:self.controller.reset_color(self.VarCol))
        self.ButtonReset.pack(side=LEFT,padx=(5,10))

        self.FrameSize = Frame(self.FrameRH, bg='white',bd=1,relief='solid')
        self.FrameSize.pack(side=LEFT, fill='y', anchor='nw',padx=10,pady=5)

        self.LabelSize = Label(self.FrameSize , text="Size class (cm)", font=("Roboto 12"),bg='white')
        self.LabelSize.pack(pady=(5,0))


        self.FrameMid = Frame(self.FrameSize,bg='white')
        self.FrameMid.pack(anchor='w')
        
        self.Frame7 = Frame(self.FrameMid,bg='white')
        self.Frame7.pack(side=LEFT, anchor='n',pady=5,padx=10)

        self.Frame14 = Frame(self.FrameMid,bg='white')
        self.Frame14.pack(side=LEFT, anchor='n',pady=5,padx=10)

        self.Frame21 = Frame(self.FrameMid,bg='white')
        self.Frame21.pack(side=LEFT, anchor='n',pady=5,padx=10)

        listeFrameSize =[self.Frame7,self.Frame14,self.Frame21]
        compteur = 0

        self.VarSize = StringVar()

        widg , size = self.controller.get_size()

        self.SizeRadio = Radiobutton(self.Frame7,variable=self.VarSize, text="NA", value="NA", font=self.custom_font,bg='white',fg=color_police,
                                      command=lambda:self.controller.update_size(self.VarSize.get(),self.FrameSize,self.LabelSize,self.LabelAutre))
        self.SizeRadio.pack(anchor='w')
        for j in listeFrameSize:
            for i in range(7):
                self.SizeRadio = Radiobutton(j , variable=self.VarSize, text=f"{compteur}-{compteur+1}", value= f"{compteur}-{compteur+1}", font=self.custom_font,bg='white',fg=color_police,
                                             command=lambda:self.controller.update_size(self.VarSize.get(),self.FrameSize,self.LabelSize,self.LabelAutre))
                self.SizeRadio.pack(anchor='w')
                compteur += 1

        self.FrameAutre = Frame(self.FrameSize)
        self.FrameAutre.pack(pady=5)

        self.LabelAutre = Label(self.FrameAutre ,text='Other',  font=("Roboto 12"),bg='white')
        self.LabelAutre.pack(side=LEFT)

        self.EntrySize = NumpadEntry(self.FrameAutre, font=("Roboto 12"),width=10,bd=1,relief='solid',textvariable=self.VarSize)
        self.EntrySize.pack(side=LEFT)

        self.EntrySize.bind('<FocusOut>', lambda event:self.controller.update_size(self.VarSize.get(),self.FrameSize,self.LabelSize,self.LabelAutre))

        
        if widg == 'e':
            self.EntrySize.delete(0, END)
            self.EntrySize.insert(0,size)
        if widg =='c':
            self.VarSize.set(size)
        if widg =='n':
            self.VarSize.set(size)
            self.FrameSize.configure(background='#ff0033')
            self.LabelSize.configure(background='#ff0033',fg='white')
            self.LabelAutre.configure(background='#ff0033',fg='white')
            for radio_button in listeFrameSize:
                radio_button.config(variable=None)



        paramSize = self.controller.get_param('Param_Size')
        if paramSize == 0:
            self.FrameSize.pack_forget()

        self.FrameRB = Frame(self.FrameRight,bg='white')
        self.FrameRB.pack(side=BOTTOM, expand=True, fill=BOTH,padx=10,pady=5)

        self.FrameRB1 = Frame(self.FrameRB,bg='white')
        self.FrameRB1.pack(side=LEFT,expand=True,fill=BOTH,padx=10)

        self.FrameBulk = Frame(self.FrameRB1,bg='white',bd=1,relief=SOLID)
        self.FrameBulk.pack(expand=True,fill=BOTH,pady=10)

        self.LabelBulk = Label(self.FrameBulk,text="Bulk",font=("Roboto 12"),bg='white')
        self.LabelBulk.pack(pady=(5,0))

        self.listeClass =['LBN','FBN','SBN','Skull','NID']

        self.listeFBN =['FBN','VRT','RIB','STE','SCP','COX','HYO']

        self.listeLBN =['LBN','HUM','RAU','FEM','TIB','FIB','PHA','MC','MT','MP']

        self.listeSBN =['SBN','CAR','TAR','PAT','MAL','SES']

        self.listeSpecies = self.controller.put_species()


        self.comboClass = ttk.Combobox(self.FrameBulk,values=self.listeClass,width=7,state="readonly")
        self.comboClass.pack(expand=True,pady=(5,0))

        class_pos = self.controller.getBulk('class')
        if class_pos is None: 
            self.comboClass.delete(0, "end")
        else:
            for cla in range(len(self.listeClass)):
                if self.listeClass[cla] == class_pos :
                    current_class = cla
                    self.comboClass.current(current_class)

        self.comboClass.bind('<<ComboboxSelected>>',lambda event: self.ChangeButton(self.comboClass.get()))
    
        

        if self.controller.getBulk('skel') is None or class_pos is None or len(class_pos)<1:
            self.comboClass.delete(0, "end")
            self.comboSkel = ttk.Combobox(self.FrameBulk,width=7,state="readonly")
            self.comboSkel.pack(expand=True,pady=(5,0))

        elif class_pos == 'LBN':
            self.comboSkel = ttk.Combobox(self.FrameBulk,width=7,state="readonly",values=self.listeLBN)
            self.comboSkel.pack(expand=True,pady=(5,0))
            class_skel = self.controller.getBulk('skel')
            for skel in range(len(self.listeLBN)):
                if self.listeLBN[skel] == class_skel :
                    current_skel = skel
                    self.comboSkel.current(current_skel)
        
        elif class_pos == 'FBN':
            self.comboSkel = ttk.Combobox(self.FrameBulk,width=7,state="readonly",values=self.listeFBN)
            self.comboSkel.pack(expand=True,pady=(5,0))
            class_skel = self.controller.getBulk('skel')
            for skel in range(len(self.listeFBN)):
                if self.listeFBN[skel] == class_skel :
                    current_skel = skel
                    self.comboSkel.current(current_skel)

        elif class_pos == 'SBN':
            self.comboSkel = ttk.Combobox(self.FrameBulk,width=7,state="readonly",values=self.listeSBN)
            self.comboSkel.pack(expand=True,pady=(5,0))
            class_skel = self.controller.getBulk('skel')
            for skel in range(len(self.listeSBN)):
                if self.listeSBN[skel] == class_skel :
                    current_skel = skel
                    self.comboSkel.current(current_skel)

        self.comboSkel.bind('<<ComboboxSelected>>',lambda event: self.controller.setBulk(self.comboSkel.get(),'skel'))

        self.comboSpecies = ttk.Combobox(self.FrameBulk,values=self.listeSpecies,width=7,state="readonly")
        self.comboSpecies.pack(expand=True,pady=(5,0))


        class_spe = self.controller.getBulk('species')

        if class_spe is None: 
            self.comboSpecies.delete(0, "end")
        else:
            for spe in range(len(self.listeSpecies)):
                if  self.listeSpecies[spe] == class_spe :
                    current_spe = spe
                    self.comboSpecies.current(current_spe)

        self.comboSpecies.bind('<<ComboboxSelected>>',lambda event: self.controller.setBulk(self.comboSpecies.get(),'species'))

        self.ButtonReset = Button(self.FrameBulk,text='Reset',bg=color_police,
                                fg=color_button,font=font_button,bd=0,
                                command=self.controller.resetBulk)
        self.ButtonReset.pack(side=BOTTOM,pady=5)


        self.ButtonUnde = Button(self.FrameRB1,text="Unidentified",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',
                                 command=self.controller.show_NID_page)
        self.ButtonUnde.pack(fill=BOTH,side=BOTTOM,pady=5)

        self.FrameRB2 = Frame(self.FrameRB,bg='white',bd=1,relief='solid')
        self.FrameRB2.pack(side=LEFT,expand=True,fill=BOTH,padx=10,pady=10)

        self.LabelMamals = Label(self.FrameRB2,text="Mammals",font=("Roboto 12"),bg='white')
        self.LabelMamals.pack(pady=(5,0))


        self.LabelNid = Label(self.FrameRB2,text="",bg='white',font=("Roboto 12"),width=28)
        self.LabelNid.pack(expand=True,fill=BOTH,pady=5,padx=10)
        self.LabelNid.pack_forget()

        self.ButtonSk = Button(self.FrameRB2,text="Skull bones and teeth",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                               command =self.controller.show_teeth_page)
        self.ButtonSk.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.ButtonLBN = Button(self.FrameRB2,text="Long Bones(including phalanges)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                command=self.controller.show_LBN_page)
        self.ButtonLBN.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.ButtonFBN = Button(self.FrameRB2,text="Flat bones(+ vertebras)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                 command=self.controller.show_FNB_page)
        self.ButtonFBN.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.ButtonSBN = Button(self.FrameRB2,text="Small bones(+ patella, malleolus)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                command=self.controller.show_SBN_page)
        self.ButtonSBN.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.FrameRB3 = Frame(self.FrameRB,bg='white',bd=1 ,relief='solid')
        self.FrameRB3.pack(side=LEFT,expand=True,fill=BOTH,padx=10,pady=10)

        self.LabelNMamals = Label(self.FrameRB3,text="Non-mammals",font=("Roboto 12"),bg='white')
        self.LabelNMamals.pack(pady=(5,0),padx=10)

        self.ButtonBB = Button(self.FrameRB3,text="Bird bones",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',
                               command=self.controller.show_Bird_page)
        self.ButtonBB.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.ButtonFBM = Button(self.FrameRB3,text="Fish bones &\r mollusca",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',
                                command=self.controller.show_NMB_page)
        self.ButtonFBM.pack(expand=True,fill=BOTH,pady=5,padx=10)

        self.Frame3 = Frame(self)
        self.Frame3.pack(side=BOTTOM, fill='both')

        self.Menu = Menu(self.Frame3,self.controller)
        self.Menu.pack()

        if self.bulk != None:
            self.ChangeButton(self.bulk.get_bulk_class())


    def ChangeButton(self,val):
        self.controller.setBulk(self.comboClass.get(),'class')
        if val =='LBN':
            self.ButtonLBN.pack_forget()
            self.ButtonLBN = Button(self.FrameRB2,text="Long Bones(including phalanges)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                     command=self.controller.show_LBN_page)
            self.ButtonLBN.pack(expand=True,fill=BOTH,pady=5,padx=10,)
            self.comboSkel.config(values=self.listeLBN)
            self.ButtonFBN.pack_forget()
            self.ButtonSBN.pack_forget()
            self.ButtonSk.pack_forget()
            self.LabelNid.pack_forget()

        elif val == 'SBN':
            self.ButtonSBN.pack_forget()
            self.ButtonSBN = Button(self.FrameRB2,text="Small bones(+ patella, malleolus)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                    command=self.controller.show_SBN_page)
            self.ButtonSBN.pack(expand=True,fill=BOTH,pady=5,padx=10)
            self.comboSkel.config(values=self.listeSBN)
            self.ButtonFBN.pack_forget()
            self.ButtonLBN.pack_forget()
            self.ButtonSk.pack_forget()
        
        elif val == 'FBN':
            self.ButtonFBN.pack_forget()
            self.ButtonFBN = Button(self.FrameRB2,text="Flat bones(+ vertebras)",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                     command=self.controller.show_FNB_page)
            self.ButtonFBN.pack(expand=True,fill=BOTH,pady=5,padx=10)
            self.comboSkel.config(values=self.listeFBN)
            self.ButtonLBN.pack_forget()
            self.ButtonSBN.pack_forget()
            self.ButtonSk.pack_forget()
        
        elif val == 'Skull':
            self.ButtonSk.pack_forget()
            self.ButtonSk = Button(self.FrameRB2,text="Skull bones and teeth",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',width=28,
                                   command =self.controller.show_teeth_page)
            self.ButtonSk.pack(expand=True,fill=BOTH,pady=5,padx=10)
            self.ButtonFBN.pack_forget()
            self.ButtonSBN.pack_forget()
            self.ButtonLBN.pack_forget()
            self.comboSkel.pack_forget()
            self.LabelNid.pack_forget()

        elif val == 'NID':
            self.LabelNid = Label(self.FrameRB2,text="",bg='white',font=("Roboto 12"),width=28)
            self.LabelNid.pack(expand=True,fill=BOTH,pady=5,padx=10)
            self.ButtonFBN.pack_forget()
            self.ButtonSBN.pack_forget()
            self.ButtonSk.pack_forget()
            self.ButtonLBN.pack_forget()
            self.comboSkel.pack_forget()

    def toggle_id(self):


        if self.VarPS.get() == 'Screen':
            self.CheckBSub.config(state='disabled')
            self.VarSub.set(0)
            self.EntrySub.config(state='normal')
            self.ButtonSub.config(state='normal')
            self.controller.update_plot_screen('Screen')

        elif self.VarPS.get() == 'Plotted':
            self.EntrySub.config(state='disabled')
            self.ButtonSub.config(state='disabled')
            self.CheckBSub.config(state='normal')
            self.controller.update_plot_screen('Plotted')

    def toggle_check(self):

        if self.VarSub.get() == 1:
            self.EntrySub.config(state='normal')
            self.ButtonSub.config(state='normal')
        else :
            self.EntrySub.config(state='disabled')
            self.ButtonSub.config(state='disabled')

    def fill_spatial(self,val,col):
        for item in self.tableau.get_children():
            self.tableau.delete(item)

        a =self.controller.update_Field(val,col)
        if a :
            for colonnes in a:
                print(colonnes)
                self.tableau.insert('', 'end', values=colonnes)

                if self.VarPS.get() == "Plotted":
                    if colonnes[1] in ["FAUNE", "FAUNA"]:
                        label = "OK"
                    elif colonnes[1] in ["SEAU", "BUCKET"]:
                        label = "OK"
                    else:
                        label = "PROBLEM"
                        self.LabelCheckV.config(background='#ff0033',fg='white')
                else:
                    label = "PROBLEM"
                    self.LabelCheckV.config(background='#ff0033',fg='white')
                self.VarCheckV.set(label)
        self.checkfab()

    def checkfab(self):
        fab =self.controller.get_fab()
        if fab :
            if fab[0][0] != None:
                if len(fab[0][0]) <1:
                    self.LabelCheckF.config(state='disabled')
                    self.CheckCodeYes.config(state='disabled')
                    self.VarCheckCode.set("No")
                    self.controller.update_checkCode('No')
                else :
                    self.LabelCheckF.config(state='normal')
                    self.CheckCodeYes.config(state='normal')
            else:
                self.LabelCheckF.config(state='disabled')
                self.CheckCodeYes.config(state='disabled')
                self.VarCheckCode.set("No")
                self.controller.update_checkCode('No')
        else :
            self.LabelCheckF.config(state='disabled')
            self.CheckCodeYes.config(state='disabled')
            self.VarCheckCode.set("No")
            self.controller.update_checkCode('No')




        

       
    """
    def ChangeID(self):

        val_actuel = self.VarPS.get()
        
        if self.VarPS.get() == 'Plotted':
            self.FrameSub.pack_forget()

            self.FrameQSub = Frame(self.FrameIDGlob)
            self.FrameQSub.pack(side=LEFT,padx=10,pady=5)
            
            self.VarSub = IntVar()

            self.CheckBSub = Checkbutton(self.FrameQSub , text="Normal that multiple remains with the same field number ?",
                                        variable=self.VarSub,onvalue=1, offvalue=0,bg='white',)
            self.CheckBSub.pack(anchor='w')

            self.FrameQSub.pack_forget() 
            # Afficher les éléments pour l'option "Screen"
            self.FrameSub = Frame(self.FrameIDGlob,bg='white')
            self.FrameSub.pack(anchor='w',padx=10,pady=5)

            self.FrameSubTop = Frame(self.FrameSub,bg='white')
            self.FrameSubTop.pack(side=LEFT)

            self.LabelSub = Label(self.FrameSubTop,text="SubID",font=("Roboto 12"),bg='white')
            self.LabelSub.pack(side=LEFT)

            sub = self.controller.get_fields('Base_Sub')

            self.EntrySub_var = StringVar()

            self.EntrySub = NumpadEntry(self.FrameSubTop,font=("Roboto 12"),width=8,bg='white',bd=1 ,relief='solid',
                                        textvariable=self.EntrySub_var)
            self.EntrySub.pack(side=LEFT,)

            if sub != None :
                self.EntrySub.delete(0, 'end')
                self.EntrySub.insert(0, sub)

            self.EntrySub_var.trace_add("write", lambda *args:self.controller.update_Field(self.EntrySub_var.get(),"Base_Sub"))


            #self.EntrySub.bind('<FocusOut>',lambda event: self.controller.update_Field(self.EntrySub.get(),"Base_Sub",self.FrameID))

            self.ButtonSub = Button(self.FrameSubTop,text="Next SubID",bg='#f0f0f0',bd=1,font=("Roboto 12"),relief='solid',
                                    command=lambda:self.controller.next_sub(self.controller.get_fields('Base_ID'),self.LabelNextSub))
            self.ButtonSub.pack(side=LEFT,padx=(20,0))

            self.LabelNextSub = Label(self.FrameSubTop,font=("Roboto 12"),fg='#ff0033',bg='white')
            self.LabelNextSub.pack(side=LEFT,padx=(5,20))
            """

            
