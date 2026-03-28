hora_g = float(input("Informe o quanto você ganha por hora: "))

hora_t = float(input("Informe quantas horas você trabalha por mês: "))

salario_bruto =  hora_t * hora_g

ir = salario_bruto / 11

inss = salario_bruto / 8

sindicato = salario_bruto / 5

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Seu salário bruto é: R${salario_bruto:.2f} ')
print(f'Seu Imposto de Renda(IR) é: R${ir:.2f}')
print(f'Seu INSS é: R${inss:.2f}')
print(f'Seu Sindicato é: R${sindicato:.2f}')
print(f'Seu salário mínimo é: R${salario_liquido:.2f}')