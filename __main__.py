from classes import *
from rich import print
from rich.panel import Panel
from time import sleep


def main():
    academia = Academia()
    conteudo = (
        "\n[yellow]1[/]  - [green3]Cadastrar aluno[/]\n"
        "[yellow]2[/]  - [green3]Buscar alunos[/]\n"
        "[yellow]3[/]  - [green3]Alterar aluno[/]\n"
        "[yellow]4[/]  - [green3]Remover aluno[/]\n"
        "[yellow]5[/]  - [green3]Listar alunos[/]\n\n"

        "[yellow]6[/]  - [green3]Cadastrar professor[/]\n"
        "[yellow]7[/]  - [green3]Buscar professor[/]\n"
        "[yellow]8[/]  - [green3]Alterar professor[/]\n"
        "[yellow]9[/]  - [green3]Remover professor[/]\n"
        "[yellow]10[/] - [green3]Listar professores[/]\n\n"
        "[yellow]0[/]  - [red]Sair[/]"

    )
    while True:
        painel = Panel(conteudo, title=" Sistema academia ", width=40)
        print(painel)
        try:
            resp = int(input("Escolha uma opção: "))
        except ValueError:
            print("[red]ERRO:[/] Digite apenas um número.")
            sleep(1)
            continue
        if not 0 <= resp <= 10:
            print("[red]ERRO:[/]  Opção INVÁLIDA")
            sleep(1)
            continue
        
        

        match resp:
            case 0:
                break
            case 1:
                while True:
                    try:
                        nome_aluno = input("Digite o nome do aluno: ")
                        Pessoa.validar_nome(nome_aluno)
                        break
                    except ValueError as e:
                        print(f"[red]ERRO:[/]  {e}")
                while True:
                    try:
                        data = input("Digite a data de nascimento. ex(00/00/0000): ")
                        academia.cadastra_aluno(nome_aluno, data)
                        print("Aluno cadastrado com [green]SUCESSO[/].")
                        sleep(1)
                        break
                    except ValueError as e:
                        print(f"[red]ERRO:[/]  {e}")



            case 2:
                nome_busca = input("Digite o nome do aluno: ")
                academia.buscar_aluno(nome_busca)
                sleep(1)

            case 3:
                if not academia.lista_alunos:
                    print("Ainda não temos alunos cadastrados... Voltando ao menu")
                    sleep(1)
                    continue
                id_aluno = academia.validar_id(academia.localizar_aluno)
                    
                while True:
                    alterar = input("Alterar nome ou data? [digite apenas um]: ")
                    if alterar.lower().strip() == "nome":
                        while True:
                            try:
                                novo_nome = input("Digite o novo nome: ")
                                academia.alterar_nome_aluno(id_aluno, novo_nome)
                                sleep(1)
                                break
                            except ValueError as e:
                                print(f"[red]ERRO:[/]  {e}")
                                sleep(1)
                                continue
                    elif alterar.lower().strip() == "data":
                        while True:
                            try:
                                nova_data = input("Digite a nova data. ex(00/00/0000): ")  
                                academia.alterar_data_aluno(id_aluno, nova_data)
                                sleep(1)
                                break
                            except ValueError as e:
                                print(f"[red]ERRO:[/]  {e}")
                                sleep(1)
                                continue
                    else:
                        print("Opção inválida") 
                        sleep(1)
                        continue
                    break    
                         

            case 4:
                if not academia.lista_alunos:
                    print("Ainda não temos alunos cadastrados... Voltando ao menu")
                    sleep(1)
                    continue
                id_remove_aluno = academia.validar_id(academia.localizar_aluno)
                try:
                    aluno = academia.localizar_aluno(id_remove_aluno)
                
                    while True:
                        decisao = input(f"Tem certeza que deseja remover o(a) aluno(a) {aluno.nome}? [S/N] ")  
                        if decisao.upper().strip() == "S":
                            academia.remover_aluno(id_remove_aluno)
                            sleep(1)
                            break
                        elif decisao.upper().strip() == "N":
                            print("Voltando para o menu...")
                            sleep(1)
                            break
                        else:
                            print("Opção inválida")
                            sleep(1)
                except ValueError as e:
                    print(f"[red]ERRO:[/]  {e}")
                    sleep(1)

            case 5:
                academia.mostrar_alunos()
                sleep(1)

            case 6:
                while True:
                    try:
                        nome_prof = input("Digite o nome do professor: ")
                        Pessoa.validar_nome(nome_prof)
                        break
                    except ValueError as e:
                        print(f"[red]ERRO:[/]  {e}")
                while True:
                    try:
                        data_prof = input("Digite a data de nscimento. ex(00/00/0000): ")
                        academia.cadastrar_professor(nome_prof, data_prof)
                        print("Professor cadastrado com [green]SUCESSO[/].")
                        sleep(1)
                        break
                    except ValueError as e:
                        print(f"[red]ERRO:[/]  {e}")

            case 7:
                prof_busca = input("Digite o nome do professor: ")
                academia.buscar_professor(prof_busca)
                sleep(1)

            case 8:
                if not academia.lista_professores:
                    print("Ainda não temos professores cadastrados... Voltando ao menu")
                    sleep(1)
                    continue
                id_prof = academia.validar_id(academia.localizar_professor)

                while True:
                    altera_prof = input("Alterar nome ou data? [digite apenas um]: ")
                    if altera_prof.strip().lower() == "nome":
                        while True:
                            try:
                                novo_nome_prof = input("Digite o novo nome: ")
                                academia.alterar_nome_professor(id_prof, novo_nome_prof)
                                sleep(1)
                                break
                            except ValueError as e:
                                print(f"[red]ERRO:[/]  {e}")
                                sleep(1)
                                continue
                    elif altera_prof.strip().lower() == "data":
                        while True:
                            try:
                                nova_data_prof = input("Digite a nova data. ex(00/00/0000): ")
                                academia.alterar_data_professor(id_prof, nova_data_prof)
                                sleep(1)
                                break
                            except ValueError as e:
                                print(f"[red]ERRO:[/]  {e}")
                                sleep(1)
                                continue
                    else:
                        print("Opção inválida")
                        sleep(1)
                        continue
                    break

            case 9:
                if not academia.lista_professores:
                    print("Ainda não temos professores cadastrados... Voltando ao menu")
                    sleep(1)
                    continue
                id_remove_prof = academia.validar_id(academia.localizar_professor)
                try:
                    prof = academia.localizar_professor(id_remove_prof)
                    while True:
                        decisao_prof = input(f"Tem certeza que deseja remover o(a) professor(a) {prof.nome}? [S/N] ")
                        if decisao_prof.upper().strip() == "S":
                            academia.remover_professor(id_remove_prof)
                            sleep(1)
                            break
                        elif decisao_prof.upper().strip() == "N":
                            print("Voltando para o menu...")
                            sleep(1)
                            break
                        else:
                            print("Opção inválida")
                            sleep(1)
                except ValueError as e:
                    print(f"[red]ERRO:[/]  {e}")
                    sleep(1)

            case 10:
                academia.mostrar_professores()
                sleep(1)

if __name__ == '__main__':
    main()