from .DatabaseModel import Database


class TaphoParamModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def get_By_Id(self, id):
        query = f"SELECT * FROM Tapho_Param Where Tapho_id = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Tapho_Param ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def update_taxon(self,Tapho_id,tParam_id,val):
        query = "Update Tapho_Param set Tapho_Param_Value = ? Where Tapho_id =? And TParam_Id = ?;"
        self.db.execute_query(query,(val,Tapho_id,tParam_id))
    
    def insert_Refits(self,Tapho_id,tParam_id):
        query = "Insert Into Tapho_Param(Tapho_id,tParam_id) Values(?,?)"
        self.db.execute_query(query,(Tapho_id,tParam_id))
