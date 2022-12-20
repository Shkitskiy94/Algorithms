# len_str = 27
# right_str = 'Algorithms and Data Structures'
# left_str = 'BBBBBBBBBBBYBYYYYBBBBBBBBBB'


def search_for_ugly_words(len_str: int, right_str: str, left_str: str) -> int:
    count = 0
    result = ''
    for i in range(len_str):
        if right_str[i] == ' ':
            result += right_str[i]
        else:
            result += left_str[i]
    list_result = result.split(' ')
    for i in range(len(list_result)):
        if 'BB' in list_result[i]:
            count += 1
        elif 'YY' in list_result[i]:
            count += 1
        else:
            count += 0
    return count

if __name__ == '__main__':
    len_str = int(input())
    right_str = input().strip()
    left_str = input().strip()
    print(search_for_ugly_words(len_str, right_str, left_str))


def search_for_ugly_words(len_str: int, right_str: str, left_str: str) -> int:
    count = 0
    sum = 0
    skipping = False
    for i in range(len_str):
        if right_str[i] == ' ':
            sum = 0
            skipping = False
        if skipping:
            continue
        if left_str[i] == 'B':
            sum += 1
        if left_str[i] == 'Y':
            sum += -1
        if abs(sum) == 2:
            count += 1
            skipping = True

    return count

if __name__ == '__main__':
    len_str = int(input())
    right_str = input().strip()
    left_str = input().strip()
    print(search_for_ugly_words(len_str, right_str, left_str))
