# desenho da forca


def desenho(erros):
    """
    :param erros: Recebe da variável quantidade de erros
    :return: Retorna o desenho correspondente de acordo com a quantidade de erros
    """
    if erros == 0:
        print('''
--------
|      |
|
|
|
|
~~~~~~~~~''')
    elif erros == 1:
        print('''
 ---------
 |       |     
 O       |     
         |  
         |
         |
 ~~~~~~~~~''')
    elif erros == 2:
        print('''
 ---------
 |       |     
 O       |     
 |       |  
         |
         |
 ~~~~~~~~~''')
    elif erros == 3:
        print('''
 ---------
 |       |     
 O       |     
/|       |  
         |
         |
 ~~~~~~~~~''')
    elif erros == 4:
        print('''
 ---------
 |       |     
 O       |     
/|\      |  
         |
         |
 ~~~~~~~~~ ''')
    elif erros == 5:
        print('''
 ---------
 |       |     
 O       |     
/|\      |  
/        |
         |
 ~~~~~~~~~''')
    elif erros == 6:
        print('''
 ---------
 |       |     
 O       |     
/|\      |  
/ \      |
         |
 ~~~~~~~~~''')


def linha(tam=25):
    """
    :param tam: Quantidade de traços a ser exibida
    :return: Retorna sequência de traços
    """
    return '-' * tam


def titulo(txt):
    """
    :param txt: Recebe texto a ser inserido no título
    :return: Retorna texto dentro da formatação
    """
    print(linha())
    print(txt.center(25))
    print(linha())


