from lib.tools import *
from lib.interface import *
from time import sleep

partidas = vitorias = derrotas = 0  # variáveis do placar
jogar = True
nome = str(input('Digite seu nome para começar: '))
print(f'Bem vindo(a), {nome}')
titulo('THE HANGMAN')
erros = acertos = ''  # variáveis para armazenar letras
pOculta = sorteio()


while jogar:  # laço principal
    print(f'A dica é: {dica}')
    play(erros, acertos, pOculta)
    palpite = str(input('Digite uma letra: ')).upper()  # recebe palpite

    if palpite in pOculta:  # verifica se palpite está certo
        acertos += palpite
        if vitoria(pOculta, acertos):
            partidas += 1
            vitorias += 1
            print(f'Parabéns, {nome}! A palavra é {pOculta}.')
            print(linha())
            jogar = False
    elif palpite not in pOculta:  # verifica se palpite está errado
        erros += palpite
        if len(erros) == 6:  # verifica quantidade de erros é igual a 6
            partidas += 1
            derrotas += 1
            play(erros, acertos, pOculta)
            linha()
            print(f'Lamento {nome}, você perdeu!')
            print(linha())
            jogar = False # finaliza laço do jogo se quantidade de erros for igual 6

    if not jogar:  # confirmação para reiniciar ou finalizar jogo
        continuar = str(input('Deseja jogar novamente [S/N]: '))
        if continuar in 'Ss':
            erros = ''  # reinicia o placar
            acertos = ''
            jogar = True
            pOculta = sorteio() # seleciona nova palavra

        elif continuar in 'Nn':  # finaliza o jogo mostrando o placar
            print(linha(30))
            print(f'''{nome}, Sua pontuação foi:
Partidas Jogadas: {partidas}
Vitórias: {vitorias}
Derrotas: {derrotas}''')
            print(linha())
            print('Encerrando...')
            sleep(1)
            print(f'Até mais, {nome}! ')
            break




