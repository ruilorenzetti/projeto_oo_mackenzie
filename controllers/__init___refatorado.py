from daos.cliente_dao import SQLiteClienteDAO
from daos.usuario_dao import SQLiteUsuarioDAO
from daos.problema_dao import SQLiteProblemaDAO
from daos.chamado_dao import SQLiteChamadoDAO
from models import Cliente, Usuario, Problema, Chamado
from services.database_service import ConectaBanco

class BaseController:
    def __init__(self, db_name, dao_class):
        self.conexao = ConectaBanco(db_name)
        self.dao = dao_class(self.conexao)
        self.dao.criar_tabela()

    def criar(self, obj):
        self.dao.inserir(obj)

    def visualizar(self, obj_id):
        return self.dao.visualizar(obj_id)

    def alterar(self, obj):
        self.dao.alterar(obj)

    def excluir(self, obj_id):
        self.dao.excluir(obj_id)

class ClienteController(BaseController):
    def __init__(self):
        super().__init__("clientes.db", SQLiteClienteDAO)

class UsuarioController(BaseController):
    def __init__(self):
        super().__init__("usuarios.db", SQLiteUsuarioDAO)

class ProblemaController(BaseController):
    def __init__(self):
        super().__init__("problemas.db", SQLiteProblemaDAO)

class ChamadoController(BaseController):
    def __init__(self):
        super().__init__("chamados.db", SQLiteChamadoDAO)

    def atribuir_atendente(self, chamado: Chamado):
        self.dao.atribuir_atendente(chamado)

    def alterar_status(self, chamado: Chamado):
        self.dao.alterar_status(chamado)

    def fechar(self, chamado: Chamado):
        self.dao.fechar(chamado)
