import math


def list_of_terms(n):
    list_sum = []
    for i in range(2, n):
        list_sum.append([n - i])
        list_sum[i - 2].append(i)
    return list_sum


def lcm(n):
    list_sum = list_of_terms(n)
    nok = []
    for i in range(len(list_sum)):
        nok.append((list_sum[i][0] * list_sum[i][1]) // math.gcd(list_sum[i][0], list_sum[i][1]))
    dict_min_nok = dict(zip(nok, list_sum))
    min_nok = dict_min_nok[min(nok)]
    return f'{min_nok[0]} {min_nok[1]}'

if __name__ == '__main__':
    n = int(input())
    print(lcm(n))
