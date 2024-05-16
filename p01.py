# Kolekcije podataka
# Liste

streets = [
    ['Miroslava Krleze', 73, '10290', 'Zapresic'],
    ['Ilica', 125, '10000', 'Zagreb']
]

print(streets[0][0])

name = 'Pythonnohtyp'
reversed_name = name[ : : -1]

if name.lower() == reversed_name.lower():
    print(f'Naziv: {name} JE palindrom!')
else:
    print(f'Naziv: {name} NIJE palindrom!')

for street in streets:
    for street_prop in street:
        print(street_prop, end=' ')
    print()
