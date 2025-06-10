from .pessoa import Pessoa

class Usuario:
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero, login, senha):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero)
        if not login or not senha: 
            raise ValueError("Login e senha não podem ser vazios.") 
        self.__login = login # utiliza CPF ou email
        self.__senha = senha # 8 digitos, 1 maiuculo, numero e simbolo


    
    
    
    def __str__(self):
        return # to do: Texto de apresentação 
