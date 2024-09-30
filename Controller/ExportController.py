import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from Controller.getDatabase import get_database_path

from Model.BaseModel import BaseModel
from Model.ParamModel import ParamModel
from Model.SpeciesModel import SpeciesModel
from Model.SkelModel import SkelModel
from Model.BoneColorModel import BoneColorModel
from Model.TeethModel import TeethModel
from Model.Skel_NDEModel import SkelNdeModel

from View.Home import HomeInterface
from View.Base.BoneColor import BoneColorInterface
from View.Base.Base import BaseInterface
from Model.SpatialModel import SpatialModel

from View.Home import HomeInterface

import pandas as pd

import sqlite3
import datetime




class ExportController:
    def __init__(self,master=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.param = ParamModel(self.path)
        self.bulk = bulk

        self.base = BaseModel(self.path)
        self.species = SpeciesModel(self.path)
        self.species = SpeciesModel(self.path)
        self.spatial = SpatialModel(self.path)
        self.boneColor =BoneColorModel(self.path)
        self.teeth = TeethModel(self.path)
        self.skel =SkelModel(self.path)
        self.skel_nde = SkelNdeModel(self.path)

        self.export="Export"


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


    def getspe(self):
        return self.species.getAll()




    def export_species(self):
       columns = [
    "pk_ID", "fieldID", "SubID", "Size", "PlottedScreen", "Obs", "SPATIAL::Square_field",
    "SPATIAL::Dec", "SPATIAL::USfield", "SPATIAL::Group1", "SPATIAL::Group2",
    "SPATIAL::Group3", "SPATIAL::X", "SPATIAL::Y", "SPATIAL::Z", "SPATIAL::Year",
    "SPECIES::Taxon", "SPECIES::CheckImprove", "SPECIES::ObsTaxon", "SKEL::Anat_Class",
    "SKEL::Anat", "SKEL::Anat_Detail", "SKEL::Frag", "SKEL::AgeCort", "SKEL::Spongy",
    "RemID", "REFITS::RemType"]
       
       data = self.base.ExportSpecies()

       dataframe=pd.DataFrame(data,columns=columns)

       dataframe.to_excel(self.export+"/Species.xlsx",index=False)

       messagebox.showinfo(title="Export Species", message="EXPORT DONE \rYou can find the file in the Export repertory")


    def export_teeth(self,val):
       columns = [
      "BASE::pk_ID", "BASE::fieldID", "BASE::SubID", "SPATIAL::USfield",
    "SPATIAL::Group1", "SPATIAL::Group2", "SPATIAL::Group3", "SPECIES::Taxon",
    "SKEL::Anat", "pk_teethID", "LowerUpper",
    "Dentition", "Type", "Class", "Number", "Side", "OccSup50", "FR",
    "Portion", "UW_Crown", "UW_Root", "UW_RootResorp", "UW_AgeClass", "CH"]
       
       if val :
        data = self.base.ExportTeethval(val)
       else:
        data = self.base.ExportTeeth()

       dataframe=pd.DataFrame(data,columns=columns)

       dataframe.to_excel(self.export+"/Teeth.xlsx",index=False)
       messagebox.showinfo(title="Export Teeth", message="EXPORT DONE \rYou can find the file in the Export repertory")


    def export_NDE(self,val):
      columns1 =['BASE::pk_ID', 'BASE::fieldID', 'BASE::SubID', 'SPATIAL::USfield', 'SPATIAL::Group1', 
                 'SPATIAL::Group2', 'SPATIAL::Group3', 'SPECIES::Taxon', 'SKEL::Anat_Class', 'SKEL::Anat','SKEL::Anat_Detail','SKEL::AgeCort', 'SKEL::AgeFus',]
      columns2=[
                  'Ldmk_17', 'Ldmk_30', 'Ldmk_88mesRib', 'Ldmk_89mesRad', 'Ldmk_90mesMan', 
                 'Ldmk_91mesFem', 'Ldmk_01', 'Ldmk_02', 'Ldmk_03', 'Ldmk_04', 'Ldmk_05', 'Ldmk_06', 'Ldmk_07', 
                 'Ldmk_08', 'Ldmk_09', 'Ldmk_10', 'Ldmk_11', 'Ldmk_12', 'Ldmk_13', 'Ldmk_14', 'Ldmk_15', 'Ldmk_16', 
                 'Ldmk_18', 'Ldmk_19', 'Ldmk_20', 'Ldmk_21', 'Ldmk_22', 'Ldmk_23', 'Ldmk_24', 'Ldmk_25', 'Ldmk_26', 
                 'Ldmk_27', 'Ldmk_28', 'Ldmk_29', 'Ldmk_31', 'Ldmk_31a', 'Ldmk_31b', 'Ldmk_32', 'Ldmk_33', 'Ldmk_34', 
                 'Ldmk_35', 'Ldmk_36', 'Ldmk_37', 'Ldmk_38', 'Ldmk_38tymp', 'Ldmk_39', 'Ldmk_40', 'Ldmk_40basi', 'Ldmk_40cera', 
                 'Ldmk_40thyr', 'Ldmk_41', 'Ldmk_42', 'Ldmk_43', 'Ldmk_44', 'Ldmk_45', 'Ldmk_46', 'Ldmk_47', 'Ldmk_48', 'Ldmk_49', 
                 'Ldmk_50', 'Ldmk_51', 'Ldmk_52', 'Ldmk_53', 'Ldmk_54', 'Ldmk_55', 'Ldmk_56', 'Ldmk_57', 'Ldmk_58', 'Ldmk_59', 'Ldmk_60', 
                 'Ldmk_61', 'Ldmk_62', 'Ldmk_63', 'Ldmk_63cen', 'Ldmk_63pis', 'Ldmk_63rad', 'Ldmk_64', 'Ldmk_64cap', 'Ldmk_64tra', 'Ldmk_64trapd', 
                 'Ldmk_65', 'Ldmk_66', 'Ldmk_67', 'Ldmk_68', 'Ldmk_69', 'Ldmk_70', 'Ldmk_71', 'Ldmk_71de', 'Ldmk_71ds', 'Ldmk_71pe', 'Ldmk_71ps', 
                 'Ldmk_72', 'Ldmk_73', 'Ldmk_74', 'Ldmk_75', 'Ldmk_76', 'Ldmk_77', 'Ldmk_77acc', 'Ldmk_77cub', 'Ldmk_77nav', 'Ldmk_78', 'Ldmk_78first', 
                 'Ldmk_78int', 'Ldmk_78med', 'Ldmk_78sec', 'Ldmk_79', 'Ldmk_80', 'Ldmk_81', 'Ldmk_82', 'Ldmk_83', 'Ldmk_84', 'Ldmk_85', 'Ldmk_86', 'Ldmk_87', 
                 'Ldmk_92ph1', 'Ldmk_93ph2', 'Ldmk_94ph3']

      if val :
        dataNDE = self.skel_nde.val_NDE(val)
        data = self.base.ExportNDEval(val)
      else:
        dataNDE ,c= self.skel_nde.All_NDE()
        data = self.base.ExportNDE()

      dataD = pd.DataFrame(data,columns=columns1)
      

      for col in columns2:
         dataD[col]=None

      for nde in dataNDE:
         for dd,d in dataD.iterrows():
             if d["BASE::pk_ID"] == nde[0]:
               dataD.loc[dd, nde[1]] = nde[2]
               print(nde[0])

            #if d[1] == nde[0]:
               #print(nde)

      print(dataD)
      dataD.to_excel(self.export+"/NDEData.xlsx",index=False)

      

      """dataD = pd.DataFrame(data)
      print(dataD)
      dataframe=pd.DataFrame(data,columns=columns)
      d =dataframe.append(dataD,ignore_index = True)"""





      
      
      

       #dataframe=pd.DataFrame(data,columns=columns)

       #dataframe.to_excel(self.export+"/NDE .xlsx",index=False)

      #messagebox.showinfo(title="Export NDE", message="EXPORT DONE \rYou can find the file in the Export repertory")


    def export_All_CSV(self):
        date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        pos = self.path.removesuffix('.sqlite3').removeprefix('Database/')
        path = self.export+"/"+pos+"_"+date
        os.mkdir(path)


        data , col =self.base.All_Base()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/Base.csv",index=False)

        data , col =self.species.All_Species()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/Species.csv",index=False)

        data , col =self.boneColor.All_Color()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/BoneColor.csv",index=False)


        data , col =self.skel.All_Skel()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/Skel.csv",index=False)

        data , col =self.spatial.All_Spatial()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/Spatial.csv",index=False)

        data , col =self.teeth.All_teeth()
        listecol =[]
        for c in col:
           listecol.append(c[0])
           
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/Teeth.csv",index=False)

        data , col =self.skel_nde.All_NDE()
        listecol =[]
        for c in col:
         listecol.append(c[0])
         
        dataframeBase = pd.DataFrame(data,columns=listecol)
        dataframeBase.to_csv(path+"/NDE.csv",index=False)

        messagebox.showinfo(title="Export All Data in CSV", message="EXPORT DONE \rYou can find the all the file in the Export repertory")




    def export_All_XSLX(self):
      date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
      pos = self.path.removesuffix('.sqlite3').removeprefix('Database/')
      path = self.export+"/"+pos+"_"+date
      os.mkdir(path)


      data , col =self.base.All_Base()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/Base.xlsx",index=False)

      data , col =self.species.All_Species()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/Species.xlsx",index=False)

      data , col =self.boneColor.All_Color()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/BoneColor.xlsx",index=False)


      data , col =self.skel.All_Skel()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/Skel.xlsx",index=False)

      data , col =self.spatial.All_Spatial()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/Spatial.xlsx",index=False)

      data , col =self.teeth.All_teeth()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/Teeth.xlsx",index=False)

      data , col =self.skel_nde.All_NDE()
      listecol =[]
      for c in col:
         listecol.append(c[0])
         
      dataframeBase = pd.DataFrame(data,columns=listecol)
      dataframeBase.to_excel(path+"/NDE.xlsx",index=False)

      messagebox.showinfo(title="Export All Data in EXCEL", message="EXPORT DONE \rYou can find the all the file in the Export repertory")
      



