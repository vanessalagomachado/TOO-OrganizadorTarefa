from model.TarefaGamer import TarefaGamer
from model.TarefaProfissional import TarefaProfissional
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina
from model.TarefaPessoal import TarefaPessoal
from model.StatusTarefa import StatusTarefa

class TarefaFactory():

    @staticmethod
    def criar_tarefa(tipo_tarefa: str, **args):
        """
        Método retorna a instância de tarefa de acordo com o tipo informado
        
        Parâmetros:
        - tipo_tarefa(str): tipo da tarefa: "pessoal", "profissional", "escolar", "gamer"
        - **args: argumentos específicos de cada tipo de tarefa
        """
        if tipo_tarefa == "pessoal":
            return TarefaPessoal(
                titulo=args.get("titulo",None),
                tipo=args.get("tipo", None),
                descricao=args.get("descricao", None),
                data_realizacao=args.get("data_realizacao", None),
                status=args.get("status", StatusTarefa.A_FAZER)
            )
        elif tipo_tarefa == "profissional":
            return TarefaProfissional(
                titulo=args.get("titulo", "Tarefa Profissional sem título"),
                projeto=args.get("projeto", None),
                data_entrega=args.get("data_entrega", None),
                descricao=args.get("descricao", None),
                status=args.get("status", StatusTarefa.A_FAZER)
            )
        elif tipo_tarefa == "gamer":
            return TarefaGamer(
                titulo=args.get("titulo", "Tarefa Gamer sem título"),
                tipo=args.get("tipo", None),
                descricao=args.get("descricao", None),
                data_realizacao=args.get("data_realizacao", None),
                status=args.get("status", StatusTarefa.A_FAZER),
                jogo=args.get("jogo", None)
            )
        elif tipo_tarefa == "escolar":
            return TarefaEscolar(
                nome_tarefa=args.get("titulo", "Tarefa Gamer sem título"),
                descricao=args.get("descricao", None),
                data_realizacao=args.get("data_realizacao", None),
                status=args.get("status", StatusTarefa.A_FAZER),
                data_entrega=args.get("data_entrega", None),
                peso = args.get("peso", 0),
                disciplina=args.get("disciplina", None)
            )
        else:
            raise f"Tipo de tarefa inválida: {tipo_tarefa}"