"""
import modelos/pessoa.py
import modelos/usuario.py
import modelos/aluno.py
import modelos/professor.py
import modelos/oficina.py
import os
"""


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
    print("\n0. Sair")
    print("="*22)
    return captura_input_menu(12)




