class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        count = 0
        if new_floor > self.number_of_floors or new_floor < 0:
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                count += 1
                print(count)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
