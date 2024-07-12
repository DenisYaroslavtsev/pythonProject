data_structure = [[1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculator_data_structure(data_structure):
        sum_num = 0
        for i in data_structure:
                if isinstance(i, int):
                        sum_num += i
                elif isinstance(i, str):
                        sum_num += len(i)
                elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i,set):
                        sum_num += calculator_data_structure(i)
                elif isinstance(i, dict):
                        sum_num += calculator_data_structure(i.keys()) + calculator_data_structure(i.values())
        return sum_num

result = calculator_data_structure(data_structure)
print(result)

