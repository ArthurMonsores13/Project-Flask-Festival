class Evento:
    def __init__(self):
        self.titulo = ""

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo


class Palestrantes(Evento):
    def __init__(self):
        super().__init__()
        self.nome = ""
        self.titulo = "Palestrantes"
        self.cargo = ""
        self.descricao = ""

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao


class Categorias(Evento):
    def __init__(self):
        super().__init__()
        self.titulo = "Categorias"
        self.descricao = ""

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

class Inicio(Evento):
    def __init__(self):
        super().__init__()
        self.descricao = ""
        
    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao
        