"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией.
Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 1000. В каждой из следующих n строк
записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.
"""


class Q:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.size == 1:
            x = self.head
            self.head = self.Node()
            self.tail = self.Node()
            self.size -= 1
            return x
        if self.size == 2:
            x = self.head
            self.head = self.tail
            self.size -= 1
            return x
        x = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.size -= 1
        return x

    def put(self, x):
        if self.size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size += 1

    def __str__(self):
        return self.value


if __name__ == '__main__':
    n = int(input())
    s = Q()
    res = []
    for i in range(n):
        command = input().split()
        if len(command) == 2:
            a = s.put(command[1])
            if a == 'error':
                res.append(a)
        if command[0] == 'get':
            res.append(s.get())
        if command[0] == 'size':
            res.append(s.size)

    for x in res:
        print(x)
