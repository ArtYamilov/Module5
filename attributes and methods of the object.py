class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        for i in range(1, new_floor+1):
            if 1 < new_floor < self.number_of_floors:
                print(i)
        if new_floor < 1:
            print('Такого этажа не существует')
        elif new_floor > self.number_of_floors:
            print('Такого этажа не существует')


gk1 = House('ЖК Градострой', 13)
gk2 = House('ЖК Благострой', 21)
gk1.go_to(8)
gk2.go_to(34)
