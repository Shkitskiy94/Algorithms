#ID 75556513, 75692953, 75697932
"""
Тимофей ищет место, чтобы построить себе дом.
 Улица, на которой он хочет жить, имеет длину n,
 то есть состоит из n одинаковых идущих подряд участков.
 Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние
до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю-расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
Ввод	         Вывод
5                0 1 2 1 0
0 1 4 9 0
"""
from typing import Tuple, List


def read_input() -> Tuple[int, List[int]]:
    len_street = int(input())
    street = [int(n) for n in input().split(' ')]
    return len_street, street


def calculate(lenght_street: int, street: List[int]) -> List[int]:
    sum_length = [] * lenght_street
    sum = lenght_street
    for n in range(lenght_street):
        sum = 0 if street[n] == 0 else sum + 1
        sum_length.append(sum)
    return sum_length


def nearest_zero(len_street: int, street: List[int]) -> List[int]:
    to_right = calculate(len_street, street)
    to_left = (calculate(len_street, street[::-1]))[::-1]
    result = [min(to_right[n], to_left[n]) for n in range(len_street)]
    return result


if __name__ == '__main__':
    length, number_street = read_input()
    print(' '.join(str(x) for x in nearest_zero(length, number_street)))
