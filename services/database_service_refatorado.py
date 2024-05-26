import sqlite3

class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_conexao(self):
        return sqlite3.connect(self.db_name)

    def __enter__(self):
        self.conexao = self.get_conexao()
        return self.conexao

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'conexao'):
            self.conexao.close()
