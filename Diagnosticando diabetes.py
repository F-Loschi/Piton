glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
estado = [('Hipoglicemia', i) if i<=70 else ('Normal', i) if i>70 and i<=99 else ('Alterada', i) if i>=100 and i<=125 else ('Diabetes', i)  for i in glicemia]
print(estado)
