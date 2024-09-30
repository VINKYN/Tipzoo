from .DatabaseModel import Database


class SpeciesModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()


    def All_Species(self):
        query = "SELECT * FROM Species"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description
    
    def get_By_Id(self, id):
        query = f"SELECT * FROM Species Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_column(self,id,colonne):
        query = f"SELECT {colonne} FROM Species Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def insert_Species(self,id):
        query = f"Insert Into Species(Base_pk) Values({id});"
        self.db.cursor.execute(query)
        self.db.connection.commit()
    
    def get_count(self):
        query ="Select Count(*) From Species ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def update_taxon(self,id,taxon):
        query = f'Update Species set Species_Taxon = "{taxon}" Where Base_pk ={id};'
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def update_Obs(self,id,obs):
        query = f'Update Species set Species_ObsTaxon = "{obs}" Where Base_pk ={id};'
        self.db.cursor.execute(query)
        self.db.connection.commit()
    
    def get_species(self):
        query = f"SELECT Distinct Species_Taxon FROM Species"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def delete(self,id):
        query = f"Delete from Species Where Base_pk = {id}"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def get(self,id):
        query = f"SELECT * FROM Species Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def getCheck(self,id):
        query = f"SELECT Species_CheckImprove FROM Species Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def update_CI(self,val,id):
        query = f'Update Species set Species_CheckImprove = "{val}" Where Base_pk ={id};'
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def getAll(self):
        query = f"SELECT Species_Taxon FROM Species;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
