def time_to_move(point):
    if point <= 4:
        if point == 1:
            return 2
        elif point == 2:
            return 1
        elif point == 4:
            return 2

    if point % 3 == 0:
        return point / 3
    else:
        v = point // 3
        if (point - v * 3) % 2 != 0:
            v = v - 1
        r = (point - v * 3) / 2
        return v + r

count = int(input())
for i in range(count):
    point = int(input())
    time_taken = int(time_to_move(point))
    print(time_taken)
