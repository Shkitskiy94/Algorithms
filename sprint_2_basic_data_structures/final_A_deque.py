# ID 77889504
"""
Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 100000. Во второй строке записано число m — максимальный
размер дека. Он не превосходит 50000. В следующих n строках записана
одна из команд:
    push_back(value) –  добавить элемент в конец дека. Если в деке уже
                        находится максимальное число элементов,
                        вывести «error».
    push_front(value) – добавить элемент в начало дека. Если в деке уже
                        находится максимальное число элементов,
                        вывести «error».
    pop_front() –       вывести первый элемент дека и удалить его.
                        Если дек был пуст, то вывести «error».
    pop_back() –        вывести последний элемент дека и удалить его.
                        Если дек был пуст, то вывести «error».
    Value —             целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
"""


class NoItemsException(Exception):
    def __init__(self):
        pass


class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, _max_size):
        self.__deque = [None] * _max_size
        self.__max_n = _max_size
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def __get_index(self, value):
        return value % self.__max_n

    def push_front(self, value):
        if self.__size == self.__max_n:
            raise MaxItemsException
        self.__head = self.__get_index(self.__head - 1)
        self.__deque[self.__head] = value
        self.__size += 1

    def push_back(self, value):
        if self.__size == self.__max_n:
            raise MaxItemsException
        self.__tail = self.__get_index(self.__tail + 1)
        self.__deque[self.__tail] = value
        self.__size += 1

    def pop_front(self):
        if self.__is_empty():
            raise NoItemsException
        value = self.__deque[self.__head]
        self.__head = self.__get_index(self.__head + 1)
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__is_empty():
            raise NoItemsException
        value = self.__deque[self.__tail]
        self.__tail = self.__get_index(self.__tail - 1)
        self.__size -= 1
        return value


if __name__ == '__main__':
    n = int(input())
    deque = Deque(_max_size=int(input()))
    for _ in range(n):
        try:
            command, *params = input().strip().split()
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except NoItemsException:
            print('error')
        except MaxItemsException:
            print('error')
