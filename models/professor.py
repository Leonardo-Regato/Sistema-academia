from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, id):
        super().__init__(nome, data_nascimento)
        self.id = id
        