class Vehicle:
    __COLOR_VARIANTS = 'blue', 'red', 'green', 'black', 'white'

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def getmodel(self):
        return f"Модель: {self.__model}"

    def gethorsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def printinfo(self):
        print(self.getmodel())
        print(self.gethorsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


__COLOR_VARIANTS = 'BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE'


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.printinfo()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.printinfo()