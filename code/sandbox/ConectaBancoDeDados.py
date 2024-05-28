from abc import ABC, abstractmethod
import sqlite3

#Definição de uma classe para conexão com o banco de dados
class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    #Método para obter uma conexão com o banco de dados SQLite
    def get_conexao(self):
        return sqlite3.connect(self.db_name)