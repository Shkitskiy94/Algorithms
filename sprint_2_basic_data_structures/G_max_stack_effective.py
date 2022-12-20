"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд,
оно не превосходит 100000.
Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""


class StackMaxEffective:
    def __init__(self):
        self.stack_ = []

    def __bool__(self):
        return bool(self.stack_)

    def push(self, item):
        if self.stack_:
            new_max = max(item, self.stack_[-1][1])
        else:
            new_max = item
        self.stack_.append((item, new_max))

    def pop(self):
        return self.stack_.pop()[0]

    def get_max(self):
        return self.stack_[-1][1]


if __name__ == '__main__':
    s = StackMaxEffective()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'pop':
            if s:
                s.pop()
            else:
                print('error')
        if cmd[0] == 'push':
            s.push(int(cmd[1]))
        if cmd[0] == 'get_max':
            if s:
                print(s.get_max())
            else:
                print('None')