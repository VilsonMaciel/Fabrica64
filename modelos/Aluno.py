from pessoa import Pessoa
from oficina import Oficina
import json
import datetime
import random
from os import system

class Aluno(Pessoa):
    _matriculas_usadas = set() # Set é um conjunto de dados que não é possível repetir elementos

    def __init__(self, nome, cpf, email, data_nasc, telefone, genero):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero)
        self._matricula = self._gerar_matricula()
        self._oficinas_inscritas = []
        self._frequencia = {}

    def __str__(self):
        """Função para exibir as informações do aluno"""
        info = f"""
===============================================
    Ficha do aluno: {self.nome}\n
    Matrícula: {self.matricula}\n
===============================================
    CPF: \t\t{self.cpf}\n
    Email: \t{self.email}\n
    Telefone: \t{self.telefone}\n
    Data de Nascimento: \t{self.data_nasc}
    Gênero: \t{self.genero}\n
                """
        return info
        
    @property
    def matricula(self):
        """GETTER para matrícula"""
        return self._matricula
    
    @property
    def oficinas_inscrias(self):
        """GETTER para as oficinas que o aluno está inscrito."""
        return self._oficinas_inscritas
    
    @property
    def frequencia(self):
        """GETTER para frequencia"""
        return self._frequencia
    
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

    ####### Função para salvar os alunos no arquivo .json ATENÇÃO, DEVE SER CHAMADA SEMPRE QUE HOUVER ALTERAÇÃO NA LISTA DE ALUNOS!!!!!!! ########        
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
            matricula_gerada =  str(f"{ano_atual}.{numero_aleatorio}") #Juntando os ano atual e o número aleatório para gerar uma matrícula do tipo "AAAA.XXXXXX"

            if matricula_gerada not in self._matriculas_usadas: #Verificando se a matrícula atual já existe.
                self._matriculas_usadas.add(matricula_gerada)
                print(f"O(A) aluno(a) {self.nome} foi matriculado(a) com sucesso e a sua matrícula é {matricula_gerada} !!")
            return matricula_gerada        
        
        
    def _inscrever_aluno_em_oficina(self, aluno_a_inscrever, oficina_alvo):

        confirmacao = input(f"Confirma a inscrição de {aluno_a_inscrever.nome} na oficina {oficina_alvo.nome} [S/N]?").strip().lower()

        if confirmacao == 'n':
            return f"Inscrição cancelada !!"
        
        elif confirmacao == 's':
            aluno_a_inscrever._oficinas_inscritas.append(oficina_alvo)
            oficina_alvo._alunos_inscritos.append(aluno_a_inscrever)
            return f"Inscrição do(a) Aluno(a) {aluno_a_inscrever.nome} inscrito com sucesso"
               
        else:
            print("Digite uma opção válida [S/N]")
            return Aluno._inscrever_aluno_em_oficina(self, aluno_a_inscrever, oficina_alvo)

        
    def _remover_aluno_da_oficina(self, aluno_a_remover, oficina_alvo):
        
        if aluno_a_remover not in oficina_alvo._alunos_inscritos:
            return f"O aluno {aluno_a_remover.nome} não está matriculado nesta oficina"
        
        else:    
            confirmacao = input(f"Confirma a remoção de {aluno_a_remover.nome} da oficina {oficina_alvo.nome} [S/N]").strip().lower()

            if confirmacao == 'n':
                return f"Remoção cancelada"
            
            elif confirmacao == 's':
                oficina_alvo._alunos_inscritos.remove(aluno_a_remover)
                print(f"Remoção do aluno {aluno_a_remover.nome} da oficina {oficina_alvo.nome} concluída com sucesso!! ")

            else:
                print("Digite uma opção válida (S/N)")
                return Aluno._remover_aluno_da_oficina(self, aluno_a_remover, oficina_alvo)
            
    def _pesquisar_alunos(self):
        
        print("-" * 45)
        termo = input("PESQUISAR ALUNO: ")
        alunos_encontrados = []
        
        if not termo:
            print("O campo de pesquisa não pode estar vazio!!")
            return None

        for aluno in self.lista_de_alunos:
            if (termo in aluno.nome.lower() or
                termo in aluno.cpf.lower() or
                termo in aluno.email.lower() or
                termo in aluno.matricula.lower()):
                
                alunos_encontrados.append(aluno)

        if not alunos_encontrados:
            print("Nenhum aluno encontrado com esse termo.")
            return None

        for aluno in enumerate(alunos_encontrados, 1):
            print(aluno)
            print("-" * 45)
    
    def _pesquisar_e_selecionar_aluno(self):

        print("-" * 45)
        termo = input("PESQUISAR ALUNO (por nome, cpf, email, etc): ").lower() # .lower() para busca insensível
        
        if not termo:
            print("Termo de pesquisa não pode ser vazio.")
            return None

        alunos_encontrados = []

        for aluno in self.lista_de_alunos:
            # Convertemos todos os campos para minúsculas para a comparação
            if (termo in aluno.nome.lower() or
                termo in aluno.matricula.lower() or
                termo in aluno.cpf.lower() or
                termo in aluno.email.lower()):
                alunos_encontrados.append(aluno)

        # CASO 1: Nenhum aluno encontrado
        if not alunos_encontrados:
            print("Nenhum aluno encontrado com este termo de pesquisa.")
            return None

        # CASO 2: Apenas um aluno encontrado
        if len(alunos_encontrados) == 1:
            print("Apenas um aluno encontrado:")
            print(f"-> {alunos_encontrados[0]}") # Imprime usando o __str__ do aluno
            return alunos_encontrados[0] # Captura e retorna o único aluno

        # CASO 3: Vários alunos encontrados, pedir para o utilizador escolher
        print("Vários alunos encontrados. Por favor, escolha um:")
        for indice, aluno in enumerate(alunos_encontrados, 1):
            print(f"{indice}. {aluno}") 

        # Loop para garantir que o utilizador escolha uma opção válida
        while True:
            try:
                escolha = int(input("\nDigite o número do aluno que deseja selecionar: "))
                if 1 <= escolha <= len(alunos_encontrados):
                    # O utilizador escolheu um número válido.
                    # "Capturamos" o aluno da lista.
                    aluno_selecionado = alunos_encontrados[escolha - 1] # -1 porque a lista começa em 0
                    print(f"Aluno '{aluno_selecionado.nome}' selecionado!")
                    return aluno_selecionado # Retorna o objeto do aluno escolhido
                else:
                    print("Opção inválida. Por favor, digite um número da lista.")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas o número.")

    def _editar_informacoes_aluno(self, aluno):
        pass