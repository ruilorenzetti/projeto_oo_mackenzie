from abc import ABC, abstractmethod
from ConectaBancoDeDados import *

class Cliente:
    def __init__(self, nome, email, empresa, telefone):
        self.nome = nome
        self.email = email
        self.empresa = empresa
        self.telefone = telefone

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
    def alterar(self, cliente):
        pass

    @abstractmethod
    def excluir(self, cliente_id):
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
                        telefone TEXT NOT NULL)''')
        conexao.commit()

    def inserir(self, cliente: Cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO clientes (nome,email,empresa,telefone) VALUES (?,?,?,?)''',
                        (cliente.nome, cliente.email, cliente.empresa, cliente.telefone))
        conexao.commit()

    def visualizar(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = (?)', (cliente_id,))
        return cursor.fetchall()

    def alterar(self, cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE clientes SET nome = (?) WHERE id = (?)', (cliente.nome, cliente.id))

    def excluir(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM clientes WHERE id = (?)', (cliente_id,))
        conexao.commit()

class ClienteController():
    def __init__(self):
        self.conexao = ConectaBanco("clientes.db")
        self.cliente_dao = SQLiteClienteDAO(self.conexao)
        self.cliente_dao.criar_tabela()

    def criar_cliente(self, cliente: Cliente):
        self.cliente_dao.inserir(cliente)

    def visualizar_cliente(self, cliente_id):
        return self.cliente_dao.visualizar(cliente_id)

    def alterar_cliente(self, cliente):
        self.cliente_dao.alterar(cliente)

    def excluir_cliente(self, cliente_id):
        self.cliente_dao.excluir(cliente_id)