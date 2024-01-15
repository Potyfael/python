#LE 4 numeros do usuario
tupla = (int(input('Digite um numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite o ultimo numero: ')))

#CONTA QUANTOS NUMEROS PARES TEM
pares = 0
for c in tupla:
    if c % 2 == 0:
        pares += 1

#RESULTADO DA ANALISE
print('-='*20)
print(f"Voce digitou os valore: {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
print(f"O valor 3 apareceu na posicao {tupla.index(2)}")
print(f"Os valores pares digitados foram: {pares}")
