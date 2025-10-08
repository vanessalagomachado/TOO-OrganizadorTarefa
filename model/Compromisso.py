from .Agendamento import Agendamento
from .Tarefa import Tarefa

class Compromisso(Agendamento, Tarefa):
    def __init__(self, titulo, descricao=None, data_hora_ini=None, data_hora_fim=None, local=None):
        # Inicializa a parte da Tarefa
        Tarefa.__init__(self, nome_tarefa=titulo, descricao=descricao, data_realizacao=data_hora_ini)
            
        # Inicializa a parte do Agendamento
        Agendamento.__init__(self, 
                            data_inicio=data_hora_ini, 
                            data_final=data_hora_fim, 
                            atividades=descricao or "", 
                            nome=titulo, 
                            local=local)
        
    def exibir_dados(self):
        """Sobrescreve para exibir as informações combinadas de Tarefa e Agendamento."""
        dados_tarefa = Tarefa.exibir_dados(self)  # chama exibir_dados da classe Tarefa
        dados_agendamento = (
            f"Local: {self.local}\n"
            f"Início: {self.data_inicio.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_inicio, datetime) else self.data_inicio}\n" if self.data_inicio else ""
            f"Término: {self.data_final.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_final, datetime) else self.data_final}\n" if self.data_final else ""
        )
        return f"--- Compromisso ---\n{dados_tarefa}\n{dados_agendamento}"

    def __str__(self):
        return f"Compromisso: {self.nome} em {self.local if self.local else 'local indefinido'}"