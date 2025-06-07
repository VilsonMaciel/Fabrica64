import re
import datetime

class Pessoa:
    def __init__(self, nome, cpf, email, data_nasc, telefone, sexo):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.sexo = sexo

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
            cpf = input("CPF (somente números): ")
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
    
    def validar_email(): #função para validar email de usuários

        while True: 
            email = input("Email: ").lower()
    
    def validar_telefone(): #função para validar contato e formatá-lo
        while True:
            try:
                telefone = input("Telefone: ")
                telefone = re.sub(r"[^\d]", "", telefone) #remove tudo que não for número

                if re.fullmatch(r"\d{10,11}", telefone): #Formata para (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
                    if len(telefone) == 11:
                        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
                    elif len(telefone) == 10:
                        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
                print("Número inválido. Digite um número com DDD e 8 ou 9 dígitos.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

    def valid_data_nasc(): #função para validar data de nascimento
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