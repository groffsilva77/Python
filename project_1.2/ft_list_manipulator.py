def show_menu():
    print("\n--- Menu de Manipulação de Listas ---")
    print("1. Adicionar elemento")
    print("2. Remover elemento")
    print("3. Buscar elemento")
    print("4. Ordenar lista (crescente)")
    print("5. Contar ocorrências de um elemento")
    print("6. Exibir lista atual")
    print("7. Sair")
    print("-------------------------------------")

def append_element(lista):
    element = input("Digite o elemento para adicionar: ")
    lista.append(element)
    print(f"'{element}' adicionado à lista.")

def remove_element(lista):
    if not lista:
        print("A lista está vazia.")
        return

    element = input("Digite o elemento para remover: ")
    if element in lista:
        lista.remove(element)
        print(f"'{element}' removido da lista.")
    else:
        print(f"'{element}' não encontrado na lista.")

def search_element(lista):
    if not lista:
        print("A lista está vazia.")
        return

    element = input("Digite o elemento para buscar: ")
    ocorrencias = []
    for i, item in enumerate(lista):
        if item == element:
            ocorrencias.append(i)
    
    if ocorrencias:
        print(f"'{element}' encontrado nas posições: {ocorrencias}")
    else:
        print(f"'{element}' não encontrado na lista.")

def order_list(lista):
    if not lista:
        print("A lista está vazia.")
        return

    lista.sort()
    print("Lista ordenada com sucesso!")

def occur_count(lista):
    if not lista:
        print("A lista está vazia.")
        return
    
    element = input("Digite o elemento que queres encontrar: ")
    count = lista.count(element)
    print(f"O '{element}' aparece '{count}' vezes na lista.")

def show_list(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print(f"Lista atual: {lista}")

def main():
    my_list = []

    while True:
        show_menu()
        choose = input("Escolha uma opção (1-7): ")

        if choose == '1':
            append_element(my_list)
        elif choose == '2':
            remove_element(my_list)
        elif choose == '3':
            search_element(my_list)
        elif choose == '4':
            order_list(my_list)
        elif choose == '5':
            occur_count(my_list)
        elif choose == '6':
            show_list(my_list)
        elif choose == '7':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor digite um número entre 1 e 7.")

if __name__ == "__main__":
    main()
