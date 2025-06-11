import re
import datetime

class Pessoa:
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero):
        self.nome = nome
        self.cpf = cpf 
        self.email = email
        self.data_nasc = data_nasc #dd/mm/YYYY
        self.telefone = telefone 
        self.genero = genero #masculino, feminino, não binário
    
    def __str__ (self):
        return f""" ---- Dados do Usuário ----
Nome: {self.nome}  
CPF: {self.cpf}
Email: {self.email}
Data de nascimento: {self.data_nasc}
Telefone: {self.telefone}
Gênero: {self.genero}
"""

    def validar_nome(): #função para validar o nome
        while True:
            try:
                nome = input("Nome: ").strip().title()
                if not nome:
                    raise ValueError("O nome não pode estar vazio.")
                if not all(palavra.isalpha() for palavra in nome.split()):
                    raise ValueError("O nome deve conter apenas letras.")
                return nome
            except ValueError as e:
                print(f"Erro: {e}")

    def validar_cpf(): #função para validar o cpf
        def calcular_digito(cpf, peso_inicial): #validação matemática dos dígitos verificadores do CPF
            soma = sum(int(digito) * peso for digito, peso in zip(cpf, range(peso_inicial, 1, -1)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)
                
        while True:
            cpf = int(input("CPF (somente números): "))
            if len(cpf) == 11 and cpf.isdigit():
            #verifica se todos os dígitos são iguais (ex: 11111111111), o que é inválido
                if cpf == cpf[0] * 11:
                    print("CPF inválido! Todos os dígitos são iguais.")
                    continue

            #calcula os dois dígitos verificadores
                primeiro_digito = calcular_digito(cpf[:9], 10)
                segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, 11)

                if cpf[-2:] == primeiro_digito + segundo_digito:
                    return cpf
                else:
                    print("CPF inválido! Dígitos verificadores não conferem.")
            else:
                print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
    
    def validar_email(email): #função para validar email de usuários
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while True: 
            email = input("Email: ").lower()         
            if re.match(padrao, email):
                    print('E-mail válido')
                    return email
            else:
                print('E-mail inválido! Digite novamente.')
                
    def validar_telefone():
        ddds_validos = { #todos os ddds do brasil
        '11', '12', '13', '14', '15', '16', '17', '18', '19',
        '21', '22', '24', '27', '28',
        '31', '32', '33', '34', '35', '37', '38',
        '41', '42', '43', '44', '45', '46',
        '47', '48', '49',
        '51', '53', '54', '55',
        '61', '62', '63', '64', '65', '66', '67', '68', '69',
        '71', '73', '74', '75', '77', '79',
        '81', '82', '83', '84', '85', '86', '87', '88', '89',
        '91', '92', '93', '94', '95', '96', '97', '98', '99'
        }

        while True: 
            telefone = input('Telefone (com DDD): ')
            (r"[^\d]", "", telefone)

            if not re.fullmatch(r"\d{10,11}", telefone):
                print("Número inválido. Deve conter DDD + 8 ou 9 dígitos.")
                continue

            ddd = telefone[:2]
            if ddd not in ddds_validos:
                print(f"DDD inválido: {ddd}.")
                continue

            primeiro_digito = telefone[2]
            if len(telefone) == 11 and primeiro_digito != '9':
                print("Número de celular inválido. Deve começar com 9." )
            elif len(telefone) == 10 and primeiro_digito not in '2345':
                print("Número fixo inválido. Deve começar com 2, 3, 4 ou 5.")
                continue

            #formatação telefone
            if len(telefone) == 11:
                return f"({ddd}) {telefone[2:7]}-{telefone[7:]}"
            else:
                return f"({ddd}) {telefone[2:6]}-{telefone[6:]}"

    def validar_data_nasc(): #função para validar data de nascimento
        while True:
            data_str = input("Data de nascimento (dd/mm/yyyy): ")
            try:
                data_nasc = datetime.datetime.strptime(data_str, '%d/%m/%Y')
                hoje = datetime.datetime.today()
                idade = (hoje - data_nasc).days // 365

                if data_nasc > hoje:
                    print("A data de nascimento não pode ser no futuro.")
                elif idade > 120:
                    print("Idade inválida. Verifique a data digitada.")
                else:
                    return data_nasc
            except ValueError:
                print("Formato inválido. Use o formato dd/mm/yyyy.")
    

    def validar_genero(): #função para escolher o genero
        opcoes = {
        1: "Masculino",
        2: "Feminino",
        3: "Prefiro não dizer",
        4: "Outro"
        }

        while True:
            print('''Qual seu gênero?
1. Masculino
2. Feminino
3. Prefiro não dizer
4. Outro''')

            try:
                opcao = int(input("Escolha uma opção (1-4): "))
                if opcao in opcoes:

                    if opcao == 4:
                        genero_personalizado = input("Por favor, digite como você se identifica: ").strip()
                        if genero_personalizado:
                            return genero_personalizado
                        else:
                            print("Entrada inválida. Tente novamente.")
                    else:
                        return opcoes[opcao]
                else:
                    print("Opção inválida. Escolha um número entre 1 e 4.")
            except ValueError:
                print("Por favor, digite um número válido.")

