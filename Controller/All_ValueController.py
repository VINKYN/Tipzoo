import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from Controller.getDatabase import get_database_path

from Model.BaseModel import BaseModel
from View.Home import HomeInterface
from View.All_Value import AllValueInterface

from Model.SpatialModel import SpatialModel
from Model.Skel_NDEModel import SkelNdeModel

import sqlite3




class AllValueController:
    def __init__(self,master=None,label=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.label = label
        self.bulk = bulk
        self.skel_nde = SkelNdeModel(self.path)
        print(self.bulk)
        self.spatial = SpatialModel(self.path)


    def show_home_page(self):
        # Supprimer tous les widgets de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.HomeController import HomeController
        # Créer et afficher la page des paramètres
        home_controller = HomeController(self.master,self.bulk)
        home_controller = HomeInterface(self.master, home_controller)
        home_controller.pack(expand=True, fill='both')

    def delete(self):
        self.spatial.deleteAll()
        # Supprimer tous les widgets de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.All_ValueController import AllValueController
        # Créer et afficher la page des paramètres
        all_controller = AllValueController(self.master,'Spatial',self.bulk)
        all_interface = AllValueInterface(self.master, all_controller,'Spatial')
        all_interface.pack(expand=True, fill='both')


    def get_column(self,label):
        if label == 'Skel_NDE':
            data , col =self.skel_nde.All_NDE()
            listeC =[]
            for c in col:
                listeC.append(c[0])
        else:
            column = self.base.get_Pragma(label)
            listeC = []
            for i in column :
                listeC.append(i[0])
        return listeC
    
    def getAll(self,label):
        if label == 'Skel_NDE':
            data , col =self.skel_nde.All_NDE()
            return data
        else:
            return self.base.get_all(label)
