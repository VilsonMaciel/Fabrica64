from modelos.pessoa import Pessoa
from modelos.usuario import Usuario
from modelos.professor import Professor
from modelos.aluno import Aluno
from modelos.oficina import Oficina
import json
import os


def captura_input_menu(max_opcao):
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
    print(" \n --- Sistema de Gestão de Oficinas ---")
    print("\n --- Entrar ---")
    input("")
    input("")












def menuOpcoes():
    print(" \n --- Sistema de Gestão de Oficinas ---")
    print("\n1. Cadastrar Professor")
    print("\n2. Cadastrar alunos")
    print("\n3. Criar Oficina")
    print("\n4. Inscrever Aluno em Oficina")
    print("\n5. Associar Professor à Oficina")
    print("\n6. Registrar Frequência de Aluno")
    print("\n7. Listar Professor")
    print("\n8. Listar Alunos")
    print("\n9. Listar Oficinas")
    print("\n10. Ver Oficinas de um Professor")
    print("\n11. Ver Alunos Inscritos em uma Oficina")
    print("\n12. Ver Frequência de um Aluno em uma Oficina")
    print("\n13. FAQ - Dúvidas")
    print("\n14. FAQ - Responder FAQ")
    print("\n0. Sair")
    print("="*22)
    return captura_input_menu(14)

if __name__ == "__main__":
    while True:
        opcao_digitada = menuOpcoes()
        
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
            print("Você encerrou o programa")
            break



