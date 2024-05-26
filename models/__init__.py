__init__.py# models.py

class Cliente:
    def __init__(self, nome, email, empresa, telefone):
        self.nome = nome
        self.email = email
        self.empresa = empresa
        self.telefone = telefone

class Usuario:
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

class Problema:
    def __init__(self, descricao, sla):
        self.descricao = descricao
        self.sla = sla

class Chamado:
    def __init__(self, titulo, descricao, status, data_abertura, data_max, data_fechamento):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura
        self.data_max = data_max
        self.data_fechamento = data_fechamento
