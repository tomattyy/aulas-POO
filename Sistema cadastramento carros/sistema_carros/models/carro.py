from models.base import BaseModel

class Carro(BaseModel):
    #HERDA BASEMODEL E CONSEGUE SALVAR E CARREGAR DADOS DO JSON
    arquivo = "carros.json"
    
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    #GETTERS
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_ano(self):
        return self.__ano

    #SETTERS
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def set_ano(self, ano):
        self.__ano = ano

    #PREPARA OS DADOS DO CARRO E ENVIA PARA BaseModel.salvar()
    def salvar_carro(self):
        
        dados = {
            "marca": self.__marca,
            "modelo": self.__modelo,
            "ano": self.__ano
        }
        
        #CHAMANDO O METODO DA CLASSE MÃE.
        super().salvar(dados) 