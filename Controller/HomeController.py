import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
import pandas as pd
from Model.BaseModel import BaseModel
from Model.SpeciesModel import SpeciesModel
from Model.SpatialModel import SpatialModel
from Model.SkelModel import SkelModel
from Model.TeethModel import TeethModel
from Model.TaphoModel import TaphoModel
from Model.Cut_BaseModel import CutBaseModel
from Model.RefitsModel import RefitsModel
from Model.Skel_NDEModel import SkelNdeModel

from View.Settings import SettingsInterface
from View.All_Value import AllValueInterface
from View.Base.Base import BaseInterface
from View.Home import HomeInterface
from View.Export import ExportInterface
from Controller.getDatabase import get_database_path
import tkinter.filedialog

import sqlite3



class HomeController:
    def __init__(self,master=None,bulk=None):
        self.master = master
        self.path = get_database_path()
        self.base = BaseModel(self.path)
        self.species = SpeciesModel(self.path)
        self.spatial = SpatialModel(self.path)
        self.skel = SkelModel(self.path)
        self.skel_nde = SkelNdeModel(self.path)
        self.teeth = TeethModel(self.path)
        self.tapho = TaphoModel(self.path)
        self.cut = CutBaseModel(self.path)
        self.refits = RefitsModel(self.path)
        self.bulk = bulk
        self.order = 'DESC'


    def show_settings_page(self):
        # Supprimer les widgets actuels de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.SettingsController import SettingsController
        # Créer et afficher la page des paramètres
        param_controller = SettingsController(self.master,self.bulk)  # Importation à l'intérieur de la méthode
        settings_interface = SettingsInterface(self.master, param_controller)  # Passer l'instance du contrôleur
        settings_interface.pack(expand=True, fill='both')


    def show_export_page(self):
        # Supprimer les widgets actuels de la fenêtre principale
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.ExportController import ExportController
        # Créer et afficher la page des paramètres
        export_controller = ExportController(self.master,self.bulk)  # Importation à l'intérieur de la méthode
        export_interface = ExportInterface(self.master, export_controller,self.bulk)  # Passer l'instance du contrôleur
        export_interface.pack(expand=True, fill='both')


    def show_allvalue_page(self,label):
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.All_ValueController import AllValueController
        # Créer et afficher la page des paramètres
        allvalue_controller = AllValueController(self.master,label,self.bulk)  # Importation à l'intérieur de la méthode
        allvalue_interface = AllValueInterface(self.master, allvalue_controller,label)  # Passer l'instance du contrôleur
        allvalue_interface.pack(expand=True, fill='both')

    def show_new_Base_create(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
            
        from Controller.BaseController import BaseController
        # Créer et afficher la page des paramètres
        id = self.base.insert_Base(self.put_database())
        base_controller = BaseController(self.master,id,self.bulk)  # Importation à l'intérieur de la méthode
        base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
        base_interface.pack(expand=True, fill='both')

    def show_new_Base(self,tab):
        item = tab.item(tab.selection(), 'values')
        if item :
            rid = item[0]
            for widget in self.master.winfo_children():
                widget.pack_forget()
                
            from Controller.BaseController import BaseController
            # Créer et afficher la page des paramètres
            base_controller = BaseController(self.master,rid,self.bulk)  # Importation à l'intérieur de la méthode
            base_interface = BaseInterface(self.master, base_controller,self.bulk)  # Passer l'instance du contrôleur
            base_interface.pack(expand=True, fill='both')


    def put_database(self):
        tpath = self.path.removesuffix('.sqlite3')
        tpath = tpath.removeprefix('Database/')
        return tpath.upper()

    def get_count_All(self):
        CountListe =[self.base.get_count(),self.species.get_count(),self.skel.get_count(),
                     self.skel_nde.get_count(),self.tapho.get_count(),self.teeth.get_count(),
                     self.cut.get_count(),self.spatial.get_count(),self.refits.get_count()]
        return CountListe
    
    def get_treeview(self):
        liste =[]
        for i in self.base.get_All():
            i = list(i)
            sub = i[3]
            sqr = i[2]
            field = i[1]
            if not sub :
                sub=''
            else:
                sub ='_'+sub
            if not sqr :
                sqr=''
            else:
                sqr = sqr+'_'
            if field:
                i[1]=sqr+field+sub
                
                i.pop(2)
                i.pop(2)
                liste.append(i)
        return liste
    
    """if i[1]!=None:
        if i[2] != None and i[3] == None :
            i[1]=str(i[2])+'_'+str(i[1])
            i.pop(2)
        if i[2] != None and i[3]!=None :
            i[1]=str(i[2])+'_'+str(i[1])+'_'+str(i[3])
            i.pop(2)
            i.pop(2)
        if i[2] == None and i[3] != None :
            i[1]=str(i[1])+'_'+str(i[3])
            i.pop(3)"""
            
    

    def vider_tableau(self,tab):
        for item in tab.get_children():
            tab.delete(item)


    def order_by(self,tab,colonne):
        self.vider_tableau(tab)
    
        tab.tag_configure('1', background='white')
        tab.tag_configure('2', background='#f0f0f0')
        tag = 1

        if self.order == 'DESC':
            self.order ='ASC'
        else :
            self.order ='DESC'

        for colonnes in self.base.get_All_order_by(colonne,self.order):
            colonnes=list(colonnes)

            sub = colonnes[3]
            sqr = colonnes[2]
            field = colonnes[1]
            if not sub :
                sub=''
            else:
                sub ='_'+sub
            if not sqr :
                sqr=''
            else:
                sqr = sqr+'_'
            if field:
                colonnes[1]=sqr+field+sub
                colonnes.pop(2)
                colonnes.pop(2)

            if tag == 1 :
                tab.insert('', END, values=colonnes, tags = (tag))
                tag += 1
            else :
                tab.insert('', END, values=colonnes, tags = (tag))
                tag = 1
    
    def delete_base(self,tab):
        item = tab.item(tab.selection(), 'values')

        id = item[0]
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to remove this element?")
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

            tab.delete(tab.selection())
    
    def search(self,tab,entry):
        self.vider_tableau(tab)

        val = entry.get()

        
        if len(val)<1 :
            col = self.base.get_All()
        else :
            col = self.base.get_Search(val)

        tab.tag_configure('1', background='white')
        tab.tag_configure('2', background='#F7F7F7')
        tag = 1

        for colonnes in col:
            colonnes = list(colonnes)
            sub = colonnes[3]
            sqr = colonnes[2]
            field = colonnes[1]
            if not sub :
                sub=''
            else:
                sub ='_'+sub
            if not sqr :
                sqr=''
            else:
                sqr = sqr+'_'
            if field:
                colonnes[1]=sqr+field+sub
                colonnes.pop(2)
                colonnes.pop(2)

            if tag == 1 :
                tab.insert('', END, values=colonnes, tags = (tag))
                tag += 1
            else :
                tab.insert('', END, values=colonnes, tags = (tag))
                tag = 1
    """
    def get_path_Spatial(self):
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if not file_path.endswith('.xlsx'):
            messagebox.showerror('Wrong File',"Please choose an EXCEL file (.xlsx) ")
        else:
            column = ['Year','fieldID','Code','Square_field',
                      'Square_true','Dec','USfield','FabID',
                      'X','Y','Z','Group1','Group2','Group3']
            fichier = pd.read_excel(file_path,usecols=column)

            fichier['X'] = pd.to_numeric(fichier['X'],errors='coerce')
            fichier['Y'] = pd.to_numeric(fichier['Y'],errors='coerce')
            fichier['Z'] = pd.to_numeric(fichier['Z'],errors='coerce')            
            nbLigneI = 0
            nbLigneNI = 0
            listeNi =[]
            for ligne ,col in fichier.iterrows():
                try:
                    val = list(col)
                    self.spatial.insert_spatial(val[0],val[1],val[2],val[3],val[4],
                                        val[5],val[6],val[6],val[7],val[8],
                                        val[9],val[10],val[11],val[12],val[13],
                                        None)
                    nbLigneI+=1
                except Exception as e:
                    nbLigneNI += 1
                    listeNi.append(ligne)

            """

    """def get_path_Spatial(self):
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if not file_path.endswith('.xlsx'):
            messagebox.showerror('Wrong File', "Please choose an EXCEL file (.xlsx) ")
        else:
            column = ['Year', 'fieldID', 'Code', 'Square_field', 'Square_true', 'Dec', 'USfield', 'FabID', 'X', 'Y', 'Z', 'Group1', 'Group2', 'Group3']
            try:
                fichier = pd.read_excel(file_path, usecols=column)
                fichier[['X', 'Y', 'Z']] = fichier[['X', 'Y', 'Z']].apply(pd.to_numeric, errors='coerce')

                nbLigneI = 0
                nbLigneNI = 0

                for _, row in fichier.iterrows():
                    try:
                        self.spatial.insert_spatial(row['Year'], row['fieldID'], row['Code'], row['Square_field'], row['Square_true'],
                                                    row['Dec'], row['USfield'], row['FabID'], row['X'], row['Y'], row['Z'],
                                                    row['Group1'], row['Group2'], row['Group3'], None)
                        nbLigneI += 1
                    except Exception as e:
                        nbLigneNI += 1
                        # Peut-être afficher une erreur spécifique ici ou enregistrer les lignes qui ont échoué
                        print(f"Failed to insert row {nbLigneI + nbLigneNI}: {e}")

                messagebox.showinfo('Insertion Complete', f"Successfully inserted {nbLigneI} rows.")

            except pd.errors.ParserError:
                messagebox.showerror('Parse Error', "Unable to parse the Excel file.")
            except Exception as e:
                messagebox.showerror('Error', str(e))"""
    
    def get_path_Spatial(self):
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if not file_path.endswith('.xlsx'):
            messagebox.showerror('Wrong File', "Please choose an EXCEL file (.xlsx) ")
        else:
            column = ['Year', 'fieldID', 'Code', 'Square_field', 'Square_true', 'Dec', 'USfield', 'FabID', 'X', 'Y', 'Z', 'Group1', 'Group2', 'Group3']
            try:
                fichier = pd.read_excel(file_path, usecols=column)
                fichier.replace(r'^\s*$', None, regex=True,inplace=True)
                fichier[['X', 'Y', 'Z']] = fichier[['X', 'Y', 'Z']].apply(pd.to_numeric, errors='coerce')

                nbLigneI = 0
                nbLigneNI = 0

                for _, row in fichier.iterrows():
                    if row.notna().any():
                        try:
                            self.spatial.insert_spatial(row['Year'], row['fieldID'], row['Code'], row['Square_field'], row['Square_true'],
                                                        row['Dec'], row['USfield'], row['FabID'], row['X'], row['Y'], row['Z'],
                                                        row['Group1'], row['Group2'], row['Group3'], None)
                            nbLigneI += 1
                        except Exception as e:
                            nbLigneNI += 1
                            print(f"Failed to insert row {nbLigneNI}: {e}")

                messagebox.showinfo('Insertion Complete', f"Successfully inserted {nbLigneI} rows. Failed to insert {nbLigneNI} rows.")

            except pd.errors.ParserError:
                messagebox.showerror('Parse Error', "Unable to parse the Excel file.")
            except Exception as e:
                messagebox.showerror('Error', str(e))

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


    def switch_database(self,base):
        listdb = self.get_database()
        if base not in listdb:
            self.create_database(base)

        fichier = 'Database/path.txt'
        with open(fichier, "w") as path:
            path.write(base)
        self.show_home_page()


    def create_database(self,base):
        try:
            conn = sqlite3.connect('Database/'+base+'.sqlite3')
            cursor = conn.cursor()
            cursor.executescript("""
                DROP TABLE if EXISTS BASE;
                DROP TABLE if EXISTS Spatial;
                DROP TABLE IF EXISTS Refits;
                DROP TABLE IF EXISTS Species;
                DROP TABLE IF EXISTS Skel;
                DROP TABLE IF EXISTS Teeth;
                DROP TABLE IF EXISTS BoneColor;
                DROP TABLE IF EXISTS Cut;
                DROP TABLE IF EXISTS Cut_Base;
                DROP TABLE IF EXISTS Tapho;
                DROP TABLE IF EXISTS TParam;
                DROP TABLE IF EXISTS Tapho_Param;
                DROP TABLE IF EXISTS NDE;
                DROP TABLE IF EXISTS Skel_NDE;
                DROP TABLE IF EXISTS Param;

                CREATE TABLE Param(
                Param_IDNumb VARCHAR(15) CHECK(Param_IDNumb IN('Unique ID' , 'Square ID')),
                Param_Size INTEGER CHECK(Param_Size IN(0,1)),
                Param_Side INTEGER CHECK(Param_Size IN(0,1)),
                Param_Tapho INTEGER CHECK(Param_Tapho IN(0,1,2,3,4)),
                Param_Path Text 
                );

                CREATE TABLE BoneColor(
                Color_ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                Color_Value TEXT ,
                Color_Hexcode Text,
                Color_Path Text
                );

                CREATE TABLE Base (
                Base_pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Base_ID VARCHAR(25),
                Base_Sub VARCHAR(25),
                Base_Square VARCHAR(25),
                Base_CheckCode VARCHAR(7) CHECK(Base_CheckCode IN('Yes','No')),
                Base_Observation TEXT ,
                Base_PlottedScreen VARCHAR(7) CHECK(Base_PlottedScreen IN ('Screen' , 'Plotted')),
                Base_Burnt VARCHAR(12) CHECK(Base_Burnt IN ('No','Partially','Mostly black','Mostly grey','Mostly white')),
                Base_SiteName VARCHAR(255),
                Base_SIZE VARCHAR(10),
                DateEnter TEXT ,
                DateModif TEXT,
                Color_ID Integer,
                FOREIGN KEY(Color_ID) REFERENCES BoneColor(Color_ID)

                );

                CREATE TABLE Spatial(
                Spatial_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Spatial_FieldID INTEGER ,
                Spatial_Code VARCHAR(255) ,
                Spatial_Dec VARCHAR(255),
                Spatial_FabID VARCHAR(255) ,
                Spatial_Square_field VARCHAR(255) ,
                Spatial_Square_true VARCHAR(255),
                Spatial_USfield VARCHAR(255),
                X REAL ,
                Y REAL,
                Z REAL,
                Spatial_year INTEGER,
                Spatial_Group1 TEXT,
                Spatial_Group2 TEXT,
                Spatial_Group3 TEXT,
                Base_pk INTEGER,
                FOREIGN KEY(Base_pk) REFERENCES Base(Base_pk)
                );

                CREATE TABLE Refits(
                Base_pk1 Integer,
                Base_pk2 Integer, 
                REFITS_Type VARCHAR(255),
                PRIMARY KEY(Base_pk1,Base_pk2),
                FOREIGN KEY(Base_pk1) REFERENCES Base(Base_pk),
                FOREIGN KEY(Base_pk2) REFERENCES Base(Base_pk)
                );

                CREATE TABLE Species (
                Species_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Species_CheckImprove VARCHAR(40),
                Species_ObsTaxon TEXT,
                Species_Taxon VARCHAR(20),
                Base_pk Integer,
                FOREIGN KEY(Base_pk) REFERENCES Base(Base_pk)
                );




                CREATE TABLE Cut(
                Cut_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Cut_Param VARCHAR(255)
                );

                CREATE TABLE Cut_Base(
                Cut_ID INTEGER,
                Base_pk INTEGER,
                PRIMARY KEY(Cut_ID,Base_pk),
                FOREIGN KEY (Cut_ID) REFERENCES Cut(Cut_ID),
                FOREIGN KEY (Base_pk) REFERENCES Base(Base_pk)
                );



                CREATE TABLE Tapho (
                Tapho_ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                Tapho_Abra INT CHECK(Tapho_Abra IN('1','2')),
                Tapho_Black INT CHECK(Tapho_Black IN(1,2,3)),
                Tapho_Conc INT CHECK(Tapho_Conc IN(1,2,3)),
                Tapho_ConcType VARCHAR(4) CHECK(Tapho_ConcType IN('calc','dirt')),
                Tapho_Crack INT CHECK(Tapho_Crack IN(1,2)),
                Tapho_Sheet INT CHECK(Tapho_Sheet IN(1,2)),
                Tapho_DenD INT CHECK(Tapho_DenD IN(0,1)),
                Tapho_DenE INT CHECK(Tapho_DenE IN(0,1)),
                Tapho_CirE INT CHECK(Tapho_CirE IN(0,1)),
                Tapho_Exfo INT CHECK(Tapho_Exfo IN(0,1)),
                Tapho_Fract1 VARCHAR(6) CHECK(Tapho_Fract1 IN('Green','Dry','Recent')),
                Tapho_Fract2 VARCHAR(6) CHECK (Tapho_Fract2 IN('Green','Dry','Recent')),
                Tapho_Read VARCHAR(2) CHECK (Tapho_Read IN('1','2','3','4','NA')),
                Tapho_Scrape_Asso VARCHAR(55) CHECK (Tapho_Scrape_Asso IN('Fracturation' , 'Retouchoir' , 'Nothing' , '?')),
                Base_pk VARCHAR(25),
                FOREIGN KEY(Base_pk) REFERENCES Base(Base_pk)
                );

                CREATE TABLE TParam(
                TParam_Id Integer PRIMARY KEY AUTOincrement,
                Tapho_Name VARCHAR(255)
                );

                CREATE TABLE Tapho_Param(
                Tapho_Id INTEGER,
                TParam_Id INTEGER,
                Tapho_Param_Value CHAR CHECK(Tapho_Param_Value IN('1','0','?')),
                PRIMARY KEY(Tapho_Id,TParam_Id),
                FOREIGN KEY (Tapho_Id) REFERENCES Tapho(Tapho_Id),
                FOREIGN KEY (TParam_Id) REFERENCES Tparam(TParam_Id)
                );

                CREATE TABLE Skel(
                Skel_ID integer PRIMARY KEY AUTOINCREMENT,
                Skel_AgeCort CHAR(1) CHECK(Skel_AgeCort IN ('F','J','A','?')),
                Skel_AgeFus VARCHAR(255),
                Skel_Anat_Detail VARCHAR(255),												
                Skel_Anat VARCHAR(55),
                Skel_Anat_Class VARCHAR(55),
                Skel_Frag VARCHAR(55),
                Skel_Segment VARCHAR(55),
                Skel_SHC VARCHAR(10),
                Skel_Side VARCHAR(15) CHECK(Skel_Side IN('Left','Right','Left+Right','?')),
                Skel_Spongy INT CHECK(Skel_Spongy IN(0,1)),
                Skel_Portion VARCHAR(255),
                Base_pk INTEGER,
                FOREIGN KEY(Base_pk) REFERENCES Base(Base_pk)
                );


                CREATE TABLE NDE(
                Nde_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NDE_Param VARCHAR(255)
                );

                CREATE TABLE Skel_NDE(
                Skel_ID INTEGER,
                NDE_ID INTEGER,
                Value Text,
                PRIMARY KEY(Skel_ID,NDE_ID),
                FOREIGN KEY (Skel_ID) REFERENCES SKEL(Skel_ID),
                FOREIGN KEY (NDE_ID) REFERENCES NDE(NDE_ID)
                );


                CREATE TABLE Teeth (
                Teeth_ID Integer PRIMARY KEY AUTOINCREMENT,
                Teeth_Dentition VARCHAR(10) CHECK(Teeth_Dentition IN('Deciduous','Permanent','?')),
                Teeth_CH INT,
                Teeth_FR VARCHAR(3) CHECK(Teeth_FR IN('CO','ACO','FR')),
                Teeth_Class VARCHAR(50),
                Teeth_Number VARCHAR(3),
                Teeth_Type VARCHAR(8) CHECK(Teeth_Type IN('ANTERIOR','Cheek','?')),
                Teeth_Portion VARCHAR(50),
                Teeth_OccSup50 INT CHECK(Teeth_OccSup50 IN(0,1)),
                Teeth_LowerUpper VARCHAR(5) CHECK(Teeth_LowerUpper IN('Lower','Upper','?')),
                Teeth_Side VARCHAR(6) CHECK(Teeth_Side IN('Left','Right','?')),
                Teeth_UW_AgeClass INT,
                Teeth_UW_Crown INT,
                Teeth_UW_Root INT,
                Teeth_UW_RootResorp INT CHECK(Teeth_UW_RootResorp IN(0,1)),
                SKEL_ID INTEGER,
                FOREIGN KEY(SKEL_ID) REFERENCES Skel(SKEL_id)
                );

                --INSERT

            INSERT INTO Param (Param_IDNumb, Param_Size , Param_Side , Param_Tapho) VALUES ('Unique ID' ,1,1,1);


            INSERT INTO CUT(CUT_PARAM) VALUES('At_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_ds');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_es');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_fs');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('At_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_ip');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_j');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_jp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_js');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_k');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_kp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ax_ks');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cal_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cbn_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cbn_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ctt_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ctt_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_ds');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_gs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_ip');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_j');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_jp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_k');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_kp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_l');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_lp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_ls');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_m');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_n');
            INSERT INTO CUT(CUT_PARAM) VALUES('Cv_o');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fd_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fib_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fib_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fib_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('fk_ID');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fp_ip');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fs_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Fs_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Gcf_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hd_hp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_hp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_ip');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_j');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_k');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_kp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_l');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_lp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_m');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hp_mp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hs_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Hs_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lun_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lun_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lun_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lun_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lun_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_cs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_ds');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_es');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_hp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_ip');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_j');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_k');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_kp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_l');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_m');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_mp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_n');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_ns');
            INSERT INTO CUT(CUT_PARAM) VALUES('Lv_o');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_gs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Man_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcd_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_as');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mcs_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ml_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtd_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mtp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_as');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Mts_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pat_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_fs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph1_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph2_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph2_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph2_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ph2_hp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pis_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pis_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pis_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pis_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pis_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pyr_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pyr_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pyr_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pyr_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Pyr_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rd_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_fs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rp_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Rs_cs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sac_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_as');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sc_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sca_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sca_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Sca_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ses_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_cs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tal_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_as');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_f p');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_f s');
            INSERT INTO CUT(CUT_PARAM) VALUES('Td_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tp_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_ds');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_ep');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ts_es');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_as');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_cp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_dp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_ds');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_es');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_fp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_gp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_hp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_j');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_k');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_l');
            INSERT INTO CUT(CUT_PARAM) VALUES('Tv_lp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Ud_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Unc_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Unc_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_bp');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_c');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_d');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_e');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_f');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_g');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_h');
            INSERT INTO CUT(CUT_PARAM) VALUES('Up_i');
            INSERT INTO CUT(CUT_PARAM) VALUES('Us_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Us_ap');
            INSERT INTO CUT(CUT_PARAM) VALUES('Us_b');
            INSERT INTO CUT(CUT_PARAM) VALUES('Us_bs');
            INSERT INTO CUT(CUT_PARAM) VALUES('Vest_a');
            INSERT INTO CUT(CUT_PARAM) VALUES('Vest_as');

            INSERT INTO TParam(Tapho_Name) VALUES('C_cren');
            INSERT INTO TParam(Tapho_Name) VALUES('C_furr');
            INSERT INTO TParam(Tapho_Name) VALUES('C_pit');
            INSERT INTO TParam(Tapho_Name) VALUES('C_punct');
            INSERT INTO TParam(Tapho_Name) VALUES('C_scoop');
            INSERT INTO TParam(Tapho_Name) VALUES('C_scor');

            INSERT INTO TParam(Tapho_Name) VALUES('P_cort');
            INSERT INTO TParam(Tapho_Name) VALUES('P_flake');
            INSERT INTO TParam(Tapho_Name) VALUES('P_mark');
            INSERT INTO TParam(Tapho_Name) VALUES('P_oppo');
            INSERT INTO TParam(Tapho_Name) VALUES('P_peel');
            INSERT INTO TParam(Tapho_Name) VALUES('P_scar');
            INSERT INTO TParam(Tapho_Name) VALUES('P_spong');
            INSERT INTO TParam(Tapho_Name) VALUES('P_tooth');

            INSERT INTO TParam(Tapho_Name) VALUES('Ret');
            INSERT INTO TParam(Tapho_Name) VALUES('Rodent');
            INSERT INTO TParam(Tapho_Name) VALUES('Sheet');
            INSERT INTO TParam(Tapho_Name) VALUES('Tramp');
            INSERT INTO TParam(Tapho_Name) VALUES('BoneTool');
            INSERT INTO TParam(Tapho_Name) VALUES('Chop');
            INSERT INTO TParam(Tapho_Name) VALUES('CorDig');
            INSERT INTO TParam(Tapho_Name) VALUES('Cut');



            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_01');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_02');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_03');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_04');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_05');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_06');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_07');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_08');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_09');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_10');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_11');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_12');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_13');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_14');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_15');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_16');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_17');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_18');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_19');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_20');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_21');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_22');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_23');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_24');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_25');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_26');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_27');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_28');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_29');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_30');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_31');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_31a');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_31b');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_32');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_33');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_34');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_35');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_36');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_37');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_38');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_38tymp');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_39');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_40');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_40basi');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_40cera');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_40thyr');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_41');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_42');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_43');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_44');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_45');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_46');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_47');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_48');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_49');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_50');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_51');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_52');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_53');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_54');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_55');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_56');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_57');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_58');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_59');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_60');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_61');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_62');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_63');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_63cen');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_63pis');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_63rad');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_64');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_64cap');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_64tra');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_64trapd');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_65');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_66');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_67');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_68');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_69');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_70');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_71');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_71de');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_71ds');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_71pe');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_71ps');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_72');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_73');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_74');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_75');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_76');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_77');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_77acc');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_77cub');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_77nav');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_78');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_78first');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_78int');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_78med');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_78sec');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_79');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_80');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_81');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_82');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_83');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_84');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_85');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_86');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_87');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_88mesRib');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_89mesRad');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_90mesMan');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_91mesFem');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_92ph1');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_93ph2');
            INSERT INTO Nde(Nde_Param) VALUES('Ldmk_94ph3');
            """)                  
            conn.commit()
            cursor.close()
            conn.close()
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la base de données : {e}")





