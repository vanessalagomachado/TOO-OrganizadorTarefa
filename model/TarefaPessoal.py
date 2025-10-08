from .Tarefa import Tarefa
from datetime import datetime

class TarefaPessoal(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao)
        self.tipo = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.

    # --- Encapsulamento ---
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tp_tarefa):
        self.__tipo = tp_tarefa.strip().title() if tp_tarefa else None

    # --- Método especial ---
    def __str__(self):
        tipo_str = f" - Tipo: {self.tipo}" if self.tipo else ""
        return f"[Tarefa Pessoal] {super().__str__()}{tipo_str}"

    # --- Sobrescrita de método ---
    def exibir_dados(self):
        """
        Sobrescreve o método exibir_dados() da classe Tarefa
        para incluir o tipo da tarefa pessoal.
        """
        base = super().exibir_dados()  # reutiliza exibição da classe mãe
        tipo = f"Tipo: {self.tipo}\n" if self.tipo else ""
        return f"{base}\n{tipo}"
        
    def definir_termino(self):
        self.data_realizacao = datetime.now()
   