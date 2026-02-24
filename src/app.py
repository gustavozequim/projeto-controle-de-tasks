from adicionar_tarefa import AdicionaTarefa
from listar_tarefas import ListarTarefas
from remover_tarefas import RemoveTarefas

#Menu inicial

print(f"{'='*60:^100}")
print(f"{'Bem-vindo ao sistema de gerenciamento de tarefas!':^100}")
print(f"{'='*60:^100}")

#Menu de opções
print("\nEscolha uma opção:")
print("1. Adicionar tarefa")
print("2. Listar tarefas")
print("3. Remover tarefa")
print("4. Concluir tarefa")
print("5. Sair")
opcao = input("Digite o número da opção desejada: ")
while int(opcao) != 5:
    while int(opcao) not in [1, 2, 3, 4, 5]:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        opcao = input("Digite o número da opção desejada: ")
    if int(opcao) == 1:
        AdicionaTarefa(tarefas=[])
    elif int(opcao) == 2:
        ListarTarefas()
    elif int(opcao) == 3:   
        RemoveTarefas()
    elif int(opcao) == 4:
        ... #Código para concluir tarefa
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Concluir tarefa")
    print("5. Sair")
    opcao = input("Digite o número da opção desejada: ")
print("Saindo do sistema. Até mais!")
