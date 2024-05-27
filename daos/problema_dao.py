# problema_dao.py
from abc import ABC, abstractmethod
from services.database_service import ConectaBanco
from models import Problema
import sqlite3

class CategoriaProblemaDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, problema: Problema):
        pass

    @abstractmethod
    def visualizar(self, problema_id):
        pass

    @abstractmethod
    def alterar(self, problema: Problema):
        pass

    @abstractmethod
    def excluir(self, problema_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

class SQLiteCategoriaProblemaDAO(CategoriaProblemaDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS problemas
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT NOT NULL,
                        sla TEXT NOT NULL)''')
        conexao.commit()

    def inserir(self, problema: Problema):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO problemas (descricao,sla) VALUES (?,?)''',
                        (problema.descricao, problema.sla))
        conexao.commit()

    def visualizar(self, problema_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM problemas WHERE id = (?)', (problema_id,))
        return cursor.fetchall()

    def alterar(self, problema: Problema):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE problemas SET descricao = (?) WHERE id = (?)', (problema.descricao, problema.id))
        conexao.commit()

    def excluir(self, problema_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM problemas WHERE id = (?)', (problema_id,))
        conexao.commit()

    def listar_todos(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM problemas')
        return cursor.fetchall()