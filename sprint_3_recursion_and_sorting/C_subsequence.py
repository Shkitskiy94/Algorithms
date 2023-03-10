"""
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно
понять, является ли первая из них подпоследовательностью второй.
Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию,
которая решает эту задачу.

Формат ввода
В первой строке записана строка s.

Во второй —- строка t.

Обе строки состоят из маленьких латинских букв,
длины строк не превосходят 150000. Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.
"""


def subsequence(substring, whole_line):
    if len(substring) == 0:
        return True
    count = - 1
    for i in substring:
        count = whole_line.find(i, count + 1)
        if count == - 1:
            return False
    return True


if __name__ == '__main__':
    substring = input()
    whole_line = input()
    print(subsequence(substring, whole_line))
