import re
import datetime

class Pessoa:
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero):
        self.__nome = nome
        self.__cpf = cpf 
        self.__email = email
        self.__data_nasc = data_nasc  #dd/mm/YYYY
        self.__telefone = telefone 
        self.__genero = genero  #masculino, feminino, outros.
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() and all(p.isalpha() or p.isspace() for p in novo_nome):
            self.__nome = novo_nome.strip().title()
        else:
            raise ValueError("Nome inválido. Deve conter apenas letras e espaços.")
    
    @staticmethod
    def chamar_nome():
        #Solicita e valida o nome do usuário.
        while True:
            nome = input('Nome: ').strip()
            if nome and all(p.isalpha() or p.isspace() for p in nome):
                return nome.title()
            print("Nome inválido. Digite apenas letras e espaços.")
  
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if Pessoa.validar_cpf(novo_cpf):
            self.__cpf = re.sub(r'\D', '', novo_cpf)
        else:
            raise ValueError("CPF inválido.")
    
    @staticmethod
    def chamar_cpf():
        #Solicita e valida o CPF do usuário.
        while True:
            cpf = input("CPF (somente números): ").strip()
            if Pessoa.validar_cpf(cpf):
                return re.sub(r'\D', '', cpf)
            print("CPF inválido.")

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        #validação de cpf
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        def calcular_digito(cpf_parcial, peso_inicial): #calculo dos digitos do cpf
            soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)
        
        digito1 = calcular_digito(cpf[:9], 10)
        digito2 = calcular_digito(cpf[:9] + digito1, 11)
        return cpf[-2:] == digito1 + digito2

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        #Formata um CPF no padrão ***.***.***-**
        cpf = re.sub(r"[^\d]", "", cpf)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(padrao, novo_email):
            self.__email = novo_email.lower()
        else:
            raise ValueError("Email inválido.")
    
    @staticmethod
    def chamar_email():
        #Solicita e valida o email do usuário.
        while True:
            email = input("Email: ").strip()
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                return email.lower()
            print("Email inválido.")
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if Pessoa.validar_telefone(novo_telefone):
            self.__telefone = re.sub(r'\D', '', novo_telefone)
        else:
            raise ValueError("Telefone inválido.")
    
    @staticmethod
    def chamar_telefone():
        #Solicita e valida o telefone do usuário.
        while True:
            telefone = input("Telefone (com DDD): ").strip()
            if Pessoa.validar_telefone(telefone):
                return re.sub(r'\D', '', telefone)
            print("Telefone inválido.")

    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        #Valida um número de telefone usando todos os ddds do Brasil.
        telefone = re.sub(r'\D', '', telefone)
        if not re.fullmatch(r'\d{10,11}', telefone):
            return False
            
        ddds_validos = {
            '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '21', '22', '24', '27', '28', '31', '32', '33', '34',
            '35', '37', '38', '41', '42', '43', '44', '45', '46',
            '47', '48', '49', '51', '53', '54', '55', '61', '62',
            '63', '64', '65', '66', '67', '68', '69', '71', '73',
            '74', '75', '77', '79', '81', '82', '83', '84', '85',
            '86', '87', '88', '89', '91', '92', '93', '94', '95',
            '96', '97', '98', '99'
        }
        
        ddd = telefone[:2]
        if ddd not in ddds_validos:
            return False
            
        if len(telefone) == 11 and telefone[2] != '9':
            return False
        elif len(telefone) == 10 and telefone[2] not in '2345':
            return False
            
        return True

    @staticmethod
    def formatar_telefone(telefone: str) -> str:
        #Formata um telefone no padrão (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) == 11:
            return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        elif len(telefone) == 10:
            return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        raise ValueError("Número inválido. Deve ter 10 ou 11 dígitos.")

    @property
    def data_nasc(self):
        return self.__data_nasc
    
    @data_nasc.setter
    def data_nasc(self, valor):
        try:
            data = datetime.datetime.strptime(valor, '%d/%m/%Y')
            if data > datetime.datetime.today():
                raise ValueError("Data no futuro não é válida.")
            self.__data_nasc = valor
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato dd/mm/yyyy.")
    
    @staticmethod
    def chamar_data_nasc():
        #Solicita e valida a data de nascimento do usuário.
        while True:
            data = input("Data de nascimento (dd/mm/yyyy): ").strip()
            try:
                dt = datetime.datetime.strptime(data, '%d/%m/%Y')
                if dt > datetime.datetime.today():
                    print("Data no futuro não é válida.")
                else:
                    return data
            except ValueError:
                print("Formato inválido. Use dd/mm/yyyy.")

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__genero = valor.strip()
        else:
            raise ValueError("Gênero inválido.")
    
    @staticmethod
    def chamar_genero():
        #Solicita e valida o gênero do usuário.
        opcoes_genero = {
            1: "Masculino",
            2: "Feminino",
            3: "Prefiro não dizer",
            4: "Outro"
        }
        while True:
            print("\nQual seu gênero?")
            for k, v in opcoes_genero.items():
                print(f"{k}. {v}")
                
            try:
                opcao = int(input("Escolha uma opção (1-4): "))
                if opcao in opcoes_genero:
                    if opcao == 4:
                        genero = input("Digite como você se identifica: ").strip()
                        if genero:
                            return genero
                        print("Entrada inválida.")
                    else:
                        return opcoes_genero[opcao]
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Por favor, digite um número.")

    def __str__(self):
        #Retorna os dados formatados da pessoa.
        return f"""---- Dados do Usuário ----
Nome: {self.__nome}
CPF: {Pessoa.formatar_cpf(self.__cpf)}
Email: {self.__email}
Data de nascimento: {self.__data_nasc}
Telefone: {Pessoa.formatar_telefone(self.__telefone)}
Gênero: {self.__genero}"""

