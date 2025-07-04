from pessoa import Pessoa
import json
import datetime
import random

class Aluno(Pessoa):
    _matriculas_usadas = set() #Criando lista de matrículas que já foram usadas por aluno.

    def __init__(self,nome, cpf, email, data_nasc, telefone, genero, matricula):
        super().__init__(self, nome, cpf, email, data_nasc, telefone, genero)
        self.matricula = self.gerar_matricula()
        self.oficinas_inscritas = []
        self.frequencia = {}
        return
    
    def importando_arquivo_alunos(self):
        try:
            with open("Alunos.json", 'r', encoding='uft-8') as arquivo:
                dados = json.load(arquivo)  #Abrindo o arquivo Alunos.json e carregando os dados.
            for dados_alunos in dados:
                aluno_obj = Aluno(dados_alunos['nome'], dados_alunos['cpf'], dados_alunos['email'], dados_alunos['data_nasc'],
                                  dados_alunos['telefone'], dados_alunos['genero'], dados_alunos['matricula'])
                aluno_obj.oficinas_inscritas = dados_alunos.get('oficinas_inscritas', [])
                aluno_obj.frequencia = dados_alunos.get('frequencia', {})
                self.lista_de_alunos.append(aluno_obj) #Pegando os arquivos carregados de alunos e transformando-os em objetos e colocando-os na lista lista_de_alunos

        except FileNotFoundError:
            self.lista_de_alunos = []
            
    def salvar_arquivo_alunos(self):

        dados = [{"nome": aluno.nome, "cpf": aluno.cpf, "email": aluno.email, 
                  "data_nasc": aluno.data_nasc, "telefone": aluno.telefone, "genero": aluno.genero,
                  "matricula": aluno.matricula, "oficinas_inscritas": aluno.oficinas_inscritas, "frequencia": aluno.frequencia}
                    for aluno in self.lista_de_alunos]
        
        with open("Aluno.json", 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent= 4)


    def _gerar_matricula(self):
        ano_atual = datetime.date.today().year

        while True:
            numero_aleatorio = random.randint(100000, 999999)
            matricula_gerada = f"{ano_atual}.{numero_aleatorio}"

            if matricula_gerada not in self._matriculas_usadas:
                self._matriculas_usadas.add(matricula_gerada)
                print(f"A matrícula {matricula_gerada} foi gerada com sucesso!!")
                return matricula_gerada
            
    