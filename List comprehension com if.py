aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

numero = [exp[1] for exp in aluguel if exp[0] == 'Apartamento']

print(numero)
