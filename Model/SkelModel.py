from .DatabaseModel import Database


class SkelModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_Skel(self):
        query = f"SELECT * FROM Skel"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description


    def get_By_Id(self, id):
        query = f"SELECT * FROM Skel Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_Base_Id(self, id):
        query = f"SELECT Base_Pk FROM Skel Where Skel_id = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Skel ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    """def update_Skel(self,colonne,param):
        query = f"Update Skel set {colonne} = ? ;"
        self.db.execute_query(query,param)"""

    def get_column(self,id,column):
        query = f"SELECT {column} FROM Skel Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    
    def insert_Skel(self,id,anat_class):
        query = f"Insert Into Skel(Skel_Spongy,Skel_Anat_Class,Base_pk) Values(0,'{anat_class}',{id});"
        self.db.cursor.execute(query)
        self.db.connection.commit()


    def update_Skel(self,id,colonne , val):
        query = f"Update Skel set '{colonne}' = ? where Base_pk = ? ;"
        self.db.cursor.execute(query,(val,id,))
        self.db.connection.commit()
        print('update '+str(colonne)+' ' +str(val))


    def delete(self,id):
        query = f"Delete from Skel Where Base_pk = {id}"
        self.db.cursor.execute(query)
        self.db.connection.commit()
    
    def get_id(self,id):
        query = f"Select Skel_Id from Skel Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def getcat(self,id):
        query = f"Select Skel_Anat_Class from Skel Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


        