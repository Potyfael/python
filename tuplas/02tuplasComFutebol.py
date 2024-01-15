print('Brasileirao 2019')
print('-='*20)
brasileirao_2019_standings = (
    "Flamengo",
    "Santos",
    "Palmeiras",
    "Grêmio",
    "Athletico Paranaense",
    "São Paulo",
    "Internacional",
    "Corinthians",
    "Fortaleza",
    "Goiás",
    "Bahia",
    "Vasco da Gama",
    "Atlético Mineiro",
    "Fluminense",
    "Botafogo",
    "Ceará",
    "Cruzeiro",
    "CSA",
    "Chapecoense",
    "Avaí"
)
print(f"Os primeiros 5 colocados sao: {brasileirao_2019_standings[0:5]}")
print('-='*50)
print(f"Os times rebeixados sao {brasileirao_2019_standings[-4:]}")
print('-='*50)
print(f"Os times em ordem alfabetica: {sorted(brasileirao_2019_standings)}")
print('-='*50)
print(f"A chapecoense esta em {brasileirao_2019_standings.index('Chapecoense')}")
