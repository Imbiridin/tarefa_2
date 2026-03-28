peso = float(input("Digite o peso: "))

excedente = 50


if peso > excedente:
    multao = (peso - 50) * 4
    print(f"Seu João, você precisa pagar R${multao:.2f}")
else:
    print(f'Sem multa para você João')