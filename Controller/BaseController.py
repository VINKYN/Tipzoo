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
from Model.RefitsModel import RefitsModel


from View.Home import HomeInterface
from View.Base.BoneColor import BoneColorInterface
from View.Base.Base import BaseInterface
from Model.SpatialModel import SpatialModel
from Model.SkelModel import SkelModel
from Model.Skel_NDEModel import SkelNdeModel
from Model.TeethModel import TeethModel


from View.Skull.Skel.Teeth import TeethInterface
from View.Skull.LBN.LBN import LBNInterface
from View.Skull.FBN.FNB import FNBInterface
from View.Skull.SBN.SBN import SBNInterface
from View.Skull.BIRD.Bird import BirdInterface
from View.Skull.NMB.NMB import NMBInterface
from View.Skull.NID.NID import NIDInterface
from View.Species.Species import Species


import sqlite3




class BaseController:
    def __init__(self,master=None,id=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.param = ParamModel(self.path)
        self.species = SpeciesModel(self.path)
        self.spatial = SpatialModel(self.path)
        self.boneColor =BoneColorModel(self.path)
        self.refits = RefitsModel(self.path)
        self.skel_nde = SkelNdeModel(self.path)
        self.skel = SkelModel(self.path)
        self.teeth = TeethModel(self.path)
        

        self.skel =SkelModel(self.path)
        
        self.id = id
        self.bulk = bulk


    def  delete_no_id(self):
        id = self.id
        confirmation = TRUE

        if not self.base.get_column("Base_ID",id)[0][0] :
            confirmation = messagebox.askyesno("Confirmation", "This fragment is missing a Field ID,any associated information will be deleted :( ")
            if confirmation == True :
                if self.skel.get_id(id) :
                    idskel = self.skel.get_id(id)[0][0]

                    if self.skel_nde.getNde(idskel):
                        self.skel_nde.delete_Skel_Nde_All(idskel) 

                    if self.teeth.get(idskel):
                        self.teeth.delete_all(idskel)

                    self.skel.delete(id)

                if self.species.get(id):
                        self.species.delete(id)

                if self.refits.get(id):
                        self.refits.delete(id)

                self.base.delete(id)
        return confirmation
    

    def id_no_skel(self):
        id = self.id

        if not self.base.get_column("Base_ID",id)[0][0] :
            messagebox.showinfo("Confirmation", "This fragment is missing a Field ID")
            return True
        else:
            return False
            




    def show_home_page(self):

        #if self.message_field():
            # Supprimer tous les widgets de la fenêtre principale
        #self.base.delete(self.id)
        if self.delete_no_id() == TRUE:

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


    def show_Base_pre(self):
        self.delete_no_id()
        if self.base.get_previous(self.id):
            rid = self.base.get_previous(self.id)[0][0]
        else :
            rid = self.id
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        base_controller = BaseController(self.master,rid,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')

    def show_Base_next(self):
        if self.delete_no_id() == TRUE:
            if self.base.get_next(self.id):
                rid = self.base.get_next(self.id)[0][0]
            else :
                rid = self.id
            for widget in self.master.winfo_children():
                widget.pack_forget()
                
            from Controller.BaseController import BaseController
            # Créer et afficher la page des paramètres
            base_controller = BaseController(self.master,rid,self.bulk)  # Importation à l'intérieur de la méthode
            base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
            base_interface.pack(expand=True, fill='both')

    #Parmetres
    def get_param(self,param):
        return self.param.get_params(param)[0][0]
    

    # Plot / Screen     
    def get_plot_screen(self):
        return self.base.get_column('Base_PlottedScreen',self.id)[0][0]
    
    def update_plot_screen(self,val):
        self.base.update_Base('Base_PlottedScreen' , val , self.id )


    # Burnt
    def get_Burnt(self):
        return self.base.get_column('Base_Burnt',self.id)[0][0]
    
    def update_burnt(self, val):
        self.base.update_Base('Base_Burnt',val,self.id)
    
    # Color 
    def get_Allcolor(self):
        return self.boneColor.get_all()
    
    def get_color(self):
        return self.base.get_column('Color_id',self.id)
    
    def update_color(self,val):
        self.base.update_Base('Color_ID',int(val),self.id)

    def reset_color(self,widg):
        self.base.get_reset(self.id)
        widg.set(None)

    def get_Spa(self,id):
        return self.spatial.get_By_Id(id)
    
    def get_CheckCode(self):
        return self.base.get_column('Base_CheckCode',self.id)
    

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

    # Size
    def get_size(self):
        size = self.base.get_column('Base_SIZE',self.id)[0][0]
        if size == None or len(size)<2:
            return 'n',size
        elif size=='NA':
            return 'c',size
        else :
            size_split = size.split('-')
            if int(size_split[0]) > 21 :
                return ('e',size)
            else :
                return 'c',size
            
    def update_size(self,val,widg1,widg2,widg3):
        self.base.update_Base('Base_Size' , val , self.id )
        widg1.configure(bg='white')
        widg2.configure(bg='white',fg='#1b1b1b')
        widg3.configure(bg='white',fg='black')



    #Field

    def update_Field(self,val,col):
        if val:
            
            self.base.update_Base(col,val,self.id)            
            return self.get_Spa(val)

        
    def get_fields(self,colonne):
        return self.base.get_column(colonne,self.id)[0][0]
    
    def get_fab(self):
        if self.get_fields('Base_ID'):
            print(self.id)
            self.spatial.update_by_id(self.id,self.get_fields('Base_ID'))
            return self.spatial.get_fab(self.get_fields('Base_ID'))
    
    def update_checkCode(self,val):
        self.base.update_Base('Base_CheckCode',val,self.id)
    
    def put_square(self):
        liste_sqr = []
        for i in self.base.get_sqr():
            if i[0] != None:
                if len(i[0])>0:
                    liste_sqr.append(i[0])
        return liste_sqr
    
    def next_sub(self,id,widg):
        if id != None :
            if len(id) > 0 :
                sub = self.base.get_next_sub(id)[0][0]
                if sub != None:
                    widg.config(text=int(sub) + 1)
                else:
                    widg.config(text=1)
            widg.config(text=1)
                

    """     
    def get_field(self):
        field = self.base.get_column('Base_ID',self.id)[0][0]
        if field == None:
            return
        if field
        field_split = field.split('_')
        print(field,field_split)"""
    
    #Bulk

    def show_teeth_page(self):

        if self.change('Skull') == True:
            self.delete_skel()

        if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'Skull')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','Skull')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            skull_interface = TeethInterface(self.master, skel_controller,self.bulk)
            skull_interface.pack(expand=True, fill='both')


    def show_LBN_page(self):
         
         if self.change('LBN') == True:
            self.delete_skel()

         if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'LBN')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','LBN')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            lBN_interface = LBNInterface(self.master, skel_controller,self.bulk)
            lBN_interface.pack(expand=True, fill='both')

    def show_FNB_page(self):
         
         if self.change('FNB') == True:
            self.delete_skel()

         if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'FNB')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','FNB')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            fnb_interface = FNBInterface(self.master, skel_controller,self.bulk)
            fnb_interface.pack(expand=True, fill='both')

    def show_SBN_page(self):
         
        if self.change('SNB') == True:
            self.delete_skel()


        if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'SNB')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','SNB')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            sbn_interface = SBNInterface(self.master, skel_controller,self.bulk)
            sbn_interface.pack(expand=True, fill='both')

    def show_Bird_page(self):
         
        if self.change('Bird') == True:
            self.delete_skel()

        if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'Bird')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','Bird')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            bird_interface = BirdInterface(self.master, skel_controller,self.bulk)
            bird_interface.pack(expand=True, fill='both')

    def show_NMB_page(self):

        if self.change('NMB') == True:
            self.delete_skel()

        if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()

            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'NMB')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','NMB')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            nmb_interface = NMBInterface(self.master, skel_controller,self.bulk)
            nmb_interface.pack(expand=True, fill='both')
    
    def show_NID_page(self):
        if self.change('NID') == True:
            self.delete_skel()

        if self.id_no_skel() == False:
            for widget in self.master.winfo_children():
                widget.pack_forget()


            # Afficher la vue HomeInterface
            from Controller.SkelController import SkellController
            # Créer et afficher la page des paramètres
            if not self.skel.get_By_Id(self.id):
                    self.skel.insert_Skel(self.id,'NID')
                    self.skel.update_Skel(self.id,'Skel_Anat','NID')
            else :
                self.skel.update_Skel(self.id,'Skel_Anat_Class','NID')
                self.skel.update_Skel(self.id,'Skel_Anat','NID')

            skel_controller = SkellController(self.master,self.id,self.bulk)
            nid_interface = NIDInterface(self.master, skel_controller,self.bulk)
            nid_interface.pack(expand=True, fill='both')


    def put_species(self):
        liste_spe = []
        for i in self.species.get_species():
           if i[0] != None :
                if len(i[0])>0:
                    liste_spe.append(i[0])
        return liste_spe
    
    def getBulk(self,att):
        if att == 'class':
            return self.bulk.get_bulk_class()
        elif att == 'skel':
            return self.bulk.get_bulk_skel()
        elif att == 'species':
            return self.bulk.get_bulk_species()

    def setBulk(self,val,att):
        if att == 'class':
            self.bulk.set_bulk_class(val)
        elif att == 'skel':
            self.bulk.set_bulk_skel(val)
        elif att == 'species' :
            self.bulk.set_bulk_species(val)

    def resetBulk(self):
        self.bulk.set_bulk_class(None)
        self.bulk.set_bulk_skel(None)
        self.bulk.set_bulk_species(None)

        for widget in self.master.winfo_children():
                widget.pack_forget()
                
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        base_controller = BaseController(self.master,self.id,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')



    #Menu

    def get_menu(self):
        b = self.id
        sk = self.skel.get_By_Id(self.id)
        s = self.species.get_By_Id(self.id)
        return b,sk ,s
    
    def message_field(self):
        if self.base.get_column('Base_ID',self.id)[0][0]==None:
            confirmation = messagebox.askretrycancel("Field Id Manquant", "Les données ne seront pas sauvegardé car il manque un Field ID")
            return confirmation
        else :
            True

    def change(self,val):
        if self.skel.get_column(self.id,'Skel_Anat_Class'):
            if self.skel.get_column(self.id,'Skel_Anat_Class')[0][0]!= val:
                confirmation = messagebox.askyesno("Anatomy already entered", "Do you wish to delete previous entry, and re-enter anatomy\rfor this remain? Anatomy, Species and taphonomic records \r will be deleted if you click Yes!")
                return confirmation
            else :
                return False
            
    def delete_skel(self):
        idskel = self.skel.get_id(self.id)[0][0]
        if self.skel_nde.getNde(idskel):
            self.skel_nde.delete_Skel_Nde_All(idskel) 

        if self.teeth.get(idskel):
            self.teeth.delete_all(idskel)

        self.skel.delete(self.id)

        if self.species.get(self.id):
            self.species.delete(self.id)

