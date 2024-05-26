from abc import ABC, abstractmethod
import sqlite3

# Definição de uma classe para conexão com o banco de dados
class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    # Método para obter uma conexão com o banco de dados SQLite
    def get_conexao(self):
        return sqlite3.connect(self.db_name)

# Definição da Classe Cliente
class Cliente:
    def __init__(self, nome, email, empresa, telefone):
        self.nome = nome
        self.email = email
        self.empresa = empresa
        self.telefone = telefone

# Definição da classe abstrata ClienteDAO com métodos abstratos para operações com clientes
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
    def alterar(self, cliente: Cliente):
        pass

    @abstractmethod
    def excluir(self, cliente_id):
        pass

class SQLiteClienteDAO(ClienteDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            empresa TEXT NOT NULL,
                            telefone TEXT NOT NULL)''')

    def inserir(self, cliente: Cliente):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO clientes (nome, email, empresa, telefone) 
                              VALUES (?, ?, ?, ?)''',
                           (cliente.nome, cliente.email, cliente.empresa, cliente.telefone))

    def visualizar(self, cliente_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
            return cursor.fetchone()

    def alterar(self, cliente: Cliente):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE clientes 
                              SET nome = ?, email = ?, empresa = ?, telefone = ? 
                              WHERE id = ?''',
                           (cliente.nome, cliente.email, cliente.empresa, cliente.telefone, cliente.id))

    def excluir(self, cliente_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()

class ClienteController:
    def __init__(self):
        self.conexao = ConectaBanco("clientes.db")
        self.cliente_dao = SQLiteClienteDAO(self.conexao)

    def criar_cliente(self, cliente: Cliente):
        self.cliente_dao.inserir(cliente)

    def visualizar_cliente(self, cliente_id):
        return self.cliente_dao.visualizar(cliente_id)

    def alterar_cliente(self, cliente: Cliente):
        self.cliente_dao.alterar(cliente)

    def excluir_cliente(self, cliente_id):
        self.cliente_dao.excluir(cliente_id)

# Definição da Classe Usuario
class Usuario:
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

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

class UsuarioController:
    def __init__(self):
        self.conexao = ConectaBanco("usuarios.db")
        self.usuario_dao = SQLiteUsuarioDAO(self.conexao)

    def criar_usuario(self, usuario: Usuario):
        self.usuario_dao.inserir(usuario)

    def visualizar_usuario(self, usuario_id):
        return self.usuario_dao.visualizar(usuario_id)

    def alterar_usuario(self, usuario: Usuario):
        self.usuario_dao.alterar(usuario)

    def excluir_usuario(self, usuario_id):
        self.usuario_dao.excluir(usuario_id)

# Definição da Classe Problema
class Problema:
    def __init__(self, descricao, sla):
        self.descricao = descricao
        self.sla = sla

class ProblemaDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, problema: Problema):
        pass

    @abstractmethod
    def visualizar(self, problema_id):
        pass

    @abstractmethod
    def alterar(self, problema: Problema):
        pass

    @abstractmethod
    def excluir(self, problema_id):
        pass

class SQLiteProblemaDAO(ProblemaDAO):
    def __init__(self, db_conexao: ConectaBanco):
        super().__init__(db_conexao)
        self.criar_tabela()

    def criar_tabela(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS problemas
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descricao TEXT NOT NULL,
                            sla INT NOT NULL)''')

    def inserir(self, problema: Problema):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO problemas (descricao, sla) 
                              VALUES (?, ?)''',
                           (problema.descricao, problema.sla))

    def visualizar(self, problema_id):
        with self._get_cursor() as cursor:
            cursor.execute('SELECT * FROM problemas WHERE id = ?', (problema_id,))
            return cursor.fetchone()

    def alterar(self, problema: Problema):
        with self._get_cursor() as cursor:
            cursor.execute('''UPDATE problemas 
                              SET descricao = ?, sla = ? 
                              WHERE id = ?''',
                           (problema.descricao, problema.sla, problema.id))

    def excluir(self, problema_id):
        with self._get_cursor() as cursor:
            cursor.execute('DELETE FROM problemas WHERE id = ?', (problema_id,))

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()

class ProblemaController:
    def __init__(self):
        self.conexao = ConectaBanco("problemas.db")
        self.problema_dao = SQLiteProblemaDAO(self.conexao)

    def criar_problema(self, problema: Problema):
        self.problema_dao.inserir(problema)

    def visualizar_problema(self, problema_id):
        return self.problema_dao.visualizar(problema_id)

    def alterar_problema(self, problema: Problema):
        self.problema_dao.alterar(problema)

    def excluir_problema(self, problema_id):
        self.problema_dao.excluir(problema_id)

# Definição da Classe Chamado
class Chamado:
    def __init__(self, titulo, descricao, status, data_abertura, data_max, data_fechamento):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura
        self.data_max = data_max
        self.data_fechamento = data_fechamento

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
                            data_abertura DATE NOT NULL,
                            data_max DATE NOT NULL,
                            data_fechamento DATE NOT NULL)''')

    def abrir(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('''INSERT INTO chamados (titulo, descricao, status, data_abertura, data_max, data_fechamento) 
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento))

    def atribuir_atendente(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('UPDATE chamados SET usuarios(id) = ? WHERE id = ?', (chamado.atendente_id, chamado.id))

    def alterar_status(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('UPDATE chamados SET status = ? WHERE id = ?', (chamado.status, chamado.id))

    def fechar(self, chamado: Chamado):
        with self._get_cursor() as cursor:
            cursor.execute('UPDATE chamados SET status = "Fechado" WHERE id = ?', (chamado.id,))

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

    def _get_cursor(self):
        conexao = self.db_conexao.get_conexao()
        return conexao.cursor()

class ChamadoController:
    def __init__(self):
        self.conexao = ConectaBanco("chamados.db")
        self.chamado_dao = SQLiteChamadoDAO(self.conexao)

    def criar_chamado(self, chamado: Chamado):
        self.chamado_dao.abrir(chamado)

    def atribuir_atendente_chamado(self, chamado: Chamado):
        self.chamado_dao.atribuir_atendente(chamado)

    def alterar_status_chamado(self, chamado: Chamado):
        self.chamado_dao.alterar_status(chamado)

    def fechar_chamado(self, chamado: Chamado):
        self.chamado_dao.fechar(chamado)

    def visualizar_chamado(self, chamado_id):
        return self.chamado_dao.visualizar(chamado_id)

    def alterar_chamado(self, chamado: Chamado):
        self.chamado_dao.alterar(chamado)

    def excluir_chamado(self, chamado_id):
        self.chamado_dao.excluir(chamado_id)
