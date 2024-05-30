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
    def __init__(self, descricao=None, sla=None, id=None,):
        self.descricao = descricao
        self.sla = sla
        self.id = id

class Chamado:
    def __init__(self, titulo=None, descricao=None, status=None, data_abertura=None, data_max=None, data_fechamento=None, id_categoria=None, id_cliente=None, id_usuario=None, id=None):
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

    def __str__(self):
        return (f"Chamado("
                f"titulo='{self.titulo}', "
                f"descricao='{self.descricao}', "
                f"status='{self.status}', "
                f"data_abertura='{self.data_abertura}', "
                f"data_max='{self.data_max}', "
                f"data_fechamento='{self.data_fechamento}', "
                f"id_categoria={self.id_categoria}, "
                f"id_cliente={self.id_cliente}, "
                f"id_usuario={self.id_usuario}, "
                f"id={self.id})")

