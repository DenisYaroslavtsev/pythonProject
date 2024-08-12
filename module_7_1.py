class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    open(__file_name, 'a').close()


    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            text_content = file.read()

        return text_content
    def add(self, *products):
        list_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in list_products:
                    file.write(f'{str(product)} \n')
                    list_products += str(product) + '\n'
                else:
                    print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
