#ID 75559142, 75657845, 75681589
"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.
Найдите число баллов,
которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.
Формат вывода
Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.
Ввод	Вывод
3       2
1231
2..2
2..2
2..2

"""
from typing import List, Tuple


def trainer(number: int, list_matrix: List[str]) -> int:
    numbers = {a: 0 for a in range(1, 10)}
    scores = 0
    for i in range(4):
        for k in list_matrix[i]:
            if k == '.':
                continue
            numbers[int(k)] += 1
    for i in numbers.values():
        if 0 < i <= 2 * number:
            scores += 1
    return scores


def read_input() -> Tuple[int, List[str]]:
    number = int(input())
    list_matrix = [str(input()) for _ in range(4)]
    return number, list_matrix


if __name__ == '__main__':
    number, list_matrix = read_input()
    print(trainer(number, list_matrix))


"""
Максим твой фидбэк вдохновляет, поэтому я придумал еще одно решение.
"""


def max_point(finger, matrix, players=2, digits='123456789'):
    """Расчет количества баллов в тренажере."""
    return sum(0 < matrix.count(time) <= finger*players
               for time in digits)


if __name__ == "__main__":
    print(max_point(
        int(input()),
        input() + input() + input() + input()
        )
    )
