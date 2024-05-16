import json

from p02 import convert_to_json
# from p03.p03 import Address
from p03 import Address
from p04 import FileManager
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


# Dict - rjecnik
postal_address = {
    'street': 'Ilica',
    'house_number': 256,
    'postal_code': '10000',
    'city': 'Zagreb',
    'country': 'Hrvatska'
}

print(postal_address['street'])

json_txt_01 = json.dumps(postal_address)
print(json_txt_01)

json_txt_02 = convert_to_json(postal_address)
print(json_txt_02)


hq_address = Address(street='Ilica 256', 
                     postal_code='10000',
                     city='Zagreb',
                     country='Hrvatska')

invoice_address = Address(street='Marmontova 15', 
                          postal_code='21000',
                          city='Split',
                          country='Hrvatska')

print(hq_address.street)
print(invoice_address)


file_manager = FileManager(file_path='datoteke_test1')
file_manager.write(hq_address, 'address', 'w')
file_manager.write(invoice_address, 'address')
