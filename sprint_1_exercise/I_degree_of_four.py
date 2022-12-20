
"""
Степень четырёх
Напишите программу, которая определяет, будет ли положительное целое число
степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n,
где n – целое неотрицательное число.
Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.
Формат вывода
Выведите «True», если число является степенью четырёх,
«False» –— в обратном случае.
Пример 1
Ввод	            Вывод
15                  False
"""


def is_power_of_four(number: int) -> bool:
    if number <= 0:
        return False
    while number > 1:
        if number % 4 != 0:
            return False
        number = number // 4
    return True


print(is_power_of_four(int(input())))
