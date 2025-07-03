import json
import os
from .usuario import Usuario
from .tipo_usuario import TipoUsuario

caminho_arquivo = "professores.json"

class Professor(Usuario):
    def __init__(self, nome, cpf, email, data_nasc, telefone, genero, senha, especialidade):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero, senha, TipoUsuario.professor)

        if not especialidade or not isinstance(especialidade, str):
            raise ValueError("Especialidade não pode estar vazia.")
        
        self._especialidade = especialidade
        self._oficinas = []

    # Getter e Setter usando @property
    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade):
        if not nova_especialidade or not isinstance(nova_especialidade, str):
            raise ValueError("Nova especialidade não pode estar vazia.")
        self._especialidade = nova_especialidade

    # Métodos relacionados a oficinas
    def adicionar_oficina_professor(self, oficina):
        if oficina not in self._oficinas:
            self._oficinas.append(oficina)
            if hasattr(oficina, "associar_professor"):
                oficina.associar_professor(self)

    def listar_oficinas_professor(self):
        return self._oficinas

    # Salvar/cadastrar professor no JSON
    def cadastrar_professor(self):
        professor_dict = {
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.login["email"],
            "data_nasc": self.data_nasc,
            "telefone": self.telefone,
            "genero": self.genero,
            "senha": self.login["senha"],
            "especialidade": self._especialidade
        }

        professores = []
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r", encoding="utf-8") as file:
                try:
                    professores = json.load(file)
                except json.JSONDecodeError:
                    professores = []

        professores.append(professor_dict)

        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            json.dump(professores, file, indent=4, ensure_ascii=False)

    # Representação do professor
    def __str__(self):
        return (
            f"Professor: {self.login['email']} | Nome: {self.nome} | "
            f"Especialidade: {self._especialidade} | "
            f"Total de oficinas: {len(self._oficinas)}"
        )

    # Método estático para carregar todos os professores do JSON
    @staticmethod
    def carregar_professores():
        if not os.path.exists(caminho_arquivo):
            return []

        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            try:
                dados = json.load(file)
                professores = []
                for p in dados:
                    prof = Professor(
                        nome=p["nome"],
                        cpf=p["cpf"],
                        email=p["email"],
                        data_nasc=p["data_nasc"],
                        telefone=p["telefone"],
                        genero=p["genero"],
                        senha=p["senha"],
                        especialidade=p["especialidade"]
                    )
                    professores.append(prof)
                return professores
            except json.JSONDecodeError:
                return []






      