from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome, cpf, email, data_nasc, telefone, genero, matricula, oficinas_inscritas, frequencia):
        super().__init__(self, nome, cpf, email, data_nasc, telefone, genero)
        self.matricula = matricula
        self.oficinas_inscritas = []
        self.frequencia = {}
        return
    
    def cadastrar_aluno(self):
        
        
