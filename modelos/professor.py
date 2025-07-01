from .usuario import Usuario
from .tipo_usuario import TipoUsuario

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


#métodos relacionados a oficinas 
        
    def adicionar_oficina_professor(self,oficina):

        if oficina not in self._oficinas:
            self._oficinas.append(oficina)
            if hasattr(oficina, "associar_professor"):
                oficina.associar_professor(self)


  
    def listar_oficinas_professor(self):
        return self.__oficinas

    # Representação do professor
    def __str__(self):
        return (
            f"Professor: {self.login['email']} | Nome: {self.nome} | "
            f"Especialidade: {self._especialidade} | "
            f"Total de oficinas: {len(self._oficinas)}"
        )






      