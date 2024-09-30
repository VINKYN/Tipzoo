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
from View.Skull.Skel.AddTeeth import AddTeethInterface
from View.Species.Species import Species

from View.Skull.Skel.Teeth import TeethInterface
from View.Skull.LBN.LBN import LBNInterface
from View.Skull.FBN.FNB import FNBInterface
from View.Skull.SBN.SBN import SBNInterface
from View.Skull.BIRD.Bird import BirdInterface
from View.Skull.NMB.NMB import NMBInterface
from View.Skull.NID.NID import NIDInterface

import sqlite3




class SkellController:
    def __init__(self,master=None,id=None,bulk=None):
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

    def update_skel(self,val,col):
        self.skel.update_Skel(self.id,col,val)

    def getSPong(self):
        return self.skel.get_column(self.id,'Skel_Spongy')[0][0]

    def getFrag(self):
        return self.skel.get_column(self.id,'Skel_Frag')[0][0]
    
    def getAge(self):
        return self.skel.get_column(self.id,'Skel_AgeCort')[0][0]
    
    def getSide(self):
        return self.skel.get_column(self.id,'Skel_Side')[0][0]
    
    def getPortion(self):
        return self.skel.get_column(self.id,'Skel_Portion')[0][0]
    
    def getSegment(self):
        return self.skel.get_column(self.id,'Skel_Segment')[0][0]
    
    def getAgeFus(self):
        return self.skel.get_column(self.id,'Skel_AgeFus')[0][0]
    
    def getCirc(self):
        return self.skel.get_column(self.id,'Skel_SHC')[0][0]
    
    def getAnat_Detail(self):
        return self.skel.get_column(self.id,'Skel_Anat_Detail')[0][0]
    
    def get_anat(self):
        return self.skel.get_column(self.id,'Skel_Anat')[0][0]
    
    def set_portion(self):
        return  self.update_skel(None, 'Skel_Portion')
    
    def set_but(self,val):
        self.skel.update_Skel(self.id,'Skel_Anat_Detail',val)

    def AgeFus(self):
        string = self.getAgeFus()
        apf=''
        apj=''
        apu=''
        adf=''
        adj=''
        adu=''
        aef=''
        aej=''
        aeu=''
        if string != None:
            lettres = string.split(',')
            if 'Pfus' in lettres:
                apf='Pfus'
            if 'Pjustfus' in lettres:
                apj='Pjustfus'
            if 'Punfus' in lettres:
                apu='Punfus'
            if 'Dfus' in lettres:
                adf='Dfus'
            if 'Djustfus' in lettres:
                adj='Djustfus'
            if 'Dunfus' in lettres:
                adu='Dunfus'
            if 'Efus' in lettres:
                aef='Efus'
            if 'Ejustfus' in lettres:
                aej='Ejustfus'
            if 'Eunfus' in lettres:
                aeu='Eunfus'
        return apf ,apj ,apu ,adf,adj,adu,aef,aej,aeu
    

    def SkelAgeFus(self):
        string = self.getAgeFus()
        af=''
        aj=''
        au=''
        if string != None:
            lettres = string.split(',')
            if 'fus' in lettres:
                af='fus'
            if 'justfus' in lettres:
                aj='justfus'
            if 'unfus' in lettres:
                au='unfus'
        return af, aj , au

    
    def portion(self):
        string = self.getPortion()
        p=''
        s=''
        d=''
        e=''
        if string != None:
            lettres = string.split(',')
            if 'P' in lettres:
                p='P'
            if 'S' in lettres:
                s='S'
            if 'D' in lettres:
                d='D'
            if 'E' in lettres:
                e='E'
        return p , s ,d ,e
    
    def portion2(self):
        string = self.getPortion()
        bod = ''
        bode = ''
        disc = ''
        disce = ''
        trp = ''
        arp = ''
        spivrt = ''

        if string != None:
            lettres = string.split(',')
            if 'BOD' in lettres:
                bod = 'BOD'
            if 'BODe' in lettres:
                bode = 'BODe'
            if 'DISC' in lettres:
                disc = 'DISC'
            if 'DISCe' in lettres:
                disce = 'DISCe'
            if 'TRP' in lettres:
                trp = 'TRP'
            if 'ARP' in lettres:
                arp = 'ARP'
            if 'SPIvrt' in lettres:
                spivrt = 'SPIvrt'

        return bod, bode, disc, disce, trp, arp, spivrt
    

    def portion3(self):
        string = self.getPortion()
        P=''
        D=''
        C=''
        if string != None:
            lettres = string.split(',')
            if 'P' in lettres:
                P='P'
            if 'D' in lettres:
                D='D'
            if 'COST' in lettres:
                C='COST'
        return P , D ,C
    

    def portion4(self):
        string = self.getPortion()
        G=''
        Bs=''
        Sp=''
        if string != None:
            lettres = string.split(',')
            if 'GLEscp' in lettres:
                G='GLEscp'
            if 'BODscp' in lettres:
                Bs='BODscp'
            if 'SPIscp' in lettres:
                Sp='SPIscp'
        return G , Bs ,Sp
    

    def portion5(self):
        string = self.getPortion()
        pub=''
        isc=''
        ili=''
        ace=""
        if string != None:
            lettres = string.split(',')
            if 'PUB' in lettres:
                pub='PUB'
            if 'ISC' in lettres:
                isc='ISC'
            if 'ILI' in lettres:
                ili='ILI'
            if 'ACE' in lettres:
                ace='ACE'
        return pub , isc ,ili ,ace
    

    def portionBird(self):
        string = self.getPortion()
        A=''
        M=''
        if string != None:
            lettres = string.split(',')
            if 'A' in lettres:
                A='A'
            if 'M' in lettres:
                M='M'
        return A ,M 
    
    def portionMandible(self):
        string = self.getPortion()
        S=''
        D1=''
        D2=''
        A1=''
        A2=''
        if string != None:
            lettres = string.split(',')
            if 'S' in lettres:
                S='S'
            if 'D1' in lettres:
                D1='D1'
            if 'D2' in lettres:
                D2='D2'
            if 'A1' in lettres:
                A1='A1'
            if 'A2' in lettres:
                A2='A2'
        return S,D1,D2,A1,A2 
    
    def portionFurcula(self):
        string = self.getPortion()
        F=''
        C1=''
        C2=''
        FA1=''
        FA2=''
        if string != None:
            lettres = string.split(',')
            if 'F' in lettres:
                F='F'
            if 'C1' in lettres:
                C1='C1'
            if 'C2' in lettres:
                C2='C2'
            if 'A1' in lettres:
                FA1='A1'
            if 'A2' in lettres:
                FA2='A2'
        return F,C1,C2,FA1,FA2
    
    def portionSternum(self):
        string = self.getPortion()
        R=''
        KS=''
        KE=''
        P=''
        if string != None:
            lettres = string.split(',')
            if 'R' in lettres:
                R='R'
            if 'KS' in lettres:
                KS='KS'
            if 'KE' in lettres:
                KE='KE'
            if 'P' in lettres:
                P='P'
        return R,KE,KS,P
    
    def portionCoxal(self):
        string = self.getPortion()
        Ace=''
        thick=''
        thin=''
        if string != None:
            lettres = string.split(',')
            if 'ACE' in lettres:
                Ace='ACE'
            if 'THICK' in lettres:
                thick='THICK'
            if 'THIN' in lettres:
                thin='THIN'
        return Ace,thin,thick
    
    def portionCra(self):
        string = self.getPortion()
        Max =""
        Nas =""
        Fro =""
        Orb =""
        Tem =""
        Par =""
        Occ =""
        if string != None:
            lettres = string.split(',')
            if 'MAX' in lettres:
                Max='MAX'
            if 'NAS' in lettres:
                Nas='NAS'
            if 'FRO' in lettres:
                Fro = 'FRO'
            if 'ORB' in lettres:
                Orb = 'ORB'
            if 'TEM' in lettres:
                Tem = 'TEM'
            if 'PAR' in lettres:
                Par = 'PAR'
            if 'OCC' in lettres:
                Occ = 'OCC'
        return Max,Nas,Fro,Orb,Tem,Par,Occ
    
    def portionMan(self):
        string = self.getPortion()
        Cond = ""
        Coro = ""
        Ram = ""
        Alv = ""
        Bodman = ""
        Sym = ""

        if string is not None:
            lettres = string.split(',')
            if 'COND' in lettres:
                Cond = 'COND'
            if 'CORO' in lettres:
                Coro = 'CORO'
            if 'RAM' in lettres:
                Ram = 'RAM'
            if 'ALV' in lettres:
                Alv = 'ALV'
            if 'BODman' in lettres:
                Bodman = 'BODman'
            if 'SYM' in lettres:
                Sym = 'SYM'

        return Cond, Coro, Ram, Alv, Bodman, Sym


    

    def segment(self):
        string = self.getSegment()
        sp=''
        sm=''
        sd=''
        sa=''
        spos=''
        smed=''
        slat=''
        snid=''
        if string != None:
            lettres = string.split(',')
            if 'P' in lettres:
                sp='P'
            if 'M' in lettres:
                sm='M'
            if 'D' in lettres:
                sd='D'
            if 'Ant' in lettres:
                sa='Ant'
            if 'Post' in lettres:
                spos='Post'
            if 'Med' in lettres:
                smed='Med'
            if 'Lat' in lettres:
                slat='Lat'
            if 'Nid' in lettres:
                snid='Nid'
        return sp ,sm ,sd ,sa,spos,smed,slat,snid 
    
    def updatePortion(self, val, check):
        string = self.getPortion()
        if string is None:
            string = ""
        if check in ['P','S','D','E','BOD','BODe','DISC','DISCe','TRP','ARP','SPIvrt','D','COST','SPIscp','BODscp','GLEscp','ILI','PUB','ACE','ISC','M','A','A1','A2','D1','D2','F','C1','C2','KS','KE','R','THICK','THIN','MAX','NAS','FRO','ORB','TEM','PAR','OCC','COND','CORO','RAM','ALV','BODman','SYM']:
            if len(val) == 0:
                string = string.replace(check+',','')
            else:
                string += val+','

        self.update_skel(string, 'Skel_Portion')

    
    def updateSegment(self, val, check):
        string = self.getSegment()
        if string is None:
            string = ""
        if check in ['P','M','D','Ant','Post','Med','Lat','Nid']:
            if len(val) == 0:
                string = string.replace(check+',','')
            else:
                string += val+','

        self.update_skel(string, 'Skel_Segment')


    def updateAgefus(self, val, check):
        string = self.getAgeFus()
        if string is None:
            string = ""
        if check in ['Pfus','Pjustfus','Punfus','Dfus','Djustfus','Dunfus','Efus','Ejustfus','Eunfus','fus','justfus','unfus']:
            if len(val) == 0:
                string = string.replace(check+',','')
            else:
                string += val+','

        self.update_skel(string, 'Skel_AgeFus')

    
    def getOnglet(self,page):
        listeLBN =['','LBN','HUM','RAU','FEM','TIB','FIB','MC','MT','MP','PHA']
        listeFBN=['','FBN','VRT','RIB','STE','SCP','COX','HYO']
        listeSBN =['','SBN','CAR','TAR','PAT','MAL','SES']
        listeBird =['','VRT','','','PHA']
        listeSkull =['CRAT','MANT','SKUT','TTH','CRA','MAN','ANT','HCO','SKU']
        liste = ''
        if page == 'LBN':
            liste = listeLBN
        elif page =='FBN':
            liste = listeFBN
        elif page =='SBN':
            liste = listeSBN
        elif page =='Bird':
            liste = listeBird
        elif page =="Skull":
            liste = listeSkull
       
        for i in range(len(liste)):
            if self.bulk.get_bulk_skel() != None:
                if liste[i] == self.bulk.get_bulk_skel():
                    return i 
            else:
                if liste[i] == self.skel.get_column(self.id,'Skel_Anat')[0][0]:
                    return i  
            
    def update_Anat(self,index,page):
        listeMP =['MP','MPV']
        listeLBN =['','LBN','HUM','RAU','FEM','TIB','FIB','MC','MT','MP','PHA']
        listeFBN=['','FBN','VRT','RIB','STE','SCP','COX','HYO']
        listeSBN =['','SBN','CAR','TAR','PAT','MAL','SES']
        listeBird =['','VRT','','','PHA']
        listeSkull =['CRAT','MANT','SKUT','TTH','CRA','MAN','ANT','HCO','SKU']
        liste = ''
        if page == 'LBN':
            liste = listeLBN
        elif page =='FBN':
            liste = listeFBN
        elif page =='SBN':
            liste = listeSBN
        elif page =='Bird':
            liste = listeBird
        elif page =='MP':
            liste = listeMP
        elif page== 'Skull':
            liste = listeSkull
        if index > 0:
            id = self.skel.get_column(self.id,'Skel_ID')[0][0]
            self.update_skel(liste[index],'Skel_Anat')
            self.update_skel(None,'Skel_Anat_Detail')
            #self.skel_nde.delete_Skel_Nde_All(id)
            self.bulk.set_bulk_skel(liste[index])

    def update_fish(self,val):
        self.update_skel(val, 'Skel_Anat')

    def getNDe(self,idnde):
        id = self.skel.get_column(self.id,'Skel_ID')[0][0]
        if self.skel_nde.get(id,idnde).is_integer():
            return int(self.skel_nde.get(id,idnde))
        else:
            return float(self.skel_nde.get(id,idnde))

    def landmark(self,idNde,val):
        id = self.skel.get_column(self.id,'Skel_ID')[0][0]
        try:
            val =float(val)
            if val > 0:
                if self.skel_nde.get_val(id,idNde) :
                    self.skel_nde.delete_Skel_Nde(id,idNde)
                    
                self.skel_nde.insert_Skel_Nde(id,idNde,val)
            if val == 0:
                self.skel_nde.delete_Skel_Nde(id,idNde)
        except ValueError:
            return

    
    def get_Val_Nde(self,ldm):
        id = self.skel.get_column(self.id,'Skel_ID')[0][0]
        if self.skel_nde.get_val(id,ldm) :
            
            return self.skel_nde.get_val(id,ldm)[0][0]
        else:
            return None
        

    def put_database(self):
        tpath = self.path.removesuffix('.sqlite3')
        tpath = tpath.removeprefix('Database/')
        return tpath.upper()
        


    def show_new_Base_create(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        id = self.base.insert_Base(self.put_database())
        base_controller = BaseController(self.master,id,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')

    


    def show_Species_page(self):

        if self.param.get_params('Param_Side')[0][0] == 1 :
            if self.getSide() == None:
                confirmation = messagebox.showwarning('NO SIDE !!!!',"Side is empty!")
            else :
                for widget in self.master.winfo_children():
                    widget.pack_forget()

                from Controller.SpeciesController import SpeciesController

                if not self.species.get_By_Id(self.id):
                        self.species.insert_Species(self.id)

                species_controller = SpeciesController(self.master,self.id,self.bulk)
                species_interface = Species(self.master, species_controller,self.bulk)
                species_interface.pack(expand=True, fill='both')
        else :

            for widget in self.master.winfo_children():
                widget.pack_forget()

            from Controller.SpeciesController import SpeciesController

            if not self.species.get_By_Id(self.id):
                    self.species.insert_Species(self.id)

            species_controller = SpeciesController(self.master,self.id,self.bulk)
            species_interface = Species(self.master, species_controller,self.bulk)
            species_interface.pack(expand=True, fill='both')
        
    def tapho_category(self):
        param = self.param.get_params('Param_Tapho')[0][0]
        size = self.base.get_column('Base_size',self.id)[0][0]
        if param == 0 :
            return 'No'
        elif size == '0-1':
            return'No'
        elif param == 1 and size=='1-2':
            return 'Yes'
        
    def getSpe(self):
        val =self.species.get_column(self.id,'Species_Taxon')
        if val:
            return val[0][0]
        else:
            return None
        
    def tapho_category(self):
        param = self.param.get_params('Param_Tapho')[0][0]
        size = self.base.get_column('Base_size', self.id)[0][0]
        if param == 0:
            return 'No'
        elif size == '0-1':
            return 'No'
        elif size == '1-2':
            if param == 1:
                return 'Yes'
            elif param > 1:
                return 'No'
            
        elif size == '2-3':
            if param == 2:
                return 'Yes'
            elif param > 2:
                return 'No'
            
        elif size == '3-4':
            if param == 3:
                return 'Yes'
            elif param > 3:
                return 'No'
            
        elif size == '4-5':
            if param == 4:
                return 'Yes'
            elif param > 4:
                return 'No'
            
        elif param >= 1:
            return 'Yes'
        

    def update_Vertebra(self,index):
        listevertebra=['VRT','ATL','AXI','CER','THO','LUM','SAC','CAU']
        if index!=None:
            self.skel.update_Skel(self.id,'Skel_Anat_Detail',listevertebra[index])

    def get_Vertebra(self):
        val=self.skel.get_column(self.id,'Skel_Anat_Detail')[0][0]
        listevertebra=['VRT','ATL','AXI','CER','THO','LUM','SAC','CAU']
        for i in range(len(listevertebra)):
            if val == listevertebra[i]:
                return i
            
    def get_Teeth(self):
        id = self.skel.get_column(self.id,'Skel_ID')[0][0]
        return self.teeth.get_By_Id(id)
    



    def show_new_teeth_create(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.TeethController import TeethController

        id2 = self.skel.get_column(self.id,'Skel_ID')[0][0]
        
        # Créer et afficher la page des paramètres
        id= self.teeth.insert_Teeth(id2)
        teeth_controller = TeethController(self.master,id,id2,self.bulk)  # Importation à l'intérieur de la méthode
        teeth_interface = AddTeethInterface(self.master, teeth_controller,self.bulk)  # Passer l'instance du contrôleur
        teeth_interface.pack(expand=True, fill='both')

    def show_new_teeth(self,tab):
        item = tab.item(tab.selection(), 'values')
        if item :
            rid = item[0]
            for widget in self.master.winfo_children():
                widget.pack_forget()
                
            from Controller.TeethController import TeethController
            # Créer et afficher la page des paramètres
            teeth_controller = TeethController(self.master,rid,self.id,self.bulk)  # Importation à l'intérieur de la méthode
            teeth_interface = AddTeethInterface(self.master, teeth_controller,self.bulk)  # Passer l'instance du contrôleur
            teeth_interface.pack(expand=True, fill='both')

    def get_menu(self):
        b = self.id
        sk = self.skel.get_By_Id(self.id)
        s = self.species.get_By_Id(self.id)
        return b,sk ,s
    
    def delete_teeth(self,tab):
        item = tab.item(tab.selection(), 'values')
        tab.delete(tab.selection())
        if item :
            rid = item[0]
            self.teeth.delete(rid)
            print('bang')

    def getspe(self):
        return self.species.get_column(self.id,'Species_Taxon')
    
    def updateTaxon(self,val):
        if not self.species.get_By_Id(self.id):
            self.species.insert_Species(self.id)
            self.species.update_taxon(self.id,val)
        else :
            print(val)
            self.species.update_taxon(self.id,val)

    
        

        
        