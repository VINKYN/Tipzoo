from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageColor
from tkinter import colorchooser
import os


class BoneColorInterface(Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.configure(bg='white')

        font_button = ("Helvetica 13 bold")
        font_ecriture = ("Helvetica 10")


        color_button = '#F2E2CE'

        color_bleu ='#b9e2f9'

        color_police ='#1b1b1b'

        # Appliquer la police Roboto en taille 12
        self.Frame1 = Frame(self, bg='#b9e2f9')
        self.Frame1.pack(fill='x', side=TOP, ipady=20)  # Ajout de padx et pady pour l'espacement

        self.ButtonMenu = Button(self.Frame1, text="Back", width=15, height=2, background='white',
                                 bd=0, font=font_button, command=self.controller.show_Base)
        self.ButtonMenu.pack(side=LEFT, padx=20)

        self.ButtonAdd = Button(self.Frame1, text="Add", width=15, height=2, background='white',
                                bd=0, font=font_button,command=self.controller.insert_Color)
        self.ButtonAdd.pack(side=LEFT, padx=20)




        self.Frame2 = Frame(self, bg='white')
        self.Frame2.pack(expand=True, fill=BOTH)

        self.Canvas = Canvas(self.Frame2, bg='white')  # Création du Canvas
        self.Canvas.pack(side=LEFT, fill=BOTH, expand=True)  # Remplissage du Canvas sur toute la Frame1

        self.Scrollbar = Scrollbar(self.Frame2, orient=VERTICAL, command=self.Canvas.yview)  # Scrollbar
        self.Scrollbar.pack(side=RIGHT, fill=Y)

        self.Canvas.config(yscrollcommand=self.Scrollbar.set) 
        self.Canvas.bind('<Configure>',lambda e : self.Canvas.config(scrollregion=self.Canvas.bbox('all')))

        self.Frame3 = Frame(self.Canvas, bg=color_button, bd=1)
        self.Canvas.create_window((0, 0), window=self.Frame3,width=self.winfo_screenwidth())  


        listeColor = self.controller.get_all_color()
        for id, name, hex_color,path in listeColor:
            self.Frame4 = Frame(self.Frame3,bg='white')
            self.Frame4.pack(expand=True, fill='both',pady=15,padx=15)

            self.left_frame = Frame(self.Frame4, bg='white')
            self.left_frame.pack(side=LEFT, padx=10, pady=10,expand=True)

            self.FrameName = Frame(self.left_frame,bg='white')
            self.FrameName.pack(anchor='w')

            self.labelName = Label(self.FrameName, text="Color Name ", font=font_ecriture)
            self.labelName.pack(anchor='w', padx=5, pady=5, side=LEFT)

            #self.EntryName_Val = StringVar()

            self.entryName = Entry(self.FrameName, font=font_ecriture)
            self.entryName.pack(padx=5, pady=5, side=LEFT)
            self.entryName.insert(0, str(name))

            #self.EntryName_Val.trace_add('write',lambda event, entry=self.entryName, id=id: self.controller.update_name(entry.get(), id))
            self.entryName.bind('<FocusOut>', lambda event, entry=self.entryName, id=id: self.controller.update_name(entry.get(), id))

            self.buttonCC = Button(self.FrameName, text="", font=font_button, bg=hex_color, width=15, bd=0)
            self.buttonCC.pack(padx=5, pady=5, side=LEFT)

            self.FrameHex = Frame(self.left_frame,bg='white')
            self.FrameHex.pack(anchor='w')

            self.labelHex = Label(self.FrameHex, text="Hexadecimal Code", font=font_ecriture)
            self.labelHex.pack(anchor='w', padx=5, pady=5, side=LEFT)

            self.entryHex = Entry(self.FrameHex, font=font_ecriture)
            self.entryHex.pack(padx=5, pady=5, side=LEFT)
            self.entryHex.insert(0, str(hex_color))
            self.entryHex.configure(state='disabled')

            self.buttonC = Button(self.FrameHex, text="Color", font=font_button, bg=color_police ,fg=color_button,relief='solid',bd=0,
                 command=lambda entry=self.entryHex, button=self.buttonCC, id=id: self.controller.choose_color(entry, button, id))
            self.buttonC.pack(padx=5, pady=5, side=LEFT)

            self.buttonDel = Button(self.left_frame,text='Delete',font=font_button,bg=color_police,fg=color_button,
                                    relief='solid',bd=0,
                                    command=lambda id=id: self.controller.delete_Color(id))
            self.buttonDel.pack(padx=5,pady=5,anchor='w')

            self.right_frame = Frame(self.Frame4, bg=color_button,width=200,height=200)
            self.right_frame.pack(side=LEFT, padx=10, pady=10,expand=True)

            self.image_label = None

            self.image_frame = Frame(self.right_frame, bg=color_button,width=200, height=200)
            self.image_frame.pack(side=BOTTOM, padx=10, pady=10)
            self.image_label = Label(self.image_frame,bg='white')

            if path :
                if os.path.isfile(path):
                    self.image = Image.open(path)
                    self.image = self.image.resize((200, 200))  
                    self.photo = ImageTk.PhotoImage(self.image)
                    self.image_label.configure(image=self.photo)
                    self.image_label.image = self.photo
                else:
                    self.image_label.configure(text="Image not found \rThe image has changed directory",font=font_ecriture)

            self.image_label.pack()

            self.button = Button(self.right_frame, text="Image", font=font_button,relief=SOLID,bd=0,
                                    command=lambda label=self.image_label ,id=id: self.controller.get_path_img(id,label))
            self.button.pack(side=TOP,padx=5, pady=5)

            


    

