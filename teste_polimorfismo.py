from model.TarefaGamer import TarefaGamer
from datetime import datetime
from model.TarefaProfissional import TarefaProfissional
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina
from model.TarefaPessoal import TarefaPessoal

t1 = TarefaPessoal("Limpar casa")


t2 = TarefaGamer(titulo="Coletar item X")
t2.jogo = "Ragnarok"


t3 = TarefaProfissional("implementar ação da página Home", "Website IFSUL", "07-10-2025")

d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")
t4 = TarefaEscolar("introducao Herança", d1, 3)
t4.data_entrega = "19-09-2025"



t4.concluir()
t2.concluir()


lista_tarefas = [t1, t2, t3, t4]

for obj_tarefa in lista_tarefas:
    print(obj_tarefa.exibir_dados())