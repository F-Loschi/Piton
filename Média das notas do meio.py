#Criando a lista
notas = []
#Entrando as notas na lista
for i in range(1,6):
    nota = float(input("Digite a nota {}: ".format(i)))
    notas.append(nota)

#Definindo uma função de médias de notas
def media(lista):
    #Removendo a maior e menor nota e fazendo a nota
    media = 0
    lista.remove(max(lista))
    lista.remove(min(lista))
    return sum(lista)/len(lista)

#Chamando a função e dando print
medianota = media(notas)
print(f"A média das notas é: {medianota}")
