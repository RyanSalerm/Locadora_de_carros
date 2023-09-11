from init import arquivoExiste, criarArquivo
from ValidarOpcoes import continuar
from AlugarCarro import escreva
from DevolverCarro import devolvercarro

arq = "carros.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    print('Bem-vindo a locadora de carros!\n'
          'O que deseja fazer: ?\n'
          '0 - Mostrar seu portifólio | 1 - Alugar um carro | 2 - Devolver um carro\n')
    opcao = str(input('>>> ')).strip()[0]
    if opcao in '0':
        escreva(True)
        print('='*20)
    if opcao in '1':
        print('[ALUGAR] ')
        escreva(True)
        escreva(False)
    if opcao in '2':
        print('[DEVOLVER]')
        devolvercarro()
    se = continuar('Deseja continuar? [S/N] ', 'SsNn')
    if se == 'N':
        break
