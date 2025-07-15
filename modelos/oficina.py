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

    # Chamadas de funções
      
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

    # Metodos de Alteração

    def adicionar_aluno(self, aluno_nome):

        if len(self.__alunos_inscritos) < self.__capacidade_maxima:

            if aluno_nome not in self.__alunos_inscritos:
                self.__alunos_inscritos.append(aluno_nome)
                print(f"aluno ({aluno_nome}) inscrito na oficina ({self.__nome})")
                return True
            
            else:
                print(f"aluno ({aluno_nome}) ja está inscrito nesta oficina")

        else:
            print(f" a oficina ({self.__nome}) esta cheia (Não é possível adicionar mais alunos)")
        return False

    # remove um aluno da oficina

    def remover_aluno(self, aluno_nome):

        if aluno_nome in self.__alunos_inscritos:
            self.__alunos_inscritos.remove(aluno_nome)
            print(f"aluno ({aluno_nome}) removido da oficina ({self.__nome})")
            return True
        
        else:
            print(f"aluno ({aluno_nome}) nao encontrado nesta oficina")
            return False

    # associa um professor a oficina
        
    def associar_professor(self, professor_nome):

        if professor_nome not in self.__professores_associados:
            self.__professores_associados.append(professor_nome)
            print(f"professor ({professor_nome}) associado a oficina ({self.__nome})")
            return True
        
        else:
            print(f"professor ({professor_nome}) ja esta associado a esta oficina")
            return False

    def __str__(self):
        alunos_str = ', '.join(self.__alunos_inscritos) if self.__alunos_inscritos else "nenhum aluno inscrito"
        professores_str = ', '.join(self.__professores_associados) if self.__professores_associados else 'nenhum professor associado'

        return (

            f"Oficina: {self.__nome}\n"
            f"  Descrição: {self.__descricao}\n"
            f"  Vagas: {len(self.__alunos_inscritos)}/{self.__capacidade_maxima}\n"
            f"  Professores: {professores_str}\n"
            f"  Alunos: {alunos_str}"

        )

    # cria um dicionario pra JSON
    
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

# funçoes do JSON

def salvar_oficina_em_json(oficina, caminho_arquivo):

   
    with open(caminho_arquivo, 'w', encoding = 'utf-8') as f:
        json.dump(oficina.to_dict(), f, ensure_ascii = False, indent = 4)
    print(f"Oficina '{oficina.get_nome()}' salva com sucesso em ({caminho_arquivo})")


def carregar_oficina_de_json(caminho_arquivo):
    try:
       
        with open(caminho_arquivo, 'r', encoding = 'utf-8') as f:
            dados = json.load(f)

        oficina = Oficina.from_dict(dados)
        print(f"Oficina ({oficina.get_nome()}) carregada com sucesso de ({caminho_arquivo})")
        return oficina
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"falha ao carregar oficina: {e}")
        return None

# pesquisa de oficinas

def carregar_todas_oficinas(caminho_arquivo):
    oficinas = []

    try:
       
        with open(caminho_arquivo, 'r', encoding = 'utf-8') as f:
            dados = json.load(f)
    
        if isinstance(dados, list):
            oficinas = [Oficina.from_dict(d) for d in dados]
            print(f"{len(oficinas)} oficinas carregadas com sucesso")

        else:
            oficinas = [Oficina.from_dict(dados)]
            print("oficina carregada")
        
        return oficinas
    
    except FileNotFoundError:
        print(f"arquivo ({caminho_arquivo}) nao encontrado")
        
    except json.JSONDecodeError:
        print(f"arquivo ({caminho_arquivo}) esta corrompido ou mal formatado")

    return oficinas

def pesquisar_oficina(nome, caminho_arquivo):
    oficinas = carregar_todas_oficinas(caminho_arquivo)

    for oficina in oficinas:

        if oficina.get_nome().lower() == nome.lower():
            print("Oficina encontrada:")
            print(oficina)
            return oficina
        
    print(f"nenhuma oficina com o nome ({nome}) foi encontrada")
    return None