from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.TarefaProfissional import TarefaProfissional
from model.Disciplina import Disciplina
from model.TarefaPessoal import TarefaPessoal




d1 = Disciplina("   tecnologia de Orientação à Objetos", "BCC", 75, "Vanessa")

print("Nome validado pelo construtor: "+d1.nome)

d1.nome = "   tecnologia de Orientação à Objetos"
print("Nome validado pelo setter: "+d1.nome)

tEscolar = TarefaEscolar("introducao Herança", d1, -1)
tEscolar.data_entrega = "19-09-2025"
tEscolar.iniciarTarefa()
print(f"Tarefa Escolar:\n {tEscolar.exibir_dados()}")
print("\n\n")

tProfissional = TarefaProfissional(
        titulo="Documentar sistema",
        projeto="ERP Interno",
        data_entrega="15-10-2025",
        descricao="Criar documentação técnica do módulo financeiro"
    )

print(tProfissional)
print(tProfissional.exibir_dados())

print("\n\n")
tpessoal = TarefaPessoal(
        titulo="Fazer caminhada",
        tipo="Saúde",
        descricao="Caminhar 30 minutos na gare",
        data_realizacao="09-10-2025"
    )
tpessoal.concluir()

#print(tpessoal)
print(tpessoal.exibir_dados())

print("\n\n")