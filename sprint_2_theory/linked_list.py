from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data()) + ' -> '
            cur_node = cur_node.get_next()
        print(output)

    def lenght(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node != None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev

my_list = LinkedList()
my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)
my_list.show()
my_list.lenght()
my_list.remove(2)
my_list.show()
