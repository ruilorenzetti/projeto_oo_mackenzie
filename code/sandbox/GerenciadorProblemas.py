from abc import ABC, abstractmethod
from ConectaBancoDeDados import *

class Problema:
    def __init__(self, descricao, sla):
        self.descricao = descricao
        self.sla = sla

class ProblemaDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, problema):
        pass

    @abstractmethod
    def visualizar(self, problema_id):
        pass

    @abstractmethod
    def alterar(self, problema):
        pass

    @abstractmethod
    def excluir(self, problema_id):
        pass

class SQLiteProblemaDAO(ProblemaDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS problemas
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT NOT NULL,
                        sla INT NOT NULL)''')
        conexao.commit()

    def inserir(self, problema):
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

    def alterar(self, problema):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE problemas SET descricao = (?) WHERE id = (?)', (problema.descricao, problema.id))

    def excluir(self, problema_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM problemas WHERE id = (?)', (problema_id,))
        conexao.commit()

class ProblemaController():
    def __init__(self):
        self.conexao = ConectaBanco("problemas.db")
        self.problema_dao = SQLiteProblemaDAO(self.conexao)
        self.problema_dao.criar_tabela()

    def criar_problema(self, problema):
        self.problema_dao.inserir(problema)

    def visualizar_problema(self, problema_id):
        return self.problema_dao.visualizar(problema_id)

    def alterar_problema(self, problema):
        self.problema_dao.alterar(problema)

    def excluir_problema(self, problema_id):
        self.problema_dao.excluir(problema_id)