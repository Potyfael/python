#LE 4 numeros do usuario
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
n3 = int(input('Digite outro numero: '))
n4 = int(input('Digite o ultimo numero: '))

#CONTA QUANTOS NUMEROS PARES TEM
pares = 0
tupla = n1, n2, n3, n4,
for c in tupla:
    if c % 2 == 0:
        pares += 1

#RESULTADO DA ANALISE
print('-='*20)
print(f"Voce digitou os valore: {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
print(f"O valor 3 apareceu na posicao {tupla.index(2)}")
print(f"Os valores pares digitados foram: {pares}")
