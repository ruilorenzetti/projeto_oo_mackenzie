# database_service.py
import sqlite3

class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_conexao(self):
        return sqlite3.connect(self.db_name)
