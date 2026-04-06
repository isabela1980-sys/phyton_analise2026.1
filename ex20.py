s=float(input("Digite o valor do salário: "))
if s>5000:
    i=s*0.075
    sd=s-i
    print(f"O salário é {s}, o valor do imposto pago é {i}, totalizando o salário líquido em {sd}")
elif s>8000:
    i=s*0.27
    sd=s-i
    print(f"O salário é {s}, o valor do imposto pago é {i}, totalizando o salário líquido em {sd}")
else:
    print("Não paga imposto")