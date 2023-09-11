def continuar(txt, opcoes_validas):
    """
    :param txt: O texto que você quer colocar para interagir com o usuário.
    :param opcoes_validas: Os digitos que são válidos no seu texto.
    :return: Retorna o texto se as opções forem válidas
    """
    texto = str(input(txt)).strip().upper()
    while texto not in opcoes_validas or len(texto) == 0:
        print('\033[0;31;1mERRO\033[m')
        texto = str(input(txt)).strip().upper()
    return texto



