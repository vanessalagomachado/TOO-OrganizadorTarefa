from model.TarefaGamer import TarefaGamer
from datetime import datetime


a = TarefaGamer(titulo="Projeto Teste")

print(a)
a.concluir()
print(a.exibir_dados())