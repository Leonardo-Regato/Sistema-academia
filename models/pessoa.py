from datetime import datetime, date
import re


class Pessoa:
    def __init__(self,nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        Pessoa.validar_nome(novo_nome)
        self._nome = novo_nome.strip()

    @staticmethod
    def validar_nome(nome): 
        padrao = r"^[A-Za-zÀ-ÿ\s]+$"
        nome = nome.strip()
        if nome == "":
            raise ValueError("O nome é obrigatório.")
        
        if not re.match(padrao, nome):
            raise ValueError("O nome contém caracteres inválidos.")

        

    @property
    def data_nascimento(self):
        return self._data_nascimento



    @data_nascimento.setter
    def data_nascimento(self,nova_data):
        data_valida = self.validar_data(nova_data)
        self._data_nascimento = data_valida

    @staticmethod
    def validar_data(nova_data):
        try:
            if isinstance(nova_data, date):
                data_provisoria = nova_data
            else:
                data_provisoria = datetime.strptime(nova_data, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Informe a data no formato DD/MM/AAAA.")

        if data_provisoria > date.today(): 
            raise ValueError("A data de nascimento não pode ser posterior à data atual.")

        if data_provisoria.year <  date.today().year - 100: 
            raise ValueError("Data de nascimento fora do período permitido.")
        return data_provisoria

        
    
            

    @property
    def idade(self):
        cal_idade = date.today().year - self._data_nascimento.year
        if (date.today().month, date.today().day) >= (self._data_nascimento.month, self._data_nascimento.day):
            idade = cal_idade
        else:
            idade = cal_idade -1
        return idade
                