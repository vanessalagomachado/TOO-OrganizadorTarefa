from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.TarefaProfissional import TarefaProfissional
from model.Disciplina import Disciplina
from model.TarefaPessoal import TarefaPessoal




d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")

print("Nome validado pelo construtor: "+d1.nome)

d1.nome = "   tecnologia de Orientação à Objetos"
print("Nome validado pelo setter: "+d1.nome)

t4 = TarefaEscolar("introducao Herança", d1, -1)
t4.data_entrega = "19-09-2025"

print(f"Tarefa Escolar:\n {t4.exibir_dados()}")


tp = TarefaProfissional(
        titulo="Documentar sistema",
        projeto="ERP Interno",
        data_entrega="15-10-2025",
        descricao="Criar documentação técnica do módulo financeiro"
    )

print(tp)
print(tp.exibir_dados())


tpessoal = TarefaPessoal(
        titulo="Fazer caminhada",
        tipo="Saúde",
        descricao="Caminhar 30 minutos na gare",
        data_realizacao="09-10-2025"
    )

print(tpessoal)
print(tpessoal.exibir_dados())