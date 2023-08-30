def pesquisa_linear(Lista, x):
    n=0
    for i in Lista:
        n += 1
        if i == x:
            print(f"Elemento {x} está presente .")
            print(f"Foram feitas {n} operações para achar o elemento .")
            return
    print(f"Elemento {x} não está presente .")

def pesquisa_binaria(A, item):
    esquerda = 0 
    direita = len(A) - 1
    n = 0
    while esquerda <= direita:
        n += 1
        meio = (esquerda + direita) // 2
        if A[meio] == item:     
            return print(f"Elemento {item} está presente .\nForam feitas {n} operações para achar o elemento .")
        elif A[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

Lista = list(range(100))

pesquisa_linear(Lista, 83)
pesquisa_linear(Lista, 200)
pesquisa_binaria(Lista, 10)
pesquisa_binaria(Lista, 200)
