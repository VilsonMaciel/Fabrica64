import datetime
from typing import Dict, List, Optional
from aluno import Aluno
from oficina import Oficina

class ControleFrequencia:
    def __init__(self):
        #inicializa o controle de frequência com estrutura em memória
    
        self.registros = {}  #estrutura principal de armazenamento

    def registrar_frequencia(self, oficina: Oficina, alunos: List[Aluno], 
                           data: Optional[datetime.date] = None, 
                           status: str = 'presente') -> bool:
        #registra frequência para uma lista de alunos
                
        try:
            #validação de entrada
            if not isinstance(oficina, Oficina):
                raise ValueError("Oficina inválida")
                
            if not alunos or not all(isinstance(a, Aluno) for a in alunos):
                raise ValueError("Lista de alunos inválida")
                
            status = status.lower()
            if status not in ['presente', 'falta']:
                raise ValueError("Status deve ser 'presente' ou 'falta'")
                
            data = data or datetime.date.today()
            if not isinstance(data, datetime.date):
                raise ValueError("Data inválida")
                
            data_str = data.strftime('%d/%m/%Y')  #formato brasileiro
            
            #operação principal
            if oficina.get_nome() not in self.registros:
                self.registros[oficina.get_nome()] = {}
                
            for aluno in alunos:
                if aluno.matricula not in self.registros[oficina.get_nome()]:
                    self.registros[oficina.get_nome()][aluno.matricula] = {}
                
                self.registros[oficina.get_nome()][aluno.matricula][data_str] = status
            
            return True
            
        except Exception as e:
            print(f"ERRO: Falha ao registrar frequência: {str(e)}")
            return False

    def editar_frequencia(self, oficina: Oficina, aluno: Aluno, 
                         data: datetime.date, novo_status: str) -> bool:
        #edita um registro de frequência existente
        
        try:
            #validação de entrada
            if not isinstance(oficina, Oficina):
                raise ValueError("Oficina inválida")
                
            if not isinstance(aluno, Aluno):
                raise ValueError("Aluno inválido")
                
            novo_status = novo_status.lower()
            if novo_status not in ['presente', 'falta']:
                raise ValueError("Status deve ser 'presente' ou 'falta'")
                
            if not isinstance(data, datetime.date):
                raise ValueError("Data inválida")
                
            data_str = data.strftime('%d/%m/%Y')
            
            #verifica existência do registro
            if (oficina.get_nome() not in self.registros or 
                aluno.matricula not in self.registros[oficina.get_nome()] or 
                data_str not in self.registros[oficina.get_nome()][aluno.matricula]):
                raise ValueError("Registro não encontrado")
            
            #atualiza o registro
            self.registros[oficina.get_nome()][aluno.matricula][data_str] = novo_status
            
            return True
            
        except Exception as e:
            print(f"ERRO: Falha ao editar frequência: {str(e)}")
            return False

    def visualizar_frequencia_aluno(self, oficina: Oficina, aluno: Aluno) -> Dict[str, str]:
        #retorna o histórico completo de frequência de um aluno
        
        if not isinstance(oficina, Oficina) or not isinstance(aluno, Aluno):
            raise ValueError("Oficina ou aluno inválidos")
            
        if (oficina.get_nome() in self.registros and 
            aluno.matricula in self.registros[oficina.get_nome()]):
            return self.registros[oficina.get_nome()][aluno.matricula]
        return {}

    def listar_frequencia_oficina(self, oficina: Oficina) -> Dict[str, Dict]:
        #lista a frequência de todos os alunos de uma oficina
        
        if not isinstance(oficina, Oficina):
            raise ValueError("Oficina inválida")
            
        if oficina.get_nome() not in self.registros:
            return {}
            
        resultado = {}
        alunos_inscritos = {a.matricula: a for a in oficina.get_alunos_inscritos()}
        
        for matricula, registros in self.registros[oficina.get_nome()].items():
            if matricula in alunos_inscritos:
                aluno = alunos_inscritos[matricula]
                resultado[aluno.nome] = {
                    'matricula': matricula,
                    'registros': registros,
                    'porcentagem': self._calcular_porcentagem(registros)
                }
        return resultado

    def calcular_porcentagem(self, registros: Dict[str, str]) -> float:
        #método auxiliar para cálculo de porcentagem de presença
        if not registros:
            return 0.0
        total = len(registros)
        presentes = sum(1 for s in registros.values() if s == 'presente')
        return round((presentes / total) * 100, 2)

    def calcular_porcentagem_frequencia(self, oficina: Oficina, aluno: Aluno) -> float:
        #calcula a porcentagem de presença de um aluno na oficina
        
        registros = self.visualizar_frequencia_aluno(oficina, aluno)
        return self.calcular_porcentagem(registros)

    def limpar_registros_oficina(self, oficina: Oficina) -> bool:
        #remove todos os registros de frequência de uma oficina
        
        try:
            if not isinstance(oficina, Oficina):
                raise ValueError("Oficina inválida")
                
            if oficina.get_nome() in self.registros:
                del self.registros[oficina.get_nome()]
                return True
            return False
        except Exception as e:
            print(f"Erro ao limpar registros: {str(e)}")
            return False

    def menu_frequencia(self, usuario, oficina: Oficina = None):
        #menu principal do sistema de frequência
        try:
            if not oficina or not isinstance(oficina, Oficina):
                print("Oficina inválida ou não selecionada.")
                return
                
            while True:
                print("\n--- MENU FREQUÊNCIA ---")
                print(f"Oficina: {oficina.get_nome()}")
                print("1. Registrar frequência para alunos")
                print("2. Editar registro de frequência")
                print("3. Visualizar frequência de um aluno")
                print("4. Listar frequência da turma")
                print("5. Ver porcentagem de frequência da turma")
                print("0. Voltar")
                
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '0':
                    break
                elif opcao == '1':
                    self.menu_registrar_frequencia(oficina)
                elif opcao == '2':
                    self.menu_editar_frequencia(oficina)
                elif opcao == '3':
                    self.menu_visualizar_frequencia(oficina)
                elif opcao == '4':
                    self.menu_listar_frequencia(oficina)
                elif opcao == '5':
                    self.menu_porcentagem_frequencia(oficina)
                else:
                    print("Opção inválida. Tente novamente.")
                    
        except Exception as e:
            print(f"ERRO CRÍTICO: {str(e)}")