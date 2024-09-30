from .DatabaseModel import Database


class BoneColorModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_Color(self):
        query = "SELECT * FROM BoneColor"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description

    def get_all(self):
        query = f"SELECT * FROM BoneColor Order by 1 DESC"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From BoneColor ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def insert_Color(self):
        query = "INSERT INTO BoneColor(Color_Hexcode)Values('#ffffff')"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def delete(self,id):
        query = f"Delete from BoneColor Where Color_ID = {id}"
        self.db.cursor.execute(query)
        self.db.connection.commit()


    def update_column(self,column,id,val):
        query = f"Update BoneColor set '{column}' = '{val}' where Color_id = {id} ;"
        self.db.cursor.execute(query)
        self.db.connection.commit()