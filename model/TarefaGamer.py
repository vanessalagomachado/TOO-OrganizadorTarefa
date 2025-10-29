from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from datetime import datetime

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None, jogo=None, status = StatusTarefa.A_FAZER):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao, status=status)
        self.tipo = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.
        self.jogo = jogo

    @property
    def jogo(self):
        return self._jogo
    
    @jogo.setter
    def jogo(self, nome_jogo):
        if(nome_jogo):
            self._jogo = nome_jogo.strip().title()

    def definir_termino(self):
        self.data_realizacao = datetime.now()
        
    def exibir_dados(self):
        base = super().exibir_dados()
        txt_gamer = f"Tipo: {self.tipo}"
        txt_gamer += f"\nJogo: {self.jogo}"
        return f"{base}\n{txt_gamer}"
    