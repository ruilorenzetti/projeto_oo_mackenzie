# controllers.py
from daos.TIPO_ESTADO_CHAMADO import TIPO_ESTADO_CHAMADO
from daos.cliente_dao import SQLiteClienteDAO
from daos.usuario_dao import SQLiteUsuarioDAO
from daos.problema_dao import SQLiteCategoriaProblemaDAO
from daos.chamado_dao import SQLiteChamadoDAO
from models import Cliente, Usuario, Problema, Chamado
from services.database_service import ConectaBanco

class ClienteController:
    def __init__(self):
        self.conexao = ConectaBanco()
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

    def listar_todos(self):
        return self.cliente_dao.listar_todos()

class UsuarioController:
    def __init__(self):
        self.conexao = ConectaBanco()
        self.usuario_dao = SQLiteUsuarioDAO(self.conexao)
        self.usuario_dao.criar_tabela()

    def criar_usuario(self, usuario: Usuario):
        self.usuario_dao.inserir(usuario)

    def visualizar_usuario(self, usuario_id):
        return self.usuario_dao.visualizar(usuario_id)

    def alterar_usuario(self, usuario: Usuario):
        self.usuario_dao.alterar(usuario)

    def excluir_usuario(self, usuario_id):
        self.usuario_dao.excluir(usuario_id)

    def listar_todos(self):
        return self.usuario_dao.listar_todos()

class ProblemaController:
    def __init__(self):
        self.conexao = ConectaBanco()
        self.problema_dao = SQLiteCategoriaProblemaDAO(self.conexao)
        self.problema_dao.criar_tabela()

    def criar_problema(self, problema: Problema):
        self.problema_dao.inserir(problema)

    def visualizar_problema(self, problema_id):
        return self.problema_dao.visualizar(problema_id)

    def alterar_problema(self, problema: Problema):
        self.problema_dao.alterar(problema)

    def excluir_problema(self, problema_id):
        self.problema_dao.excluir(problema_id)

    def listar_todos(self):
        return self.problema_dao.listar_todos()

class ChamadoController:
    def __init__(self):
        self.conexao = ConectaBanco()
        self.chamado_dao = SQLiteChamadoDAO(self.conexao)
        self.chamado_dao.criar_tabela()

    def criar_chamado(self, chamado: Chamado):
        self.chamado_dao.abrir(chamado)

    def atribuir_atendente_chamado(self, chamado_id, usuario_id):
        self.chamado_dao.atribuir_atendente(chamado_id, usuario_id)

    def alterar_status_chamado(self, chamado: Chamado):
        self.chamado_dao.alterar_status(chamado)

    def fechar_chamado(self, chamado: Chamado):
        self.chamado_dao.fechar(chamado)

    def visualizar_chamado(self, chamado_id):
        return self.chamado_dao.visualizar(chamado_id)
    
    def visualizar_chamado_cliente(self, chamado_id):
        return self.chamado_dao.visualizar_chamado_cliente(chamado_id)
    
    def alterar_chamado(self, chamado: Chamado):
        self.chamado_dao.alterar(chamado)

    def excluir_chamado(self, chamado_id):
        self.chamado_dao.excluir(chamado_id)

    def listar_todos(self):
        return self.chamado_dao.listar_todos()
    
    def listar_todos_por_cliente(self, id_cliente):
        return self.chamado_dao.listar_todos_por_cliente(id_cliente)

    def listar_todos_por_categoria_problema(self,id_categoria):
        return self.chamado_dao.listar_todos_por_categoria_problema(id_categoria)
    
    def listar_todos_por_status(self, status:TIPO_ESTADO_CHAMADO):
        return self.chamado_dao.listar_todos_por_status(status)
    
    def listar_todos_por_status_e_cliente(self, status:TIPO_ESTADO_CHAMADO, id_cliente):
        return self.chamado_dao.listar_todos_por_status_e_cliente(status, id_cliente)