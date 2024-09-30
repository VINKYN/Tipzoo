from .DatabaseModel import Database


class TeethModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_teeth(self):
        query ="Select * From teeth ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description

    def get_By_Id(self, id):
        query = f"SELECT Teeth_ID,Teeth_LowerUpper,Teeth_Side,Teeth_Type,Teeth_Dentition,Teeth_Class,Teeth_Number,Teeth_Portion,Teeth_OccSup50 FROM Teeth Where Skel_id = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From teeth ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def update_teeth(self,id,val,colonne):
        query = f"Update teeth set {colonne} = ? Where Base_pk =?;"
        self.db.execute_query(query,(id,val))


    def update_col(self,colonne,val,id):
        query = f"Update Teeth set '{colonne}' = ? where Teeth_id = ? ;"
        self.db.cursor.execute(query,(val,id,))
        self.db.connection.commit()
        print('update '+str(colonne)+' ' +str(val))
    
    def insert_Teeth(self,id):
        query = f"INSERT INTO Teeth('SKEL_ID') VALUES ({id});"        
        self.db.cursor.execute(query)
        self.db.connection.commit()
        return self.db.cursor.lastrowid
    
    def get_column(self,id,column):
        query = f"SELECT {column} FROM Teeth Where Teeth_id = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def delete(self,id):
        query =f"Delete From Teeth Where Teeth_id = {id};"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def delete_all(self,id):
        query =f"Delete From Teeth Where Skel_id = {id};"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def get(self,idsk):
        query = f"SELECT * FROM Teeth Where Skel_id = {idsk}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


   