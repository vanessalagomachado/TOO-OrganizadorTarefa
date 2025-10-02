class Disciplina:
    def __init__(self, nome, curso, carga_horaria, professor):
        self.nome = nome
        self.__curso = curso.strip().title()
        if(0 < carga_horaria < 1000):
            self.__carga_horaria = carga_horaria
        else:
            print("Valor para Carga Horária inválido!!")
            # ajustar para impedir a criação do objeto
        self.professor = professor
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip().title()
        
    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        self.__professor = professor.strip().title()
        
    @property
    def curso(self):
        return self.__curso