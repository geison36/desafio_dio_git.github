python media das notas


def somaL(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma
    
def mediaL(lista):
    for i in lista:
        soma = soma + lista[i]
    return mediaL

def mediaPonderada(lista, listaPesos):
    num = 0
    num2 = 0
    n = len(lista)

    for i in range(n):
        num += (lista[i] * listaPesos[i])
        num2 += listaPesos[i]

    medPonderada = num / num2
    return medPonderada


pesos = [3, 2.5, 3.1, 4.5, 5.9, 6, 2.1, 3.5, 5, 6.5]
lista = [2, 6, 8, 4, 8, 5, 3, 7, 2, 1]

soma = somaL(lista)
media = somaL(lista) / len(lista)

print(lista)
print(" | |\n")
print(" | |\n")
print("\   /\n")
print(" \ /\n")
print("  V \n")
print("A soma dos elementos = {0:.2f}".format(soma))
print("A media dos elementos = {0:.2f}".format(media))
print("A media Ponderada é = {0:.2f}".format(mediaPonderada(lista, pesos)))