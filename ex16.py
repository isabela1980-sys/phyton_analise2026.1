n1=float(input("Digite o valor 1: "))
n2=float(input("Digite o valor 2: "))
n3=float(input("Digite o valor 3: "))
if n1>n2 and n1>n3:
    print(f"O número {n1} é maior que número {n2} e o número {n3}")
elif n2>n1 and n2>n3:
    print(f"O número {n2} é maior que número {n1} e o número {n3}")
else:
    print(f"O número {n3} é maior que número {n1} e o número {n2}")

