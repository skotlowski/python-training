class Person:
    def __init__(self, age, salary):
        self.age = age
        self.salary = salary

    def __lt__(self, other):
        return self.age < other.age


person1 = Person(20, 2000)
person2 = Person(25, 3000)

print(person1 < person2)