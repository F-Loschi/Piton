x = int(input("Coordenadas em X: "))
y = int(input("Coordenadas em Y: "))
if x>0 and y>0:
    print("Você está no primeiro quadrante!")
elif x<0 and y>0:
    print("Você está no segundo quadrante!")
elif x<0 and y<0:
    print("Você está no terceiro quadrante!")
elif x>0 and y<0:
    print("Você está no quarto quadrante!")
elif x==0:
    print("Você está no eixo das ordenadas!")
elif y==0:
    print("Você está no eixo das abscissas!")
else:
    print("Você está na origem!")
