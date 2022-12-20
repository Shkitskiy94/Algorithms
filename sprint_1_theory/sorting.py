def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list


print(selection_sort([5, 3, 6, 2, 10]))
