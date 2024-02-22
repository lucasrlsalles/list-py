import main

def adiciona_item():
    item = (input("Digite uma fruta: "))
    main.list.append(item)
    print(main.list)

def remove_item():
    item = (input("Digite uma fruta: "))
    main.list.remove(item)
    print(main.list)