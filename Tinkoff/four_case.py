from math import tan, pi


def s_triangle(n_sides, s_length):
    p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
    return round(p_area, 6)


if __name__ == '__main__':
    n_sides = int(input())
    s_length = int(input())
    print(s_triangle(n_sides, s_length))
