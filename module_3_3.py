def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(228, False)
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = [2, 8, 12]
value_dict = {'a': 777, 'b': 'Login', 'c': 1234}
print_params(*value_list)
print_params(**value_dict)

value_list2 = [3.14, "index"]
print_params(*value_list2, 42)