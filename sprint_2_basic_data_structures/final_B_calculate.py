# ID 77867377
"""
Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не
превосходящие 10000. Гарантируется, что значение промежуточных выражений в
тестовых данных по модулю не больше 50000.
Формат вывода
Выведите единственное число — значение выражения.
"""


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, element):
        self.__items.append(element)

    def pop(self):
        if len(self.__items) == 0:
            raise Exception
        else:
            return self.__items.pop()


def calculate(element):
    lambda_dict = {'+': lambda x, y: x + y,
                   '-': lambda x, y: y - x,
                   '*': lambda x, y: x * y,
                   '/': lambda x, y: y // x}
    stack = Stack()
    for i in element:
        operations = lambda_dict.get(i)
        if operations:
            stack.push(operations(stack.pop(), stack.pop()))
        else:
            stack.push(int(i))
    return stack.pop()

if __name__ == '__main__':
    print(calculate(input().split(' ')))
