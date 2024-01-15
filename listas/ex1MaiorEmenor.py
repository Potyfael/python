lista = []
for c in range(0, 5):
    n = int(input(f"Digite o valor para a posicao {c}: "))
    lista.append(n)
print(lista)
print(f'O menor numero e {min(lista)}')
print(f'O maior numero e {max(lista)}')
