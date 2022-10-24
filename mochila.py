from minerio import Minerio

# Função que diz como deve ser ordenado


def ordernar(value):
    return value.valor / value.peso

# Função que vai printar os itens que foram colocados na mochila


def mostrarLista(items):
    print(20 * '=')
    print("Items na mochila: ")
    for item in items:
        print(" ", item.nome + " :", item.valor)
    print("Espaço restante", W)
    print(20 * '=')


# Capacidade
W = 6

# Itens
N = [
    Minerio(1, 60, 'Diamante'), Minerio(3, 150, "Ferro"),
    Minerio(3, 120, 'Carvão'), Minerio(4, 160, 'Redstone'),
    Minerio(5, 200, 'Ouro'), Minerio(5, 150, 'Lápis-lazúli'),
    Minerio(6, 60, 'Esmeralda')
]

# Subconjunto de elementos que vai preencher a mochila
S = []

# Ordenação
N.sort(key=ordernar, reverse=True)

# Colocando itens na mochila
for item in N:
    if(W - item.peso > 0):
        S.append(item)
        W = W - item.peso

mostrarLista(S)
