class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def to_go(self, new_floor):
        new_floor = int(new_floor)
        for i in range (1, new_floor+1):

            if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

h1=House('ЖК Горский', 18)
h2=House('Домик в деревне', 2)
#h1.to_go(5)
#h2.to_go(10)

print(h1)
print(h2)

print(len(h1))
print(len(h2))