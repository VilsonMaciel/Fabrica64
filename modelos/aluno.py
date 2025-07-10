from pessoa import Pessoa
from oficina import Oficina
import json
import datetime
import random
import os

class Aluno(Pessoa):
    _matriculas_usadas = set() # Set é um conjunto de dados que não é possível repetir elementos

    def __init__(self, nome, cpf, email, data_nasc, telefone, genero):
        super().__init__(nome, cpf, email, data_nasc, telefone, genero)
        self._matricula = self._gerar_matricula()
        self._oficinas_inscritas = []

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
    def oficinas_inscritas(self):
        """GETTER para as oficinas que o aluno está inscrito."""
        return self._oficinas_inscritas
    
    
    #Função para importar alunos do arquivo Alunos.json
    @classmethod
    def importando_arquivo_alunos(cls):
        try:
            with open("Alunos.json", 'r', encoding='uft-8') as arquivo: #Abrindo o arquivo "Alunos.json" como "arquivo" dentro do meu código
                dados = json.load(arquivo) #Carregando os dados do meu arquivo que chamei de "arquivo"
            for dados_alunos in dados:
                aluno_obj = Aluno(dados_alunos['nome'], dados_alunos['cpf'], dados_alunos['email'], dados_alunos['data_nasc'],
                                  dados_alunos['telefone'], dados_alunos['genero'], dados_alunos['matricula'])
                aluno_obj.oficinas_inscritas = dados_alunos.get('oficinas_inscritas', [])
                cls.lista_de_alunos.append(aluno_obj) #Extraindo as informações que existem em forma de dicionário no arquivo .json e os convertando para Objetos Alunos.

        except FileNotFoundError:
            cls.lista_de_alunos = []

    ####### Função para salvar os alunos no arquivo .json ATENÇÃO, DEVE SER CHAMADA SEMPRE QUE HOUVER ALTERAÇÃO NA LISTA DE ALUNOS!!!!!!! ########      
    @classmethod  
    def salvar_arquivo_alunos(cls):

        dados = [{"nome": aluno.nome, "cpf": aluno.cpf, "email": aluno.email, 
                  "data_nasc": aluno.data_nasc, "telefone": aluno.telefone, "genero": aluno.genero,
                  "matricula": aluno.matricula, "oficinas_inscritas": aluno.oficinas_inscritas}
                    for aluno in cls.lista_de_alunos]
        
        with open("Alunos.json", 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent= 4)

    @classmethod
    #Função para gerar matrículas aleatórias iniciando pelo ano atual.
    def _gerar_matricula(self):
        ano_atual = datetime.date.today().year #Capturando o ano atual

        while True: #Entrando no laço de verificação da matrícula.
            numero_aleatorio = random.randint(100000, 999999) #Criando um número aleatório de 6 dígitos (entre 100000 e 999999)
            matricula_gerada =  str(f"{ano_atual}.{numero_aleatorio}") #Juntando os ano atual e o número aleatório para gerar uma matrícula do tipo "AAAA.XXXXXX"

            if matricula_gerada not in self._matriculas_usadas: #Verificando se a matrícula atual já existe.
                Aluno._matriculas_usadas.add(matricula_gerada)
                print(f"O(A) aluno(a) {self.nome} foi matriculado(a) com sucesso e a sua matrícula é {matricula_gerada} !!")
            return matricula_gerada        
        
    @classmethod
    def _inscrever_aluno_em_oficina(cls, aluno_a_inscrever, oficina_alvo):

        while True:
            confirmacao = input(f"Confirma a inscrição de {aluno_a_inscrever.nome} na oficina {oficina_alvo.nome} [S/N]?").strip().lower()

            if confirmacao == 'n':
                print(f"Inscrição cancelada !!")
                break

            elif confirmacao == 's':
                aluno_a_inscrever._oficinas_inscritas.append(oficina_alvo)
                oficina_alvo._alunos_inscritos.append(aluno_a_inscrever)
                print(f"Inscrição do(a) Aluno(a) {aluno_a_inscrever.nome} inscrito com sucesso")
                cls.salvar_arquivo_alunos()
                break
                
            else:
                print("Digite uma opção válida [S/N]")


    @classmethod
    def _remover_aluno_da_oficina(cls, aluno_a_remover, oficina_alvo):
        
        if aluno_a_remover not in oficina_alvo._alunos_inscritos:
            return f"O aluno {aluno_a_remover.nome} não está matriculado nesta oficina"
        
        else:
            while True:
                confirmacao = input(f"Confirma a remoção de {aluno_a_remover.nome} da oficina {oficina_alvo.nome} [S/N]").strip().lower()

                if confirmacao == 'n':
                    print(f"Remoção cancelada")
                    break
                
                elif confirmacao == 's':
                    oficina_alvo._alunos_inscritos.remove(aluno_a_remover)
                    print(f"Remoção do aluno {aluno_a_remover.nome} da oficina {oficina_alvo.nome} concluída com sucesso!! ")
                    cls.salvar_arquivo_alunos()
                    break

                else:
                    print("Digite uma opção válida (S/N)") 
    @classmethod        
    def _pesquisar_alunos(cls):
        
        print("-" * 45)
        termo = input("PESQUISAR ALUNO: ")
        alunos_encontrados = []
        
        if not termo:
            print("O campo de pesquisa não pode estar vazio!!")
            return None

        for aluno in cls.lista_de_alunos:
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

    @classmethod
    def _pesquisar_e_selecionar_aluno(cls):

        print("-" * 45)
        termo = input("PESQUISAR ALUNO (por nome, cpf, email, etc): ").lower() 
        
        if not termo:
            print("Termo de pesquisa não pode ser vazio.")
            return None

        alunos_encontrados = []

        for aluno in cls.lista_de_alunos:
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

    @classmethod
    def _editar_informacoes_aluno(cls): 
        
        aluno_editar = cls._pesquisar_e_selecionar_aluno() #Capturando o aluno que queremos editar

        if not aluno_editar:
            print("Nenhum aluno selecionado. Retornando ao menu!!")
            return
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"==== EDITANDO INFORMAÇÕES DO ALUNO: {aluno_editar.nome} ====")
        print("\tPressione ENTER para manter a informação atual")
        print("-" * 50)

        #----- CAMPO NOME -----#
        while True:
            try:
                novo_nome = input(f"Nome atual [{aluno_editar.nome}]: ").strip()
                if novo_nome: 
                    aluno_editar.nome = novo_nome # Fazendo a alteração e acionando a validação dentro do setter na classe Pessoa
                    print(">> Nome atualizado!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        #----- CAMPO CPF -----#
        while True:
            try:
                novo_cpf = input(f"CPF atual [{aluno_editar.cpf}]: ").strip()
                if novo_cpf:
                    if any(aluno.cpf == novo_cpf and aluno.matricula != aluno_editar.matricula for aluno in cls.lista_de_alunos):
                        raise ValueError("Este CPF pertence a outro aluno!")
                    aluno_editar.cpf = novo_cpf
                    print(">> CPF Atualizado!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        #----- CAMPO EMAIL -----#
        while True:
            try:
                novo_email = input(f"Email atual [{aluno_editar.email}]: ").strip()
                if novo_email:
                    aluno_editar.email = novo_email
                    print(">> Email atualizado!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        #----- CAMPO DATA DE NASCIMENTO -----#
        while True:
            try:
                novo_data_nasc = input(f"Data de nascimento atual [{aluno_editar.data_nasc}]: ").strip()
                if novo_data_nasc:
                    aluno_editar.data_nasc = novo_data_nasc
                    print(">> Data de nascimento atualizada!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        #----- CAMPO TELEFONE -----#
        while True:
            try:
                novo_telefone = input(f"Telefone atual [{aluno_editar.telefone}]: ").strip()
                if novo_telefone:
                    aluno_editar.telefone = novo_telefone
                    print(">> Telefone atualizado!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        #----- CAMPO GENERO -----#
        while True:
            try:
                novo_genero = input(f"Email atual [{aluno_editar.genero}]: ").strip()
                if novo_genero:
                    aluno_editar.genero = novo_genero
                    print(">> Gênero atualizado!")
                break
            except ValueError as e:
                print(f"ERRO: {e}")

        print("-" * 50)
        print("\n--- REVISE AS ALTERAÇÕES ---")
        
        # Ao fazer print(aluno_editar), o método __str__ será chamado
        print(aluno_editar)
        
        print("-" * 50)
        
        # --- PASSO DE CONFIRMAÇÃO FINAL ---
        confirmacao = input("Deseja salvar estas alterações? (S/N): ").strip().lower()
        
        if confirmacao == 's':
            # Se o utilizador confirmar, nós gravamos as alterações no ficheiro.
            cls.salvar_arquivo_alunos()
            print("\nAlterações salvas com sucesso!")
        else:
            # Se o utilizador cancelar, nós não fazemos nada. As alterações
            # feitas no objeto em memória serão simplesmente descartadas
            # quando a função terminar.
            print("\nOperação cancelada. As alterações não foram salvas.")

<<<<<<< Updated upstream
        input("Pressione Enter para continuar...")
=======
        input("Pressione Enter para continuar...")
>>>>>>> Stashed changes
