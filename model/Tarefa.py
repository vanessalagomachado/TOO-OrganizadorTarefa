from datetime import datetime
from abc import ABC, abstractmethod

class Tarefa(ABC):
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None):
        self.nome = nome_tarefa
        self.__concluido = False
        self.__descricao = descricao
        self.__data_realizacao = None   # inicializa
        if data_realizacao: # se tiver valor, atualiza
            self.data_realizacao = data_realizacao 
    
    
    ## encapsulamento: getter e setter
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_tarefa):
        self.__nome = nome_tarefa.title()
        
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc
        
    @property
    def data_realizacao(self):
        return self.__data_realizacao ## alterar para publico
    
    @data_realizacao.setter
    def data_realizacao(self, data):
        self.__data_realizacao = None #inicializando
        if data is not None:
            if isinstance(data, str):
                try:
                    self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
                except ValueError as e:
                    print(f"Data em formato inválido: {e}")
            elif isinstance(data, datetime):
                self.__data_realizacao = data
            else:
                print("Data inválida")
        
    
    
    ## outros métodos
    def concluir(self):
        self.__concluido = True   
        self.definir_termino() 
    
    
    
    
    
    def __str__(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        return f"{self.__nome} [{status}]"
    
    def __eq__(self, outro):
        if(self.nome == outro.nome and self.data_realizacao == outro.data_realizacao):
            return True
        else:
            return False
        

    @abstractmethod
    def exibir_dados(self):
        status = "CONCLUÍDO" if self.__concluido else "A FAZER"
        descricao = f"Descrição: {self.descricao}\n" if self.descricao else ""
        data = f"{self.data_realizacao.strftime('%d-%m-%Y')}" if self.data_realizacao else "Sem data definida"
        return f"Tarefa cadastrada:\n {self.nome} [{status}]\n {descricao} Data Prevista: {data}"

    @abstractmethod
    def definir_termino(self):
        pass