from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina

d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")

print("Nome validado pelo construtor: "+d1.nome)

d1.nome = "   tecnologia de Orientação à Objetos"
from model.TarefaEscolar import TarefaEscolar
from model.TarefaProfissional import TarefaProfissional
from model.Disciplina import Disciplina
print("Nome validado pelo setter: "+d1.nome)

t4 = TarefaEscolar("introducao Herança", d1, -1)
t4.data_entrega = "19-09-2025"

print(f"Tarefa Escolar:\n {t4.exibir_dados()}")

t4.concluir()

print(f"----\n\nTarefa Escolar:\n {t4.exibir_dados()}")