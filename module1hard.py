grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_sum = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])
sorted_studens = sorted(students)
dict_students = dict([[sorted_studens[0],grades_sum[0]],[sorted_studens[1],grades_sum[1]],[sorted_studens[2],grades_sum[2]],[sorted_studens[3],grades_sum[3]],[sorted_studens[4],grades_sum[4]]])
print(dict_students)


