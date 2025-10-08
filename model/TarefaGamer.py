from .Tarefa import Tarefa

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao)
        self.tipo = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.

