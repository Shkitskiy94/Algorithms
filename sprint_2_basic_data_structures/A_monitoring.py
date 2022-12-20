""""
Алла получила задание, связанное с мониторингом работы различных серверов.
Требуется понять, сколько времени обрабатываются определённые запросы на конкретных серверах.
Эту информацию нужно хранить в матрице, где номер столбца соответствуют идентификатору запроса,
а номер строки — идентификатору сервера. Алла перепутала строки и столбцы местами.
С каждым бывает. Помогите ей исправить баг.
Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.
Транспонированная матрица получается из исходной заменой строк на столбцы.
Например, для матрицы А (слева) транспонированной будет следующая матрица (справа):

Формат ввода
В первой строке задано число n — количество строк матрицы.
Во второй строке задано m — число столбцов, m и n не превосходят 1000. В следующих n строках задана матрица.
Числа в ней не превосходят по модулю 1000.

Формат вывода
Напечатайте транспонированную матрицу в том же формате, который задан во входных данных. Каждая строка матрицы выводится на отдельной строке, элементы разделяются пробелами.

Пример 1
Ввод	 Вывод
4        1 0 7 2
3        2 2 4 7
1 2 3    3 6 1 0
0 2 6
7 4 1
2 7 0
"""


def data_input():
    n = int(input())
    m = int(input())
    matrix = [input().split(' ') for j in range(n)]
    return n, m, matrix


def matrix_calculations(n, m, matrix):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')


if __name__ == '__main__':
    n, m, matrix = data_input()
    matrix_calculations(n, m, matrix)
