from .Tarefa import Tarefa
from datetime import datetime

class TarefaProfissional(Tarefa):
    def __init__(self, titulo, projeto, data_entrega, descricao=None):
        super().__init__(titulo, descricao=descricao)
        self.projeto = projeto
        self.data_entrega = data_entrega

    @property
    def projeto(self):
        return self.__projeto

    @projeto.setter
    def projeto(self, proj):
        self.__projeto = proj.strip().title() if proj else None

    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, dt_entrega):
        """Aceita tanto string ('dd-mm-YYYY') quanto objeto datetime"""
        self.__data_entrega = None
        if dt_entrega:
            try:
                if isinstance(dt_entrega, str):
                    self.__data_entrega = datetime.strptime(dt_entrega, "%d-%m-%Y")
                elif isinstance(dt_entrega, datetime):
                    self.__data_entrega = dt_entrega
                else:
                    raise TypeError("Data de entrega deve ser str ('dd-mm-YYYY') ou datetime.")
            except (ValueError, TypeError) as e:
                print(f"Erro ao definir data de entrega: {e}")
                
    def __str__(self):
        data = self.data_entrega.strftime("%d-%m-%Y") if self.data_entrega else "Sem data definida"
        return f"[Tarefa Profissional] {self.nome} - Projeto: {self.projeto} (Entrega: {data})"

    # --- Método exibir_dados ---
    def exibir_dados(self):
        """
        Sobrescreve o método exibir_dados() da classe Tarefa
        e adiciona informações do projeto e da data de entrega.
        """
        base = super().exibir_dados()  # reaproveita a exibição da classe Tarefa
        projeto = f"Projeto: {self.projeto}\n" if self.projeto else ""
        data = f"Data de Entrega: {self.data_entrega.strftime('%d-%m-%Y')}\n" if self.data_entrega else ""
        
        return f"{base}\n{projeto}{data}"         
    
    def definir_termino(self):
        self.data_realizacao = datetime.now()
        if(self.data_realizacao > self.data_entrega):
            str_desc = f"{self.descricao} [Entrega em atraso]" if self.descricao else "[Entrega em atraso]"
            self.descricao = str_desc