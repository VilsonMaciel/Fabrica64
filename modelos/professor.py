from .usuario import Usuario

class Professor(Usuario):

    def __init__(self,nome,cpf,email,data_nasc,telefone,genero,login,senha,especialidade):

        super().__init__(nome,cpf,email,data_nasc,telefone,genero,login,senha)

        if not especialidade or not isinstance(especialidade,str):
            raise ValueError("Especialidade não pode estar vazia.")
        
        self._especialidade=especialidade
        self.oficinas=[]

#Getter e Setter da especialidade
    def get_especialidade(self):
        return self._especialidade
    

    def set_especialidade(self,nova_especialidade):
        if not nova_especialidade or not isinstance(nova_especialidade, str):
            raise ValueError("Nova especialidade não pode estar vazia.")
        self._especialidade = nova_especialidade


#métodos relacionados a oficinas 
        
    def adicionar_oficina(self,oficina):
        if oficina not in self._oficinas:
            self._oficina.append(oficina)
            if hasattr(oficina, "associar_professor"):# hasattr verifica o objeto se possui o atributo especifíco como "associar_professor"
                oficina.associar_professor(self)

    def listar_oficinas(self):
        return self.__oficinas

    # Representação do professor
    def __str__(self):
        return (f"Professor: {self._Usuario__login} | Nome: {self._Usuario__nome} | "
                f"Especialidade: {self.__especialidade} | "
                f"Total de oficinas: {len(self.__oficinas)}")






      