from task_manager import TaskManager
from tabulate import tabulate

def menu():
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Editar tarefa")
    print("4. Excluir tarefa")
    print("5. Sair")

def main():
    manager = TaskManager()

    while True:
        menu()
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            description = input("Descrição da tarefa: ")
            due_date = input("Data de vencimento (AAAA-MM-DD): ")
            priority = int(input("Prioridade (1 a 5): "))
            category = input("Categoria: ")
            manager.add_task(description, due_date, priority, category)
            print("Tarefa adicionada com sucesso!")
        elif choice == 2:
            tasks = manager.view_tasks()
            print("Tarefas:")
            print(tabulate(tasks, headers=["ID", "Descrição", "Vencimento", "Prioridade", "Categoria"], tablefmt="fancy_grid"))
        elif choice == 3:
            task_id = int(input("ID da tarefa a ser editada: "))
            description = input("Nova descrição (deixe em branco para não alterar): ")
            due_date = input("Nova data de vencimento (deixe em branco para não alterar): ")
            priority = input("Nova prioridade (deixe em branco para não alterar): ")
            category = input("Nova categoria (deixe em branco para não alterar): ")
            manager.edit_task(task_id, description or None, due_date or None, int(priority) if priority else None, category or None)
            print("Tarefa editada com sucesso!")
        elif choice == 4:
            task_id = int(input("ID da tarefa a ser excluída: "))
            manager.delete_task(task_id)
            print("Tarefa excluída com sucesso!")
        elif choice == 5:
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()
