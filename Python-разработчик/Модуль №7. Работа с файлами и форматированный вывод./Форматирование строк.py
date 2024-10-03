import random

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 5
team2_num = 6
tasks_total = random.randrange(10, 100)
score_1 = random.randrange(2, tasks_total)
score_2 = random.randrange(2, tasks_total)
team1_time = random.randrange(50, 100)
team2_time = random.randrange(50, 100)

time_avg = (team1_time / score_1 + team2_time / score_2) / 2



# Использование %:
print('в команде "%s" %s участников' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team2_num, team1_num))

# Использование format():
print('Команда "{}" решила задач: {}'.format(team2_name, score_2))
print('Команда "{}" решила задачи за {} минут'.format(team2_name, team2_time))

# Использование f-строк:
print(f'Команды решили задач: {score_1} и {score_2}')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    rslt = team1_name
    print(f'Результат битвы: победила команда "{rslt}"')
elif score_2 > score_1 or score_1 == score_2 and team1_time > team2_time:
    rslt = team2_name
    print(f'Результат битвы: победила команда "{rslt}"')
else:
    rslt = 'Ничья'
    print(f'Результат битвы: "{rslt}"')

print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} минуты на задачу')
