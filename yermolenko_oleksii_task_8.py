# Домашнее задание 8
# Добавлено: 30.03.2020 20:10
# ДЗ ООП
# Описать классы
#
# Машина
# Самолет
# Корабль
# Машина амфибия
#
#
# Каждый класс должен иметь
#
# Минимум 3 свойства
# Минимум 3 метода
# Минимум 2 метода должны принимать параметры


class Car:
    fuel = 0
    tank = 70

    def __init__(self, name, color, fuel, add_fuel):
        self.add_fuel = int(add_fuel)
        self.name = name
        self.color = color
        self.fuel = int(fuel)

    def refuel(self):
        self.fuel = self.fuel + self.add_fuel
        return self.fuel


        pass

    def move(self):
        pass

    def stop(self):

        pass

class Plane:
    pass

class Boat:
    pass

class Amfibia(Car, Boat):
    pass

my_car = Car('Ford', 'green', 34, 0)
print(my_car.move())
my_car.add_fuel(20)
