class Animals:
    def say_something(self):
        pass

    def eat(self):
        pass


class Dog(Animals):
    def say_something(self):
        print('Hau')


class Penguin(Animals):
    def say_something(self):
        print('Kowalski analiza')


class Cat(Animals):
    def say_something(self):
        print('Miau')


class Snake(Animals):
    def say_something(self):
        print('ss')


class Cow(Animals):
    def say_something(self):
        print('muu')


class Horse(Animals):
    def eat(self):
        print('Siano')


class Bird(Animals):
    def eat(self):
        print('Ziarno')


class Pegasus(Bird, Horse):
    pass



# arka_noego = [Dog(), Pegasus(), Cat(), Snake(), Cow(), Dog(),
#              Penguin(), Cat(), Snake(), Cow()]

# for animal in arka_noego:
#     animal.daj_glos()


pegasus = Pegasus()
pegasus.eat()
