from .DatabaseModel import Database


class RefitsModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def get_By_Id(self, id):
        query = f"SELECT * FROM Refits Where Base_pk1 = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Refits ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def delete_Cut_Base(self ,id1,id2):
        query = f"Delete from Refits Where Base_pk1 = ? And Base_pk2 = ?"
        self.db.cursor.execute(query,(id1,id2))

    def update_Type(self,param , id1,id2):
        query = "Update Refits set Refits_Type = ? Where Base_pk1 = 1 And Base_pk2 = id2;"
        self.db.execute_query(query,(param,id1,id2))
    
    def insert_Refits(self,id1,id2,typeR):
        query = "Insert Into Refits(Base_pk1 , Base_pk2 , type) Values(?,?,?)"
        self.db.execute_query(query,(id1,id2,typeR))

    def delete(self,id):
        query = f"Delete from Refits Where Base_pk = {id}'"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def get(self,id):
        query = f"SELECT * FROM Refits Where Base_pk1 = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
