immutable_var = 1, 2, 3, 'apple', 'orange'
print(immutable_var) # переменная immutable_var - имеет класс "tuple"(кортеж). Кортеж - неизменяймый тип данных!
mutable_list = [1, 2, 3, 'juice', 'orange']
print(mutable_list)
mutable_list[0] = 8
mutable_list[-1] = 'banana'
print(mutable_list)