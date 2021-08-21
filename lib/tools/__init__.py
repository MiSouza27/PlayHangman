from random import randint
from lib.interface.lista_palavras import*
from lib.interface import*

sort_word = randint(0, 3)  # gera um número aleatório
dica = (dicas[sort_word])  # recebe número aleatório e seleciona palavra correspondente
pOculta = listagem.get(dica).upper()  # armazena palavra secreta
erros = acertos = ''  # armazena letras


def sorteio():
    """
    :return: Retorna palavra secreta
    """
    global sort_word, dica, pOculta
    return pOculta


def espaços(palavra):
    """
    :param palavra: recebe uma palavra
    :return: retorna palavra com espaços entre as letras
    """
    for l in palavra:
        print(l, end=' ')
    print()


def play(erros, acertos, pOculta):
    """
    :param erros: recebe a variável erros
    :param acertos: recebe a variável acertos
    :param pOculta: recebe a variável com a palavra secreta
    :return: retorna desenho da forca, traços correspondentes ao número de letras da palavra oculta e recebe as letras erradas
    """
    chutes = len(erros)
    desenho(chutes)
    traço = '_'*len(pOculta)
    for i in range(len(pOculta)):
        if pOculta[i] in acertos:
            traço = traço[:i] + pOculta[i] + traço[i+1:]
    espaços(traço)
    print('Letras erradas: ', end=' ')
    for e in erros:
        print(e, end=' ')
    print()


def vitoria(pOculta, acertos):
    """
    :param pOculta: recebe palavra oculta
    :param acertos: recebe letras certas
    :return: retorna se jogador acertou a palavra
    """
    ganhar = True
    for p in pOculta:
        if p not in acertos:
            ganhar = False
            break
    return ganhar
