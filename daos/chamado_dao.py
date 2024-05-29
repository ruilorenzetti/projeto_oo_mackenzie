# chamado_dao.py
from abc import ABC, abstractmethod
from services.database_service import ConectaBanco
from models import Chamado
import sqlite3

class ChamadoDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def abrir(self, chamado: Chamado):
        pass

    @abstractmethod
    def atribuir_atendente(self, chamado_id, usuario_id):
        pass

    @abstractmethod
    def alterar_status(self, chamado: Chamado):
        pass

    @abstractmethod
    def fechar(self, chamado: Chamado):
        pass

    @abstractmethod
    def visualizar(self, chamado_id):
        pass

    @abstractmethod
    def alterar(self, chamado: Chamado):
        pass

    @abstractmethod
    def excluir(self, chamado_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def listar_todos_por_categoria_problema(self, id_categoria):
        pass


class SQLiteChamadoDAO(ChamadoDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chamados
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        descricao TEXT NOT NULL,
                        id_categoria INT NOT NULL,
                        id_cliente INT NOT NULL,
                        id_usuario INT,
                        status TEXT NOT NULL,
                        data_abertura DATE NOT NULL,
                        data_max DATE NOT NULL,
                        data_fechamento DATE)''')
        conexao.commit()

    def abrir(self, chamado: Chamado):
        try:
            conexao = self.db_conexao.get_conexao()
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO chamados (titulo,descricao,status,data_abertura,data_max, data_fechamento,id_categoria,id_cliente,id_usuario) VALUES (?,?,?,?,?,?,?,?,?)''',
                            (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento, chamado.id_categoria, chamado.id_cliente, chamado.id_usuario))
            conexao.commit()
            conexao = self.db_conexao.get_conexao()
            cursor.execute('SELECT MAX(id) FROM chamados')
            id = cursor.fetchone()
            chamado.id = id
        except Exception as e:
            print(e)
        
    def atribuir_atendente(self, chamado_id, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''UPDATE chamados SET id_usuario = (?), status = 'Atribuído' WHERE id = (?)''', (usuario_id, chamado_id))
        conexao.commit()

    def alterar_status(self, chamado: Chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''UPDATE chamados SET status = (?) WHERE id = (?)''', (chamado.status, chamado.id))
        conexao.commit()

    def fechar(self, chamado: Chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''UPDATE chamados SET status = (?) WHERE id = (?)''', (chamado, chamado.id))
        conexao.commit()

    def visualizar(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id AND c.id = (?)', (chamado_id,))
        return cursor.fetchall()

    def alterar(self, chamado: Chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET titulo = (?) WHERE id = (?)', (chamado.titulo, chamado.id))
        conexao.commit()

    def excluir(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM chamados WHERE id = (?)', (chamado_id,))
        conexao.commit()

    def listar_todos(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id')
        return cursor.fetchall()

    #TODO falta colocar o join no metodo abaixo
    def listar_todos_por_categoria_problema(self, id_categoria):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM chamados WHERE id_categoria = (?)', (id_categoria,))
        return cursor.fetchall()