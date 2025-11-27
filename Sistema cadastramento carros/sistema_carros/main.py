
from models.carro import Carro

def menu_principal():
    print("\n===SISTEMA DE CADASTRO DE CARROS===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

def menu_marca_carro():
    print("1 - Fiat")
    print("2 - Chevrolet")
    print("3 - VOlkswagen")
    return int(input("Escolha uma opção: "))

def menu_modelo_carro():
    print("1 - Uno")
    print("2 - Argo")
    print("3 - Mobi")
    return int(input("Escolha uma opção: "))

while True:
    opcao = menu_principal()
    
    if opcao == 1:
        print("\n--- Cadastrar Carro ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

        print("Carro salvo com sucesso!")
    
    elif opcao == 2:
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_todos()

        if not lista:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")
    
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")