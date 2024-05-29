# models.py
class Cliente:
    def __init__(self, nome, email, empresa, telefone, id, senha):
        self.nome = nome
        self.email = email
        self.empresa = empresa
        self.telefone = telefone
        self.id = id
        self.senha = senha

class Usuario:
    def __init__(self, nome, email, senha, cargo, id):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.id = id

class Problema:
    def __init__(self, descricao, sla, id,):
        self.descricao = descricao
        self.sla = sla
        self.id = id

class Chamado:
    def __init__(self, titulo, descricao, status, data_abertura, data_max, data_fechamento, id_categoria, id_cliente, id_usuario, id):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id_categoria = id_categoria
        self.data_abertura = data_abertura
        self.data_max = data_max
        self.data_fechamento = data_fechamento
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.id = id