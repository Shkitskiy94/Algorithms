def twosum_with_sort(numbers, X):
    # Сортируем исходный массив стандартной функцией.
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None, None


numbers = [2, 1, 3, 5, 5]
X = 4

print(twosum_with_sort(numbers, X))
