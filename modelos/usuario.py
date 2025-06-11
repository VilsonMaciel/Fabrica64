from .pessoa import Pessoa
import re

class Usuario(Pessoa):
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero, login, senha):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero)
        if not login or not senha: 
            raise ValueError("Login e senha não podem ser vazios.") 
        self.__login = login # utiliza CPF ou email
        self.__senha = senha # 8 digitos, 1 maiuculo, numero e simbolo

    def validar_senha(senha: str) -> bool:
        # Pelo menos 8 caracteres
        comprimento_valido = re.fullmatch(r'.{8,}', senha)
        tem_maiuscula = re.search(r'[A-Z]', senha)
        tem_numero = re.search(r'\d', senha)
        tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)
        return bool(comprimento_valido and tem_maiuscula and tem_numero and tem_especial)
                
    @property # Transforma o metodo em um get.
    def login(self): # Retorna o login do usuário.
        return self.__login
    
    @property 
    def senha(self): # Retorna a senha do usuário.
        return self.__senha # Usar Hashing.
    
    @login.setter # Transforma o metodo em set.
    def login(self, novo_login): # Define um novo login.
        if not novo_login:
            raise ValueError("O login não pode ser vazio.") 
        self.__login = novo_login
    
    @senha.setter
    def senha(self, nova_senha):
        if not nova_senha:
            raise ValueError("A senha não pode ser vazia.")
        self.__senha = nova_senha # Usar Hashing.

    def __str__(self):
        return f"Usuário: {self.get_login()}, {super().__str__()}" # to do: Texto de apresentação 
 