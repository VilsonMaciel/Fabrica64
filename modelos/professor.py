import json
import os
from typing import List
from .usuario import Usuario
from .tipo_usuario import TipoUsuario

caminho_arquivo = "professores.json"

class Professor(Usuario):
    def __init__(self, nome: str, cpf: str, email: str, data_nasc: str,
                 telefone: str, genero: str, senha: str, especialidade: str):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero, senha, TipoUsuario.professor)

        if not especialidade or not isinstance(especialidade, str):
            raise ValueError("A especialidade do professor deve ser uma string não vazia.")
        
        self._especialidade = especialidade
        self._oficinas: List[object] = []

    @property
    def especialidade(self) -> str:
        return self._especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade: str):
        if not nova_especialidade or not isinstance(nova_especialidade, str):
            raise ValueError("A nova especialidade deve ser uma string não vazia.")
        self._especialidade = nova_especialidade

    def adicionar_oficina_professor(self, oficina: object):
        if oficina not in self._oficinas:
            self._oficinas.append(oficina)
            if hasattr(oficina, "associar_professor"):
                oficina.associar_professor(self)

    def listar_oficinas_professor(self) -> List[object]:
        return self._oficinas

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
            try:
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    professores = json.load(f)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo de professores. Um novo será criado.")

        professores.append(professor_dict)

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(professores, f, indent=4, ensure_ascii=False)
        print(f"Professor {self.nome} cadastrado com sucesso.")

    def __str__(self) -> str:
        return (
            f"Professor: {self.login['email']} | Nome: {self.nome} | "
            f"Especialidade: {self._especialidade} | "
            f"Oficinas: {len(self._oficinas)}"
        )

    @staticmethod
    def carregar_professores() -> List['Professor']:
        if not os.path.exists(caminho_arquivo):
            return []

        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [
                    Professor(
                        nome=p["nome"],
                        cpf=p["cpf"],
                        email=p["email"],
                        data_nasc=p["data_nasc"],
                        telefone=p["telefone"],
                        genero=p["genero"],
                        senha=p["senha"],
                        especialidade=p["especialidade"]
                    ) for p in dados
                ]
        except json.JSONDecodeError:
            print("Arquivo JSON corrompido.")
            return []

    def listar_professor(self):
        professores = Professor.carregar_professores()
        if not professores:
            print("Nenhum professor cadastrado.")
            return

        for prof in professores:
            print(prof)





      