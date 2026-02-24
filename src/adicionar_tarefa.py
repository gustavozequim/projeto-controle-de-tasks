def AdicionaTarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    with open("tarefas.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
