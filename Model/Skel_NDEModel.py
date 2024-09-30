from .DatabaseModel import Database


class SkelNdeModel:
    def __init__(self, db_file):
        self.db = Database(db_file)
        self.db.connect()

    def All_NDE(self):
        query = """SELECT b.Base_pk , n.NDE_Param, sn.Value
                    FROM Skel sk , Skel_NDE sn , Base b , NDE n
                    WHERE b.Base_pk = sk.Base_pk
                    AND sk.Skel_ID = sn.Skel_ID
                    AND sn.NDE_ID = n.Nde_ID"""
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall(),self.db.cursor.description
    
    def val_NDE(self,val):
        query = f"""SELECT b.Base_pk , n.NDE_Param, sn.Value
                    FROM Skel sk , Skel_NDE sn , Base b , NDE n , Species s
                    WHERE b.Base_pk = sk.Base_pk
                    AND sk.Skel_ID = sn.Skel_ID
                    AND s.Base_pk = b.Base_pk
                    AND sn.NDE_ID = n.Nde_ID
                    AND s.Species_Taxon = '{val}'"""
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


    def get_By_Id(self, id):
        query = f"SELECT * FROM Skel_NDE Where Skel_id = {id}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_val(self, id,idnde):
        query = f"SELECT Value FROM Skel_NDE Where Skel_id = {id} ANd NDE_ID = {idnde}"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def get_count(self):
        query ="Select Count(*) From Skel_NDE ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()[0][0]
    
    def insert_Skel_Nde(self,id,idnde,val):
        query = f"Insert Into Skel_Nde(Skel_ID,NDE_ID,Value) Values({id},{idnde},'{val}');"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def delete_Skel_Nde(self, id, idnde):
        query = f"DELETE FROM Skel_Nde WHERE Skel_ID = {id} AND NDE_ID = {idnde};"
        self.db.cursor.execute(query)
        self.db.connection.commit()


    def delete_Skel_Nde_All(self,id):
        query = f"DELETE FROM Skel_Nde WHERE Skel_ID = {id};"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def get(self,id ,idnde):
        query =f"Select * From Skel_NDE WHERE Skel_ID = {id} AND NDE_ID = {idnde} ;"
        self.db.cursor.execute(query)
        liste_res= self.db.cursor.fetchall()
        if liste_res :
            return float(liste_res[0][2])
        else :
            return float(0)
        
    def getNde(self,idsk):
        query =f"Select * From Skel_NDE WHERE Skel_ID = {idsk} ;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
        
