import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()