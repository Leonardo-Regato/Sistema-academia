from models.aluno import Aluno
from models.professor import Professor
from rich import print


class Academia:
    def __init__(self):
        self.lista_alunos = []
        self.lista_professores =[]
        self.proximo_aluno_id = 1
        self.proximo_professor_id = 1
        
    def cadastra_aluno(self, nome, data_nascimento):
        id_aluno = self.proximo_aluno_id
        aluno = Aluno(nome, data_nascimento, id_aluno)
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
        id_prof = self.proximo_professor_id
        professor = Professor(nome, data_nascimento, id_prof)
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
