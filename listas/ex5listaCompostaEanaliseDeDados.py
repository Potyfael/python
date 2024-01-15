dados = list()

#coletando peso e nome
while True:
    nome = str(input('Nome: '))
    peso = float(input('peso: '))
    print('-'*20)

    #adicionando os dados a uma lista
    dados.append(nome)
    dados.append(peso)

    #pergunta se o usuario quer interromper o loop
    r = input('Voce deseja continuar? [S/N] ')
    if r in 'Nn':
        break

#separando nome de peso
for c in dados:
    print(c)
    