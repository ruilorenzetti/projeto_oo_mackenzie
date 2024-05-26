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

class SQLiteUsuarioDAO(UsuarioDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            senha TEXT NOT NULL,
                            cargo TEXT NOT NULL)''')

    def inserir(self, usuario: Usuario):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO usuarios (nome, email, senha, cargo) 
                              VALUES (?, ?, ?, ?)''',
                           (usuario.nome, usuario.email, usuario.senha, usuario.cargo))

    def visualizar(self, usuario_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
            return cursor.fetchone()

    def alterar(self, usuario: Usuario):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE usuarios 
                              SET nome = ?, email = ?, senha = ?, cargo = ? 
                              WHERE id = ?''',
                           (usuario.nome, usuario.email, usuario.senha, usuario.cargo, usuario.id))

    def excluir(self, usuario_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()
