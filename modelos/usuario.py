import re
from .pessoa import Pessoa
from .tipo_usuario import TipoUsuario
from .tipo_usuario import role_required

class Usuario(Pessoa):
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero, senha, tipousuario):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero)
        if not senha: 
            raise ValueError("Senha não pode ser vazia.") 
        self.__login = {"email": email, "CPF": cpf} # utiliza CPF e/ou email
        self.__senha = senha # 8 digitos, 1 maiuculo, numero e simbolo
        self.__tipo_usuario = tipousuario

    @staticmethod
    def validar_senha(senha: str) -> bool:
        comprimento_valido = re.fullmatch(r'.{8,}', senha) # Comprova se a senha tem pelo menos 8 caracteres.
        tem_maiuscula = re.search(r'[A-Z]', senha) # Comprova se a senha tem pelo menos uma letra maiúscula.
        tem_numero = re.search(r'\d', senha) # Comprova se a senha tem pelo menos um número.
        tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha) # Comprova se a senha tem pelo menos um símbolo especial.
        return bool(comprimento_valido and tem_maiuscula and tem_numero and tem_especial)
    
    def autenticar(self, login: str, senha: str) -> bool: # Verifica se o login e a senha estão corretos.
        if (login == self.email or login == self.cpf) and senha == self.__senha:
            return True
        return False
      
    @property # Transforma o metodo em um get.
    def login(self): # Retorna o login do usuário.
        return self.__login
    
    @property
    def senha(self): # Retorna a senha do usuário.
        return self.__senha
    
    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @senha.setter
    @role_required(TipoUsuario.adm)
    def senha(self, nova_senha): # Define uma nova senha.
        if not nova_senha:
            raise ValueError("A senha não pode ser vazia.")
        if not self.validar_senha(nova_senha):
            raise ValueError("A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, um número e um símbolo.")
        self.__senha = nova_senha
    
    def __str__(self):
        login_info = f"Email: {self.__login['email']}, CPF: {self.__login['CPF']}"
        return f"Usuário: {login_info}, {super().__str__()}" # to do: Texto de apresentação 
 