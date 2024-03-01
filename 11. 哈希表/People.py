class People:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return (self.name, self.age, self.salary) \
               == (other.name, other.age, other.salary)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return self.name + str(self.age) + str(self.salary)


p1 = People("Tom", "1", 20)
p5 = People("Tom", "1", 18)

p2 = People("Zion", "2", 18)
p3 = People("Adam", "3", 20)
p4 = People("Alice", "4", 18)

dict = {p1: 'A', p2: "B", p3: "C", p4: "D", p5: "E"}
print(dict)
for key in dict:
    print(key, 'corresponds to', dict[key])