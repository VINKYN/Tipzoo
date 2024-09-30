from .DatabaseModel import Database
import datetime
class BaseModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_Base(self):
        query = "SELECT * FROM Base"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description



    def get_By_Id(self, id):
        query = f"SELECT * FROM Base Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_All(self):
        query = f"SELECT DISTINCT b.Base_pk,b.Base_ID,b.Base_Square,b.Base_Sub,s.Species_Taxon,sk.Skel_Anat_Class, sk.Skel_Anat, sk.Skel_Side, sk.Skel_Anat_Detail, b.DateModif , b.DateModif FROM Base b LEFT JOIN Species s ON b.Base_pk = s.Base_pk LEFT JOIN Skel sk ON b.Base_pk = sk.Base_pk  WHERE b.Base_id is not Null  ORDER BY b.Base_pk DESC;"
        
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_sqr(self):
        query =f"Select Distinct Base_Square from Base ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_next_sub(self,id):
        query=f"Select Base_Sub from Base where Base_ID = {id} ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_previous(self,id):
        query=f"Select Base_pk from Base where Base_pk < {id} Order by Base_pk Desc limit 1;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_next(self,id):
        query=f"Select Base_pk from Base where Base_pk > {id} Order by Base_pk Asc limit 1;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_Check(self,id):
        query=f"Select Base_CheckCode from Base where Base_pk = {id} ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    
    
    def get_column(self,colonne,id):
        query =f'Select {colonne} from Base where Base_pk = {id}'
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_All_order_by(self,colonne,order):
        query = f"SELECT DISTINCT b.Base_pk,b.Base_ID,b.Base_Square,b.Base_Sub,s.Species_Taxon,sk.Skel_Anat_Class, sk.Skel_Anat, sk.Skel_Side, sk.Skel_Anat_Detail, b.DateModif , b.DateModif FROM Base b LEFT JOIN Species s ON b.Base_pk = s.Base_pk LEFT JOIN Skel sk ON b.Base_pk = sk.Base_pk WHERE b.Base_id is not Null ORDER BY {colonne} {order};"
        
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_Search(self,val):
        query = f"SELECT DISTINCT b.Base_pk,b.Base_ID,b.Base_Square,b.Base_Sub,s.Species_Taxon,sk.Skel_Anat_Class, sk.Skel_Anat, sk.Skel_Side, sk.Skel_Anat_Detail, b.DateModif , b.DateModif FROM Base b LEFT JOIN Species s ON b.Base_pk = s.Base_pk LEFT JOIN Skel sk ON b.Base_pk = sk.Base_pk WHERE b.Base_id is not Null AND b.Base_ID LIKE '%{val}%' OR b.Base_Sub LIKE '%{val}%' OR b.Base_Square LIKE '%{val}%'"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_reset(self,id):
        query=f'Update Base set Color_ID = Null where Base_pk = {id};'
        self.db.cursor.execute(query)
        self.db.connection.commit()        
        self.update_date(id)


    def get_count(self):
        query ="Select Count(*) From Base ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def update_Base(self , colonne , valeur , id ):
        query = f"Update Base set '{colonne}' = ? where Base_pk = ? ;"
        self.db.cursor.execute(query,(valeur,id,))
        self.db.connection.commit()
        self.update_date(id)
        print('update'+str(colonne)+ str(valeur))

    def update_date(self,id):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        query = f"Update Base set DateModif = ? where Base_pk = ? ;"
        self.db.cursor.execute(query,(date,id,))
        self.db.connection.commit()

    def insert_Base(self,site):
        query ="INSERT INTO Base(Base_SiteName,Base_PlottedScreen,Base_Burnt,DateEnter) Values (?,'Plotted','No',?)"
        self.db.cursor.execute(query,(site,datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))
        self.db.connection.commit()
        return self.db.cursor.lastrowid

    def delete(self,id):
        query = f"Delete from Base Where Base_pk = {id}"
        self.db.cursor.execute(query)
        self.db.connection.commit()
        
    """Partie ALl Vues"""

    def get_Pragma(self,label):
        query = f"SELECT name FROM pragma_table_info('{label}');"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_all(self,label):
        query = f"Select * from '{label}' Order By 1 DESC;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    '''def insert_spatail(self,ligne):
        query ="""INSERT INTO Spatial (Spatial_Code, Spatial_Dec, Spatial_FabID, Spatial_Square_field, 
                   Spatial_Square_true, Spatial_USfield, X, Y, Z, Spatial_year, Spatial_Group1, Spatial_Group2, 
                   Spatial_Group3, Base_pk)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        self.db.cursor.execute(query,(ligne))'''
    
    def get(self,id):
        query = f"SELECT * FROM Base Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()




    def ExportSpecies(self):
        query = """	SELECT Distinct
                        b.Base_pk,b.Base_ID, b.Base_Sub, b.Base_SIZE, b.Base_PlottedScreen, b.Base_Observation,
                        sp.Spatial_Square_field, sp.Spatial_Dec, sp.Spatial_USfield, sp.Spatial_Group1, sp.Spatial_Group2,
                        sp.Spatial_Group3, sp.X, sp.Y, sp.Z, sp.Spatial_year,
                        s.Species_Taxon, s.Species_CheckImprove, s.Species_ObsTaxon,
                        sk.Skel_Anat_Class, sk.Skel_Anat, sk.Skel_Anat_Detail, sk.Skel_Frag, sk.Skel_AgeCort, sk.Skel_Spongy,
                        r.Base_pk2, r.REFITS_Type
                    FROM 
                        Base b
                    LEFT JOIN 
                        Species s ON b.Base_pk = s.Base_pk
                    LEFT JOIN 
                        Skel sk ON b.Base_pk = sk.Base_pk
                    LEFT JOIN 
                        Spatial sp ON b.Base_pk = sp.Base_pk
                    LEFT JOIN
                        Refits r ON b.Base_pk = r.Base_pk1;"""

        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    

    def ExportTeeth(self):
        query = """	SELECT Distinct
                       b.Base_pk,b.Base_ID, b.Base_Sub,
                        sp.Spatial_USfield, sp.Spatial_Group1, sp.Spatial_Group2,sp.Spatial_Group3,
                        s.Species_Taxon,
                        sk.Skel_Anat,
                        t.Teeth_ID ,t.Teeth_LowerUpper,t.Teeth_Dentition,t.Teeth_Type,t.Teeth_Class,t.Teeth_Number,t.Teeth_Side,
								t.Teeth_OccSup50,t.Teeth_FR,t.Teeth_Portion,t.Teeth_UW_Crown,t.Teeth_UW_Root,t.Teeth_UW_RootResorp ,t.Teeth_UW_AgeClass,t.Teeth_CH
                    FROM 
                        Base b 
                    LEFT JOIN 
                        Species s ON b.Base_pk = s.Base_pk
                    LEFT JOIN 
                        Skel sk ON b.Base_pk = sk.Base_pk
                    LEFT JOIN 
                        Spatial sp ON b.Base_pk = sp.Base_pk
                    LEFT JOIN
                        Refits r ON b.Base_pk = r.Base_pk1
                  	LEFT JOIN
								Teeth t ON sk.Skel_ID = t.SKEL_ID
							WHERE t.Teeth_ID is NOT null"""

        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    


    def ExportTeethval(self,val):
        query = f"""SELECT Distinct
                       b.Base_pk,b.Base_ID, b.Base_Sub,
                        sp.Spatial_USfield, sp.Spatial_Group1, sp.Spatial_Group2,sp.Spatial_Group3,
                        s.Species_Taxon,
                        sk.Skel_Anat,
                        t.Teeth_ID ,t.Teeth_LowerUpper,t.Teeth_Dentition,t.Teeth_Type,t.Teeth_Class,t.Teeth_Number,t.Teeth_Side,
								t.Teeth_OccSup50,t.Teeth_FR,t.Teeth_Portion,t.Teeth_UW_Crown,t.Teeth_UW_Root,t.Teeth_UW_RootResorp ,t.Teeth_UW_AgeClass,t.Teeth_CH
                    FROM 
                        Base b 
                    LEFT JOIN 
                        Species s ON b.Base_pk = s.Base_pk
                    LEFT JOIN 
                        Skel sk ON b.Base_pk = sk.Base_pk
                    LEFT JOIN 
                        Spatial sp ON b.Base_pk = sp.Base_pk
                    LEFT JOIN
                        Refits r ON b.Base_pk = r.Base_pk1
                  	LEFT JOIN
								Teeth t ON sk.Skel_ID = t.SKEL_ID
							WHERE t.Teeth_ID is NOT null
                            AND s.Species_Taxon = '{val}'"""
                        

        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    

    def ExportNDEval(self,val):
        query = f"""SELECT Distinct
                       b.Base_pk,b.Base_ID, b.Base_Sub,
                        sp.Spatial_USfield, sp.Spatial_Group1, sp.Spatial_Group2,sp.Spatial_Group3,
                        s.Species_Taxon,
                        sk.Skel_Anat_Class,sk.Skel_Anat,sk.Skel_Anat_Detail,sk.Skel_AgeCort,sk.Skel_AgeFus
                        From
                        Base b 
                    LEFT JOIN 
                        Species s ON b.Base_pk = s.Base_pk
                    LEFT JOIN 
                        Skel sk ON b.Base_pk = sk.Base_pk
                    LEFT JOIN 
                        Spatial sp ON b.Base_pk = sp.Base_pk
                    WHere s.Species_Taxon = '{val}'"""
                        
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    

    def ExportNDE(self):
        query = f"""SELECT Distinct
                       b.Base_pk,b.Base_ID, b.Base_Sub,
                        sp.Spatial_USfield, sp.Spatial_Group1, sp.Spatial_Group2,sp.Spatial_Group3,
                        s.Species_Taxon,
                        sk.Skel_Anat_Class,sk.Skel_Anat,sk.Skel_Anat_Detail,sk.Skel_AgeCort,sk.Skel_AgeFus
                        From
                        Base b 
                    LEFT JOIN 
                        Species s ON b.Base_pk = s.Base_pk
                    LEFT JOIN 
                        Skel sk ON b.Base_pk = sk.Base_pk
                    LEFT JOIN 
                        Spatial sp ON b.Base_pk = sp.Base_pk"""
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    


    