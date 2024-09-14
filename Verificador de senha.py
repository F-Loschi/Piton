nome = input("Entre seu nome: ")
senha = input("Entre sua senha: ") 
i = False
while i == 0:
    if nome == 'Felipe' and senha == 'Pikachu':
        print("Seja bem vindo!!")
        i = True
    else:
        print("Quem tu acha que tu é?")
        print("Tenta denovo, comédia")
        nome = input(" ")
        senha = input(" ")
print("Fim do programa")
