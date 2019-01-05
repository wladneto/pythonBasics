def soma(v):
    soma = 0
    for item in v:
        if item.isdigit():
            soma += int(item)
        else:
            soma = "isso nao é um numero"    
    return soma

entrada = input ("Entre com um valor inteiro:")
result = soma(entrada)
print (result)



