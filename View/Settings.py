from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from Controller.SettingsController import SettingsController
from View.Home import HomeInterface

class SettingsInterface(Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)

        self.master = master
        self.controller = controller  # Assigning the controller
        self.configure(bg='white')
        self.pack(expand=True, fill='both')

        # You can call put_Param here or wherever it's needed

        self.Frame1 = Frame(self, bg='#b9e2f9')
        self.Frame1.pack(fill='x', side=TOP,ipady=20)  # Ajout de padx et pady pour l'espacement

        self.ButtonMenu = Button(self.Frame1, text="Home", width=15, height=2, background='#f0f0f0',
                                relief='solid', bd=1, activebackground='white', font=("Roboto", 12),
                                command=self.controller.show_home_page)
        self.ButtonMenu.pack(side=LEFT, padx=20)  # Ajout de padx pour l'espacement à gauche

        #self.LabelTitre = Label(self.Frame1, text="Recording settings", font=("Roboto", 12), bg='#b9e2f9')
        #self.LabelTitre.pack(side='top',)  # Ajout de padx pour l'espacement entre le bouton et le label

        self.FrameBodySetting = Frame(self, bg='white')
        self.FrameBodySetting.pack(fill='both', padx=30, pady=30)


        self.FrameID = Frame(self.FrameBodySetting,bg='white',bd=1,relief=SOLID)
        self.FrameID.pack(anchor='w',pady=15)

        self.LabelID = Label(self.FrameID, text="Settings for ID numbers", font=("Roboto", 12), bg='white')
        self.LabelID.pack(side=LEFT)

        self.varID = StringVar()

        self.RadioID = Radiobutton(self.FrameID, text="Unique ID", value='Unique ID', variable=self.varID,
                                   font=("Roboto", 12), bg='white',
                                   command= lambda : self.controller.update_param('Param_IDNumb','Unique ID'))
        self.RadioID.pack(side=LEFT)

        self.RadioSquare = Radiobutton(self.FrameID, text="Square ID", value='Square ID', variable=self.varID, font=("Roboto", 12),
                                       bg='white', command=lambda : self.controller.update_param('Param_IDNumb','Square ID'))
        self.RadioSquare.pack(side=LEFT)

        if self.controller.put_Param('Param_IDNumb') == 'Unique ID':
            self.RadioID.select()
        else:
            self.RadioSquare.select()


        self.FrameSize = Frame(self.FrameBodySetting, bg='white',bd=1,relief=SOLID)
        self.FrameSize.pack(anchor='w',pady=15)

        self.LabelSize = Label(self.FrameSize, text="Settings for Size:", font=("Roboto", 12), bg='white')
        self.LabelSize.pack(anchor='w',padx=20,side=LEFT)

        self.varSize = IntVar()

        self.RadioSizeYes = Radiobutton(self.FrameSize, text="Yes", value=1, variable=self.varSize, font=("Roboto", 12),
                                         bg='white',command=lambda : self.controller.update_param('Param_Size',1))
        self.RadioSizeYes.pack(side=LEFT ,padx=(0,10))

        self.RadioSizeNo = Radiobutton(self.FrameSize, text="No", value=0, variable=self.varSize, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Size',0))
        self.RadioSizeNo.pack(side=LEFT)

        self.LabelChoose = Label(self.FrameSize, text="Choose 'No' if you do not wish the program to ask for the size of each fragment", font=("Roboto", 12), bg='white')
        self.LabelChoose.pack(padx=10)

        if self.controller.put_Param('Param_Size') == 1:
            self.RadioSizeYes.select()
        else:
            self.RadioSizeNo.select()


        self.FrameSide = Frame(self.FrameBodySetting, bg='white',bd=1,relief=SOLID)
        self.FrameSide.pack(anchor='w',pady=15)

        self.LabelSide = Label(self.FrameSide, text="Settings for Side:", font=("Roboto", 12), bg='white')
        self.LabelSide.pack(anchor='w',padx=20,side=LEFT)

        self.varSide = IntVar()

        self.RadioSideYes = Radiobutton(self.FrameSide, text="Yes", value=1, variable=self.varSide, font=("Roboto", 12),
                                         bg='white',command=lambda : self.controller.update_param('Param_Side',1))
        self.RadioSideYes.pack(side=LEFT)

        self.RadioSideNo = Radiobutton(self.FrameSide, text="No", value=0, variable=self.varSide, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Side',0))
        self.RadioSideNo.pack(side=LEFT)

        self.LabelChooseSD = Label(self.FrameSide, text='Choose "No" if you do not wish the program to check that identifiable remains are lateralised', font=("Roboto", 12), bg='white')
        self.LabelChooseSD.pack(padx=10)

        if self.controller.put_Param('Param_Side') == 1:
            self.RadioSideYes.select()
        else:
            self.RadioSideNo.select()


        self.FrameTapho = Frame(self.FrameBodySetting, bg='white',bd=1,relief=SOLID)
        self.FrameTapho.pack(anchor='w',pady=15)

        self.LabelTitre = Label(self.FrameTapho , text="Settings for taphonomic analyses", font=("Roboto", 12), bg='white',state='disabled')
        self.LabelTitre.pack(anchor='w',padx=20)

        self.varTapho = IntVar()

        self.RadioTapho1 = Radiobutton(self.FrameTapho, text="1", value=1, variable=self.varTapho, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Tapho',1),state='disabled')
        self.RadioTapho1.pack(padx=(0,10),anchor='w')
    
        self.RadioTapho2 = Radiobutton(self.FrameTapho, text="2", value=2, variable=self.varTapho, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Tapho',2),state='disabled')
        self.RadioTapho2.pack(padx=(0,10),anchor='w')

        self.RadioTapho3 = Radiobutton(self.FrameTapho, text="3", value=3, variable=self.varTapho, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Tapho',3),state='disabled')
        self.RadioTapho3.pack(padx=(0,10),anchor='w')

        self.RadioTapho4 = Radiobutton(self.FrameTapho, text="4", value=4, variable=self.varTapho, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Tapho',4),state='disabled')
        self.RadioTapho4.pack(padx=(0,10),anchor='w')

        self.FrameNone = Frame(self.FrameTapho,bg='white')
        self.FrameNone.pack(anchor='w')

        self.RadioTaphoN = Radiobutton(self.FrameNone, text="None", value=0, variable=self.varTapho, font=("Roboto", 12),
                                        bg='white',command=lambda : self.controller.update_param('Param_Tapho',0),state='disabled')
        self.RadioTaphoN.pack(anchor='w',side=LEFT)

        self.LabelTExpli = Label(self.FrameNone , text="Select 'None' if you do not wish to record taphonomic data", font=("Roboto", 12), bg='white',state='disabled')
        self.LabelTExpli.pack(padx=10,side=LEFT,anchor='w')

        self.LabelTExpli2 = Label(self.FrameTapho, text="Set the minimal length (in cm) above which the precise taphonomic data \r(bone surface modifications, etc.) is entered \r", font=("Roboto", 12), bg='white',state='disabled')
        self.LabelTExpli2.pack(padx=10,anchor='w')

        valDefaut = self.controller.put_Param('Param_Tapho')

        if valDefaut == 1:
            self.RadioTapho1.select()
        elif valDefaut == 2:
            self.RadioTapho2.select()
        elif valDefaut == 3:
            self.RadioTapho3.select()
        elif valDefaut == 4:
            self.RadioTapho4.select()
        else :
            self.RadioTaphoN.select()



        


        """
        self.FrameColor = Frame(self, bg='white')
        self.FrameColor.pack(anchor='w',padx=30)

        self.labelChoix = Label(self.FrameColor, text='Group of values used in the "BoneColor" variable:', font=("Roboto", 12), bg='white')
        self.labelChoix.pack(side=LEFT)

        listeProduits=["Laptop", "Imprimante","Tablette","SmartPhone"]

        self.listeCombo = ttk.Combobox(self.FrameColor, values=listeProduits)
        self.listeCombo.current(0)
        self.listeCombo.config(font=("Roboto", 12))
        self.listeCombo.pack(side=LEFT)

        """