# lista de palavras para o jogo
listagem = {'objeto': 'espelho', 'País': 'Espanha', 'Comida': 'espagueti', 'Profissão': 'professor'}
dicas = list()

# arquivo para armazenar as palavras e dicas
d = open('palavra.txt', 'wt+')
d.close()
d = open('palavra.txt', 'at')
for k, v in listagem.items():
    d.write(f'Dica: {k}, ')  # armazena as dicas
    d.write(f'Palavra: {v} \n')  # armazena as palavras
    dicas.append(k) # salva lista completa no arquivo
d.close()
