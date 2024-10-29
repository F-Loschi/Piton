lista = [0,1,2,3,4,5,6,7,8,9,10]

def tabuada(x: int):
    for i in lista:
        print(f"{x} x {i} = {x*i}")

x = int(input("Qual tabuada tu quer? "))
tabuada(x)
