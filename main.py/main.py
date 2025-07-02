import json
import os

ARQUIVO = "clientes.json"

# Carrega clientes do arquivo (se existir)
def carregar_clientes():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    return []

# Salva clientes no arquivo
def salvar_clientes(clientes):
    with open(ARQUIVO, 'w') as f:
        json.dump(clientes, f, indent=4)

# Adiciona um novo cliente
def adicionar_cliente(clientes):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    
    for c in clientes:
        if c['cpf'] == cpf:
            print("CPF já cadastrado.")
            return

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone
    }

    clientes.append(cliente)
    salvar_clientes(clientes)
    print("Cliente adicionado com sucesso!")

# Lista todos os clientes
def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    for c in clientes:
        print(f"\nNome: {c['nome']}")
        print(f"CPF: {c['cpf']}")
        print(f"E-mail: {c['email']}")
        print(f"Telefone: {c['telefone']}")

# Remove cliente por CPF
def remover_cliente(clientes):
    cpf = input("Digite o CPF do cliente a remover: ")
    novos_clientes = [c for c in clientes if c['cpf'] != cpf]

    if len(novos_clientes) == len(clientes):
        print("CPF não encontrado.")
    else:
        salvar_clientes(novos_clientes)
        print("Cliente removido com sucesso!")

    return novos_clientes

# Menu principal
def menu():
    clientes = carregar_clientes()

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Remover Cliente")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_cliente(clientes)
        elif opcao == '2':
            listar_clientes(clientes)
        elif opcao == '3':
            clientes = remover_cliente(clientes)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
