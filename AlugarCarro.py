from ValidarOpcoes import continuar


def escreva(imprimi=False):
    """
    Faz uma lista de dicionários e imprimi tudo em colunas
    :param imprimi: Imprimi os dados do arquivo txt em colunas. Se for falso procura o carro na lista
    """
    sistema = list()
    with open("carros.txt", "rt") as arquivo:
        for linha in arquivo:
            cont, carro, valor = linha.strip().split(";")
            carros = {
                'Cod': cont,
                'Carros': carro,
                'Valor': valor
            }
            sistema.append(carros)
    if imprimi:
        print(f'{"Cod":<5}{"Carros":<20}{"Valor":<10}')
        for carros in sistema:
            d, e, f = carros.values()
            print(f'{d:<5}{e:<20}{f:<10}')
        print()
    else:
        cod = continuar('Escolha o código do carro: ', '01234567')
        dias = continuar('Quantos dias? ', '0123456789')
        carro_encontrado = False
        for procura in sistema:
            if procura['Cod'] == cod:
                aluguel_total = float(procura["Valor"]) * int(dias)
                print(f'Você escolheu o {procura["Carros"]} por {dias} dias.')
                print(f'O aluguel totaliza R${aluguel_total:.2f}')

                with open("CarrosAlugados.txt", "a") as arquivo:
                    arquivo.write(f'{procura["Cod"]};{procura["Carros"]};{procura["Valor"]}\n')

                carro_encontrado = True
                break
        if not carro_encontrado:
            print('Carro não encontrado')
