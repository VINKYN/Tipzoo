import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from Controller.getDatabase import get_database_path

from Model.BaseModel import BaseModel
from Model.BoneColorModel import BoneColorModel
from View.Base.Base import BaseInterface
from View.Base.BoneColor import BoneColorInterface
from tkinter import colorchooser
from tkinter import filedialog

from PIL import Image, ImageTk, ImageColor,ImageStat

import sqlite3

from collections import Counter




class BoneColorController:
    def __init__(self,master=None,id=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.boneColor =BoneColorModel(self.path)
        self.id = id
        self.bulk = bulk


    def show_Base(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        base_controller = BaseController(self.master,self.id,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')

    def show_color_page(self):
        # Supprimer tous les widgets de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.BoneColorController import BoneColorController
        # Créer et afficher la page des paramètres
        bone_controller = BoneColorController(self.master,self.id,self.bulk)
        bone_interface = BoneColorInterface(self.master, bone_controller)
        bone_interface.pack(expand=True, fill='both')


    def get_all_color(self):
        return self.boneColor.get_all()
    
    def insert_Color(self):
        self.boneColor.insert_Color()
        self.show_color_page()

    def delete_Color(self,id):
        confirmation = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet élément ?")
        if confirmation == True :
            self.boneColor.delete(id)
            self.show_color_page()

    def choose_color(self, entry, button, id):
        color = colorchooser.askcolor(title='Select a color')
        if color[1]:
            entry.configure(state='normal')
            entry.delete(0, END)
            entry.insert(0, color[1])
            entry.configure(state='disabled')
            button.configure(bg=color[1])
            self.boneColor.update_column('Color_Hexcode', id, color[1])

    def update_name(self,name,id):
        self.boneColor.update_column('Color_Value',id,name)


    def get_path_img(self,id,label):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg"), ("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        self.boneColor.update_column('Color_Path',id,file_path)
        image = Image.open(file_path)
        image = image.resize((200, 200))  # Redimensionner l'image si nécessaire
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo


