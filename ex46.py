def par_impar(n):
    if n %2==0:
         return "par"
    else:
         return "impar"
v=int(input("Digite o valor: "))
y=par_impar(v)
print(y)

