valor = float(input("Digite o valor:"))
porcentagem = float(input("Digite a porcentagem:"))
resultado = (valor*porcentagem)/100
total = valor - resultado
print(f"{porcentagem}% de {valor} é {resultado}")