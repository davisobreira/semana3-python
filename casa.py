print('-' * 12, 'Minha Casa Minha Vida', '-' * 12)
continua = 'S'
while continua == 'S':
    val_house = float(input('Informe o valor do imóvel: '))
    sal = float(input('Informe a sua renda mensal: '))
    val_min = float((sal * 30)/100)
    years = int(input('Informe em quantos anos você quer pagar o imóvel: '))
    q_installment = int(years * 12)
    installment = q_installment
    val_installment = float(val_house / installment)
    if val_installment > val_min:
        print('Empréstimo NEGADO!')
        continua = input('Desejas procurar outro imóvel? [s/n] ').upper()
    else:
        print(f'Empréstimo APROVADO!\n O valor das {q_installment} prestações será de {val_installment:,.2f}')
        continua = input('Realizar mais um empréstimo? [s/finalizar] ').upper()
print('Consulta finalizada. Obrigado!')
