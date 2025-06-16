from pessoa import Pessoa
from oficina import Oficina
import json
import datetime
import random
from os import system

class Aluno(Pessoa):
    _matriculas_usadas = set() # Set é um conjunto de dados que não é possível repetir elementos

    def __init__(self,nome, cpf, email, data_nasc, telefone, genero):
        super().__init__(self, nome, cpf, email, data_nasc, telefone, genero)
        self._matricula = self._gerar_matricula()
        self._oficinas_inscritas = []
        self._frequencia = {}
        return
        
    @property
    def matricula(self):
        """GETTER para matrícula"""
        return self._matricula
    
    @property
    def oficinas_inscrias(self):
        """GETTER para as oficinas que o aluno está inscrito."""
        return 
    
    #Função para importar alunos do arquivo Alunos.json
    def importando_arquivo_alunos(self):
        try:
            with open("Alunos.json", 'r', encoding='uft-8') as arquivo: #Abrindo o arquivo "Alunos.json" como "arquivo" dentro do meu código
                dados = json.load(arquivo) #Carregando os dados do meu arquivo que chamei de "arquivo"
            for dados_alunos in dados:
                aluno_obj = Aluno(dados_alunos['nome'], dados_alunos['cpf'], dados_alunos['email'], dados_alunos['data_nasc'],
                                  dados_alunos['telefone'], dados_alunos['genero'], dados_alunos['matricula'])
                aluno_obj.oficinas_inscritas = dados_alunos.get('oficinas_inscritas', [])
                aluno_obj.frequencia = dados_alunos.get('frequencia', {})  
                self.lista_de_alunos.append(aluno_obj) #Extraindo as informações que existem em forma de dicionário no arquivo .json e os convertando para Objetos Alunos.

        except FileNotFoundError:
            self.lista_de_alunos = []

    #Função para salvar os alunos no arquivo .json ATENÇÃO, DEVE SER CHAMADA SEMPRE QUE HOUVER ALTERAÇÃO NA LISTA DE ALUNOS!!!!!!!        
    def salvar_arquivo_alunos(self):

        dados = [{"nome": aluno.nome, "cpf": aluno.cpf, "email": aluno.email, 
                  "data_nasc": aluno.data_nasc, "telefone": aluno.telefone, "genero": aluno.genero,
                  "matricula": aluno.matricula, "oficinas_inscritas": aluno.oficinas_inscritas, "frequencia": aluno.frequencia}
                    for aluno in self.lista_de_alunos]
        
        with open("Aluno.json", 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent= 4)


    #Função para gerar matrículas aleatórias iniciando pelo ano atual.
    def _gerar_matricula(self):

        ano_atual = datetime.date.today().year #Capturando o ano atual
        while True: #Entrando no laço de verificação da matrícula.
            numero_aleatorio = random.randint(100000, 999999) #Criando um número aleatório de 6 dígitos (entre 100000 e 999999)
            matricula_gerada = f"{ano_atual}.{numero_aleatorio}" #Juntando os ano atual e o número aleatório para gerar uma matrícula do tipo "AAAA.XXXXXX"

            if matricula_gerada not in self._matriculas_usadas: #Verificando se a matrícula atual já existe.
                self._matriculas_usadas.add(matricula_gerada)
            return matricula_gerada        
        
    def _inscrever_aluno_em_oficina(self, aluno_a_inscrever, oficina_alvo):

        confirmacao = input(f"Confirma a inscrição de {aluno_a_inscrever.nome} na oficina {oficina_alvo.nome} [S/N]?").strip().lower()
        if confirmacao == 'n':
            return f"Inscrição cancelada !!"
        
        else:
            aluno_a_inscrever._oficinas_inscritas.append(oficina_alvo)
            oficina_alvo._alunos_inscritos.append(aluno_a_inscrever)
            return f"Inscrição do(a) Aluno(a) {aluno_a_inscrever.nome} inscrito com sucesso"
        
