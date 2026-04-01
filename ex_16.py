compra = float(input("Informe os metros quadrados da área a ser pintada: "))

lata = compra / 3 

cobertura = lata // 18

if lata % 18 > 0:
    cobertura = cobertura + 1

preco = cobertura * 80

print(f"Você precisará de {cobertura} und")
print(f"E o valor total é de R${preco:.2f}")