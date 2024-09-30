from .DatabaseModel import Database


class CutBaseModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def get_By_Id(self, id):
        query = f"SELECT * FROM Cut_Base Where Base_pk = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Cut_Base ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def delete_Cut_Base(self ,id_cut,id_Base):
        query = f"Delete from Cut_Base Where Cut_id = ? And Base_pk = ?"
        self.db.cursor.execute(query,(id_cut,id_Base))

    def insert_Cut_Base(self,id_cut , id_base):
        query ="INSERT INTO Cut_Base(Cut_id , Base_Pk) Values (?,?)"
        self.db.cursor.execute(query,(id_cut,id_base))
