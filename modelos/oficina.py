import os


def get_nome(self):
        """Retorna o nome da oficina."""
        
        return self.__nome

def get_descricao(self):
        """Retorna a descrição da oficina."""
        return self.__descricao

def get_capacidade_maxima(self):
        """Retorna a capacidade máxima de alunos da oficina."""
        return self.__capacidade_maxima
def get_alunos_inscritos(self):
        """Retorna a lista de alunos inscritos na oficina."""
        return self.__alunos_inscritos

def get_professores_associados(self):
        """Retorna a lista de professores associados à oficina."""
        return self.__professores_associados

def adicionar_aluno(self, aluno):
        """
        Adiciona um aluno à oficina, se houver capacidade.
        Args:
            aluno (Aluno): O objeto Aluno a ser adicionado.
        Returns:
            bool: True se o aluno foi adicionado, False caso contrário.
        """
        if len(self.__alunos_inscritos) < self.__capacidade_maxima:
            if aluno not in self.__alunos_inscritos:
                self.__alunos_inscritos.append(aluno)
                print(f"Aluno {aluno.get_nome()} inscrito na oficina {self.get_nome()}.")
                return True
            else:
                print(f"Aluno {aluno.get_nome()} já está inscrito na oficina {self.get_nome()}.")
                return False
        else:
            print(f"Oficina {self.get_nome()} está cheia. Não é possível adicionar mais alunos.")
            return False

def remover_aluno(self, aluno):
        """
        Remove um aluno da oficina.
        Args:
            aluno (Aluno): O objeto Aluno a ser removido.
        Returns:
            bool: True se o aluno foi removido, False caso contrário.
        """
        if aluno in self.__alunos_inscritos:
            self.__alunos_inscritos.remove(aluno)
            print(f"Aluno {aluno.get_nome()} removido da oficina {self.get_nome()}.")
            return True
        else:
            print(f"Aluno {aluno.get_nome()} não está inscrito na oficina {self.get_nome()}.")
            return False

def associar_professor(self, professor):
        """
        Associa um professor a esta oficina.
        Args:
            professor (Professor): O objeto Professor a ser associado.
        """
        if professor not in self.__professores_associados:
            self.__professores_associados.append(professor)
            print(f"Professor {professor.get_nome()} associado à oficina {self.get_nome()}.")
        else:
            print(f"Professor {professor.get_nome()} já está associado à oficina {self.get_nome()}.")
def __str__(self):
        """
        Retorna uma representação em string da Oficina.
        """
        return f"Oficina: {self.get_nome()} (Capacidade: {len(self.get_alunos_inscritos())}/{self.get_capacidade_maxima()})"












