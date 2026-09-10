from abc import ABC, abstractmethod
from datetime import datetime, date


class Pessoa(ABC):
    def __init__(self,nome, data_nascimento):
        self.nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    @property
    def idade(self):
        cal_idade = date.today().year - self._data_nascimento.year
        if (date.today().month, date.today().day) >= (self._data_nascimento.month, self._data_nascimento.day):
            idade = cal_idade
        else:
            idade = cal_idade -1
        return idade
                

    @abstractmethod
    def apresentacao(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def apresentacao(self):
        print(f'O(A) aluno(a) {self.nome} que tem {self.idade} anos foi cadastrado(a) com SUCESSO!')    
              

class Professor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def apresentacao(self):
        print(f'O(A) professor(a) {self.nome} que tem {self.idade} anos foi cadastrado(a) com SUCESSO!')    


class Academia():
    def __init__(self):
        self.lista_alunos = []
        self.lista_professores =[]
        

    def add_aluno(self,aluno):
        self.lista_alunos.append(aluno)


    def mostrar_alunos(self): 
        print("- - ALUNOS - -")  
        for aluno in self.lista_alunos:
            print(f"- {aluno.nome} = {aluno.idade} anos.")


    def remover_aluno(self, nome):
        for aluno in self.lista_alunos:
            if aluno.nome == nome:
                self.lista_alunos.remove(aluno)
                print(f'Aluno(a) {nome} removido do sistema.')
                return
        print("O(A) aluno(a) não foi encontrado(a) em nosso sistema.")


    def buscar_aluno(self, nome):
        for aluno in self.lista_alunos:
            if aluno.nome == nome:
                print(f'Aluno(a) encontrado(a).')
                print(f'- {aluno.nome} = {aluno.idade} anos.')
                return
        print(f'O(A) aluno(a) {nome} não foi encontrado(a).')

                

    def add_professor(self, professor):
        self.lista_professores.append(professor)


    def mostrar_professores(self):
        print("- - PROFESSORES - -")
        for professor in self.lista_professores:
            print(f"- {professor.nome} = {professor.idade} anos.")
            

    def remover_professor(self, nome):
        for professor in self.lista_professores:
            if professor.nome == nome:
                self.lista_professores.remove(professor)
                print(f"O(A) professor(a) {nome} não faz mais parte de nossa equipe.")
                return
        print("Professor(a) não encontrado(a).")


    def buscar_professor(self, nome):
            for professor in self.lista_professores:
                if professor.nome == nome:
                    print(f'professor(a) encontrado(a).')
                    print(f'- {professor.nome} = {professor.idade} anos.')
                    return
            print(f'O(A) professor(a) {nome} não foi encontrado(a).')

    

