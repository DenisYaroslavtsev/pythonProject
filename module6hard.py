class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = False
        if self.__is_valid_sides(*sides):
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, diameter):
        super().__init__(color, diameter)
        self.__radius = self.get_sides()[0] / 2

    def get_square(self):
        pi = 3,14
        return pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*new_sides)
            self.__radius = self.get_sides()[0] / 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__(color, side1, side2, side3)
        self.__height = self.calculate_height()

    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def calculate_height(self):
        a, b, c = self.get_sides()
        return (2 * self.get_square()) / a


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, side_length)
        self.__sides = [side_length] * self.sides_count

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(new_sides[0])
            self.__sides = [new_sides[0]] * self.sides_count


# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
