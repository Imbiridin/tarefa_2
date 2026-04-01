compra = float(input("Informe os metros quadrados da área a ser pintada: "))

cobertura = compra / 6

lata_1 = cobertura // 18
lata_2 = cobertura // 3.6

if cobertura % 18 > 0:
    lata_1 = lata_1 + 1

if cobertura % 3.6 > 0:
    lata_2 = lata_2 + 1

preco_1 = lata_1 * 80

preco_2 = lata_2 * 25

litros_com_folga = cobertura * 1.1

galoes_mistura = litros_com_folga // 18
resto_mistura = litros_com_folga % 18
latas_mistura = resto_mistura // 3.6

if resto_mistura % 3.6 > 0:
    latas_mistura = latas_mistura + 1

preco_3 = (galoes_mistura * 80) + (latas_mistura * 25)

print(f'A quantidade necessária de tinta é: {lata_1} Galão ou {lata_2} Latas')
print(f'Se você preferir comprar o galão de 18L fica: R${preco_1:.2f}')
print(f'Se você preferir comprar a lata de 3.6L fica: R${preco_2:.2f}')
print(f'Caso prefira comprar os galões e latas fica: R${preco_3:.2f} ')

