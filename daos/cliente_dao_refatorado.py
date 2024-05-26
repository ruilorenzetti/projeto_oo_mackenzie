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

class SQLiteClienteDAO(ClienteDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            empresa TEXT NOT NULL,
                            telefone TEXT NOT NULL)''')

    def inserir(self, cliente: Cliente):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO clientes (nome, email, empresa, telefone) 
                              VALUES (?, ?, ?, ?)''',
                           (cliente.nome, cliente.email, cliente.empresa, cliente.telefone))

    def visualizar(self, cliente_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
            return cursor.fetchone()

    def alterar(self, cliente: Cliente):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE clientes 
                              SET nome = ?, email = ?, empresa = ?, telefone = ? 
                              WHERE id = ?''',
                           (cliente.nome, cliente.email, cliente.empresa, cliente.telefone, cliente.id))

    def excluir(self, cliente_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()
