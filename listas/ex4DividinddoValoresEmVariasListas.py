lista = []
lista_impar = []
lista_par = []
while True:
    #le um numero e adiciona a uma lista
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('-=-'*20)
    
    #verifica se o usuario quer continuar
    x = str(input('Voce quer continuar? [S/N] '))
    if x in 'Nn':
        break
    
    #VERIFICA OS VALORES IMPARES E PARES E ADICIONA A UMA LISTA
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)

print(f'Lista original: {lista}')
print(f'Lista apenas com numeros PARES: {lista_par}')
print(f'Lista apenas com numeros impares: {lista_impar}')
