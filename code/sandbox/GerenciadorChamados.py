from abc import ABC, abstractmethod
from ConectaBancoDeDados import *

from abc import ABC, abstractmethod
from ConectaBancoDeDados import *

class Chamado:
    def __init__(self, id, titulo, descricao, status, data_abertura, data_max, data_fechamento, nome_cliente, email_cliente, empresa_cliente, telefone_cliente, atendente_name):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura
        self.data_max = data_max
        self.data_fechamento = data_fechamento
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.empresa_cliente = empresa_cliente
        self.telefone_cliente = telefone_cliente
        self.atendente_name = atendente_name  # Novo campo para armazenar o nome do atendente

class ChamadoDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def abrir(self, chamado):
        pass

    @abstractmethod
    def atribuir_atendente(self, chamado):
        pass

    @abstractmethod
    def alterar_status(self, chamado):
        pass

    @abstractmethod
    def fechar(self, chamado):
        pass

    @abstractmethod
    def visualizar(self, chamado_id):
        pass

    @abstractmethod
    def alterar(self, chamado):
        pass

    @abstractmethod
    def excluir(self, chamado_id):
        pass

class SQLiteChamadoDAO(ChamadoDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL,
                data_abertura DATE NOT NULL,
                data_max DATE NOT NULL,
                data_fechamento DATE,
                nome_cliente TEXT NOT NULL,
                email_cliente TEXT NOT NULL,
                empresa_cliente TEXT NOT NULL,
                telefone_cliente TEXT NOT NULL,
                atendente_name TEXT NOT NULL 
            )
        ''')
        conexao.commit()

    def abrir(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO chamados (
                titulo, descricao, status, data_abertura, data_max, data_fechamento,
                nome_cliente, email_cliente, empresa_cliente, telefone_cliente, atendente_name
            ) VALUES (?, ?, ?, ?, ?, NULL, ?, ?, ?, ?, ?)
        ''', (
            chamado.titulo, chamado.descricao, chamado.status,
            chamado.data_abertura, chamado.data_max,
            chamado.nome_cliente, chamado.email_cliente, chamado.empresa_cliente, chamado.telefone_cliente, chamado.atendente_name
        ))
        conexao.commit()

    def visualizar(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM chamados WHERE id = ?', (chamado_id,))
        row = cursor.fetchone()
        if row:
            return Chamado(*row)
        return None

    def atribuir_atendente(self, chamado, atendente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET atendente_id = ? WHERE id = ?', (atendente_id, chamado.id))
        conexao.commit()

    def alterar_status(self, chamado, novo_status):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET status = ? WHERE id = ?', (novo_status, chamado.id))
        conexao.commit()

    def fechar(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET status = "Fechado", data_fechamento = CURRENT_DATE WHERE id = ?', (chamado.id,))
        conexao.commit()

    def alterar(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET titulo = ?, descricao = ?, status = ?, data_abertura = ?, data_max = ?, data_fechamento = ?, nome_cliente = ?, email_cliente = ?, empresa_cliente = ?, telefone_cliente = ?, atendente_name = ? WHERE id = ?',
                       (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento, chamado.nome_cliente, chamado.email_cliente, chamado.empresa_cliente, chamado.telefone_cliente, chamado.atendente_name, chamado.id))
        conexao.commit()

    def excluir(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM chamados WHERE id = ?', (chamado_id,))
        conexao.commit()

    def listar_chamados(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT id, titulo, descricao, status, data_abertura, data_max, data_fechamento, nome_cliente, email_cliente, empresa_cliente, telefone_cliente, atendente_name FROM chamados')
        rows = cursor.fetchall()
        return [Chamado(id=row[0], titulo=row[1], descricao=row[2], status=row[3], data_abertura=row[4], data_max=row[5], data_fechamento=row[6], nome_cliente=row[7], email_cliente=row[8], empresa_cliente=row[9], telefone_cliente=row[10], atendente_name=row[11]) for row in rows]

class ChamadoController():
    def __init__(self):
        self.conexao = ConectaBanco("banco.db")  # Assume que a classe ConectaBanco realiza a conexão com o SQLite
        self.chamado_dao = SQLiteChamadoDAO(self.conexao)
        self.chamado_dao.criar_tabela()

    def criar_chamado(self, chamado):
        self.chamado_dao.abrir(chamado)

    def atribuir_atendente_chamado(self, chamado, atendente_id):
        self.chamado_dao.atribuir_atendente(chamado, atendente_id)

    def alterar_status_chamado(self, chamado, novo_status):
        self.chamado_dao.alterar_status(chamado, novo_status)

    def fechar_chamado(self, chamado):
        self.chamado_dao.fechar(chamado)

    def visualizar_chamado(self, chamado_id):
        return self.chamado_dao.visualizar(chamado_id)

    def alterar_chamado(self, chamado):
        self.chamado_dao.alterar(chamado)

    def excluir_chamado(self, chamado_id):
        self.chamado_dao.excluir(chamado_id)

    def listar_chamados(self):
        return self.chamado_dao.listar_chamados()