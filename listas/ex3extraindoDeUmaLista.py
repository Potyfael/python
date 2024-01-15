lista = []
cont = 0
while True:

    n = int(input('Digite um valor: '))
    print('-'*30)
    cont += 1

    lista.append(n)

    #PERGUNTA SE O USUARIO QUER ADICIONAR MAIS NUMEROS
    r = str(input('Deseja continaur? [S,N] '))
    if r in 'Nn':
        break

print('-='*30)
print(f"Voce digitou {cont} numeros")
#ORDENA A LISTA EM ORDEM DECRESCENTE
lista.sort(reverse=True)
print(lista)
if 5 not in lista:
    print(f'O valor 5 nao foi encontrado na lista!')
