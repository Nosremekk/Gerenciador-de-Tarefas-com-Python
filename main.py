from src.funcoes import GerenciadorDeTarefas
from src.interface import Interface

def executar():
    gerenciador = GerenciadorDeTarefas()
    interface = Interface()

    while True:
        opcao = interface.exibir_menu()

        if opcao == "1":
            titulo = input("Descrição da tarefa: ")
            gerenciador.adicionar_tarefa(titulo)
        
        elif opcao == "2":
            tarefas = gerenciador.listar_tarefas()
            interface.mostrar_lista(tarefas)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "3":
            tarefas = gerenciador.listar_tarefas()
            interface.mostrar_lista(tarefas)
            idx = interface.solicitar_id("Digite o número da tarefa concluída: ")
            if idx is not None and 0 <= idx < len(tarefas):
                tarefas[idx].marcar_concluida()
                gerenciador.salvar()
        
        elif opcao == "4":
            tarefas = gerenciador.listar_tarefas()
            interface.mostrar_lista(tarefas)
            idx = interface.solicitar_id("Digite o número da tarefa para remover: ")
            if idx is not None:
                if gerenciador.remover_tarefa(idx):
                    print("Tarefa removida!")
                else:
                    print("ID inválido.")
        
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    executar()