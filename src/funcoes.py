import json
import os
from .modelo import Tarefa

class GerenciadorDeTarefas:
    def __init__(self, caminho_arquivo='data/tarefas.json'):
        self.caminho_arquivo = caminho_arquivo
        self.tarefas = self._carregar_tarefas()

    def _carregar_tarefas(self):
        if not os.path.exists(self.caminho_arquivo):
            return []
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [Tarefa(t['titulo'], t['concluida']) for t in dados]
        except (json.JSONDecodeError, IOError):
            return []

    def salvar(self):
        os.makedirs(os.path.dirname(self.caminho_arquivo), exist_ok=True)
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as f:
            dados_json = [t.converte_dicionario() for t in self.tarefas]
            json.dump(dados_json, f, indent=4, ensure_ascii=False)

    def adicionar_tarefa(self, titulo):
        nova_tarefa = Tarefa(titulo)
        self.tarefas.append(nova_tarefa)
        self.salvar()

    def listar_tarefas(self):
        return self.tarefas

    def remover_tarefa(self, indice):
        try:
            self.tarefas.pop(indice)
            self.salvar()
            return True
        except IndexError:
            return False