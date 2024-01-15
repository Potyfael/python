numeros=('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis' ,'sete' ,'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')     
s=''
while True:
    while True:
        n = int(input('Digite um valor entre 0 e 20: '))
        if n > len(numeros):
            print('Voce digitou um valor errado')
        else:
            break
    print(f'Voce digitou o numero {numeros[n]}')
    print('-='*30)
    s = str(input('Voce quer continuar? '))
    if s == 'nao':
        break
