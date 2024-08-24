first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) >= 5]
second_result = [(i, k) for i in first_strings for k in second_strings if len(i) == len(k)]
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)