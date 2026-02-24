from listar_tarefas import ListarTarefas

def RemoveTarefas():
    with open("tarefas.txt", "r") as arquivo:
        if arquivo.read() == "":
            print("Não há tarefas para remover. Crie sua primeira tarefa!")
            return
        tarefa = input("Digite a tarefa que deseja remover: ")
        tarefas = arquivo.readlines()
    with open("tarefas.txt", "w") as arquivo:
        for linha in tarefas:
            if linha.strip() != tarefa:
                arquivo.write(linha)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
        while not tarefa in tarefas:
            print(f"Tarefa '{tarefa}' não encontrada.")
            ListarTarefas()
            tarefa = input("Digite a tarefa que deseja remover: ")