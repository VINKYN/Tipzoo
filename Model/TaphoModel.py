from .DatabaseModel import Database


class TaphoModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def get_By_Id(self, id):
        query = f"SELECT * FROM Tapho Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Tapho ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def update_tapho(self,id,val,colonne):
        query = f"Update Species set {colonne} = ? Where Base_pk =?;"
        self.db.execute_query(query,(id,val))
    
    def insert_Refits(self,id,taxon):
        query = "Insert Into Tapho(Base_pk,Species_taxon) Values(?)"
        self.db.execute_query(query,id)
