class House:
    houses_history=[]

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print (f"{self.name} снесен, но он останется в истории")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __add__(self, value):
        if isinstance(value, int):
                self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            return House.__add__(self, value)

    def __radd__(self, value):
       if isinstance(value, int):
           return House.__add__(self, value)

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


    

h1=House('ЖК Эльбрус', 10)
print(House.houses_history)
h2=House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



#h1.to_go(5)
#h2.to_go(10)
#print(len(h1)) #высота этажей
#print(len(h2))
#print(h1==h2) #eq
#h1=h1 + 10
#print(h1)
#print (h1==h2)#не работает, разобрать попозже
#h1+=10 #iadd
#print(h1)
#h2= 10+h2 #radd
#print(h2)
#print(h1<h2) #lt
#print(h1<=h2) #le
#print(h1 > h2) #gt
#print(h1>= h2) #ge
#print(h1!= h2) #ne
