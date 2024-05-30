# cliente_dao.py
from abc import ABC, abstractmethod
from services.database_service import ConectaBanco
from models import Cliente
import sqlite3

class ClienteDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, cliente: Cliente):
        pass

    @abstractmethod
    def visualizar(self, cliente_id):
        pass

    @abstractmethod
    def alterar(self, cliente: Cliente):
        pass

    @abstractmethod
    def excluir(self, cliente_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

class SQLiteClienteDAO(ClienteDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        empresa TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        senha TEXT NOT NULL)''')
        conexao.commit()

    def inserir(self, cliente: Cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO clientes (nome,email,empresa,telefone,senha) VALUES (?,?,?,?,?)''',
                        (cliente.nome, cliente.email, cliente.empresa, cliente.telefone, cliente.senha))
        conexao.commit()
        cursor.execute('SELECT MAX(id) FROM clientes')
        id = cursor.fetchone()
        cliente.id = id

    def visualizar(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = (?)', (cliente_id,))
        return cursor.fetchall()

    def alterar(self, cliente: Cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE clientes SET nome = (?) WHERE id = (?)', (cliente.nome, cliente.id))
        conexao.commit()

    def excluir(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM clientes WHERE id = (?)', (cliente_id,))
        conexao.commit()

    def listar_todos(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()