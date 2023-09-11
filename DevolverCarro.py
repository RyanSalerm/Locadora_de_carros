from init import criarArquivo, arquivoExiste
from ValidarOpcoes import continuar

arq = "CarrosAlugados.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

def devolvercarro(texto=False):

    sistema = []
    with open("CarrosAlugados.txt", "rt") as arquivo:
        for linha in arquivo:
            cont, carro, valor = linha.strip().split(";")
            carrosAlugados = {
                'Cod': cont,
                'Carros': carro,
                'Valor': valor,
            }
            sistema.append(carrosAlugados)

    print('Esses são os carros alugados: ')
    for carrosAlugados in sistema:
        print(f"{carrosAlugados['Cod']:<5}{carrosAlugados['Carros']:<20}{carrosAlugados['Valor']:<10}")
    print()

    devolver = continuar('Qual carro você quer devolver: ', '01234567')

    """
    Nesse trecho, o arquivo "CarrosAlugados.txt" é aberto novamente, mas no modo de escrita ("w"). 
    O loop for itera sobre cada dicionário carrosAlugados na lista sistema.
    Se o código do carro (Cod) corresponder ao carro que está sendo devolvido (devolver), uma mensagem é impressa no 
    console.
    Caso contrário, a linha correspondente ao dicionário atual é recriada utilizando as informações do 
    dicionário ('Cod', 'Carros' e 'Valor'), e essa linha é escrita no arquivo usando o método write. 
    O caractere \n no final da string garante que cada linha seja seguida por uma quebra de linha.
    Dessa forma, o arquivo é reescrito com todas as linhas, exceto aquela que corresponde ao carro que está sendo 
    devolvido, mantendo assim apenas os registros não devolvidos no arquivo.
"""
    with open("CarrosAlugados.txt", "w") as arquivo:
        for carrosAlugados in sistema:
            if carrosAlugados['Cod'] == devolver:
                print('Obrigado por devolver este carro.')
            else:
                arquivo.write(f"{carrosAlugados['Cod']};{carrosAlugados['Carros']};{carrosAlugados['Valor']}\n")
