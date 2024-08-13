team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = ((team1_time / score1) + (team2_time / score2)) / 2
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья"

challenge_result = result
team1 = 'В команде Мастера кода участников: %d!' % team1_num
team2 = "В команде Мастера кода уастников: %d и %d!" % (team1_num, team2_num)
team2_score = "Команда Волшебники данных решила задач: {}!".format(score2)
time_team1 = "Волшебники данных решили задачи за {} c!".format(team1_time)


print(team1)
print(team2)
print(team2_score)
print(time_team1)
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} cекунды на задачу!')