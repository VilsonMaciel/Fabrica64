#oficina
# modelos/oficina.py
 

class Oficina:
    

    def __init__(self, nome, descricao, capacidade_maxima):
        if not nome or not descricao or capacidade_maxima <= 0:
            raise ValueError("Nome, descrição e capacidade_maxima (maior que zero) são obrigatórios.")

        self.__nome = nome
        self.__descricao = descricao
        self.__capacidade_maxima = capacidade_maxima
        self.__alunos_inscritos = []
        self.__professores_associados = []

#Retorna o nome das funções 
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_capacidade_maxima(self):
        return self.__capacidade_maxima

    def get_alunos_inscritos(self):
        return self.__alunos_inscritos

    def get_professores_associados(self):
        return self.__professores_associados

#Assoacia o aluno a Oficina
    def adicionar_aluno(self, aluno_nome):

        if len(self.__alunos_inscritos) < self.__capacidade_maxima:

            if aluno_nome not in self.__alunos_inscritos:
                self.__alunos_inscritos.append(aluno_nome)
                print(f"Aluno {aluno_nome} inscrito na oficina {self.__nome}.")
                return True
            
            else:
                print(f"Aluno {aluno_nome} já está inscrito na oficina {self.__nome}.")

        else:
            print(f"Oficina {self.__nome} está cheia. Não é possível adicionar mais alunos.")
        return False

 #Remove o aluno
    def remover_aluno(self, aluno_nome):

        if aluno_nome in self.__alunos_inscritos:
            self.__alunos_inscritos.remove(aluno_nome)
            print(f"Aluno {aluno_nome} removido da oficina {self.__nome}.")
            return True
        
        else:
            print(f"Aluno {aluno_nome} não está inscrito na oficina {self.__nome}.")
            return False

#Associa o professor a oficina  
    def associar_professor(self, professor_nome):
        if professor_nome not in self.__professores_associados:
            self.__professores_associados.append(professor_nome)
            print(f"Professor {professor_nome} associado à oficina {self.__nome}.")

        else:
            print(f"Professor {professor_nome} já está associado à oficina {self.__nome}.")
            
#----------------------------------------------------------------------------------------------#

    def __str__(self):
        return (
            f"Oficina: {self.__nome}\n"
            f"Descrição: {self.__descricao}\n"
            f"Capacidade: {len(self.__alunos_inscritos)}/{self.__capacidade_maxima}\n"
            f"Alunos: {', '.join(self.__alunos_inscritos)}\n"
            f"Professores: {', '.join(self.__professores_associados)}"
        )


    def to_dict(self):
        return {
            "nome": self.__nome,
            "descricao": self.__descricao,
            "capacidade_maxima": self.__capacidade_maxima,
            "alunos_inscritos": self.__alunos_inscritos,
            "professores_associados": self.__professores_associados        
        }
    
    
    @classmethod
    def from_dict(cls, data):
        oficina = cls(
            data["nome"],
            data["descricao"],
            data["capacidade_maxima"]
        )
        oficina.__alunos_inscritos = data.get("alunos_inscritos", [])
        oficina.__professores_associados = data.get("professores_associados", [])
        return oficina
#----------------------------------------------------------------------------------------------#












