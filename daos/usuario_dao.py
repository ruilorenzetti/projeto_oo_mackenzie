# usuario_dao.py
from abc import ABC, abstractmethod
from services.database_service import ConectaBanco
from models import Usuario
import sqlite3

class UsuarioDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, usuario: Usuario):
        pass

    @abstractmethod
    def visualizar(self, usuario_id):
        pass

    @abstractmethod
    def alterar(self, usuario: Usuario):
        pass

    @abstractmethod
    def excluir(self, usuario_id):
        pass
    @abstractmethod
    def listar_todos(self):
        pass


class SQLiteUsuarioDAO(UsuarioDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        cargo TEXT NOT NULL)''')
        conexao.commit()

    def inserir(self, usuario: Usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO usuarios (nome,email,senha,cargo) VALUES (?,?,?,?)''',
                        (usuario.nome, usuario.email, usuario.senha, usuario.cargo))
        conexao.commit()
        cursor.execute('SELECT MAX(id) FROM usuarios')
        id = cursor.fetchall()
        usuario.id = id

    def visualizar(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = (?)', (usuario_id,))
        return cursor.fetchall()

    def alterar(self, usuario: Usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE usuarios SET nome = (?) WHERE id = (?)', (usuario.nome, usuario.id))
        conexao.commit()

    def excluir(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = (?)', (usuario_id,))
        conexao.commit()

    def listar_todos(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()