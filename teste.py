from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina

t1 = Tarefa("Aula TOO", "teste")
print(t1.exibir_dados())
t1.concluir()
print(t1.exibir_dados())

t2 = Tarefa("Fazer compras mercado", "teste", "19-09-2025")
print(t2.exibir_dados())

print(t2.exibir_dados())

t3 = Tarefa("Fazer compras mercado", "teste", "19-09-2025")

if(t2 == t3):
    print("Tarefas iguais")
else:
    print("Tarefas diferentes")
    



d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")

print("Nome validado pelo construtor: "+d1.nome)

d1.nome = "   tecnologia de Orientação à Objetos"
print("Nome validado pelo setter: "+d1.nome)

t4 = TarefaEscolar("introducao Herança", d1, -1)
t4.data_entrega = "19-09-2025"

print(f"Tarefa Escolar:\n {t4.exibir_dados()}")


