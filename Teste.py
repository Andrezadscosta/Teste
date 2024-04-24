imovel = float(input('Insira o valor do imóvel: R$ '))
renda = float(input('Insira a sua renda mensal: R$ '))
prazo = int(input('Insira o prazo em anos: '))
prestação = imovel / (prazo * 12)
if prestação <= (renda * 0,3):
    print(f'{prestação:.2f}')
else:
    print('Recusado')