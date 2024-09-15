lista = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
