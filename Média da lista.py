lista = [30, 40, 50, 60]
soma = 0

try:
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
