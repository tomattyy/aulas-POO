import json
import os

#CLASSE RESPONSAVEL POR CRIAR E LER ARQUVIOS JSON.
#SALVAR DADOS E CARREGAR DADOS NO JSON.
#OUTRAS CLASSES HERDAM ESTA CLASSE.
class BaseModel:

    arquivo = ""

    #ESTA FUNÇÃO CARREGA TODOS OS REGISTROS JÁ EXISTENTES.
    #ADICIONA O NOVO DADO A LISTA.
    #SALVA TUDO NO ARQUIVO NOVAMENTE.
    def salvar(self, dados):
        lista = self.carregar_todos()
        lista.append(dados)
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

    #LÊ TODOS OS REGISTROS DO ARQUIVO JSON.
    #SE O ARQUIVO NÃO EXISTIR DEVOLVE UMA LISTA.
    def carregar_todos(self):
        if not os.path.exists(self.arquivo):
            return []
    
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
        