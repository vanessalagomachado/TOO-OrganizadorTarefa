from model.TarefaFactory import TarefaFactory
from model.Disciplina import Disciplina

t1 = TarefaFactory.criar_tarefa(tipo_tarefa="pessoal",
                               titulo="Fazer caminhada",
                               tipo="Saúde",
                                descricao="Caminhar 30 minutos na gare",
                                data_realizacao="09-10-2025")

print(t1)
print(t1.exibir_dados())
print("\n\n")

t2 = TarefaFactory.criar_tarefa(tipo_tarefa="profissional",
                                titulo="Documentar sistema",
                                projeto="ERP Interno",
                                data_entrega="15-10-2025",
                                descricao="Criar documentação técnica do módulo financeiro")
print(t2.exibir_dados())

print("\n\n")

d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")
t3 = TarefaFactory.criar_tarefa(tipo_tarefa="escolar",
                                titulo="Prova TOO",
                                data_realizacao="12-11-2025",
                                descricao="Estudar para a prova",
                                disciplina = d1)
print(t3.exibir_dados())

print("\n\n")


