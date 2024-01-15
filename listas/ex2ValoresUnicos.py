lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Nao vou adicionar.')
    x = str(input('Voce quer continuar? [S/N]'))
    if x in 'Nn':
        break   
print('-_'*30)
lista.sort()
print(lista)
