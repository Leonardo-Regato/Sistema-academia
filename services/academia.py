from models.aluno import Aluno
from models.professor import Professor
from rich import print
from database.conexao import conectar
from models.pessoa import Pessoa


class Academia:

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - |
#              FUNÇÕES RELACIONADAS A CRIAÇÃO E MANIPULAÇÃO DOS ALUNOS                  |
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - |

    def cadastra_aluno(self, nome, data_nascimento):
        Pessoa.validar_nome(nome)
        data_nascimento = Pessoa.validar_data(data_nascimento)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO alunos (nome, data_nascimento) VALUES (%s, %s) RETURNING id",
                (nome, data_nascimento)
            )
            id_aluno = cursor.fetchone()[0]
            aluno = Aluno(nome, data_nascimento, 
            id_aluno)
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:
            if conexao is not None:
                conexao.close()
        return aluno

    def mostrar_alunos(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM alunos"
        )
        alunos = cursor.fetchall()
        conexao.close()
        print("==== ALUNOS ====")  
        for aluno in alunos:
            id_aluno, nome_aluno, data_nascimento = aluno
            aluno = Aluno(nome_aluno, data_nascimento, id_aluno)
            print(f"{aluno.id} | {aluno.nome} | {aluno.idade} anos.")


    def buscar_aluno(self, nome):
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
      
            cursor.execute(
                "SELECT * FROM alunos WHERE nome ILIKE %s",
                (f"%{nome}%",)
            )
            alunos = cursor.fetchall()
        finally:
            if conexao is not None:
                conexao.close()
    
        resultado = []
        if alunos:
            for aluno in alunos:
                id_aluno, nome_aluno, data_nascimento = aluno
                aluno = Aluno(nome_aluno, data_nascimento, id_aluno)
                resultado.append(aluno)
            return resultado
                
        else:
            raise ValueError(f"Aluno(a) '{nome}' não encontrado(a).")
            


    def localizar_aluno(self, id_aluno):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
           "SELECT * FROM alunos WHERE id = %s",
           (id_aluno,)
       )
        aluno = cursor.fetchone()
        if aluno:
            id_aluno, nome_aluno, data_nascimento = aluno
            aluno = Aluno(nome_aluno, data_nascimento, id_aluno)
            conexao.close()
            return aluno
        else:
            conexao.close()
            raise ValueError("O ID informado não foi encontrado.")

    def listar_alunos(self):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
        
            cursor.execute(
                "SELECT * FROM alunos"
            )
            alunos = cursor.fetchall()
            resultado = []
            for aluno in alunos:
                id_aluno, nome_aluno, data_nascimento = aluno
                resultado.append(Aluno(nome_aluno, data_nascimento, id_aluno))
            return resultado
        finally:
            conexao.close()
         

    def alterar_nome_aluno(self, id_aluno, novo_nome):
        Pessoa.validar_nome(novo_nome)
        self.localizar_aluno(id_aluno)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
        
            cursor.execute(
                "UPDATE alunos SET nome = %s WHERE id = %s",
                (novo_nome, id_aluno,)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:       
            if conexao is not None:
                conexao.close()
        return self.localizar_aluno(id_aluno)
    
        
        
    def alterar_data_aluno(self, id_aluno, nova_data):
        nova_data = Pessoa.validar_data(nova_data)
        self.localizar_aluno(id_aluno)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE alunos SET data_nascimento = %s WHERE id= %s",
                (nova_data,id_aluno)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:
            if conexao is not None:
                conexao.close()
        return self.localizar_aluno(id_aluno)




    def remover_aluno(self, id_aluno):
        self.localizar_aluno(id_aluno)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE from alunos WHERE id = %s",
                (id_aluno,)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise

        finally:
            if conexao is not None:
                conexao.close()
        

    def validar_id(self, localizador):
        while True:
            try:
                valor = int(input("Digite o ID: "))
            except ValueError:
                print("[red]ERRO:[/] Informe um ID válido.")
                continue
            try:
                localizador(valor)
                return valor
            except ValueError as e:
                print(f"[red]ERRO:[/]  {e}")

    def existem_alunos(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM alunos)"
        )
        resultado = cursor.fetchone()[0]
        existe = bool(resultado)
        conexao.close()      
        return existe
                                
            
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - -|
#              FUNÇÕES RELACIONADAS A CRIAÇÃO E MANIPULAÇÃO DOS PROFESSORES                  |
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - -|
        

    def cadastrar_professor(self, nome, data_nascimento):
        Pessoa.validar_nome(nome)
        data_nascimento = Pessoa.validar_data(data_nascimento)
        conexao = None
        try:
            conexao = conectar()     
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO professores (nome, data_nascimento) VALUES (%s, %s) RETURNING id",
                (nome,data_nascimento)
            )       
            id_professor = cursor.fetchone()[0]
            professor = Professor(nome, data_nascimento, id_professor)
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise

        finally:
            if conexao is not None:
                conexao.close()

        return professor    

    def mostrar_professores(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM professores"
        )
        professores = cursor.fetchall()
        conexao.close()
        print("==== PROFESSORES ====") 
        for professor in professores:
            id_professor, nome_professor, data_nascimento = professor 
            professor = Professor(nome_professor, data_nascimento, id_professor)
            print(f"{professor.id} | {professor.nome} | {professor.idade} anos.") 


    def buscar_professor(self, nome):
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
            "SELECT * FROM professores WHERE nome ILIKE %s",
            (f"%{nome}%",)
            )
            professores = cursor.fetchall()
        finally:
            if conexao is not None:
                conexao.close()

        resultado = []        
        if professores:
            for professor in professores:
                id_professor, nome_professor, data_nascimento = professor 
                professor = Professor(nome_professor, data_nascimento, id_professor)
                resultado.append(professor)
            return resultado

        else:
            raise ValueError(f"Professor '{nome}' não encontrado(a).")


    def listar_professores(self):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
        
            cursor.execute(
                "SELECT * FROM professores"
            )
            professores = cursor.fetchall()
            resultado = []
            for professor in professores:
                id_professor, nome_professor, data_nascimento = professor
                resultado.append(Professor(nome_professor, data_nascimento, id_professor))
            return resultado
        finally:
            conexao.close()
            

    
    def localizar_professor(self, id_prof):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM professores WHERE id = %s",
            (id_prof,)
        )
        professor = cursor.fetchone()
        if professor:
            id_professor, nome_professor, data_nascimento = professor 
            professor = Professor(nome_professor, data_nascimento, id_professor)
            conexao.close()
            return professor
        else:
            conexao.close()
            raise ValueError("O ID informado não foi encontrado.")



    def alterar_nome_professor(self, id_prof, novo_nome):
        Pessoa.validar_nome(novo_nome)
        self.localizar_professor(id_prof)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE professores SET nome = %s WHERE id = %s",
                (novo_nome, id_prof)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:       
            if conexao is not None:
                conexao.close()
        return self.localizar_professor(id_prof)


    def alterar_data_professor(self, id_prof, nova_data):
        nova_data = Pessoa.validar_data(nova_data)
        self.localizar_professor(id_prof)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE professores SET data_nascimento = %s WHERE id = %s",
                (nova_data, id_prof)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:       
            if conexao is not None:
                conexao.close()
        return self.localizar_professor(id_prof)

    
    def remover_professor(self, id_prof):
        self.localizar_professor(id_prof)
        conexao = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM professores WHERE id = %s",
                (id_prof,)
            )
            conexao.commit()
        except Exception:
            if conexao is not None:
                conexao.rollback()
            raise
        finally:       
            if conexao is not None:
                conexao.close()

    def existem_professores(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM professores)"
        )
        resultado = cursor.fetchone()[0]
        existe = bool(resultado)
        conexao.close()      
        return existe
