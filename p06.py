


stanje = 5000

def podizanje_novca(iznos_za_podici: float):
    return stanje + iznos_za_podici

print('Trenutno stanje racuna je:', stanje, 'EUR')
a = float(input('Upisite koliko novca zelite podici: '))

print('Preostali iznos na racunu je:', podizanje_novca(a), 'EUR')
