lista = [[], []]

#le 7 numeros e adiciona a uma lista
for c in range(7):
    n = (int(input('Digite um valor: ')))
    #se o numero fo par, ele fica numa lista interna. Caso contrario, fica em outra lsita interna.
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-'*20)
print(f'Os valores pares sao: {lista[0]}')
print(f'Os valores impares sao: {lista[1]}')
