from .DatabaseModel import Database

class ParamModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def get_params(self,colonne):
        query = f"SELECT {colonne} FROM Param"
        result = self.db.cursor.execute(query)
        return result.fetchall()
    

    def update_Param(self,colonne,param):
        query = f"Update Param set '{colonne}' = ? ;"
        self.db.cursor.execute(query,(param,))
        self.db.connection.commit()

