from funcao import adiciona_item, remove_item

my_list = ['banana','morango']

while True:
    print('Lista contém: ', my_list)
    print("1 - Criar um item")
    print("2 - Remover Item")
    print("3 - Fechar")
    
    answer = int(input("Opção: "))

    if answer == 1:
        adiciona_item(my_list)
        

    elif answer == 2:
        remove_item(my_list)

    else:
        print("!!! Escolha incorreta !!!")
        break