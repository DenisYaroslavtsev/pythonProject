my_dict = {'Denis': 1997, 'Ivan': 2000, 'Dima': 1999}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Andrey'))
my_dict.update({'Alice': 2002,
                'Milana': 1996 })
del my_dict['Ivan']
print(my_dict)
my_set = {1, 2, 3, 4, 5, 'Car', 3, 5, 1, 5, 'Car', 3}
print(my_set)
my_set.add(9)
my_set.add((1, 2, 3))
my_set.discard('Car')
print(my_set)