from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk



class ExportInterface(Frame):
    def __init__(self, master=None,controller= None,bulk=None):
        super().__init__(master)

        self.master = master
        self.configure(bg='white')
        self.pack(expand=True, fill='both')
        self.controller = controller
        self.bulk =bulk


        self.Frame1 = Frame(self,bg='#b9e2f9')
        self.Frame1.pack(anchor='n',fill='x', side=TOP)

        self.ButtonMenu = Button(self.Frame1 , text="Home",width=15 ,height=2, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='white',font=("Roboto 12"),
                                   command=self.controller.show_home_page)
        self.ButtonMenu.pack(side=LEFT,pady=20,padx=20)

        self.FrameTaxon = Frame(self.Frame1,bg='#b9e2f9')
        self.FrameTaxon.pack(pady=20)

        self.LabelTaxon = Label(self.FrameTaxon, text="Select Taxon for export \r(or leave empty to export all)",
                                font=("Roboto 12"),bg='#b9e2f9')
        self.LabelTaxon.pack(side=LEFT)

        val = self.controller.getspe()
        self.Vartax = StringVar()

        self.EntryTaxon = ttk.Combobox(self.FrameTaxon,font=("Roboto 12"),values=val,textvariable=self.Vartax)
        self.EntryTaxon.pack(ipady=10,side=RIGHT)

        self.Frame2 =Frame(self , bg='white',)
        self.Frame2.pack(fill='both',expand=True,padx=50,pady=30)

        self.FrameAll = Frame(self.Frame2, bg='white')
        self.FrameAll.pack(side=LEFT, padx=50, fill='both', expand=True ,)

        self.ButtonCSV = Button(self.FrameAll , text="Export ALL DATA to .csv \n(each table in a separate file)",width=20 ,height=10, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),
                                   command=lambda:self.controller.export_All_CSV())
        self.ButtonCSV.pack(pady=20,ipadx=20)

        self.ButtonExcel = Button(self.FrameAll , text="Export ALL DATA to Excel \r(each table in a separate file)",width=20 ,height=10, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),
                                   command=lambda:self.controller.export_All_XSLX())
        self.ButtonExcel.pack(pady=20,ipadx=20)

        self.FrameST = Frame(self.Frame2,bg='white')
        self.FrameST.pack(side=LEFT, padx=50, fill='both', expand=True)

        self.ButtonS = Button(self.FrameST , text="Export Species DATA \r(with anat and spatial info)",width=20 ,height=10, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),
                                   command=lambda:self.controller.export_species())
        self.ButtonS.pack(pady=20,ipadx=40)

        self.ButtonT = Button(self.FrameST , text="Export Tapho DATA \n (with species, anat and spatial info)",width=20 ,height=10, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),state='disabled')
        self.ButtonT.pack(pady=20,ipadx=40)

        self.FrameCNT = Frame(self.Frame2,bg='white')
        self.FrameCNT.pack(side=LEFT, padx=(50, 0), fill='both', expand=True)   

        self.ButtonC = Button(self.FrameCNT , text="Export CUT DATA",width=20 ,height=5, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),state='disabled')
        self.ButtonC.pack(pady=20)

        self.ButtonN = Button(self.FrameCNT , text="Export NDE DATA",width=20 , height=5,background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),
                                   command=lambda:self.controller.export_NDE(self.Vartax.get()))
        self.ButtonN.pack(pady=20)

        self.ButtonTe = Button(self.FrameCNT , text="Export Teeth DATA",width=20 ,height=5, background='#f0f0f0' 
                                   ,relief='solid',bd=1,activebackground='#b9e2f9',font=("Roboto 12"),
                                   command=lambda:self.controller.export_teeth(self.Vartax.get()))
        self.ButtonTe.pack(pady=20)

        self.FrameMessage = Frame(self,bg='#b9e2f9')
        self.FrameMessage.pack(fill='both',side=BOTTOM)

        self.LabelMessage = Label(self.FrameMessage,text="After clicking one of the buttons above, files will be created in the /export folder",
                                  font=("Roboto 12"),bg='#b9e2f9')
        self.LabelMessage.pack(pady=20)


