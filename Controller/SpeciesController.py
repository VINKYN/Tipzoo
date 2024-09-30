import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from Controller.getDatabase import get_database_path

from Model.BaseModel import BaseModel
from Model.ParamModel import ParamModel
from Model.SpeciesModel import SpeciesModel
from Model.BoneColorModel import BoneColorModel
from Model.SkelModel import SkelModel
from Model.Skel_NDEModel import SkelNdeModel


from View.Home import HomeInterface
from View.Base.BoneColor import BoneColorInterface
from View.Base.Base import BaseInterface
from View.Species.Species import Species

from View.Skull.Skel.Teeth import TeethInterface
from View.Skull.LBN.LBN import LBNInterface
from View.Skull.FBN.FNB import FNBInterface
from View.Skull.SBN.SBN import SBNInterface
from View.Skull.BIRD.Bird import BirdInterface
from View.Skull.NMB.NMB import NMBInterface
from View.Skull.NID.NID import NIDInterface

import sqlite3




class SpeciesController:
    def __init__(self,master=None,id=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.param = ParamModel(self.path)
        self.species = SpeciesModel(self.path)
        self.boneColor =BoneColorModel(self.path)
        self.skel = SkelModel(self.path)
        self.skel_nde = SkelNdeModel(self.path)
        self.id = id
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

    def show_base_page(self):
        # Supprimer tous les widgets de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        base_controller = BaseController(self.master,self.id,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')


    def show_skel_page(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

        # Afficher la vue HomeInterface
        from Controller.SkelController import SkellController
        
        skel_controller = SkellController(self.master,self.id,self.bulk)

        cat =self.skel.getcat(self.id)[0][0]
        if cat == "SBN":
            sbn_interface = SBNInterface(self.master, skel_controller,self.bulk)
            sbn_interface.pack(expand=True, fill='both')
            
        if cat =="FNB":
            fnb_interface = FNBInterface(self.master, skel_controller,self.bulk)
            fnb_interface.pack(expand=True, fill='both')

        if cat =="Skull":
            skull_interface = TeethInterface(self.master, skel_controller,self.bulk)
            skull_interface.pack(expand=True, fill='both')

        if cat =="LBN":
            lBN_interface = LBNInterface(self.master, skel_controller,self.bulk)
            lBN_interface.pack(expand=True, fill='both')
            
        if cat =="Bird":
            bird_interface = BirdInterface(self.master, skel_controller,self.bulk)
            bird_interface.pack(expand=True, fill='both')
            
        if cat =="NMB":
            nmb_interface = NMBInterface(self.master, skel_controller,self.bulk)
            nmb_interface.pack(expand=True, fill='both')
            
        if cat =="NID":
            nid_interface = NIDInterface(self.master, skel_controller,self.bulk)
            nid_interface.pack(expand=True, fill='both')

    def show_spe_page(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

        from Controller.SpeciesController import SpeciesController

        species_controller = SpeciesController(self.master,self.id,self.bulk)
        species_interface = Species(self.master, species_controller,self.bulk)
        species_interface.pack(expand=True, fill='both')


    def get_menu(self):
        b = self.id
        sk = self.skel.get_By_Id(self.id)
        s = self.species.get_By_Id(self.id)
        return b,sk ,s
    
    def getspe(self):
        return self.species.get_column(self.id,'Species_Taxon')[0][0]
    
    def updateTaxon(self,val):
        self.species.update_taxon(self.id,val)

    def getObs(self):
        return self.species.get_column(self.id,'Species_ObsTaxon')[0][0]

    def updateObs(self,val):
        self.species.update_Obs(self.id,val)

    def updateCheckImprove(self,val, check):
        string = self.species.getCheck(self.id)[0][0]
        if string is None:
            string = ""
        if check in ['To Check','To Improve']:
            if len(val) == 0:
                string = string.replace(check+',','')
            else:
                string += val+','

        self.species.update_CI(string,self.id)


    def checkimprove(self):
        string = self.species.getCheck(self.id)[0][0]
        Tc=''
        Ti=''
        if string != None:
            lettres = string.split(',')
            if 'To Check' in lettres:
                Tc='To Check'
            if 'To Improve' in lettres:
                Ti='To Improve'
        return Tc ,Ti 
