from .DatabaseModel import Database
import pandas as pd

class SpatialModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_Spatial(self):
        query ="Select * From Spatial ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description

    def get_By_Id(self, id):
        query = f"SELECT Spatial_year, Spatial_Code, Spatial_FieldID,Spatial_Square_field,Spatial_Dec,Spatial_USfield,Spatial_Group1 FROM Spatial Where Spatial_FieldID = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def update_by_id(self,val,id):
        query=f"Update Spatial set Base_pk = {val}  where Spatial_FieldID = {id};"
        print(query)
        self.db.cursor.execute(query)
        self.db.connection.commit()        
    
    def get_count(self):
        query ="Select Count(*) From Spatial ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def deleteAll(self):
        query ="Delete From Spatial;"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def get_fab(self,id):
        query = f"SELECT Spatial_FabID FROM Spatial Where Spatial_FieldID = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
 



    
    """
    def insert_spatial(self,Year,fieldID,Code,Square_field,Square_true,Dec,USfield,FabID,X,Y,Z,Group1,Group2,Group3,base):
        print('yo')
        print(Year,fieldID,Code,Square_field,
                                     Square_true,Dec,USfield,FabID,
                                     X,Y,Z,Group1,Group2,Group3,base)
        
        query=f'Insert into Spatial Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
        self.db.cursor.execute(query(Year,fieldID,Code,Square_field,
                                     Square_true,Dec,USfield,FabID,
                                     X,Y,Z,Group1,Group2,Group3,base))
        self.db.connection.commit()
        print('yahouuu')
    

    def insert_spatial(self, Year, fieldID, Code, Square_field, Square_true, Dec, USfield, FabID, X, Y, Z, Group1, Group2, Group3, base):
        print(Year, fieldID, Code, Square_field, Square_true, Dec, USfield, FabID, X, Y, Z, Group1, Group2, Group3, base)
        
        query = 'INSERT INTO Spatial VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
        values = (Code,Dec,FabID, Square_field, Square_true,  USfield, X, Y, Z,Year, Group1, Group2, Group3, base)
        self.db.cursor.execute(query, values)
        self.db.connection.commit()
        print('yahouuu')"""
    

    def insert_spatial(self, year, fieldID, code, square_field, square_true, dec, usfield, fabID, x, y, z, group1, group2, group3, base_pk):
        query="""
            INSERT INTO Spatial (Spatial_year,Spatial_FieldID, Spatial_FabID, Spatial_Code, Spatial_Square_field, Spatial_Square_true,
                                Spatial_Dec, Spatial_USfield,X, Y, Z, Spatial_Group1, Spatial_Group2,
                                Spatial_Group3, Base_pk)
            VALUES (?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.cursor.execute(query,(year, fieldID, code, square_field, square_true, dec, usfield, fabID, x, y, z, group1, group2, group3, base_pk))
        self.db.connection.commit()

