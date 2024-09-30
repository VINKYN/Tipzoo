import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from Controller.getDatabase import get_database_path

from Model.ParamModel import ParamModel
from View.Home import HomeInterface

import sqlite3




class SettingsController:
    def __init__(self,master=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.param = ParamModel(self.path)
        self.bulk = bulk


    def show_home_page(self):
        # Supprimer tous les widgets de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.HomeController import HomeController
        # Créer et afficher la page des paramètres
        home_controller = HomeController(self.master,self.bulk)
        home_interface = HomeInterface(self.master, home_controller)
        home_interface.pack(expand=True, fill='both')

    def put_Param(self,colonne):
        return self.param.get_params(colonne)[0][0]

    def update_param(self,colonne,value):
        print(colonne,value)
        self.param.update_Param(colonne,value)


    def get_database(self):
            listeOs = os.listdir('Database')
            L=[]
            for l in listeOs :
                if l != 'path.txt':
                    L.append(l.removesuffix('.sqlite3'))
            return L
        
    def get_current(self,val):
            pos = val.index(self.path.removesuffix('.sqlite3').removeprefix('Database/'))
            return pos

   