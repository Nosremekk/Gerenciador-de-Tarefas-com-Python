class Tarefa:
    def __init__(self,titulo,status=False):
        #Representações de uma tarefa individual da aplicação
        #titulo: string que da nome ou descreve a tarefa
        #status: booleano que indica se a tarefa está concluída (True) ou pendente (False)
        self.titulo = titulo
        self.concluida = status
    # Criando função que marca como concluida
    def marcar_concluida(self):
        self.concluida = True

    #Criando função que da retorno visual do status
    def __str__(self):
        status_visual = "[V]" if self.concluida else "[ ]"
        return f"{status_visual} {self.titulo}"
    
    #Convertendo o obj para um dicionario
    def converte_dicionario(self):
        return {
            "titulo": self.titulo,
            "concluida": self.concluida
        }
