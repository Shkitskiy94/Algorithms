"""
Нужно реализовать класс StackMax, который поддерживает операцию
определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x),
где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд,
которое не превосходит 10000. В следующих n строках идут команды.
Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""


class StackMax:
    def __init__(self):
        self.items = []
        self.max_item = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max_item.append(int(item))
        elif int(item) > self.max_item[-1]:
            self.max_item.append(int(item))
        else:
            self.max_item.append(self.max_item[-1])
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        self.max_item.pop()
        return self.items.pop()

    def get_max(self):
        if self.isEmpty():
            return 'None'
        return self.max_item[-1]


if __name__ == '__main__':
    stack = StackMax()
    m = int(input())
    result = []
    for _ in range(m):
        command = input().split()
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'push':
            stack.push(command[1])
        if command[0] == 'get_max':
            result.append(stack.get_max())
    for _ in result:
        print(_)
