from funcao import *

list = ['banana','morango']

print("1 - Criar um item")
print("2 - Remover Item")
print("3 - Fechar")
answer = int(input("Opção: "))

if answer == 1:
    adiciona_item()

elif answer == 2:
    remove_item()

elif answer == 3:
    print("Encerrando aplicação...")
