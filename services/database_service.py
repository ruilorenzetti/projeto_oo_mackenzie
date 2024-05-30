# database_service.py
import sqlite3

class ConectaBanco:
    def __init__(self):
        self.db_name = 'projeto_oo.db'

    def get_conexao(self):
        return sqlite3.connect(self.db_name)
