from model.Tarefa import Tarefa




t1 = Tarefa("Aula TOO", "teste")
print(t1.exibir_dados())
t1.concluir()
print(t1.exibir_dados())