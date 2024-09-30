from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from View.Clavier import NumpadEntry



class HomeInterface(Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.configure(bg='white')
        self.pack(expand=True, fill='both')

        font_button = ("Helvetica  13 bold" )

        font_ecriture =("Helvetica  10" )

        color_button = '#F2E2CE'

        color_bleu ='#b9e2f9'

        color_police ='#1b1b1b'

        self.Frame1 = Frame(self , bg='white')
        self.Frame1.pack(fill='x', side=TOP)

        self.FrameLogo = Frame(self.Frame1,bg='white')
        self.FrameLogo.pack(side=LEFT , anchor='w',padx=40,pady=(5,0))

        PilLogoTipzoo = Image.open("View/img/tipzoo logo-01.png")
        PilLogoTipzoo = PilLogoTipzoo.resize((int(219*1.3), int(69*1.3)))
        LogoTipzoo = ImageTk.PhotoImage(PilLogoTipzoo)

        self.LogoTipzoo = Label(self.FrameLogo, image=LogoTipzoo , bd=0)
        self.LogoTipzoo.image = LogoTipzoo  # Gardez une référence à l'image pour éviter la suppression par le garbage collector
        self.LogoTipzoo.pack()

        self.versions = Label(self.FrameLogo,text="Versions Vincent",bg='white')
        self.versions.pack(side=LEFT,padx=30,pady=10)

        self.buttonCredit = Button(self.FrameLogo, text="Credit" ,width=10 , background=color_button,fg=color_police
                                   ,bd=0,activebackground='#b9e2f9',font=font_button)
        self.buttonCredit.pack(side=LEFT,pady=10) 

        self.FrameButton = Frame(self.Frame1 ,bg='white')
        self.FrameButton.pack(expand=TRUE,side=LEFT)

        self.buttonSettings = Button(self.FrameButton , text="Settings",height= 3, width=20 , 
                                     bg=color_button,fg=color_police,activebackground='#b9e2f9',bd=0,font=font_button,
                                     command=self.controller.show_settings_page)
        self.buttonSettings.pack(side=LEFT,padx=50)

        self.buttonImportS = Button(self.FrameButton , text="Import Spatial",height= 3, width=20 , 
                                     bg=color_button,fg=color_police,activebackground='#b9e2f9',bd=0,font=font_button,
                                     command=lambda:self.controller.get_path_Spatial())
        self.buttonImportS.pack(side=LEFT,padx=50)

        self.buttonExport = Button(self.FrameButton , text="Export",height= 3, width=20 , 
                                     bg=color_button,fg=color_police,activebackground='#b9e2f9',bd=0,font=font_button,
                                     command=self.controller.show_export_page)
        self.buttonExport.pack(side=LEFT,padx=50)


        self.Frame2 = Frame(self , bg=color_bleu)
        self.Frame2.pack(expand=True, fill='x')

        self.FrameSite = Frame(self.Frame2 , bg='white',bd=0)
        self.FrameSite.pack(side=LEFT,ipadx=40,fill='y',expand=True,pady=20)
       
        self.FrameSiteContour = Frame(self.FrameSite , bg='white')
        self.FrameSiteContour.pack(expand=True,pady=(30,0))

        self.LabelSite = Label(self.FrameSiteContour,text="Site Name :",font=font_button,bg='white')
        self.LabelSite.pack(side=LEFT)

        self.LabelSite2 = Label(self.FrameSiteContour,text=self.controller.put_database(),font=font_button,bg='white')
        self.LabelSite2.pack(side=LEFT)




        self.FrameSetting = Frame(self.FrameSite,bg='white')
        self.FrameSetting.pack(expand=True,pady=(0,30))

        val = self.controller.get_database()

        self.listeSite = ttk.Combobox(self.FrameSetting, values=val,
                                      font=("Helvetica 14"))
        
        popdown = self.listeSite.tk.eval('ttk::combobox::PopdownWindow %s' % self.listeSite)
        self.listeSite.tk.call('%s.f.l' % popdown, 'configure', '-font', self.listeSite['font'])

        self.listeSite.current(self.controller.get_current(val))

        self.listeSite.pack(pady=10)

        self.AjouterBouton = Button(self.FrameSetting,text="Switch / Add a Site",
                                    font=("Helvetica 14"),bg=color_button,fg=color_police,
                                    bd=0,command= lambda:self.controller.switch_database(self.listeSite.get()))
        self.AjouterBouton.pack(pady=10)




        self.FrameNew = Frame(self.Frame2, bg='white')
        self.FrameNew.pack(side=LEFT,ipadx=40 , fill='y',expand=True,pady=20)

        self.ButtonNew = Button(self.FrameNew, text="NEW RECORDING LAYOUT \n\rFOR FRAGMENTS",
                                height=4, width=35,bg='#473014',fg='white',activebackground='white',
                                bd=0,font=font_button,command=self.controller.show_new_Base_create)
        self.ButtonNew.pack(expand=True, pady=20)

        self.FrameCount = Frame(self.Frame2 , bg='white')
        self.FrameCount.pack(side=LEFT,expand=True,pady=20)


        #Bouton Count 

        countText = self.controller.get_count_All()
        L1Count = countText[:3]
        L2Count = countText[3:6]
        L3Count = countText[6:]

        L1=['Base','Species','Skel',]
        L2=['Skel_NDE','Tapho','Teeth']
        L3=['Cut','Spatial','Refits']

        listeCount = [L1,L2,L3]
        listeCount2 = [L1Count,L2Count,L3Count]
          
        for row, (labels, counts) in enumerate(zip(listeCount, listeCount2), start=1):
            count_frame = Frame(self.FrameCount, bg='white')
            count_frame.pack(side=LEFT,pady=10,padx=10)

            for label, count in zip(labels, counts):
                LabelC =Label(count_frame, text=label, background='white',font = font_ecriture+' bold')
                LabelC.pack(padx=10, pady=3)
                ButtonC =Button(count_frame, text=count, height=2, width=10, bg=color_button,fg=color_police, activebackground='white',
                    bd=0, font = font_ecriture+' bold',command=lambda label=label: self.controller.show_allvalue_page(label))
                ButtonC.pack(padx=10)
                if label == "Cut" or label =="Tapho" or label =="Refits":
                    LabelC.configure(state='disabled')
                    ButtonC.configure(state='disabled')

                


        self.Frame3 = Frame(self , bg='white')
        self.Frame3.pack(side=BOTTOM, fill='x')

        self.FrameTab = Frame(self.Frame3)
        self.FrameTab.pack(side=LEFT,fill='x')

        colonnes = ('base_pk','base_id', 'species_Taxon', 'skel_anat_class','skel_anat','skel_side','Skel_Anat_Detail','datemodif')

        style = ttk.Style(self.FrameTab)
        style.configure('Treeview', rowheight=40,foreground =color_police) 

        style.configure('Treeview.Heading', rowheight=40) 

        style.map('Treeview', background=[('selected', '#b9e2f9')],foreground=[('selected', color_police)])
        


        self.tableau = ttk.Treeview(self.FrameTab,columns=colonnes , show='headings',
                                selectmode='browse')
        
        self.tableau.heading('base_id', text='ID',command=lambda:self.controller.order_by(self.tableau,'b.Base_ID'))
        self.tableau.heading('species_Taxon', text='Taxon',command=lambda:self.controller.order_by(self.tableau,'s.Species_Taxon'))
        self.tableau.heading('skel_anat_class', text='Class',command=lambda:self.controller.order_by(self.tableau,'sk.Skel_Anat_Class'))
        self.tableau.heading('skel_anat', text='Anat',command=lambda:self.controller.order_by(self.tableau,'sk.Skel_Anat'))
        self.tableau.heading('skel_side', text='Side',command=lambda:self.controller.order_by(self.tableau,'sk.Skel_Side'))
        self.tableau.heading('Skel_Anat_Detail', text='Détail',command=lambda:self.controller.order_by(self.tableau,'sk.Skel_Anat_Detail'))
        self.tableau.heading('datemodif', text='Last Change',command=lambda:self.controller.order_by(self.tableau,'b.DateModif'))

        for col in colonnes:
            self.tableau.column(col, width=int(self.winfo_screenwidth()/(len(colonnes))))
            self.tableau.config(displaycolumns=('base_id', 'species_Taxon', 'skel_anat_class', 'skel_anat','skel_side','Skel_Anat_Detail', 'datemodif'))

        valTree = self.controller.get_treeview()

        self.tableau.tag_configure('1', background='white')
        self.tableau.tag_configure('2', background='#F7F7F7')
        tag = 1
        for colonnes in valTree:
            if tag == 1 :
                self.tableau.insert('', END, values=colonnes, tags = (tag))
                tag += 1
            else :
                self.tableau.insert('', END, values=colonnes, tags = (tag))
                tag = 1


        self.Scrolbar = ttk.Scrollbar(self.FrameTab)
        self.Scrolbar.configure(command=self.tableau.yview)
        self.tableau.configure(yscrollcommand=self.Scrolbar.set)
        self.Scrolbar.pack(side=RIGHT, fill=BOTH)

        self.tableau.pack(expand=True, fill='both',side=LEFT)



        self.FrameEdit = Frame(self.Frame3,bg='white')
        self.FrameEdit.pack(side=LEFT,padx=10,expand=True,fill=BOTH)

        self.FrameSearch = Frame(self.FrameEdit,bg='white')
        self.FrameSearch.pack(ipady=20,pady=10)

        self.EntrySearch = NumpadEntry(self.FrameSearch,width=7,bd=1,relief='solid',
                                       font=("Roboto 13"))
        self.EntrySearch.pack(side=LEFT,padx=(0,5))

        self.ButtonSearch = Button(self.FrameSearch,text='Search', bg=color_button,fg=color_police,
                                   bd=0, command=lambda: self.controller.search(self.tableau,self.EntrySearch))
        self.ButtonSearch.pack(side=LEFT)

        self.ButtonEdit = Button(self.FrameEdit,text='Edit',width=10,height=3,bg=color_button,fg=color_police,bd=0,font=font_button,
                                 command=lambda:self.controller.show_new_Base(self.tableau))
        self.ButtonEdit.pack(pady=10)

        self.ButtonDel = Button(self.FrameEdit,text='Delete',width=10,height=3,bd=0,font=font_button,bg=color_button,fg=color_police,
                                command=lambda: self.controller.delete_base(self.tableau))
        self.ButtonDel.pack(pady=10)
            


        
