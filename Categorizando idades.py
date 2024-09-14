numero = int(input("Entre sua idade: "))
if numero<=12 and numero>=0:
    print("Criança")
elif numero>=13 and numero<=18:
    print("Adolescente")
elif numero>=19:
    print("Adulto")
else:
    print("Você não existe")
