from modelos.pessoa import Pessoa
from modelos.usuario import Usuario
from modelos.professor import Professor
from modelos.aluno import Aluno
from modelos.oficina import Oficina
from modelos.tipo_usuario import TipoUsuario
import duvidas  
import json
import os


def captura_opcao(max_opcao):
    while True:
        try:
            captura = int(input("\nDigite a opção desejada: "))
            if 0 <= captura <= max_opcao:
                print("\n") # Adiciona espaço após input válido
                return captura
            else:
                print(f"Opção inválida. Digite um número entre 0 e {max_opcao}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def login():
    print("\n---LOGIN ---")
    login_input = input("CPF ou Email: ").strip()
    senha_input = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.autenticar(login_input, senha_input):
            print(f"\n Login bem-sucedido. Olá, {usuario.nome}!")
            return usuario
    print("CPF/Email ou senha inválidos.")
    return None
 

def menu_publico(): #menu sem login
    print("\n--- Bem vindo ao Sistema de Gestão de Oficinas ---")
    print("\n1. Listar Oficinas")
    print("\n2. FAQ - Dúvidas")
    print("\n3. Entrar no Sistema (Login)")
    print("\n0. Sair")
    print("="*22)
    return captura_opcao(3)


def menu_completo(): #menu pós login
    print(" \n --- Sistema de Gestão de Oficinas ---")

    if usuario.tipo_usuario  == TipoUsuario.adm: 
        print("\n1. Cadastrar Professor")
        print("\n2. Cadastrar alunos")
        print("\n3. Criar Oficina")
        print("\n4. Inscrever Aluno em Oficina")
        print("\n5. Associar Professor à Oficina")
        print("\n6. Registrar Frequência de Aluno")
        print("\n7. Listar Professor")
        print("\n8. Listar Alunos")
        print("\n9. Listar Todas as Oficinas")
        print("\n10. Ver Oficinas de um Professor")
        print("\n11. Ver Alunos Inscritos em uma Oficina")
        print("\n12. Ver Frequência de um Aluno em uma Oficina")
        print("\n13. FAQ - Dúvidas")
        print("\n14. FAQ - Responder FAQ")
        print("\n0. Sair")
        print("="*22)
        return captura_opcao(14)
    
    elif usuario.tipo_usuario == TipoUsuario.professor:
        print("1. Cadastrar Alunos")
        print("2. Inscrever Aluno em Oficina")
        print("3. Registrar Frequência de Aluno")
        print("4. Listar Alunos")
        print("5. Listar Minhas Oficinas")
        print("6. Ver Alunos Inscritos em uma Oficina")
        print("7. Ver Frequência de um Aluno em uma Oficina")
        print("0. Sair / Logout")
        return captura_opcao(7)

    else:
        print("Usuário sem permissão de acesso! ")
        return 0


if __name__ == "__main__":

    usuario_logado = None

    while True:
        os.system("cls")
    
        opcao_digitada = menuOpcoes()
        opcao_digitada = menu_publico()
        

        if usuario_logado is None:
            opcao_digitada = menu_publico()

            if opcao_digitada == 1:
                Oficina.listar_oficinas_disponiveis()

            elif opcao_digitada == 2:
                duvidas.exibir_faq() 

            elif opcao_digitada == 3:
                usuario_logado = login()

            elif opcao_digitada == 0:
                print("Encerrando o sistema!")  
                break
            else:
                print("Opção inválida!")    

        else:
            opcao_digitada = menu_completo(usuario_logado)

            if usuario_logado.tipo_usuario == TipoUsuario.adm:

                if opcao_digitada == 1:
                    os.system("cls")
                    cadastrar_professor()

                elif opcao_digitada == 2:
                    os.system("cls")
                    cadastrar_aluno()

                elif opcao_digitada == 3:
                    os.system("cls")
                    cadastrar_oficina()

                elif opcao_digitada == 4:
                    os.system("cls")
                    Oficina.adicionar_aluno()

                elif opcao_digitada == 5:
                    os.system("cls")
                    Oficina.associar_professor()

                elif opcao_digitada == 6:
                    os.system("cls")
                    registrar_frequencia_aluno()

                elif opcao_digitada == 7:
                    os.system("cls")
                    listar_professores()

                elif opcao_digitada == 8:
                    os.system("cls")
                    listar_alunos()

                elif opcao_digitada == 9:
                    os.system("cls")
            
                elif opcao_digitada == 10:
                    os.system("cls")
                    ver_oficinas_professor()

                elif opcao_digitada == 11:
                    os.system("cls")
                    Oficina.get_alunos_inscritos()

                elif opcao_digitada == 12:
                    os.system("cls")
                    ver_alunos_frequencia_oficina()

                elif opcao_digitada == 13:
                    os.system("cls")
                    add_duvida()

                elif opcao_digitada == 14:
                    os.system("cls")
                    add_resposta()

                elif opcao_digitada == 0:
                    os.system("cls")
                    usuario_logado = None
                    print("Você encerrou o programa")
                else:
                    print("Opção inválida! ")

            elif usuario_logado.tipo_usuario == TipoUsuario.professor:

                if opcao_digitada == 1:
                    os.system("cls")
                    cadastrar_aluno()

                elif opcao_digitada == 2:
                    os.system("cls")
                    Oficina.adicionar_aluno()
                
                elif opcao_digitada == 3:
                    os.system("cls")
                    registrar_frequencia_aluno()

                elif opcao_digitada == 4:
                    os.system("cls")
                    listar_alunos()

                elif opcao_digitada == 5:
                    os.system("cls") 
                    ver_oficinas_professor()

                elif opcao_digitada == 6:
                    os.system("cls") 
                    Oficina.get_alunos_inscritos()

                elif opcao_digitada == 7:
                    os.system("cls")
                    ver_alunos_frequencia_oficina()

                elif opcao_digitada == 0:
                    os.system("cls")
                    usuario_logado = None
                    print("Você encerrou o programa")
                else:
                    print("Opção inválida! ")


                



