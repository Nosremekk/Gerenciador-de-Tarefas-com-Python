import os

class Interface:
    @staticmethod
    def limpar_tela():
        # Limpando terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_menu(self):
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluida")
        print("4. Remover Tarefa")
        print("5. Sair")
        return input("\nEscolha uma opção: ")

    def mostrar_lista(self, tarefas):
        self.limpar_tela()
        print("--- MINHAS TAREFAS ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i}. {tarefa}")
        print("-" * 22)

    def solicitar_id(self, mensagem):
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, digite um número valido.")
            return None