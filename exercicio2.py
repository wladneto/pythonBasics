def precodapassagem(v):
    preco = 0
    distancia = 0
    if v.isdigit():
            distancia = int(v)

    if (distancia < 200):
        preco = distancia * 0.5
    else:
        preco = distancia*0.45

    return preco

entrada = input ("Qual a distância qquer percorrer em km? ")
result = precodapassagem(entrada)
if (result == 0):
    print ("Entre com uma distancia válida.")
else:
    print ("O preço da passagem é de R$" + str(result))