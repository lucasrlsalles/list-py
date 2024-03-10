def adiciona_item(_list):
    item = str(input("Digite uma fruta: "))
    _list.append(item)
    return

def remove_item(_list):
    item = str(input("Digite uma fruta: "))
    try:
        _list.remove(item)
    except Exception:
        print("\n!!! Item não encontrado !!!\n")
    return

