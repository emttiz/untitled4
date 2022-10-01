import os
from envparse import env
from lottery import stavka
env.read_envfile('settings.env')
money = int(os.getenv('MY_MONEY'))

while True:
    commands = input('Введите слот и ставку или exit-almaz для выхода: ').split()
    if commands[0] == 'exit':
        print(f'Программа завершена!‍\nОставшаяся сумма: {money}')
        break
    if not 1 <= int(commands[0]) <= 30:
        print('Неправильный слот для ставки\nПодсказка: слот должен быть целым числом от 1 до 30')
        continue
    if int(commands[1]) > money or int(commands[1]) <= 0:
        print('Неправильная сумма для ставки\nПодсказка: сумма ставки должна быть целым положительным числом не больше \
        доступного числа денег\n'+f'Доступная сумма:{money}')
        continue
    result = stavka(int(commands[0]), int(commands[1]))
    if result < 0:
        money += result
    else:
        money += result
    if money == 0:
        print('Вы обонкротились!! T-T')
        break