people = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Cho', 'house': 'Ravenclaw'},
    {'name': 'Draco', 'house': 'Slytherin'},
]

people.sort(key=lambda person: person['name'])

# lambda input person['name'] output
# pega a pessoa e retorna pelo nome ordenado
#pesquisar sobre  lambda

print(people)