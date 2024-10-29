gols_marcados = [2, 1, 3, 1, 3]
gols_sofridos = [1, 2, 2, 1, 0]

def calcula_pontos(gm,gs):
    pontos = 0
    for i in range(0,len(gs)):
        if gm[i] > gs[i]:
            pontos+=3
        elif gm[i] == gs[i]:
            pontos += 1

    aprov = 100 * pontos / (len(gols_marcados) * 3)

    return pontos, aprov

pontos, aprov = calcula_pontos(gols_marcados,gols_sofridos)
print(f"O total de pontos foi {pontos} e o aproveitamento foi {round(aprov)}%")
