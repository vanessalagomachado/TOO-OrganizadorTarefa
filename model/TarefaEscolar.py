from .Tarefa import Tarefa
from datetime import datetime

class TarefaEscolar(Tarefa):
    def __init__(self, nome_tarefa, disciplina, peso=0, descricao=None, data_realizaca=None, data_entrega=None):
        super().__init__(nome_tarefa, descricao, data_realizaca)
        self.__disciplina = disciplina
        # Construtor do TarefaEscolar não usa o setter de peso
        self.peso = peso ## 1. como usar o peso definido no setter? - atributo público, quando possui setter definido na classe, ele utiliza o setter, caso contrário fica acesso livre sem validação.
        self.__data_entrega = None
        if data_entrega is not None:
            self.data_entrega = data_entrega
        
    
    def __str__(self):
        return f"[Tarefa Escolar] {super().__str__()}"
    
    # getter e setters:
    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina
        
    @property
    def data_entrega(self):
        return self.__data_entrega
    
    @data_entrega.setter
    def data_entrega(self, str_data_entrega):
        self.__data_entrega = None
        if str_data_entrega is not None:
            try:
                self.__data_entrega = datetime.strptime(str_data_entrega, "%d-%m-%Y")
            except ValueError as e:
                print(f"Erro ao converter \"{str_data_entrega}\": {e}")
    
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        if(peso >= 0 and peso <=10):
            self.__peso = peso
        else: 
            print(f"Peso inválido!!! Informe somente [0-10]")
            self.__peso = 0
        
        
    
    def exibir_dados(self):
        data_entrega = f"{self.__data_entrega.strftime('%d-%m-%Y')}" if self.data_entrega is not None else "Sem data definida"
        txt = f"{super().exibir_dados()} \n Data Entrega: {data_entrega}"
        if(self.disciplina is not None):
            txt += f"\n Disciplina: {self.disciplina.nome}"
        if(self.peso!=0):
            txt += f"\n Peso: {self.peso}"
        return txt 