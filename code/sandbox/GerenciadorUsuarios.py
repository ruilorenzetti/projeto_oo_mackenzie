from abc import ABC, abstractmethod
from ConectaBancoDeDados import *

class Usuario:
    def __init__(self, id, nome, email, senha, cargo):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

    def __str__(self):
        return f'Usuario(id={self.id}, nome={self.nome}, email={self.email}, cargo={self.cargo})'

    def __repr__(self):
        return self.__str__()

class UsuarioDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, usuario):
        pass

    @abstractmethod
    def visualizar(self, usuario_id):
        pass

    @abstractmethod
    def alterar(self, usuario):
        pass

    @abstractmethod
    def excluir(self, usuario_id):
        pass

    @abstractmethod
    def buscar_usuario_por_email(self, email):
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

    def inserir(self, usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO usuarios (nome, email, senha, cargo) VALUES (?, ?, ?, ?)''',
                       (usuario.nome, usuario.email, usuario.senha, usuario.cargo))
        conexao.commit()

    def visualizar(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
        return cursor.fetchall()

    def alterar(self, usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE usuarios SET nome = ?, email = ?, senha = ?, cargo = ? WHERE id = ?',
                       (usuario.nome, usuario.email, usuario.senha, usuario.cargo, usuario.id))
        conexao.commit()

    def excluir(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
        conexao.commit()

    def buscar_usuario_por_email(self, email):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome, email, senha, cargo FROM usuarios WHERE email = ?', (email,))
        row = cursor.fetchone()
        if row:
            return Usuario(*row)
        return None

class UsuarioController:
    def __init__(self):
        self.conexao = ConectaBanco("banco.db")
        self.usuario_dao = SQLiteUsuarioDAO(self.conexao)
        self.usuario_dao.criar_tabela()

    def criar_usuario(self, usuario):
        self.usuario_dao.inserir(usuario)

    def visualizar_usuario(self, usuario_id):
        return self.usuario_dao.visualizar(usuario_id)

    def alterar_usuario(self, usuario):
        self.usuario_dao.alterar(usuario)

    def excluir_usuario(self, usuario_id):
        self.usuario_dao.excluir(usuario_id)

    def buscar_usuario_por_email(self, email):
        return self.usuario_dao.buscar_usuario_por_email(email)