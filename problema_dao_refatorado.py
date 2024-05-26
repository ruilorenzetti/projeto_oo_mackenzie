# problema_dao.py
from abc import ABC, abstractmethod
from services.database_service import ConectaBanco
from models import Problema
import sqlite3

class ProblemaDAO(ABC):
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

class SQLiteProblemaDAO(ProblemaDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS problemas
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descricao TEXT NOT NULL,
                            sla TEXT NOT NULL)''')

    def inserir(self, problema: Problema):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO problemas (descricao, sla) VALUES (?, ?)''',
                           (problema.descricao, problema.sla))

    def visualizar(self, problema_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM problemas WHERE id = ?', (problema_id,))
            return cursor.fetchone()

    def alterar(self, problema: Problema):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE problemas SET descricao = ?, sla = ? WHERE id = ?''',
                           (problema.descricao, problema.sla, problema.id))

    def excluir(self, problema_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM problemas WHERE id = ?', (problema_id,))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()
