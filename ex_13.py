altura = float(input("Digite a sua altura: "))

sexo = input("Digite o seu sexo: ")

if sexo == "M" or sexo == "m":
    crm = (72.2* altura) - 58
    print(f"Seu peso ideal é {crm:.2f}")
elif sexo == "F" or sexo == "f":
    crm = (62.2*altura) - 44.7
    print(f"Seu peso ideal é {crm:.2f}")
else:
    print("Não entendi:(")

