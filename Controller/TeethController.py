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
from Model.TeethModel import TeethModel


from View.Home import HomeInterface
from View.Base.BoneColor import BoneColorInterface
from View.Base.Base import BaseInterface

from View.Species.Species import Species

from View.Skull.Skel.Teeth import TeethInterface

import sqlite3




class TeethController:
    def __init__(self,master=None,id=None,id2=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.param = ParamModel(self.path)
        self.species = SpeciesModel(self.path)
        self.boneColor =BoneColorModel(self.path)
        self.skel = SkelModel(self.path)
        self.skel_nde = SkelNdeModel(self.path)
        self.teeth = TeethModel(self.path)
        self.id = id
        self.id2 = id2

        self.bulk = bulk



    def show_Skel_page(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

        id = self.skel.get_Base_Id(self.id2)[0][0]
        
        from Controller.SkelController import SkellController
        # Créer et afficher la page des paramètres
        skel_controller = SkellController(self.master,id,self.bulk)  # Importation à l'intérieur de la méthode
        skel_interface = TeethInterface(self.master, skel_controller,self.bulk)  # Passer l'instance du contrôleur
        skel_interface.pack(expand=True, fill='both')

    def update_combo(self,colonne,val):
        self.teeth.update_col(colonne,val,self.id)

    def getFr(self):
        return self.teeth.get_column(self.id,'Teeth_FR')[0][0]
    
    def updateFr(self,val):
        self.teeth.update_col('Teeth_FR',val,self.id)


    def getLowerUpper(self):
        val = self.teeth.get_column(self.id,'Teeth_LowerUpper')[0][0]
        val_lower = ['Lower','Upper','?']
        for i in range(len(val_lower)):
            if val == val_lower[i]:
                return i
            
    def getSide(self):
        val = self.teeth.get_column(self.id,'Teeth_Side')[0][0]
        val_Side = ["Left","Right","?"]
        for i in range(len(val_Side)):
            if val == val_Side[i]:
                return i
            
    def getType(self):
        val = self.teeth.get_column(self.id,'Teeth_Type')[0][0]
        val_Type = ['ANTERIOR','Cheek','?']
        for i in range(len(val_Type)):
            if val == val_Type[i]:
                return i
            
    def getDentition(self):
        val = self.teeth.get_column(self.id,'Teeth_Dentition')[0][0]
        val_Dentition = ['Permanent','Deciduous','?']
        for i in range(len(val_Dentition)):
            if val == val_Dentition[i]:
                return i
            
    def getClass(self):
        val = self.teeth.get_column(self.id,'Teeth_Class')[0][0]
        val_Class = ['Incisor','Canine','Premolar','Molar','Postcanine','?']
        for i in range(len(val_Class)):
            if val == val_Class[i]:
                return i
            
    def getNumber(self):
        val = self.teeth.get_column(self.id,'Teeth_Number')[0][0]
        val_Number = ['1','2','3','4','1-2','3-4','NID']
        for i in range(len(val_Number)):
            if val == val_Number[i]:
                return i
            
    def getPortion(self):
        string =self.teeth.get_column(self.id,'Teeth_Portion')[0][0]
        p1=""
        p2=""
        if string != None:
            lettres = string.split(',')
            if 'CRN' in lettres:
                p1='CRN'
            if 'ROOT' in lettres:
                p2='ROOT'
        return p1,p2
    
    def updatePortion(self, val, check):
        string = self.teeth.get_column(self.id,'Teeth_Portion')[0][0]
        if string is None:
            string = ""
        if check in ['CRN','ROOT']:
            if len(val) == 0:
                string = string.replace(check+',','')
            else:
                string += val+','

        self.teeth.update_col('Teeth_Portion',string,self.id)
            

    def getSurf(self):
        return self.teeth.get_column(self.id,'Teeth_OccSup50')[0][0]
    
    def updateSurf(self,val):
        if val == 0:
            val = None;
        self.teeth.update_col('Teeth_OccSup50',val,self.id)


    def getAge(self):
        return self.teeth.get_column(self.id,'Teeth_UW_AgeClass')[0][0]
    
    def updateAge(self,val):
        self.teeth.update_col('Teeth_UW_AgeClass',val,self.id)

    def getCr(self):
        return self.teeth.get_column(self.id,'Teeth_CH')[0][0]

    def updateCr(self,val):
        self.teeth.update_col('Teeth_CH',val,self.id)

    def getCrown(self):
        return self.teeth.get_column(self.id,'Teeth_UW_Crown')[0][0]

    def updateCrown(self,val):
        self.teeth.update_col('Teeth_UW_Crown',val,self.id)


    def getRoot(self):
        return self.teeth.get_column(self.id,'Teeth_UW_Root')[0][0]

    def updateRoot(self,val):
        self.teeth.update_col('Teeth_UW_Root',val,self.id)

    def getRootRe(self):
        return self.teeth.get_column(self.id,'Teeth_UW_RootResorp')[0][0]

    def updateRootRe(self,val):
        self.teeth.update_col('Teeth_UW_RootResorp',val,self.id)
        

    def updatePortionNone(self):
        self.teeth.update_col('Teeth_Portion',None,self.id)


    
