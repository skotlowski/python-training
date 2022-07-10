class Zwierze:
    def __init__(self, odglos, food):
        self.odglos = odglos
        self.food = food

    def daj_glos(self):
        print(f'{self.odglos}')

    def eat(self):
        print(f'{self.food}')


class Pies(Zwierze):
    pass


class Pingwin(Zwierze):
    pass


class Kot(Zwierze):
    pass


class Waz(Zwierze):
    pass


class Krowa(Zwierze):
    pass


#arka_noego = [Pies('Hau'), Pingwin('Kowalski analiza'), Kot('Miau'), Waz('ssss'), Krowa('mu'), Pies('Hau'),
#              Pingwin('Kowalski analiza'), Kot('Miau'), Waz('ssss'), Krowa('mu')]

# for zwierze in arka_noego:
#     zwierze.daj_glos()

