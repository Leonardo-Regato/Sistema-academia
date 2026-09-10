from classes import *
from datetime import datetime, date



def main():

    a1 = Aluno("Leonardo", "22/08/2006")
    a2 = Aluno("Julia", "18/03/2007")
    a3 = Aluno("Luiz", "10/08/2006")

    p1 = Professor("Leandro", "25/04/1979")
    p2 = Professor("Patrcia", "26/08/1978")

    academia = Academia()

    academia.add_aluno(a1)
    academia.add_aluno(a2)
    academia.add_aluno(a3)

    academia.add_professor(p1)
    academia.add_professor(p2)

    academia.mostrar_alunos()
    academia.mostrar_professores()

    academia.buscar_aluno("Leonardo")
    academia.buscar_professor("Luiz")


if __name__ == '__main__':
    main()