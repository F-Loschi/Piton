lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

mult_3 = []
def multiplo_3(lista: list) -> list:
  for i in lista:
      if i % 3 == 0:
        mult_3.append(i)
  return mult_3

# retornando a lista gerada para a variável mult_3
mult_3 = multiplo_3(lista)
print(mult_3)
