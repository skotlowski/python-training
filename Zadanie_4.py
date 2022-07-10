import random
import copy

class YearIterator:
    def __init__(self, age=100):
        self.age = age

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.age:
            result = 1 + self.n
            self.n += 1
            return result
        else:
            raise StopIteration


class Niemiec:

    first_id = 10000000000
    test_age = YearIterator().__iter__()

    def __init__(self, name):
        self.gender_vals = ["m", "w"]
        self.age = next(Niemiec.test_age)
        self.gender = self.gender_vals[random.randint(0, 1)]
        self.id = Niemiec._set_id_for_taxes()
        if type(name) is dict:
            self.name = name[self.gender]
        else:
            self.name = name

    def __mul__(self, other):
        if self.gender == other.gender:
            raise Exception("No children for you")
        else:
            if self.age < 14 or other.age < 14:
                raise Exception("One of you is under 14")
            elif self.age < 16 < other.age or other.age < 16 < self.age:
                raise Exception("One of you is over 16 and other is not")
            else:
                new_Niemiec = Niemiec.create_new_niemiec()
                new_Niemiec.age = 0
                return new_Niemiec

    @staticmethod
    def _set_id_for_taxes():
        id = Niemiec.first_id
        Niemiec.first_id = Niemiec.first_id + 1
        return id

    @classmethod
    def create_new_niemiec(cls):
        m = ["Matteo", "Noah", "Leon", "Finn", "Elias", "Paul", "Ben", "Luca", "Emil", "Louis"]
        w = ["Emilia", "Hannah", "Mia", "Emma", "Sophia", "Mila", "Lina", "Ella", "Lea", "Marie"]
        index = random.randint(0, 10)
        return cls({"m": m[index], "w": w[index]})

    def age_by_year(self):
        self.age = self.age + 1



# population = []
#
# for i in range(10):
#     population.append(Niemiec("Helmut"))
#
# for i in range(10):
#     for _ in range(len(population)):
#         index1 = random.randint(0, len(population))
#         index2 = random.randint(0, len(population))
#         try:
#             new_Niemiec = population[index1] * population[index2]
#             population.append(new_Niemiec)
#         except Exception as e:
#             # print(f"{e}")
#             pass
#     counter = 0
#
#     for j in range(len(population)):
#         population[j - counter].age_by_year()
#         if population[j - counter].age >= 100:
#             population.pop(j - counter)
#             counter = counter + 1
#
# print(len(population))
#
# for person in population:
#     print(person.name)

niemcy = [Niemiec('Hans'), Niemiec('Hans'), Niemiec('Hans')]
print('Pierwsza lista:')
print(id(niemcy))

for item in niemcy:
    print(id(item))

niemcy2 = copy.deepcopy(niemcy)
print('Druga lista:')
print(id(niemcy2))

for item in niemcy2:
    print(id(item))

