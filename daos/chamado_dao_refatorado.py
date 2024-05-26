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
    def atribuir_atendente(self, chamado: Chamado):
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

class SQLiteChamadoDAO(ChamadoDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS chamados
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            descricao TEXT NOT NULL,
                            status TEXT NOT NULL,
                            data_abertura TEXT NOT NULL,
                            data_max TEXT NOT NULL,
                            data_fechamento TEXT NOT NULL)''')

    def abrir(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO chamados (titulo, descricao, status, data_abertura, data_max, data_fechamento) 
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento))

    def atribuir_atendente(self, chamado: Chamado):
        self._atualizar_status(chamado)

    def alterar_status(self, chamado: Chamado):
        self._atualizar_status(chamado)

    def fechar(self, chamado: Chamado):
        self._atualizar_status(chamado)

    def visualizar(self, chamado_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM chamados WHERE id = ?', (chamado_id,))
            return cursor.fetchone()

    def alterar(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE chamados 
                              SET titulo = ?, descricao = ?, status = ?, data_abertura = ?, data_max = ?, data_fechamento = ?
                              WHERE id = ?''',
                           (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento, chamado.id))

    def excluir(self, chamado_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM chamados WHERE id = ?', (chamado_id,))

    def _atualizar_status(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('UPDATE chamados SET status = ? WHERE id = ?', (chamado.status, chamado.id))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()
