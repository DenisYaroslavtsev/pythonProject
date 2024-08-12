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
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        text_content = file.read()
        file.close()

        return text_content
    def add(self, *products):
        list_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in list_products:
                file.write(f'{str(product)} \n')
                list_products += str(product) + '\n'
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()
    # def add(self, *products):
    #     with open(self.__file_name, 'r') as file:
    #         list_product = file.read().split('\n')
    #         for product in products:
    #             if product.name in list_product:
    #                 print(f'Продукт {product.name} уже есть в магазине!')
    #                 break
    #             else:
    #                 with open(self.__file_name, 'a') as file1:
    #                     file1.write(f'{product}\n')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# if not os.path.isfile(self.__file_name):
#     open(self.__file_name, 'w').close()