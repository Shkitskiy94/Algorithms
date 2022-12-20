# пузырьковая сортировка
def buble_sort (number, array):
    flag = True
    for i in range(number -1):
        for j in range(number - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag:
            for x in array:
                print(x, end=' ')
            print('')
            flag = False


buble_sort(5, [11, 2, 9, 7, 1])
