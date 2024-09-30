def get_database_path():
    fichier = 'Database/path.txt'
    with open(fichier, "r") as path:
        return "Database/" + path.read()+".sqlite3"


