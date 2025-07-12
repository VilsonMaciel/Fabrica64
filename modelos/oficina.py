#oficina
# modelos/oficina.py


import json

class Oficina:

    def __init__(self, nome, descricao, capacidade_maxima):
        if not nome or not descricao or not isinstance(capacidade_maxima, int) or capacidade_maxima <= 0:
            raise ValueError("Nome, descrição e capacidade_maxima (número inteiro maior que zero) são obrigatórios.")

        self.__nome = nome
        self.__descricao = descricao
        self.__capacidade_maxima = capacidade_maxima
        self.__alunos_inscritos = []
        self.__professores_associados = []
        
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


    # adicinar aluno

    def adicionar_aluno(self, aluno_nome):

        if len(self.__alunos_inscritos) < self.__capacidade_maxima:
            if aluno_nome not in self.__alunos_inscritos:
                self.__alunos_inscritos.append(aluno_nome)
                print(f"SUCESSO: Aluno '{aluno_nome}' inscrito na oficina '{self.__nome}'.")
                return True
            
            else:

                print(f"AVISO: Aluno '{aluno_nome}' já está inscrito nesta oficina.")
        else:
            print(f"ERRO: A oficina '{self.__nome}' está cheia. Não é possível adicionar mais alunos.")
        return False
# remove aluno
    
    def remover_aluno(self, aluno_nome):
        
        if aluno_nome in self.__alunos_inscritos:
            self.__alunos_inscritos.remove(aluno_nome)
            print(f"SUCESSO: Aluno '{aluno_nome}' removido da oficina '{self.__nome}'.")

            return True
        
        else:

            print(f"ERRO: Aluno '{aluno_nome}' não encontrado nesta oficina.")
            return False
# associa um professor
        
    def associar_professor(self, professor_nome):
        
        if professor_nome not in self.__professores_associados:
            self.__professores_associados.append(professor_nome)
            print(f"SUCESSO: Professor '{professor_nome}' associado à oficina '{self.__nome}'.")
            return True
        else:
            print(f"AVISO: Professor '{professor_nome}' já está associado a esta oficina.")
            return False

    
    def __str__(self):
        
        alunos_str = ', '.join(self.__alunos_inscritos) if self.__alunos_inscritos else "Nenhum aluno inscrito."
        professores_str = ', '.join(self.__professores_associados) if self.__professores_associados else 'Nenhum professor associado.'

        return (
            f"Oficina: {self.__nome}\n"
            f"  Descrição: {self.__descricao}\n"
            f"  Vagas: {len(self.__alunos_inscritos)}/{self.__capacidade_maxima}\n"
            f"  Professores: {professores_str}\n"
            f"  Alunos: {alunos_str}"
        )
#----Dicionario para a estrutura json----#
    
    def to_dict(self):
        
        return {
            "nome": self.__nome,
            "descricao": self.__descricao,
            "capacidade_maxima": self.__capacidade_maxima,
            "alunos_inscritos": self.__alunos_inscritos,
            "professores_associados": self.__professores_associados
        }
#--------------------------------------#
    
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

#-----salva em json-----#
    
def salvar_oficina_em_json(oficina, caminho_arquivo):
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(oficina.to_dict(), f, ensure_ascii=False, indent=4)
    print(f"Oficina '{oficina.get_nome()}' salva com sucesso em '{caminho_arquivo}'.")

def carregar_oficina_de_json(caminho_arquivo):
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    oficina = Oficina.from_dict(dados)
    print(f"Oficina '{oficina.get_nome()}' carregada com sucesso de '{caminho_arquivo}'.")
    return oficina
