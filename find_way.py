import random

SIZE = 6
matrix = [[random.randint(1, 2)] * SIZE for i in range(SIZE)]
# matrix = [[1] * SIZE for i in range(SIZE)]
for i in range(SIZE):
    matrix[0][i] = 0
    matrix[i][0] = 0

for r in matrix:
    print(r)

start = (1, 1)
finish = (3, 3)


def f(q, finish, point, current_way, current_value, been):
    # print(current_way)
    if point == finish:
        q.append((current_value, current_way))
        return

    if point[1] - 1 > 0 and not been[point[1] - 1][point[0]] and 0 < matrix[point[1] - 1][point[0]] < 2:
        new_point = (point[0], point[1] - 1)
        been[new_point[1]][new_point[0]] = True
        f(q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[0] - 1 > 0 and not been[point[1]][point[0] - 1] and 0 < matrix[point[1]][point[0] - 1] < 2:
        new_point = (point[0] - 1, point[1])
        been[new_point[1]][new_point[0]] = True
        f(q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[0] + 1 < SIZE and not been[point[1]][point[0] + 1] and 0 < matrix[point[1]][point[0] + 1] < 2:
        new_point = (point[0] + 1, point[1])
        been[new_point[1]][new_point[0]] = True
        f(q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False

    if point[1] + 1 < SIZE and not been[point[1] + 1][point[0]] and 0 < matrix[point[1] + 1][point[0]] < 2:
        new_point = (point[0], point[1] + 1)
        been[new_point[1]][new_point[0]] = True
        f(q, finish, new_point, current_way + [new_point], current_value + matrix[new_point[1]][new_point[0]], been)
        been[new_point[1]][new_point[0]] = False


def find_way(matrix, start, finish):
    been = [[False] * SIZE for j in range(SIZE)]
    been[start[1]][start[0]] = True

    q = []

    f(q, finish, start, [start], matrix[start[1]][start[0]], been)
    # print(q)

    min_d = 999999
    ways = []
    for a in q:
        if a[0] < min_d:
            min_d = a[0]
            ways = [a[1]]
        elif a[0] == min_d:
            ways.append(a[1])

    min_len = 999999
    final_ways = []
    for w in ways:
        if len(w) < min_len:
            min_len = len(w)
            final_ways = [w]
        elif len(w) == min_len:
            final_ways.append(w)

    if len(final_ways) > 0:
        return final_ways[0]

    return []


print(find_way(matrix, start, finish))
