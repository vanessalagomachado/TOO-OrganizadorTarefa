from model.TarefaProfissional import TarefaProfissional

t = TarefaProfissional("implementar ação da página Home", "Website IFSUL", "07-10-2025")
print(t)
t.concluir()
print(t.exibir_dados())