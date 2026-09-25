from datetime import datetime, date
import re
from rich import print


class Academia:
    def __init__(self):
        self.lista_alunos = []
        self.lista_professores =[]
        self.proximo_aluno_id = 1
        self.proximo_professor_id = 1
        
    def cadastra_aluno(self, nome, data_nascimento):
        id = self.proximo_aluno_id
        aluno = Aluno(nome, data_nascimento, id)
        self.add_aluno(aluno)
        self.proximo_aluno_id += 1
        return aluno


    def add_aluno(self,aluno):
        self.lista_alunos.append(aluno)


    def mostrar_alunos(self): 
        print("==== ALUNOS ====")  
        for aluno in self.lista_alunos:
            print(f"[yellow]ID {aluno.id}[/] | {aluno.nome} | {aluno.idade} anos")




    def buscar_aluno(self, nome):
        encontrou = False
        print('=== Busca de alunos ===')
        for aluno in self.lista_alunos:
            if nome.lower() in aluno.nome.lower():
                print(f'- {aluno.nome} = {aluno.idade} anos.')
                encontrou = True
        if not encontrou:
            print (f'O(A) aluno(a) {nome} não foi encontrado(a).')


    def localizar_aluno(self, id_aluno):
        for aluno in self.lista_alunos:
            if id_aluno == aluno.id:
              return aluno
        raise ValueError("O id não existe")

    def alterar_nome_aluno(self, id_aluno, novo_nome):
        aluno = self.localizar_aluno(id_aluno)
        aluno.nome = novo_nome
        return aluno

    def alterar_data_aluno(self, id, nova_data):
        aluno = self.localizar_aluno(id)
        aluno.data_nascimento = nova_data
        return aluno

    def remover_aluno(self, id):
        aluno = self.localizar_aluno(id)
        self.lista_alunos.remove(aluno)
        print("Aluno(a) removido(a) com sucesso.")

    def validar_id(self, localizador):
        while True:
            try:
                valor = int(input("Digite a id: "))
            except ValueError:
                print("[red]ERRO:[/] Digite apenas números")
                continue
            try:
                localizador(valor)
                return valor
            except ValueError as e:
                print(f"[red]ERRO:[/]  {e}")

        
    def cadastrar_professor(self, nome, data_nascimento):
        id = self.proximo_professor_id
        professor = Professor(nome, data_nascimento, id)
        self.add_professor(professor)
        self.proximo_professor_id += 1
        return professor
        

    def add_professor(self, professor):
        self.lista_professores.append(professor)


    def mostrar_professores(self):
        print("==== PROFESSORES ====")
        for professor in self.lista_professores:
            print(f"[yellow]ID {professor.id}[/] | {professor.nome} | {professor.idade} anos")


    def buscar_professor(self, nome):
            encontrou = False
            print("=== Busca de professor ===")
            for professor in self.lista_professores:
                if nome.lower() in professor.nome.lower():
                    print(f'- {professor.nome} = {professor.idade} anos.')
                    encontrou = True
            if not encontrou:
                print(f"O(A) professor(a) {nome} não foi encontrado(a).")  

    
    def localizar_professor(self, id_prof):
        for professor in self.lista_professores:
            if id_prof == professor.id:
                return professor
        raise ValueError("O id não existe")

    def alterar_nome_professor(self, id_prof, novo_nome):
        professor = self.localizar_professor(id_prof)
        professor.nome = novo_nome
        return professor


    def alterar_data_professor(self, id, nova_data):
        professor = self.localizar_professor(id)
        professor.data_nascimento = nova_data
        return professor

    def remover_professor(self, id):
        professor = self.localizar_professor(id)
        self.lista_professores.remove(professor)
        print("Professor(a) removido(a) com sucesso.")




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
            raise ValueError("O nome está vazio")
        
        if not re.match(padrao, nome):
            raise ValueError("O nome contém carácteres inválidos")

        

    @property
    def data_nascimento(self):
        return self._data_nascimento



    @data_nascimento.setter
    def data_nascimento(self,nova_data):
        try:
            data_provisoria = datetime.strptime(nova_data, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data inválida")

        if data_provisoria.date() > date.today(): 
            raise ValueError("A data de nascimento está maior que a data atual.")
        self._data_nascimento = data_provisoria
    
            

    @property
    def idade(self):
        cal_idade = date.today().year - self._data_nascimento.year
        if (date.today().month, date.today().day) >= (self._data_nascimento.month, self._data_nascimento.day):
            idade = cal_idade
        else:
            idade = cal_idade -1
        return idade
                

class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, id):
        super().__init__(nome, data_nascimento)
        self.id = id              

class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, id):
        super().__init__(nome, data_nascimento)
        self.id = id
        