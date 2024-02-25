import funcao

list = ['banana','morango']

print('Lista contém: ', list)
print("1 - Criar um item")
print("2 - Remover Item")
print("3 - Fechar")
answer = int(input("Opção: "))

if answer == 1:
    funcao.adiciona_item()

elif answer == 2:
    funcao.remove_item()

elif answer == 3:
    print("Encerrando aplicação...")



