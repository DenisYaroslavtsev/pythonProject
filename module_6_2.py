class Vehicle:
    def __init__(self,owner: str, model: str,color: str, engine_power: int):
        self.owner = owner # Владелец
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    __color_variants = ['Blue', 'Red', 'Golden', 'White', 'Green', 'Black']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_house_power(self,):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self,):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_house_power())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self,new_color):
        if new_color.lower() in (color.lower() for color in self.__color_variants):
            self.__color = new_color
        else:
            print(f"Нельзя cменить цвет на {new_color} ")

class Sedan(Vehicle):
    __pasengers_limit = 5

    def __init__(self,owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
