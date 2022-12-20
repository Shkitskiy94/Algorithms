"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого
и малинового. После того как вещи других расцветок были убраны, Рита
захотела отсортировать свой новый гардероб по цветам. Сначала должны
идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.
Помогите Рите справиться с этой задачей.
Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода
В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000. Во второй строке даётся массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

Формат вывода
Нужно вывести в строку через пробел цвета предметов в правильном порядке.
"""

n = int(input())
d = {'0': 0, '1': 0, '2': 0}
if n > 0:
    for color in input().split(' '):
        d[color] += 1
print('0 ' * d['0'] + '1 ' * d['1'] + '2 ' * d['2'])
