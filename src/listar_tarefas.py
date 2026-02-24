def ListarTarefas():
    print("Tarefas em andamento:")
    with open("tarefas.txt", 'r') as arquivo:
        for linha in arquivo:
            print(f"- {linha.strip()}")