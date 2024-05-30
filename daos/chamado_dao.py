# chamado_dao.py
from daos.TIPO_ESTADO_CHAMADO import TIPO_ESTADO_CHAMADO
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
    def visualizar_chamado_cliente(self, chamado_id):
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
    def listar_todos_por_cliente(self, id_cliente):
        pass

    @abstractmethod
    def listar_todos_por_categoria_problema(self, id_categoria):
        pass
    
    @abstractmethod
    def listar_todos_por_status(self, status:TIPO_ESTADO_CHAMADO):
        pass

    @abstractmethod
    def listar_todos_por_status_e_cliente(self, status:TIPO_ESTADO_CHAMADO, id_cliente):
        pass

class SQLiteChamadoDAO(ChamadoDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chamados
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        descricao TEXT NOT NULL,
                        id_categoria INT,
                        id_cliente INT NOT NULL,
                        id_usuario INT,
                        status TEXT NOT NULL,
                        data_abertura DATE NOT NULL,
                        data_max DATE,
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
        cursor.execute('''
            SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente, 
                c.id_usuario, c.status, c.data_abertura, c.data_max, 
                c.data_fechamento, p.descricao, p.sla 
            FROM chamados c
            LEFT JOIN problemas p ON c.id_categoria = p.id
            WHERE c.id = ?
        ''', (chamado_id,))
        return cursor.fetchall()
    
    def visualizar_chamado_cliente(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento FROM chamados c WHERE c.id = (?)', (chamado_id,))
        return cursor.fetchall()

    def alterar(self, chamado: Chamado):
        conexao = self.db_conexao.get_conexao()
        sql = '''
                UPDATE chamados 
                SET titulo = ?, 
                descricao = ?, 
                status = ?, 
                data_abertura = ?, 
                data_fechamento = ?, 
                id_categoria = ?, 
                id_usuario = ?
                WHERE id = ?
            '''
        parametros = (
            chamado.titulo, 
            chamado.descricao, 
            chamado.status, 
            chamado.data_abertura, 
            chamado.data_fechamento, 
            chamado.id_categoria, 
            chamado.id_usuario, 
            chamado.id
        )
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        conexao.commit()

    def excluir(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM chamados WHERE id = (?)', (chamado_id,))
        conexao.commit()

    def listar_todos(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente, 
                c.id_usuario, c.status, c.data_abertura, c.data_max, 
                c.data_fechamento, p.descricao, p.sla 
            FROM chamados c
            LEFT JOIN problemas p ON c.id_categoria = p.id
        ''')
        return cursor.fetchall()

    def listar_todos_por_cliente(self, id_cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento FROM chamados c WHERE c.id_cliente == (?)', (id_cliente,))
        return cursor.fetchall()

    def listar_todos_por_status(self, status:TIPO_ESTADO_CHAMADO):
        if status == None:
            raise Exception('Deve haver sempre haver um tipo de status')
        if status == TIPO_ESTADO_CHAMADO.TODOS:
            conexao = self.db_conexao.get_conexao()
            cursor = conexao.cursor()
            cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id')
            return cursor.fetchall()
        if status == TIPO_ESTADO_CHAMADO.EM_ANDAMENTO:
            conexao = self.db_conexao.get_conexao()
            cursor = conexao.cursor()
            cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id AND c.status == \"Em Andamento\"')
            return cursor.fetchall()
        if status == TIPO_ESTADO_CHAMADO.FECHADO:
            conexao = self.db_conexao.get_conexao()
            cursor = conexao.cursor()
            cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id AND c.status == \"Fechado\"')
            return cursor.fetchall()
        if status == TIPO_ESTADO_CHAMADO.ABERTO:
            conexao = self.db_conexao.get_conexao()
            cursor = conexao.cursor()
            cursor.execute('SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente,c.id_usuario, c.status, c.data_abertura, c.data_max, c.data_fechamento, p.descricao, p.sla FROM chamados c, problemas p WHERE c.id_categoria==p.id AND c.status == \"Aberto\"')
            return cursor.fetchall()
        
    def listar_todos_por_status_e_cliente(self, status, id_cliente):
        if status is None:
            raise Exception('Deve haver sempre haver um tipo de status')
        
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        
        base_query = '''
            SELECT c.id, c.titulo, c.descricao, c.id_categoria, c.id_cliente, 
                   c.id_usuario, c.status, c.data_abertura, c.data_max, 
                   c.data_fechamento, p.descricao, p.sla 
            FROM chamados c
            LEFT JOIN problemas p ON c.id_categoria = p.id
            WHERE c.id_cliente = ?
        '''
        
        if status == TIPO_ESTADO_CHAMADO.TODOS:
            cursor.execute(base_query, (id_cliente,))
        elif status == TIPO_ESTADO_CHAMADO.EM_ANDAMENTO:
            query = base_query + ' AND c.status = "Em Andamento"'
            cursor.execute(query, (id_cliente,))
        elif status == TIPO_ESTADO_CHAMADO.FECHADO:
            query = base_query + ' AND c.status = "Fechado"'
            cursor.execute(query, (id_cliente,))
        elif status == TIPO_ESTADO_CHAMADO.ABERTO:
            query = base_query + ' AND c.status = "Aberto"'
            cursor.execute(query, (id_cliente,))
        else:
            raise Exception('Status inválido fornecido')
        
        resultados = cursor.fetchall()
        conexao.close()
        return resultados
        
    #TODO falta colocar o join no metodo abaixo
    def listar_todos_por_categoria_problema(self, id_categoria):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM chamados WHERE id_categoria = (?)', (id_categoria,))
        return cursor.fetchall()